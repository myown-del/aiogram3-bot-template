import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram_dialog import DialogRegistry

from bot.config import Config
from bot.handlers import register_handlers, register_dialogs
from bot.middlewares import register_middlewares
from bot.db import db_pool
from bot.utils.logging import logger


async def main() -> None:
    logger.info(f"Starting bot...")

    loop = asyncio.get_running_loop()
    config = Config.from_env()
    bot = Bot(token=config.bot_token, parse_mode="HTML")
    dp = Dispatcher(storage=MemoryStorage())
    dialog_registry = DialogRegistry(dp)

    register_handlers(dp)
    register_middlewares(dp, db_pool=db_pool)
    register_dialogs(dialog_registry)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        logger.info("Bot stopped.")


try:
    asyncio.run(main())
except (KeyboardInterrupt, SystemExit):
    pass
