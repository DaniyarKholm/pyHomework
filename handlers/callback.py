from aiogram import types, Dispatcher
from config import dp
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@dp.callback_query_handler(text='next_button_1')
async def quiz_2(callback: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    next_button = InlineKeyboardButton('Перейти к след вопросу', callback_data='next_button_2')
    markup.add(next_button)

    quiestion = "Сколько будет 2+2"
    answers = [
        "1",
        "2",
        "3",
        "4",
    ]


    await callback.message.answer_poll(
        question=quiestion,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=3,
        explanation='Это база.',
        open_period=10,
        reply_markup=markup
    )

@dp.callback_query_handler(text='next_button_2')
async def quiz_3(callback: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    next_button = InlineKeyboardButton('Перейти к след вопросу', callback_data='next_button_3')
    markup.add(next_button)
    question3 = "Действующий президент РФ?"
    answers = [
        "Ангела Меркель",
        "Садыр Жапаров",
        "Владимир Зеленский",
        "Владимир Путин",
    ]

    await callback.message.answer_poll(
        question=question3,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=3,
        explanation='Такое даже детки в Африке знают :(',
        open_period=10,
        reply_markup=markup
    )

async def quiz_4(callback: types.CallbackQuery):
    await callback.message.answer("Это были все вопросы! Удачи!)")

def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text='next_button_1')
    dp.register_callback_query_handler(quiz_3, text='next_button_2')
    dp.register_callback_query_handler(quiz_4, text='next_button_3')