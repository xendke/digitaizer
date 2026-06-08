# Digitaizer API

FastAPI backend for digit prediction.

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
cd src
uvicorn main:app --reload
```

## Endpoints

### `POST /predict`

Accepts a multipart image upload and returns digit predictions.

**Request:** `multipart/form-data` with field `image` (any common image format)

**Response:**
```json
{
  "prediction": 7,
  "confidence": 0.983241,
  "all": [
    {"digit": 7, "confidence": 0.983241},
    {"digit": 1, "confidence": 0.012345},
    ...
  ]
}
```
