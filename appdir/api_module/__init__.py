import requests

from appdir.config import Config

class APIClient:
    """Represent base URL + end point."""
    def __init__(self, base_url: str, endpoint: str, headers=None):
        self._base_url = base_url.rstrip("/")
        self._endpoint = endpoint.lstrip("/").rstrip("/")
        self._headers = headers
        self.url = self._build_url()

    def _build_url(self):
        return f"{self._base_url}/{self._endpoint}"

    def post(self, json=None):
        response = requests.post(self.url, headers=self._headers, json=json)
        return response
    
    # classmethod when using Plausible Analytics
    @classmethod
    def for_plausible(cls):
        headers = {
            'Authorization': f'Bearer {Config.API_KEY}',
            'Content-Type': 'application/json'
        }
        return cls(
            base_url=Config.API_BASE, 
            endpoint=Config.API_END,
            headers=headers)