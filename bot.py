from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os

TOKEN = os.getenv("TOKEN")  # Tokenni atrof-muhit o‘zgaruvchisi sifatida olish

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum! Men sizning Telegram botingizman!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
