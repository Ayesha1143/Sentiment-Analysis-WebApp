// Change this if your FastAPI backend runs on a different host/port.
const API_URL = "http://127.0.0.1:8000/predict";

const textInput = document.getElementById("textInput");
const predictBtn = document.getElementById("predictBtn");
const loading = document.getElementById("loading");
const resultCard = document.getElementById("resultCard");
const errorBox = document.getElementById("errorBox");
const emojiEl = document.getElementById("emoji");
const predictionLabelEl = document.getElementById("predictionLabel");
const confidenceEl = document.getElementById("confidence");

const EMOJI_MAP = {
  Positive: "😊",
  Neutral: "😐",
  Negative: "😞",
};

function resetUI() {
  resultCard.classList.add("hidden");
  errorBox.classList.add("hidden");
}

function showError(message) {
  errorBox.textContent = message;
  errorBox.classList.remove("hidden");
}

function showResult(prediction, confidence) {
  emojiEl.textContent = EMOJI_MAP[prediction] || "🤔";
  predictionLabelEl.textContent = prediction;
  predictionLabelEl.className = "prediction-label " + prediction.toLowerCase();
  confidenceEl.textContent = `Confidence: ${(confidence * 100).toFixed(1)}%`;
  resultCard.classList.remove("hidden");
}

async function predictSentiment() {
  const text = textInput.value.trim();
  resetUI();

  if (!text) {
    showError("Please enter some text before predicting.");
    return;
  }

  predictBtn.disabled = true;
  loading.classList.remove("hidden");

  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.detail || "Something went wrong. Please try again.");
    }

    showResult(data.prediction, data.confidence);
  } catch (err) {
    showError(
      err.message === "Failed to fetch"
        ? "Could not reach the backend. Is the FastAPI server running?"
        : err.message
    );
  } finally {
    predictBtn.disabled = false;
    loading.classList.add("hidden");
  }
}

predictBtn.addEventListener("click", predictSentiment);

// Allow Ctrl+Enter / Cmd+Enter to submit from the textarea
textInput.addEventListener("keydown", (e) => {
  if ((e.ctrlKey || e.metaKey) && e.key === "Enter") {
    predictSentiment();
  }
});
