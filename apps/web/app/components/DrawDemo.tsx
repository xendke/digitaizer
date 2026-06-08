"use client";

import { useRef, useState, useEffect, useCallback } from "react";

const PAD = 360;
const BRUSH = 26;

type Score = { digit: number; p: number };
type Result = { digit: number; scores: Score[] };

function emptyScores(): Score[] {
  return Array.from({ length: 10 }, (_, d) => ({ digit: d, p: 0 }));
}

export default function DrawDemo() {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const ctxRef = useRef<CanvasRenderingContext2D | null>(null);
  const drawing = useRef(false);
  const last = useRef({ x: 0, y: 0 });
  const hasInk = useRef(false);
  const predictTimer = useRef<ReturnType<typeof setTimeout> | null>(null);

  const [result, setResult] = useState<Result | null>(null);
  const [thinking, setThinking] = useState(false);
  const [empty, setEmpty] = useState(true);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    canvas.width = PAD * dpr;
    canvas.height = PAD * dpr;
    const ctx = canvas.getContext("2d")!;
    ctx.scale(dpr, dpr);
    ctx.lineJoin = "round";
    ctx.lineCap = "round";
    ctxRef.current = ctx;
    paintBg(ctx);
  }, []);

  function paintBg(ctx: CanvasRenderingContext2D) {
    ctx.save();
    ctx.fillStyle = "#ffffff";
    ctx.fillRect(0, 0, PAD, PAD);
    ctx.restore();
  }

  const pos = useCallback((e: React.MouseEvent | React.TouchEvent) => {
    const canvas = canvasRef.current!;
    const r = canvas.getBoundingClientRect();
    const src = "touches" in e ? e.touches[0] : e;
    return {
      x: ((src.clientX - r.left) / r.width) * PAD,
      y: ((src.clientY - r.top) / r.height) * PAD,
    };
  }, []);

  const start = useCallback(
    (e: React.MouseEvent | React.TouchEvent) => {
      e.preventDefault();
      drawing.current = true;
      const p = pos(e);
      last.current = p;
      const ctx = ctxRef.current!;
      ctx.strokeStyle = "#111114";
      ctx.lineWidth = BRUSH;
      ctx.beginPath();
      ctx.moveTo(p.x, p.y);
      ctx.lineTo(p.x + 0.01, p.y + 0.01);
      ctx.stroke();
      hasInk.current = true;
      setEmpty(false);
    },
    [pos]
  );

  const move = useCallback(
    (e: React.MouseEvent | React.TouchEvent) => {
      if (!drawing.current) return;
      e.preventDefault();
      const ctx = ctxRef.current!;
      const p = pos(e);
      ctx.strokeStyle = "#111114";
      ctx.lineWidth = BRUSH;
      ctx.beginPath();
      ctx.moveTo(last.current.x, last.current.y);
      ctx.lineTo(p.x, p.y);
      ctx.stroke();
      last.current = p;
    },
    [pos]
  );

  // placeholder until real API is wired in
  const runPredict = useCallback(() => {
    if (!hasInk.current) return;
    setThinking(true);
    if (predictTimer.current) clearTimeout(predictTimer.current);
    predictTimer.current = setTimeout(() => {
      setThinking(false);
      // stub — will be replaced with real API call
      const scores = emptyScores();
      setResult({ digit: scores[0].digit, scores });
    }, 320);
  }, []);

  const end = useCallback(() => {
    if (!drawing.current) return;
    drawing.current = false;
    if (predictTimer.current) clearTimeout(predictTimer.current);
    predictTimer.current = setTimeout(runPredict, 450);
  }, [runPredict]);

  const clear = useCallback(() => {
    const ctx = ctxRef.current;
    if (!ctx) return;
    paintBg(ctx);
    hasInk.current = false;
    setResult(null);
    setEmpty(true);
    setThinking(false);
    if (predictTimer.current) clearTimeout(predictTimer.current);
  }, []);

  useEffect(() => {
    const up = () => end();
    window.addEventListener("mouseup", up);
    window.addEventListener("touchend", up);
    return () => {
      window.removeEventListener("mouseup", up);
      window.removeEventListener("touchend", up);
    };
  }, [end]);

  const top = result ? result.scores[0] : null;
  const accent = "var(--accent)";

  const barScores = result
    ? result.scores.slice().sort((a, b) => a.digit - b.digit)
    : emptyScores();

  return (
    <div className="demo">
      {/* draw pane */}
      <div className="demo__draw">
        <div className="demo__drawhead">
          <span className="demo__label">
            <span className="dot" style={{ background: accent }} />
            Draw a digit
          </span>
          <button className="iconbtn" onClick={clear} aria-label="Clear canvas">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round">
              <path d="M3 6h18M8 6V4h8v2M19 6l-1 14H6L5 6" />
            </svg>
            Clear
          </button>
        </div>

        <div className="pad">
          <canvas
            ref={canvasRef}
            className="pad__canvas"
            onMouseDown={start}
            onMouseMove={move}
            onTouchStart={start}
            onTouchMove={move}
            onTouchEnd={end}
          />
          {empty && !thinking && (
            <div className="pad__hint">
              <svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
                <path d="M12 19l7-7 3 3-7 7-3-3z" />
                <path d="M18 13l-1.5-1.5" />
                <path d="M2 2l7.586 7.586" />
                <circle cx="11" cy="11" r="2" />
              </svg>
              <span>Sketch any number 0–9 here</span>
            </div>
          )}
        </div>

        <button
          className="predictbtn"
          style={{ background: accent }}
          onClick={runPredict}
        >
          {thinking ? "Analyzing…" : "Predict drawing"}
          <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.4" strokeLinecap="round" strokeLinejoin="round">
            <path d="M5 12h14M13 6l6 6-6 6" />
          </svg>
        </button>
      </div>

      {/* result pane */}
      <div className="demo__result">
        <div className="result__top">
          <div className="result__label">Prediction</div>
          <div className={"result__digit" + (top ? " is-live" : " result__digit--empty")}>
            {thinking ? (
              <span className="spinner" style={{ borderTopColor: accent }} />
            ) : top ? (
              top.digit
            ) : (
              "—"
            )}
          </div>
          {top && (
            <div className="result__conf" style={{ color: accent }}>
              {(top.p * 100).toFixed(1)}% confident
            </div>
          )}
          {!top && !thinking && (
            <div className="result__conf result__conf--muted">awaiting input</div>
          )}
        </div>

        <div className="result__breakdown">
          <div className="breakdown__head">Confidence breakdown</div>
          <div className="bars">
            {barScores.map((s) => {
              const isTop = top && s.digit === top.digit;
              return (
                <div key={s.digit} className={"bar" + (isTop ? " is-top" : "")}>
                  <span className="bar__d">{s.digit}</span>
                  <span className="bar__track">
                    <span
                      className="bar__fill"
                      style={{
                        width: (result ? Math.max(s.p * 100, 0.6) : 0) + "%",
                        background: isTop ? accent : undefined,
                      }}
                    />
                  </span>
                  <span className="bar__p">
                    {result ? (s.p * 100).toFixed(s.p >= 0.01 ? 0 : 1) : "0"}
                    <i>%</i>
                  </span>
                </div>
              );
            })}
          </div>
        </div>
      </div>
    </div>
  );
}
