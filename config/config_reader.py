import json
import os

class ConfigReader:
    def __init__(self, path="config/config.json"):
        try:
            with open(path) as f:
                self.config = json.load(f)
        except FileNotFoundError:
            raise ValueError(f"Config file not found at {path}")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON config file")

    def get(self, key, default=None):
        keys = key.split('.')  # Split dot notation
        value = self.config

        try:
            for k in keys:
                value = value[k]
            return value
        except (KeyError, TypeError):
            return default

    def get_required(self, key):
        """Get a key that MUST exist"""
        value = self.get(key)
        if value is None:
            raise KeyError(f"Required config key '{key}' missing")
        return value