import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from checkWord import checkWord

TOKEN = '1764547518:AAHvEJz9nGEeBIzPmvXpcqmmGrkKI5E_vmg'
from googletrans import Translator

translator = Translator()

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.reply("uz_imlo Botiga Xush Kelibsiz!")


@dp.message(Command('help'))
async def command_start_handler(message: Message) -> None:
    await message.reply("Botdan foydalanish uchun so'z yuboring.")


@dp.message()
async def echo_handler(message: types.Message) -> None:
    try:
        word = message.text
        result = checkWord(word)
        if result['available']:
            response = f"✅ {word.capitalize()}"
        else:
            response = f"❌{word.capitalize()}\n"
            for text in result['matches']:
                response += f"✅ {text.capitalize()}\n"
        await message.answer(response)
    except:
        await message.answer("Xatolik yuz berdi")


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
