from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Start Questionnaire 🔥",
        callback_data="start_questionnaire"
    )
    markup.add(questionnaire_button)
    return markup


async def questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    Samagons = InlineKeyboardButton(
        "Samagon",
        callback_data="Samagon"
    )
    Tikils = InlineKeyboardButton(
        "Tikila",
        callback_data="Tikila"
    )
    markup.add(Samagons)
    markup.add(Tikils)
    return markup