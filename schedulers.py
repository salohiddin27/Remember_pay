import os

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from dotenv import load_dotenv

from loader import bot
scheduler = AsyncIOScheduler()
load_dotenv()
guruh_id = os.getenv("GURUH_ID")
async def send_daily_message():
   await bot.send_message(chat_id=guruh_id, text="Assalomu alaykum qardoshlar 👋\niltimos kominal to'lovni tekshirib qo'yaylik 📲\n\n"
                                                 "agar to'lov qilsangiz guruhga check tashlashni unutmang😇\n\n"
                                                 "1.Light code: 0293805\n2.Water code: 2628336808\n3.Gas code: 09271757\n\n@akma1_577\n"
                                                 "@PA70101\n@Javoh1r65_05\n@Mr_muhammadnur\n")

scheduler.add_job(send_daily_message, "interval", seconds=6)

def start_scheduler():
    scheduler.start()