import Logo from "./Logo";

export default function Nav() {
  return (
    <header className="nav">
      <Logo />
      <a className="nav__faq" href="#faq">FAQ</a>
    </header>
  );
}
