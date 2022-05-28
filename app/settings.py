"""Application settings."""
import os

from pydantic import BaseSettings, Field, RedisDsn


class AppSettings(BaseSettings):
    """Application settings class."""

    redis_dsn: RedisDsn = Field('redis://localhost:6379/1', description='адрес редис хоста')
    timeout: int = Field(10, description='время ожидания ответа сервера canyon')
    throttling_time: float = Field(600.0, description='время ожидания между обновлениями')
    debug: bool = Field(False, description='настройка уровня логирования')
    amount_of_iterations: int = Field(0, description='сколько раз будет запускаться функция main')


app_settings = AppSettings(
    _env_file=os.path.join(os.path.dirname(__file__), '..', '.env'),
)
