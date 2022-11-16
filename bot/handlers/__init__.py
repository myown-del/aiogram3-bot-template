__all__ = (
    'register_handlers',
    'register_dialogs'
)

from aiogram import Router
from aiogram.filters.command import CommandStart

from bot.handlers.commands import handle_start
from bot.handlers.exceptions import handle_exception
from bot.handlers.dialogs import register_dialogs
from bot.config import Config

config = Config.from_env()


def register_handlers(router: Router) -> None:
    """
    Зарегистрировать все хендлеры
    :param router:
    """
    router.message.register(handle_start, CommandStart())
    router.errors.register(handle_exception)
