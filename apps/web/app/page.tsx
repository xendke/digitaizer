import Nav from "./components/Nav";
import DrawDemo from "./components/DrawDemo";
import FAQ from "./components/FAQ";
import Footer from "./components/Footer";

export default function Home() {
  return (
    <>
      <Nav />

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
      <Footer />
    </>
  );
}
