import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from icecream import ic

TOKEN = '1764547518:AAHvEJz9nGEeBIzPmvXpcqmmGrkKI5E_vmg'
from oxfordLookup import getDefinitions
from googletrans import Translator

translator = Translator()

dp = Dispatcher()


@dp.message(CommandStart(), Command('help'))
async def command_start_handler(message: Message) -> None:
    """
        This handler will be called when user sends `/start` or `/help` command
        """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message()
async def echo_handler(message: types.Message) -> None:
    try:
        ic(message)
        lang = translator.detect(message.text).lang
        if len(message.text.split()) > 2:
            dest = 'uz' if lang == 'en' else 'en'
            await message.reply(translator.translate(message.text, dest).text)
        else:
            if lang == 'en':
                word_id = message.text
            else:
                word_id = translator.translate(message.text, dest='en').text

            lookup = getDefinitions(word_id)
            if lookup:
                await message.reply(f"Word: {word_id} \nDefinitions:\n{lookup['definitions']}")
                if lookup.get('audio'):
                    await message.reply_voice(lookup['audio'])
            else:
                await message.reply("Bunday so'z topilmadi")
    except:
        await message.answer("Xatolik yuz berdi")


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
