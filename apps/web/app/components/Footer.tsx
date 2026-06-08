import Logo from "./Logo";

export default function Footer() {
  return (
    <footer className="footer">
      <div className="footer__top">
        <Logo size={22} />
        <nav className="footer__links">
          <a href="#demo">Demo</a>
          <a href="#faq">FAQ</a>
        </nav>
      </div>
      <div className="footer__bottom">
        <span>Recognizing handwritten digits, one scribble at a time.</span>
        <span>© 2026 Digitaizer</span>
      </div>
    </footer>
  );
}
