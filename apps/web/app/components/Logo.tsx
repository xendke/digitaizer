import Image from "next/image";

export default function Logo({ digit = 7, size = 26 }: { digit?: number; size?: number }) {
  return (
    <span className="logo" style={{ fontSize: size }}>
      <Image
        src={`/digits/${digit}.svg`}
        alt={`digit ${digit}`}
        width={Math.round(size * 1.35)}
        height={Math.round(size * 1.35)}
        style={{ borderRadius: 8 }}
      />
      Digit<span style={{ color: "var(--accent)" }}>ai</span>zer
    </span>
  );
}
