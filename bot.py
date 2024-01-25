import asyncio
import logging
import sys
from os import getenv

import wikipedia
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from icecream import ic

TOKEN = '1764547518:AAHvEJz9nGEeBIzPmvXpcqmmGrkKI5E_vmg'
wikipedia.set_lang('uz')

dp = Dispatcher()


@dp.message(CommandStart(), Command('help'))
async def command_start_handler(message: Message) -> None:
    """
        This handler will be called when user sends `/start` or `/help` command
        """
    await message.reply("Wikipeida Botiga Xush Kelibsiz!")


@dp.message()
async def echo_handler(message: types.Message) -> None:
    ic(message.chat.id)
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi")

async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
