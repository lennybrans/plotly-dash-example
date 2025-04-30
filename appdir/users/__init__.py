import os
import json

from appdir.config import Config

class User:
    """Define a User."""
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.settings = self._settings()
        
    def _settings(self):
        path = os.path.join(
            os.getcwd(), Config.USER_SETTINGS ,f"{self.first_name}.json"
            )
        if not os.path.exists(path):
            default_settings = {
                "user_name": self.first_name,
                "settings": {}
            }
            with open(path, mode='w', encoding="utf-8") as write_file:
                json.dump(default_settings, write_file, indent=4)
        
        with open(path, mode='r', encoding="utf-8") as read_file:
            settings = json.load(read_file)
            return settings
        
    def inject_setting(dict: dict):
        pass
