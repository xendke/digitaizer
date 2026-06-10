"use client";

import Logo from "./Logo";

export default function Footer({ digit }: { digit: number }) {
  return (
    <footer className="footer">
      <div className="footer__top">
        <Logo size={22} digit={digit} />
        <nav className="footer__links">
          <button
            className="nav__faq"
            style={{ background: "none", border: "none", cursor: "pointer", padding: 0 }}
            onClick={() => window.scrollTo({ top: 0, behavior: "smooth" })}
          >
            ↑ Back to top
          </button>
        </nav>
      </div>
      <div className="footer__bottom">
        <span>Recognizing handwritten digits, one scribble at a time.</span>
        <span>© 2026 Digitaizer</span>
      </div>
    </footer>
  );
}
