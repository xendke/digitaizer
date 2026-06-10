import Logo from "./Logo";

export default function Nav({ digit }: { digit: number }) {
  return (
    <header className="nav">
      <Logo digit={digit} />
      <a className="nav__faq" href="#faq">FAQ</a>
    </header>
  );
}
