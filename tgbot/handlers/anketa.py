from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from tgbot.states.personalData import PersonalData

state_router = Router()


# /form komandasi uchun handler yaratamiz. Bu yerda foydalanuvchi hech qanday holatda emas, None
@state_router.message(Command("form"))
async def enter_test(message: Message, state: FSMContext):
    await message.answer("To'liq ismingizni kiriting")
    await state.set_state(PersonalData.fullName)


@state_router.message(PersonalData.fullName)
async def answer_full_name(message: Message, state: FSMContext):
    full_name = message.text

    data = await state.get_data()
    data["full_name"] = full_name
    await state.set_data(data)

    await message.answer("Email manzil kiriting")

    await state.set_state(PersonalData.email)

@state_router.message(PersonalData.email)
async def answer_email(message: Message, state: FSMContext):
    email = message.text

    data = await state.get_data()
    data["email"] = email
    await state.set_data(data)

    await message.answer("Telefon raqam kiriting")

    await state.set_state(PersonalData.phoneNum)


@state_router.message(PersonalData.phoneNum)
async def answer_phone(message: Message, state: FSMContext):
    phone = "".join(message.text.split())

    data = await state.get_data()
    data["phone"] = phone
    await state.set_data(data)
    # Ma`lumotlarni qayta o'qiymiz
    data = await state.get_data()
    full_name = data.get("full_name")
    email = data.get("email")
    phone = data.get("phone")

    msg = "Quyidai ma`lumotlar qabul qilindi:\n"
    msg += f"Ismingiz - {full_name}\n"
    msg += f"Email - {email}\n"
    msg += f"Telefon: - {phone}"
    await message.answer(msg)

    # State dan chiqaramiz
    # 1-variant
    await state.clear()
