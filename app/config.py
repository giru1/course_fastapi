from typing import List

from pydantic import BaseSettings, root_validator


class Settings(BaseSettings):
    """
    Класс настроек
    """
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    class Config:
        """
        Путь к файлу со скрытыми данными для подключения и тестирование бд
        """
        env_file = 'app/.env'
        orm_mode = True


settings = Settings()


