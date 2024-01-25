from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from tgbot.keyboards.reply import menu_keyboard

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message):
    await message.answer(f"Assalom alaykum, {message.from_user.full_name}, do'konimizga xush kelibsiz!",
                         reply_markup=menu_keyboard())
