"""Base del cliente Aruba; los endpoints se validarán antes de activarlos."""
import httpx
from config import settings

class ArubaAPIError(Exception):
    pass

class ArubaAPI:
    def __init__(self):
        if not settings.aruba_base_url:
            raise ArubaAPIError("Falta configurar ARUBA_BASE_URL en las variables de entorno.")
        self.base_url = settings.aruba_base_url

    async def get(self, path: str, access_token: str) -> dict:
        url = f"{self.base_url}/{path.lstrip('/')}"
        headers = {"Authorization": f"Bearer {access_token}"}
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
