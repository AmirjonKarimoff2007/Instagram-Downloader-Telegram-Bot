from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Command
import asyncio
from loader import dp, bot
import qrcode
from io import BytesIO
from aiogram.types import InputFile
from aiogram.dispatcher.filters import Text

@dp.message_handler(Text(startswith='https'))
@dp.message_handler(Text(startswith='www'))
async def send_text_based_qr(message: types.Message):
    # Define your color scheme
    color_scheme = ('#d9851a', 'white')

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=20,
        border=2,
    )

    qr.add_data(message.text)
    qr.make(fit=True)

    img = qr.make_image(fill_color=color_scheme[0], back_color=color_scheme[1])
    
    # Save QR code to BytesIO instead of a file
    img_byte_array = BytesIO()
    img.save(img_byte_array)
    img_byte_array.seek(0)
    
    # Send QR code as a photo in the Telegram chat
    await message.reply_document(InputFile(img_byte_array, filename='photo.png'), caption=f'<b>✅ Qr code Tayyor \n\n👉@generate_qr_codes_bot</b>', parse_mode='HTML')

