async function loadWidget() {
  const userId = window.userId || "anon";

  try {
    const res = await fetch(
      `https://ai-tracker-widget-1.onrender.com/predict/${userId}`
    );
    const data = await res.json();

    const div = document.createElement("div");

    div.style = `
      position: fixed;
      bottom: 20px;
      right: 20px;
      background: #111;
      color: white;
      padding: 12px;
      border-radius: 8px;
      font-family: Arial;
      z-index: 9999;
    `;

    div.innerHTML = `
      <b>AI Insight</b><br/>
      Events: ${data.events}<br/>
      Score: ${data.score}
    `;

    document.body.appendChild(div);
  } catch (e) {
    console.error("Widget error:", e);
  }
}

// wait a bit so events get tracked first
setTimeout(loadWidget, 1000);
