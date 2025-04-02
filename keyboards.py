from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from config import list_of_buttons


async def reply_but():
    keyboard =ReplyKeyboardBuilder()
    for currency in list_of_buttons:
        keyboard.add(KeyboardButton(text = currency))
    return keyboard.adjust(1).as_markup(resize_keyboard=True)


main_lg = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Русский')],
    [KeyboardButton(text='English')]
], resize_keyboard=True)

main_pw_rus = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Простой')],
    [KeyboardButton(text='Сложный')]
], resize_keyboard=True)

main_pw_eng = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Easy')],
    [KeyboardButton(text='Strong')]
], resize_keyboard=True)