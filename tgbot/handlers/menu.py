import logging

from aiogram import Router, F
from aiogram.types import Message

from tgbot.keyboards.inline import category_keyboard

menu_router = Router()


@menu_router.message(F.text.contains('Mahsulotlar'))
async def select_category(message: Message):
    logging.info(message)
    logging.info(f"{message.from_user.username=}")
    logging.info(f"{message.from_user.full_name=}")

    await message.answer(f"Mahsulot tanlang", reply_markup=category_keyboard())