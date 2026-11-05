"""Configuración del backend: los secretos se leen desde variables de entorno."""
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    aruba_base_url = os.getenv("ARUBA_BASE_URL", "").rstrip("/")
    aruba_client_id = os.getenv("ARUBA_CLIENT_ID", "")
    aruba_client_secret = os.getenv("ARUBA_CLIENT_SECRET", "")
    aruba_refresh_token = os.getenv("ARUBA_REFRESH_TOKEN", "")

    @property
    def aruba_credentials_configured(self):
        return all([self.aruba_base_url, self.aruba_client_id, self.aruba_client_secret, self.aruba_refresh_token])

settings = Settings()
