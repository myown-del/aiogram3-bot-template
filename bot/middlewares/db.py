from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from bot.db.dals import get_dal_controller


class DbSessionMiddleware(BaseMiddleware):
    def __init__(self, db_pool: sessionmaker):
        super().__init__()
        self.db_pool = db_pool

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        async with self.db_pool() as session:
            session: AsyncSession
            data["dal"] = get_dal_controller(session)
            return await handler(event, data)
