from contextlib import suppress

from aiogram.types.error_event import ErrorEvent
from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.api.exceptions import UnknownIntent

from bot.utils.logging import logger


async def handle_exception(error: ErrorEvent, dialog_manager: DialogManager, **kwargs):
    if isinstance(error.exception, UnknownIntent):
        with suppress(Exception):
            await error.update.callback_query.message.delete()
        user = error.update.callback_query.from_user
        # await dialog_manager.start(STATE, mode=StartMode.RESET_STACK)
        logger.info(f"Restart dialog for user '{user.full_name}' (tg_id: {user.id})")
        return False

    logger.error(f"Uncaught exception, exc: {error.exception}", exc_info=True)
