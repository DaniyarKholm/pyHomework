from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp
import random



@dp.message_handler(commands=['start'])
async def start_command(message: types.Message) -> None:
    await bot.send_message(message.from_user.id, f'Приветствую тебя, {message.from_user.first_name}!')
    await message.answer('Чтобы сыграть в вкиторину напиши /quiz. Хочешь прикольную пикчу? Напиши /mem')


@dp.message_handler(commands=['mem'])
async def mem_handler(message: types.Message) -> None:
    await bot.send_photo(message.from_user.id, photo="http://forum.probki.net/uploads/monthly_07_2014/post-13384-14057168162335.jpg")

stickers = ["⚽️", "🏀", "🎲", "🎯", "🎳", "🎰"]


@dp.message_handler(commands=['game'])
async def game_message(message: types.Message):
    if message.text.startswith("game"):
        random_sticker = random.choice(stickers)
        await message.answer_sticker(random_sticker)



@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message) -> None:
    markup = InlineKeyboardMarkup()
    next_button = InlineKeyboardButton('Перейти к след вопросу', callback_data='next_button_1')
    markup.add(next_button)

    question = "Как зовут отца Пушкина?"
    answers = [
        "Сергей",
        "Андрей",
        "Игорек",
        "Криштиану Роналду",
    ]
    await message.answer_poll(
        question=question,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=0,
        open_period=10,
        reply_markup=markup
    )

def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(start_command, commands=['quiz'])
    dp.register_message_handler(start_command, commands=['mem'])
    dp.register_message_handler(start_command, commands=['game'])