from transliterate import translit
import random
from config import list_of_en_words, list_of_ru_words, list_of_spec_symb,list_of_numbers

async def get_word_ru():
    random_word = random.choice(list_of_ru_words)
    return random_word

async def get_word_en():
    random_word = random.choice(list_of_en_words)
    return random_word

async def get_spec_symb():
    random_spec_symb = random.choice(list_of_spec_symb)
    return random_spec_symb

async def get_number():
    random_number = random.choice(list_of_numbers)
    return random_number


async def simple_password_ru(x):
    fullpass=''
    fulpass_desc=''
    password_list =[]
    for i in range(x):
        y = await get_word_ru()
        password_list.append(y)
    n=await get_number()
    password_list.append(n)
    for i2 in password_list:
        pass2 = i2[:4]
        pass_desc = i2
        fullpass += pass2
        fulpass_desc += pass_desc+' '
    text_for_bot = f'Пароль: {translit(fullpass, language_code='ru', reversed=True)} \nМнемоника: {fulpass_desc}'
    return text_for_bot

async def strong_password_ru(x):
    fullpass=''
    fulpass_desc=''
    password_list =[]
    for i in range(x):
        y = await get_word_ru()
        password_list.append(y)
        y2 = await get_number()
        password_list.append(y2)
    n=await get_spec_symb()
    password_list.append(n)
    for i2 in password_list:
        pass2 = i2[:4]
        pass_desc = i2
        fullpass += pass2
        fulpass_desc += pass_desc+' '
    text_for_bot = f'Пароль: {translit(fullpass, language_code='ru', reversed=True)} \nМнемоника: {fulpass_desc}'
    return text_for_bot


async def simple_password_en(x):
    fullpass=''
    fulpass_desc=''
    password_list =[]
    for i in range(x):
        y = await get_word_en()
        password_list.append(y)
    n=await get_number()
    password_list.append(n)
    for i2 in password_list:
        pass2 = i2[:4]
        pass_desc = i2
        fullpass += pass2
        fulpass_desc += pass_desc+' '
    text_for_bot = f'Пароль: {translit(fullpass, language_code='ru', reversed=True)} \nМнемоника: {fulpass_desc}'
    return text_for_bot

async def strong_password_en(x):
    fullpass=''
    fulpass_desc=''
    password_list =[]
    for i in range(x):
        y = await get_word_en()
        password_list.append(y)
        y2 = await get_number()
        password_list.append(y2)
    n=await get_spec_symb()
    password_list.append(n)
    for i2 in password_list:
        pass2 = i2[:4]
        pass_desc = i2
        fullpass += pass2
        fulpass_desc += pass_desc+' '
    text_for_bot = f'Пароль: {translit(fullpass, language_code='ru', reversed=True)} \nМнемоника: {fulpass_desc}'
    return text_for_bot