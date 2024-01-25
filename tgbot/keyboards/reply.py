from itertools import chain

from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def menu_keyboard():
    keyboard = ReplyKeyboardBuilder()
    buttons = [
        ['Python'],
        ["Telegram bot"],
    ]
    keyboard.row(*[KeyboardButton(text=i) for i in chain(*buttons)])
    return keyboard.as_markup(resize_keyboard=True)


def menuPython_keyboard():
    keyboard = ReplyKeyboardBuilder()
    buttons = [
        ["#00 Kirish", "#01 Kerarkli dasturlar", "#02 Hello World!"],
        ["Ortga", "Boshiga"],
    ]
    keyboard.row(*[KeyboardButton(text=i) for i in chain(*buttons)], width=3)
    return keyboard.as_markup(resize_keyboard=True)


def menuStart_keyboard():
    keyboard = ReplyKeyboardBuilder()
    keyboard.row(*[KeyboardButton(text='Contact', request_contact=True)])
    keyboard.row(*[KeyboardButton(text='Location', request_location=True)])
    return keyboard.as_markup(resize_keyboard=True)