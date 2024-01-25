from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from tgbot.keyboards.reply import menu_keyboard, menuPython_keyboard

menu_router = Router()
@menu_router.message(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Kurslarni tanlang", reply_markup=menu_keyboard())

@menu_router.message(F.text == 'Telegram bot')
async def send_link(message: Message):
    await message.answer("Mukammal Telegram bot kursi: https://mohirdev.uz/courses/telegram")

@menu_router.message(F.text == 'Python')
async def send_link(message: Message):
    await message.answer("Mavzu tanlang", reply_markup=menuPython_keyboard())

@menu_router.message(F.text == '#00 Kirish')
async def send_link(message: Message):
    await message.answer("https://python.sariq.dev", reply_markup=ReplyKeyboardRemove())

@menu_router.message(F.text == 'Boshiga')
async def send_link(message: Message):
    await message.answer("Kurslarni tanlang", reply_markup=menu_keyboard())