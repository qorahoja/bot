import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
import subprocess  # Import subprocess to run the script

# Set up logging
logging.basicConfig(level=logging.INFO)

# Replace 'YOUR_BOT_TOKEN' with your actual bot token obtained from @BotFather on Telegram
BOT_TOKEN = '6141302747:AAFNdXtwbeLjs8Ii8jSvQnMv7Jc1A-RwIKQ'
# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Start command handler
@dp.message_handler(commands=['start'])
async def on_start(message: types.Message):
    await message.answer("Assalomu alaykom men USA track musiqa kanalinign boti bo'laman iltimos savol yoki takliflaringiz bo'lsa yozib qoldiring sizga adminimiz javob yozadi")



if __name__ == '__main':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
