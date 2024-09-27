import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

from config import TELEGRAM_API
from service import get_currency

bot = Bot(token=TELEGRAM_API)
dp = Dispatcher()


user_data = {}


@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    await message.answer("Добрый день. Как вас зовут?")
    user_data[message.from_user.id] = {'awaiting_name': True}


@dp.message()
async def get_name(message: types.Message):
    user_id = message.from_user.id
    currency = get_currency()
    if user_data.get(user_id, {}).get('awaiting_name'):
        name = message.text
        user_data[user_id] = {'name': name, 'awaiting_name': False}
        await message.answer(f"Рад знакомству, {name}! Курс доллара сегодня {currency:.2f}р.")


async def main() -> None:
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
