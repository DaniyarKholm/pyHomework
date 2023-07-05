from aiogram import types, Dispatcher
from config import dp, bot
# import random

# stickers = ["⚽️", "🏀", "🎲", "🎯", "🎳", "🎰"]


# async def echo_game(message: types.Message) -> None:
#     random_sticker = random.choice(stickers)
#     await bot.send_sticker(message.chat.id, random_sticker)


async def echo_text(message: types.Message) -> None:
    await bot.send_message(message.chat.id, f'Для запуска бота, напиши команду /start')

def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo_text, content_types=['text'])