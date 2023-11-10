import sqlite3

from aiogram import types, Dispatcher
from config import bot
from database.sql_commands import Database
from keyboards.inline_buttons import questionnaire_keyboard


async def start_questionnaire_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Samagon или Tikila ?",
        reply_markup=await questionnaire_keyboard()
    )


async def Samagon(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="U R Samagon"
    )


async def Tikila(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="U R Tikila"
    )


def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_questionnaire_call,
                                       lambda call: call.data == "start_questionnaire")
    dp.register_callback_query_handler(Samagon,
                                       lambda call: call.data == "Samagon")
    dp.register_callback_query_handler(Tikila,
                                       lambda call: call.data == "Tikila")