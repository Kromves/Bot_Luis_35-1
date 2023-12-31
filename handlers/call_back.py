import sqlite3

from aiogram import types, Dispatcher
from config import bot, ADMIN_ID
from database.sql_commands import Database
from keyboards.inline_buttons import questionnaire_keyboard
# from scraping.my_scraping import LisScraper
# from scraping.async_news import AsyncNewsScraper
import re
async def start_questionnaire_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Python or Mojo ?",
        reply_markup=await questionnaire_keyboard()
    )


async def python_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="U R Python Developer 🐍"
    )


async def mojo_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="U R Mojo Developer 🔥"
    )


async def admin_call(message: types.Message):
    print(ADMIN_ID)
    print(message.from_user.id)
    if message.from_user.id == int(ADMIN_ID):
        await message.delete()
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Hello master 🐲"
        )
    else:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="U r not my master 🤬"
        )


# async def lis_scraper_call(call: types.CallbackQuery):
#     scraper = LisScraper()
#     data = scraper.lis_parse_data()
#     for url in data[:4]:
#         await bot.send_message(
#             chat_id=call.from_user.id,
#             text=url
#         )


def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_questionnaire_call,
                                       lambda call: call.data == "start_questionnaire")
    dp.register_callback_query_handler(python_call,
                                       lambda call: call.data == "python")
    dp.register_callback_query_handler(mojo_call,
                                       lambda call: call.data == "mojo")
    dp.register_message_handler(admin_call,
                                lambda word: "dorei" in word.text)
    # dp.register_callback_query_handler(lis_scraper_call,
    #                                    lambda call: call.data == "news"
    #                                    )