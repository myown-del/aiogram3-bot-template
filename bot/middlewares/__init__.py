from aiogram import Dispatcher
from sqlalchemy.orm import sessionmaker

from .db import DbSessionMiddleware

__all__ = (
    'DbSessionMiddleware'
)


def register_middlewares(dp: Dispatcher, db_pool: sessionmaker) -> None:
    dp.update.outer_middleware(DbSessionMiddleware(db_pool))
