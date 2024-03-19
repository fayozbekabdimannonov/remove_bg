import asyncio
import logging
import sys 
from aiogram import Bot, Dispatcher,types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram import F
from aiogram.types import Message,CallbackQuery,FSInputFile
from mybattons import inline_menu,courses_menu,ortga,colours_inline_button,location,sayt,admin,delete
from myremovbg import bg_change_color
TOKEN = "6632943217:AAFFo8SRjTxfvSq2_fjY9N4z0ufnnc3et1E" #Token kiriting
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(text="Assalomu alaykum",reply_markup=inline_menu)


@dp.callback_query(F.data=="courses")
async def bizning_kurslar(callback:CallbackQuery):

    # await callback.answer("Bizning kurslar")

    await callback.message.edit_text("menyulardan birini tanlang👇: ",reply_markup=courses_menu)
    # await callback.message.delete()

@dp.callback_query(F.data=="back")
async def ortga_func(callback:CallbackQuery):
   await callback.message.edit_text(text="Asosiy menu",reply_markup=inline_menu)


@dp.callback_query(F.text=="uchir")

async def uchir_fuct(callback:CallbackQuery):
    await callback.message.edit_text(text="rasim tasha",reply_markup=delete)

@dp.callback_query(F.data=="back-courses")
async def ortga_kurs_func(callback:CallbackQuery):
   await callback.message.answer(text="Bizning kurslar: ",reply_markup=courses_menu)
   await callback.message.delete()



@dp.message(F.text=="orqa fon")
async def auto_keyboard(message:Message,):
    await message.answer(text="men rasm o'zgartir botman menga rasm yubor",reply_markup=auto_keyboard)







@dp.startup()
async def bot_ishga_tushdi(bot:Bot):
    await bot.send_message(chat_id=6109857994,text="Bot ishga tushdi")

@dp.shutdown()
async def bot_toxtadi(bot:Bot):
    await bot.send_message(chat_id=6109857994,text="Bot ishdan to'xtadi")

bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

@dp.message(F.photo)
async def name(message:Message):
    file_id = message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = bg_change_color(photos_url,"red")
    if rasm:
        await message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="no-remove.png"),reply_markup=colours_inline_button)
        await message.answer_document(document=types.input_file.BufferedInputFile(rasm,filename="no-remove.png"))



@dp.callback_query(F.data=="location")
async def lakatsiya(callback:CallbackQuery):
    await callback.message.edit_text(text="Bizning manzil",reply_markup=location)
    
@dp.callback_query(F.data=="about-us")
async def saytimiz(callback:CallbackQuery):
    await callback.message.edit_text(text="Bizning sayt",reply_markup=sayt)
    
@dp.callback_query(F.data=="contact-admin")
async def men(callback:CallbackQuery):
    await callback.message.edit_text(text="Admin",reply_markup=admin)


@dp.callback_query(F.data=="blue")
async def colours_changes(callback:CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = bg_change_color(photos_url,"blue")
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="blue-remove.png"),reply_markup=colours_inline_button)
    await callback.message.delete()

@dp.callback_query(F.data=="orange")
async def colours_changes(callback:CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = bg_change_color(photos_url,"orange")
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="orange-remove.png"),reply_markup=colours_inline_button)
    await callback.message.delete()


@dp.callback_query(F.data=="black")
async def colours_changes(callback:CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = bg_change_color(photos_url,"black")
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="black-remove.png"),reply_markup=colours_inline_button)
    await callback.message.delete()

@dp.callback_query(F.data=="green")
async def colours_changes(callback:CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = bg_change_color(photos_url,"green")
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="green-remove.png"),reply_markup=colours_inline_button)
    await callback.message.delete()

@dp.callback_query(F.data=="yellow")
async def colours_changes(callback:CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = bg_change_color(photos_url,"yellow")
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="yellow-remove.png"),reply_markup=colours_inline_button)
    await callback.message.delete()


@dp.callback_query(F.data=="white")
async def colours_changes(callback:CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = bg_change_color(photos_url,"white")
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="white-remove.png"),reply_markup=colours_inline_button)
    await callback.message.delete()

@dp.callback_query(F.data=="brown")
async def colours_changes(callback:CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = bg_change_color(photos_url,"brown")
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="brown-remove.png"),reply_markup=colours_inline_button)
    await callback.message.delete()


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())