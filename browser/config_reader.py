from config.settings import Settings

class ConfigReader:
    @staticmethod
    def get_ui_base_url() -> str:
        return Settings.UI_BASE_URL

    @staticmethod
    def get_browser_type() -> str:
        return Settings.BROWSER_TYPE

    @staticmethod
    def get_user_name() -> str:
        return Settings.USERNAME

    @staticmethod
    def get_password() -> str:
        return Settings.PASSWORD

    @staticmethod
    def get_headless() -> bool:
        return Settings.HEADLESS