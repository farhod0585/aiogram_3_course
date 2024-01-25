import logging

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from tgbot.keyboards.inline import courses_keyboard, books_keyboard, categories_keyboard, \
    telegram_keyboard

menu_router = Router()


@menu_router.message(F.text.contains('Mahsulotlar'))
async def select_category(message: Message):
    logging.info(message)
    logging.info(f"{message.from_user.username=}")
    logging.info(f"{message.from_user.full_name=}")

    await message.answer(f"Mahsulot tanlang", reply_markup=categories_keyboard())


@menu_router.callback_query(F.data == "courses")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await call.message.edit_reply_markup("Kurs tanlang", reply_markup=courses_keyboard())
    await call.answer(cache_time=60)


@menu_router.callback_query(F.data.contains("books"))
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.edit_reply_markup("Kitoblar", reply_markup=books_keyboard())
    await call.answer(cache_time=60)


@menu_router.callback_query(F.data == "cancel")
async def cancel_buying(call: CallbackQuery):
    # Oynada javob qaytaramiz

    await call.message.edit_reply_markup(reply_markup=categories_keyboard())
    await call.answer()


@menu_router.callback_query(F.data == "telegram")
async def buying_course(call: CallbackQuery):
    await call.message.edit_reply_markup(f"Siz Mukammal Telegram Bot Kursini tanladingiz.",
                              reply_markup=telegram_keyboard())

    await call.answer(cache_time=60)


@menu_router.callback_query(F.data == "python_book")
async def buying_book(call: CallbackQuery):
    await call.answer("Buyurtmangiz qabul qilindi", cache_time=60, show_alert=True)
