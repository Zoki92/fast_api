import logging
import os
from functools import lru_cache
from pydantic import BaseSettings


# log = logging.getLogger(__name__)


# class Settings(BaseSettings):
#     environment: str = os.getenv("Environment", "dev")
#     testing: bool = os.getenv("TESTING", 0)


# @lru_cache()
# def get_settings() -> BaseSettings:
#     log.info("Loading config settings to the environment")
#     return Settings()