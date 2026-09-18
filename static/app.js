const form = document.querySelector("#predict-form");
const button = document.querySelector("#predict-button");
const error = document.querySelector("#form-error");
const emptyState = document.querySelector("#empty-state");
const resultContent = document.querySelector("#result-content");
const score = document.querySelector("#score");
const message = document.querySelector("#result-message");
const meter = document.querySelector("#meter-fill");

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  error.textContent = "";
  button.disabled = true;
  button.querySelector("span:first-child").textContent = "Working...";

  const values = Object.fromEntries(new FormData(form).entries());

  try {
    const response = await fetch("/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(values)
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.error || "Something went wrong.");
    }

    emptyState.hidden = true;
    resultContent.hidden = false;
    score.textContent = data.prediction.toFixed(1);
    message.textContent = data.label;
    meter.style.width = data.prediction + "%";
  } catch (err) {
    error.textContent = err.message;
  } finally {
    button.disabled = false;
    button.querySelector("span:first-child").textContent = "Predict my score";
  }
});
