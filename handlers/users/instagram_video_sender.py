from aiogram import types
from loader import dp,bot
from utils.main import instadown
from aiogram.dispatcher.filters import Text
@dp.message_handler(Text(startswith='https://www.instagram.com/'))
async def send_ins(message : types.Message):
    chat_id = message.from_user.id
    link = message.text
    load = await message.answer('⏳')
    data = await instadown(link)
    if data=='Bad':
        await message.delete()
        await load.delete()
        await message.answer("Bu URL manzili orqali hech narsa topilmadi!\n<b>👉@InstagramDownloaderbbot</b>")
    else:
        if data['type']=='image':
            await message.delete()
            await load.delete()
            await bot.send_photo(chat_id=chat_id,photo=data['media'],caption='<b>👉@InstagramDownloaderbbot  \norqali yuklab olindi</b>')
        elif data['type']=='video':
            await message.delete()
            await load.delete()
            await bot.send_video(chat_id=chat_id, video=data['media'], caption='<b>👉@InstagramDownloaderbbot  \norqali yuklab olindi</b>')
        elif data['type']=='carousel':
            await message.delete()
            await load.delete()
            for i in data['media']:
                await bot.send_document(chat_id=chat_id, document=i, caption='<b>👉@InstagramDownloaderbbot  \norqali yuklab olindi</b>')
        else:
            await message.answer("Bu URL manzili orqali hech narsa topilmadi! \n<b>👉@InstagramDownloaderbbot</b>")
