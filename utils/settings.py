from .custom_types import *

class Settings(BaseSettings):
    api_key: str = os.environ.get("API_KEY")
    api_admin: str = os.environ.get("API_ADMIN")
    vk_oovc: str = os.environ.get("VK_OOVC")
    vk_admin: str = os.environ.get("VK_ADMIN")
    
settings = Settings()