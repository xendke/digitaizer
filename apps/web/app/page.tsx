import type { Metadata } from "next";
import Nav from "./components/Nav";
import DrawDemo from "./components/DrawDemo";
import FAQ from "./components/FAQ";
import Footer from "./components/Footer";

export const dynamic = "force-dynamic";

function pickDigit() {
  return new Date().getMinutes() % 10;
}

export async function generateMetadata(): Promise<Metadata> {
  const digit = pickDigit();
  return {
    title: "Digitaizer — Draw a digit, let the network read it",
    icons: { icon: `/digits/${digit}.svg` },
  };
}

export default function Home() {
  const digit = pickDigit();

  return (
    <>
      <Nav digit={digit} />

      <main className="wrap hero" id="demo" style={{ paddingTop: 0 }}>
        <span className="eyebrow">Handwritten digit recognition</span>
        <h1>
          Draw a number. <em>Watch the network read it.</em>
        </h1>
      </main>

      <div className="wrap demo-wrap">
        <DrawDemo />
      </div>

      <FAQ />
      <Footer digit={digit} />
    </>
  );
}
