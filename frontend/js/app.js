// Dirección del backend durante el desarrollo local.
// Más adelante cambiaremos esta dirección al desplegar el servidor.
const API_BASE_URL = "http://127.0.0.1:8000";

const checkButton = document.getElementById("checkBackendButton");
const statusLabel = document.getElementById("backendStatus");
const messageLabel = document.getElementById("backendMessage");
const statusDot = document.getElementById("statusDot");

async function checkBackend() {
  checkButton.disabled = true;
  statusLabel.textContent = "Comprobando...";
  messageLabel.textContent = "Intentando contactar el servidor local.";
  statusDot.className = "status-dot";

  try {
    const response = await fetch(`${API_BASE_URL}/api/health`);
    if (!response.ok) throw new Error(`Estado HTTP ${response.status}`);

    const data = await response.json();
    statusLabel.textContent = "Backend conectado";
    messageLabel.textContent = data.message;
    statusDot.className = "status-dot ok";
  } catch (error) {
    statusLabel.textContent = "Backend no disponible";
    messageLabel.textContent = "Inicia el backend local y vuelve a intentarlo.";
    statusDot.className = "status-dot error";
    console.error("Error comprobando backend:", error);
  } finally {
    checkButton.disabled = false;
  }
}

checkButton.addEventListener("click", checkBackend);
