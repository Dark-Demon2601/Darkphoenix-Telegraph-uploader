import os 
import time 
import math
from telegraph import upload_file
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from pyrogram.errors import UserNotParticipant, UserBannedInChannel


#≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈SHABIN -K≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈TEXT≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈#

DOWNLOAD_TEXT = "<code>Downloading to My Server ..📲</code>"

UPLOADING_TEXT = "<code>Downloading Completed. Now I'am Uploading to telegra.ph Link ...😎</code>"

SOMETHING_WRONG = "Something Wrong! Contact😖 @Ericbotzbot."

FREE_USER_LIMIT_Q_SZE = "Sorry Friend, Free users can only 1 request per {} minutes. Please try again after {} seconds later."

FORCE_SUBSCRIBE_TEXT = "<b><code>You Must Join My Updates Channel for using me 😌😉.press this button to join Now👇</code></b>"

BANNED_USER_TEXT = "<code>You are Banned!😬</code>"

#≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈SHABIN -K≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈CONFIG≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈#

UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "")
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
ADL_BOT_RQ = {} 
PROCESS_MAX_TIMEOUT = int(os.environ["TIME_LIMIT"])

#≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈SHABIN -K≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈MAIN≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈#

@Client.on_message(filters.media & filters.private)
async def getmedia(bot, update):
    if UPDATE_CHANNEL:
        try:
          user = await bot.get_chat_member(UPDATE_CHANNEL, update.chat.id)
          if user.status == "kicked":
            await update.reply_text(text=BANNED_USER_TEXT)
            return
        except UserNotParticipant:
          await update.reply_text(text=FORCE_SUBSCRIBE_TEXT, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="😎 Join Channel 😅", url=f"https://telegram.me/{UPDATE_CHANNEL}")]]))
          return
        except Exception:
          await update.reply_text(text=SOMETHING_WRONG, disable_web_page_preview=True)
          return 
    if update.from_user.id not in AUTH_USERS:
        if str(update.from_user.id) in ADL_BOT_RQ:
            current_time = time.time()
            previous_time = ADL_BOT_RQ[str(update.from_user.id)]
            process_max_timeout = round(PROCESS_MAX_TIMEOUT/60)
            present_time = round(PROCESS_MAX_TIMEOUT-(current_time - previous_time))
            ADL_BOT_RQ[str(update.from_user.id)] = time.time()
            if round(current_time - previous_time) < PROCESS_MAX_TIMEOUT:
                await bot.send_message(text=FREE_USER_LIMIT_Q_SZE.format(process_max_timeout, present_time), quote=True)
                return
        else:
            ADL_BOT_RQ[str(update.from_user.id)] = time.time()
    media = update.document or update.video or update.video_note
    medianame = "./DOWNLOADS/" + "ERICBOTZ/TelgraphUploadEricBot"
    dwn = await bot.send_message(chat_id=update.chat.id, text=DOWNLOAD_TEXT, parse_mode="html", disable_web_page_preview=True, reply_to_message_id=update.message_id)
    await bot.download_media(message=update, file_name=medianame)
    await dwn.edit_text(text=UPLOADING_TEXT)
    try:
        response = upload_file(medianame)
    except Exception as error:
        await dwn.edit_text(text=SOMETHING_WRONG, disable_web_page_preview=True)
        return
    await dwn.edit_text(
        text=f"<b>Link :-</b> <code>https://telegra.ph{response[0]}</code>\n\n<b>Dev :-</b> @Erichome",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Open Link", url=f"https://telegra.ph{response[0]}"), InlineKeyboardButton(text="Share Link", url=f"https://telegram.me/share/url?url=https://telegra.ph{response[0]}"), ],
                                           [InlineKeyboardButton(text="DONATE😇", url="https://telegra.ph/Ericbotzbank-03-09/")]])
        )
    try:
        os.remove(medianame)
    except:
        pass



#≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈SHABIN -K≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈END≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈#