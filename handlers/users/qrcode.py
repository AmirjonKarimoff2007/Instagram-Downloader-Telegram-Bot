from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Command
import asyncio
from loader import dp,bot
import qrcode
import requests
from io import BytesIO
from aiogram.types import InputFile
from aiogram.dispatcher.filters import Text

@dp.message_handler(Text(startswith='https://www'))
@dp.message_handler(Text(startswith='www'))
async def send_text_based_qr(message: types.Message):
    qr = qrcode.QRCode(version=1,
                       error_correction = qrcode.constants.ERROR_CORRECT_L,
                       box_size = 20, 
                       border = 2)

    qr.add_data(message.text)
    qr.make(fit = True)  

    img = qr.make_image(fill_color = 'black', back_color = 'white')
    img.save('photo.png')
    img = InputFile('photo.png')

    await message.reply_photo(img, caption = f'<b>✅ Qr code Tayyor \n\n👉@generate_qr_codes_bot</b>', parse_mode = 'HTML')

