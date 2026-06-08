import Nav from "./components/Nav";
import DrawDemo from "./components/DrawDemo";
import FAQ from "./components/FAQ";
import Footer from "./components/Footer";

export default function Home() {
  return (
    <>
      <Nav />

      <main className="wrap hero" id="demo">
        <span className="eyebrow">Handwritten digit recognition</span>
        <h1>
          Draw a number. <em>Watch the network read it.</em>
        </h1>
        <p className="hero__sub">
          Sketch any digit and a neural network guesses what you wrote — with a
          live confidence breakdown across every number from zero to nine. No
          sign-up, works on any device.
        </p>
      </main>

      <div className="wrap demo-wrap">
        <DrawDemo />
      </div>

      <FAQ />
      <Footer />
    </>
  );
}
