from aiogram.types import Message
from aiogram_dialog import DialogManager

from bot.utils.logging import logger


async def handle_start(message: Message, dialog_manager: DialogManager) -> None:
    logger.info(f"Got a start command from user '{message.from_user.full_name}' (tg_id: {message.from_user.id})")
