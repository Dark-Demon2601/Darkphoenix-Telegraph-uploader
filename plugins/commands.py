from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

START_TEXT = """<b>
Hello {},💘
im a Powerful Telgraph Uploader Bot for Free🥰.

That Can Upload Photo, Video And Gif
        
Simply send me photo, video or gif to upload to Telegra.ph

Regards
 - @ASHU_S_botS 😎
</b>"""
HELP_USER = """<b>
    There Is Nothing To KnowMore,😌
        
Just Send Me A Video/gif/photo Upto 5mb🤩.

i'll upload media/gif/ to telegra.ph and give you the direct link😎
</b>"""

START_BUTTONS = [[InlineKeyboardButton('😎 Channel💘', url='@Miss_Akshi_updates'), InlineKeyboardButton('💌share💛',url='https://telegram.m/share/url?url=&text=**Hey%20dude%E2%9D%A4%2C**%20%0A**Today%20i%20just%20found%20out%20an%20intresting%20and%20Powerful%20Telgraph%20Uploader%20Bot%20for%20Free%F0%9F%A5%B0.**%20%20%0ABot%20Link%20%3A%20%40TelgraphUploadEricBot%20%F0%9F%94%A5%0A%0A**Regards**%0A**-%C2%A9%40Ericbotz**'),],
                        [InlineKeyboardButton('Help💫' callback_data='help')]]

HELP_BUTTONS = [[InlineKeyboardButton('⚙ Channel ⚙', url='@Miss_Akshi_updates'), InlineKeyboardButton('🤡Dev', url='https://t.me/ASHU_S_botS'),],
                        [InlineKeyboardButton('Home🏠', callback_data='home')]]

@Client.on_callback_query()
async def button(bot, update):

    if update.data == "home":
        await update.message.delete()
        await start(bot, update.message)

    elif update.data == "help":
        await update.message.delete()
        await help(bot, update.message)

    elif update.data == "close":
        await update.message.delete()

@Client.on_message(filters.command(["start"]))
async def start(bot, update):
    await bot.send_message(chat_id=update.chat.id, text=START_TEXT.format(update.from_user.mention), parse_mode="html", disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup(START_BUTTONS), reply_to_message_id=update.message_id)

@Client.on_message(filters.command(["help"]))
async def help(bot, update):
    await bot.send_message(chat_id=update.chat.id, text=HELP_USER, parse_mode="html", disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup(HELP_BUTTONS), reply_to_message_id=update.message_id)
