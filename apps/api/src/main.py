from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image, ImageFilter
import numpy as np
import io
from src.network import Network

app = FastAPI(title="Digitaizer API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST"],
    allow_headers=["*"],
)

net = Network([784, 30, 10])
net.load_wb()


@app.post("/predict")
async def predict(image: UploadFile = File(...)):
    if not image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")

    data = await image.read()
    try:
        img = Image.open(io.BytesIO(data))
    except Exception:
        raise HTTPException(status_code=400, detail="Could not decode image")

    img = (
        img.filter(ImageFilter.GaussianBlur(radius=2))
        .convert("L")
        .resize((28, 28))
    )

    pixels = np.array(img.getdata(), dtype=np.float64)
    pixels = np.abs(pixels - 255) / 255
    pixels = pixels[np.newaxis].T

    output = net.predict(pixels).flatten()
    predictions = [
        {"digit": int(i), "confidence": round(float(output[i]), 6)}
        for i in range(10)
    ]
    predictions.sort(key=lambda x: x["confidence"], reverse=True)

    return {
        "prediction": predictions[0]["digit"],
        "confidence": predictions[0]["confidence"],
        "all": predictions,
    }
