import { useState } from "react";
import Header from "../components/Header";
import TaxForm from "../components/TaxForm";
import AdvicePanel from "../components/AdvicePanel";
import Footer from "../components/Footer";

export default function HomePage() {
  const [advice, setAdvice] = useState("");

  return (
    <>
      <Header />
      <main>
        <TaxForm setAdvice={setAdvice} />
        <AdvicePanel advice={advice} />
      </main>
      <Footer />
    </>
  );
}
