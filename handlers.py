from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from keyboards import main_lg, main_pw_rus, main_pw_eng
from script import simple_password_ru, strong_password_ru,simple_password_en, strong_password_en



router = Router()
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('👋 <b>Привет!</b>\nЯ генератор легких для запоминания паролей. Пожалуйста выберите язык:\n<b>/lang</b>', parse_mode=ParseMode.HTML)
    await message.answer('👋 <b>Hello!</b>\nI am an easy to remember password generator. Please select a language:\n<b>/lang</b>', parse_mode=ParseMode.HTML)

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Это команда /help')


@router.message(Command('lang'))
async def cmd_help(message: Message):
    await message.reply('<b>Язык/Language:</b>', reply_markup=main_lg, parse_mode=ParseMode.HTML)


@router.message(Command('about'))
async def cmd_about(message: Message):
    await message.answer('<b>Alex Karden</b>\nhttps://github.com/alexkarden', parse_mode=ParseMode.HTML)

@router.message(Command('alexkarden'))
async def cmd_alexkarden(message: Message):
    await message.answer('<b>Алексей\n<a href="tel:+375297047262">+375-29-704-72-62</a></b>', parse_mode=ParseMode.HTML)

@router.message()
async def all_message(message: Message):
    text = message.text
    if text == 'Русский':
       await message.answer('Какой пароль хотите: Простой или Сложный?',reply_markup=main_pw_rus,  parse_mode='html')
    elif text == 'English':
       await message.answer('What kind of password do you want: Easy or Strong?',reply_markup=main_pw_eng,  parse_mode='html')
    elif text == 'Простой':
       await message.answer(await simple_password_ru(3), parse_mode='html')
    elif text == 'Сложный':
       await message.answer(await strong_password_ru(3), parse_mode='html')
    elif text == 'Easy':
       await message.answer(await simple_password_en(3), parse_mode='html')
    elif text == 'Strong':
       await message.answer(await strong_password_en(3), parse_mode='html')
    elif text == 'alexkarden':
         await message.answer('<b>Алексей\n<a href="tel:+375297047262">+375-29-704-72-62</a></b>', parse_mode=ParseMode.HTML)
    else:
         await message.answer('Воспользуйтесь клавиатурой ниже:', parse_mode='html')






