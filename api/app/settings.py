import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application Settings
    """

    # Service variables
    menu_name: str

    # App settings
    app_name: str
    app_description: str

    # Database settings
    mashgin_db_host: str
    mashgin_db_port: str
    mashgin_db_user: str
    mashgin_db_password: str
    mashgin_db_name: str
    mashgin_db_echo_sql: bool

    class Config:
        env_file = ".env.local"
