import asyncio
import logging
import sys

from aiogram import  F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from loader import dp, bot
from schedulers import start_scheduler



@dp.message(Command('start'))
async def start_command(callback: CallbackQuery):
     await callback.answer("Assalomu alaykum xush kelibsiz!\nkerakli buttoni tanlang ⬇️")

     ikb = InlineKeyboardBuilder()
     ikb.row(
         InlineKeyboardButton(text="Avto Test", callback_data="avto_test"),
     )
     await callback.answer(text="linkni istiga bosing",reply_markup=ikb.as_markup())

@dp.callback_query(F.data == 'avto_test')
async def avto_test(callback: CallbackQuery):

    await callback.message.answer(f"Siz So'ragan Avto_test!,\n\n{'http://t.me/pravaoluzbot/app'}")


async def main():
    start_scheduler()
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())