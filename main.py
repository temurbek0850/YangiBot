from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from datebase import user

from config import BOT_ADMIN_FROM_ID, BOT_TOKEN
from asyncio import run

dp = Dispatcher()

async def startUp_answer(bot: Bot):
    await bot.send_message(BOT_ADMIN_FROM_ID, "Bot ishga tushdi✅")

async def shutDown_answer(bot: Bot):
    await bot.send_message(BOT_ADMIN_FROM_ID, "Bot ishdan to`xtadi🚫")

async def start_answer(m: Message):
    t = user.select().where(user.from_id==m.from_user.id)
    if len(t)==0:
        u = user(
            from_id = m.from_user.id,
            first_name = m.from_user.first_name,
            last_name = m.from_user.last_name or 'Mavjud emas',
            user_name = m.from_user.username or 'Mavjud emas'
        )
        u.save()
    await m.answer('Assalomu alaykum Xush kelibsiz')

async def start():
    dp.startup.register(startUp_answer)
    dp.shutdown.register(shutDown_answer)
    dp.message.register(start_answer, Command("start"))

    bot = Bot(BOT_TOKEN)
    await dp.start_polling(bot, polling_timeout=1)

run(start())