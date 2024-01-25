from itertools import chain

from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def category_keyboard():
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