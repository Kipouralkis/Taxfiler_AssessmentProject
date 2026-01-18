export default function AdvicePanel({ advice }) {
  if (!advice) return null;

  return (
    <section className="advice-section">
      <div className="advice container gradient-border border">
        <div className="advice-inner">
          <h2>Your Tax Advice</h2>
          <div dangerouslySetInnerHTML={{ __html: advice }} />
        </div>
      </div>
    </section>
  );
}
