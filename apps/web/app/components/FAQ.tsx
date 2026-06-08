"use client";

import { useState } from "react";

const ITEMS = [
  {
    q: "How do I use it?",
    a: "Draw any digit from 0 to 9 in the box with your mouse, trackpad, or finger. The network predicts what you wrote automatically and shows a confidence score for every digit.",
  },
  {
    q: "How does the prediction work?",
    a: "Your drawing is normalized — cropped to the ink, recentered, and scaled — then scored against a neural network trained on handwritten digits. The output is a probability for each digit 0–9.",
  },
  {
    q: "What model powers it?",
    a: "A small neural network trained on the MNIST dataset of 60,000 handwritten digits — the same family of models that first taught machines to read handwritten mail.",
  },
  {
    q: "How accurate is it?",
    a: "Around 95–97% on held-out handwritten digits, with each prediction returned in well under 50 milliseconds.",
  },
];

export default function FAQ() {
  const [open, setOpen] = useState<number>(0);

  return (
    <section className="faq" id="faq">
      <div className="section-head">
        <span className="eyebrow">FAQ</span>
        <h2>Good to know.</h2>
      </div>
      <div className="faq__list">
        {ITEMS.map((item, i) => (
          <div key={i} className={"faqitem" + (open === i ? " is-open" : "")}>
            <button className="faqitem__q" onClick={() => setOpen(open === i ? -1 : i)}>
              <span>{item.q}</span>
              <span className="faqitem__plus" style={{ color: "var(--accent)" }}>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round">
                  <path d="M12 5v14M5 12h14" />
                </svg>
              </span>
            </button>
            <div className="faqitem__a">
              <p>{item.a}</p>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
