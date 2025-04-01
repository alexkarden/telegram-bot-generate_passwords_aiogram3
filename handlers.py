from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from keyboards import reply_but
from script import simple_password, strong_password



router = Router()
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('👋 <b>Привет </b> \nЯ генератор легких для запоминанию паролей. Сделайте свой выбор: ', reply_markup= await reply_but(), parse_mode=ParseMode.HTML)


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Это команда /help')

@router.message(Command('about'))
async def cmd_about(message: Message):
    await message.answer('<b>Alex Karden</b>\nhttps://github.com/alexkarden', parse_mode=ParseMode.HTML)

@router.message(Command('alexkarden'))
async def cmd_alexkarden(message: Message):
    await message.answer('<b>Алексей\n<a href="tel:+375297047262">+375-29-704-72-62</a></b>', parse_mode=ParseMode.HTML)

@router.message()
async def all_message(message: Message):
    text = message.text
    if text == 'Простой':
       await message.answer(await simple_password(3), parse_mode='html')
    elif text == 'Сложный':
       await message.answer(await strong_password(3), parse_mode='html')
    elif text == 'alexkarden':
         await message.answer('<b>Алексей\n<a href="tel:+375297047262">+375-29-704-72-62</a></b>', parse_mode=ParseMode.HTML)
    else:
         await message.answer('Воспользуйтесь клавиатурой ниже:', parse_mode='html')






