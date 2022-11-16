from aiogram import Router
from sqlalchemy.orm import sessionmaker

from .db import DbSessionMiddleware

__all__ = (
    'DbSessionMiddleware'
)


def register_middlewares(router: Router, db_pool: sessionmaker) -> None:
    router.message.middleware(DbSessionMiddleware(db_pool))
    router.callback_query.middleware(DbSessionMiddleware(db_pool))
