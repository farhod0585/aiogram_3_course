from itertools import chain

from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def categories_keyboard():
    keyboard = InlineKeyboardBuilder()
    buttons = [
        ["💻 Kurslar", "courses"],
        ["📚 Kitoblar", "books"],
    ]
    keyboard.row(*[InlineKeyboardButton(text=i[0], callback_data=i[1]) for i in chain(buttons)], width=1)
    keyboard.row(InlineKeyboardButton(text="🔗 Mohirdev sahifasiga o'tish", url="https://mohirdev.uz/courses/telegram"))
    keyboard.row(InlineKeyboardButton(text="🔍 Qidirish", switch_inline_query_current_chat=""))
    keyboard.row(InlineKeyboardButton(text="✉️Ulashish", switch_inline_query="Zo'r bot ekan"))
    return keyboard.as_markup()

def courses_keyboard():
    keyboard = InlineKeyboardBuilder()
    buttons = [
        ["🐍 Python Dasturlash Asoslari", "python"],
        ["🌐 Django Web Dasturlash", "django"],
        ["🤖 Mukammal Telegram bot", "telegram"],
        ["📈 Ma'lumotlar Tuzilmasi va Algoritmlar", "algorithm"],
        ["🔙 Ortga", "cancel"],
    ]
    keyboard.row(*[InlineKeyboardButton(text=i[0], callback_data=i[1]) for i in chain(buttons)], width=1)
    return keyboard.as_markup()

def books_keyboard():
    keyboard = InlineKeyboardBuilder()
    buttons = [
        ["Python. Dasturlash asoslari", "python_book"],
        ["C++. Dasturlash tili", "cpp_book"],
        ["Mukammal Dasturlash. JavaScript", "js_book"],
        ["🔙 Ortga", "cancel"],
    ]
    keyboard.row(*[InlineKeyboardButton(text=i[0], callback_data=i[1]) for i in chain(buttons)], width=1)
    return keyboard.as_markup()

def telegram_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="🔗 Mohirdev sahifasiga o'tish", url="https://mohirdev.uz/courses/telegram"))
    return keyboard.as_markup()

def algoritm_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Ko'rish", url="https://mohirdev.uz/courses/algoritmlar/"))
    return keyboard.as_markup()
