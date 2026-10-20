from aiogram.enums import ChatType
from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery

class IsGroup(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.chat.type in (
            ChatType.GROUP,
            ChatType.SUPERGROUP,
            ChatType.CHANNEL,
        )

class IsGroupCall(BaseFilter):
    async def __call__(self, call: CallbackQuery) -> bool:
        # Check if the callback query is associated with a message
        if call.message:
            return call.message.chat.type in (
                ChatType.GROUP,
                ChatType.SUPERGROUP,
                ChatType.CHANNEL,
            )
        return False
