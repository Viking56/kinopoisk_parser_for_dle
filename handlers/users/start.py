from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from keyboards.default import menu
from loader import dp


@dp.message_handler(Command("start"), state="*")
async def start(message: Message):
    """
    Срабатывает из любого состояния и отправлет пользователю кнопки для выбора действия
    """
    await message.answer("Выберите действие", reply_markup=menu)
