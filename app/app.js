"use strict";

const phi = (1 + Math.sqrt(5)) / 2;
const result = document.querySelector("#result");
const copyButton = document.querySelector("#copy-button");
const copyLabel = document.querySelector("#copy-label");
const copyStatus = document.querySelector("#copy-status");

result.textContent = phi.toPrecision(16);

let resetTimer;

copyButton.addEventListener("click", async () => {
  window.clearTimeout(resetTimer);

  try {
    await navigator.clipboard.writeText(result.textContent);
    copyLabel.textContent = "Valeur copiée";
    copyStatus.textContent = "Le nombre d’or est dans le presse-papiers.";
  } catch {
    copyStatus.textContent =
      "Copie automatique indisponible. Sélectionne la valeur pour la copier.";
  }

  resetTimer = window.setTimeout(() => {
    copyLabel.textContent = "Copier la valeur";
    copyStatus.textContent = "";
  }, 2500);
});

if ("serviceWorker" in navigator && location.protocol !== "file:") {
  window.addEventListener("load", () => {
    navigator.serviceWorker.register("./service-worker.js").catch((error) => {
      console.error("Enregistrement hors ligne impossible :", error);
    });
  });
}
