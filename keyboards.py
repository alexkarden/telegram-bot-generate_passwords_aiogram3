from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from config import list_of_buttons


async def reply_but():
    keyboard =ReplyKeyboardBuilder()
    for currency in list_of_buttons:
        keyboard.add(KeyboardButton(text = currency))
    return keyboard.adjust(1).as_markup(resize_keyboard=True)


