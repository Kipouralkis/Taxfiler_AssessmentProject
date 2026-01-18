import { useState } from "react";

export default function TaxForm({ setAdvice }) {

  const [form, setForm] = useState({
    income: "",
    expenses: "",
    filing_status: "",
    dependents: "",
    investment_assets: ""
});


  const update = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const response = await fetch("http://localhost:8000/api/tax", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form)
    });

    const data = await response.json();
    setAdvice(data.advice);
};


  return (
    <form onSubmit={handleSubmit}>
      <div className="form-heading">
        <h1>Welcome to EasyTax! the Tax Filing Assistant.</h1>
        <p>File your taxes with our easy-to-use tax filing system. Easily and securely. <br/> To begin, enter your tax information below:</p>
      </div>
      <div className="form-group">
        <label>Income *</label>
        <input name="income" value={form.income} onChange={update} />
      </div>

      <div className="form-group">
        <label>Expenses *</label>
        <input name="expenses" value={form.expenses} onChange={update} />
      </div>

      <div className="form-group">
        <label>Filing Status *</label>
        <select name="filing_status" value={form.filing_status} onChange={update}>
          <option value="">Select Filing Status</option>
          <option value="single">Single</option>
          <option value="married-jointly">Married Filing Jointly</option>
          <option value="married-separately">Married Filing Separately</option>
          <option value="widower">Qualifying Widow(er)</option>
        </select>
      </div>

      <div className="form-group">
        <label>Dependents *</label>
        <input type="number" name="dependents" value={form.dependents} onChange={update} />
      </div>

      <div className="form-group">
        <label>Investment Assets</label>
        <textarea name="investment_assets" value={form.investment_assets} onChange={update} />
      </div>

      <button type="submit">Submit</button>
    </form>
  );
}
