from itertools import chain

from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def menu_keyboard():
    keyboard = ReplyKeyboardBuilder()
    buttons = [
        ['🛍️ Mahsulotlar'],
        ["ℹ️Qoʼllanma"],
    ]
    keyboard.row(*[KeyboardButton(text=i) for i in chain(*buttons)])
    return keyboard.as_markup(resize_keyboard=True)
