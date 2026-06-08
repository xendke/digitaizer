export default function Logo({ size = 26 }: { size?: number }) {
  return (
    <span className="logo" style={{ fontSize: size }}>
      <span className="logo__mark" style={{ borderColor: "var(--accent)" }}>
        <span style={{ color: "var(--accent)" }}>7</span>
      </span>
      Digit<span style={{ color: "var(--accent)" }}>ai</span>zer
    </span>
  );
}
