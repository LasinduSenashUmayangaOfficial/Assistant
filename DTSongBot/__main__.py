# SLT BrecLand <https://t.me/SLTBrecLand>
# @Damantha_Jasinghe

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from DTSongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from DTSongBot import DTbot as app
from DTSongBot import LOGGER

START_TEXT = """
හේ හේ හිච්චි පුතේ 😇
දන්නවනේ ඉතින්. මම තමයි අපේ නිපුන් කොලුවගෙ ඇසිස්ටන්ට්.. ඌ දැන් පට්ට බිසී 😅 
ඉස්සර වගේ නෙවේනෙ පුතේ දැන් වගකීම් එහෙමත් වැඩිනෙ ඒකාට 😅 
ඉතින් පුතේ ඔය හෙල්ප් බටන් එක එබුවම විස්තරේ එයි 😇 ගහලම බලපම්කෝ.. 
එහෙනම් හිච්චි පුතේ අපි කැපුනා 🥸
"""

HELP_TEXT = """
පුතේ මේ තීන්නෙ කමාන්ඩ්ස් ටික 👇
/help
/about
/contact
/website
/social
/github
හේ හේ මරු හැබැයි 😎
"""

START_STICKER = "CAACAgIAAxkBAAEIpNJiWuv1eyICxhrO5S4rW1GtPlgzhAAChBgAAup12UryWtFUKpG2fyQE"
Help_STICKER = "CAACAgIAAxkBAAEIpNViWuwery3UKAP_XoGcSKD3mwbcmgAC1BgAAn-z2UosweD7BFw4eCQE"

START_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('𝑹𝒆𝒑𝒐', url='https://github.com/Lasindu248/Assistant-Bot'),
        InlineKeyboardButton('𝑰𝒏𝒃𝒐𝒙',url='https://t.me/NiupunDinujaya')
        ]]
)


HELP_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('𝑰𝒏𝒃𝒐𝒙', url='https://t.me/NiupunDinujaya'),
        InlineKeyboardButton('𝑹𝒆𝒑𝒐',url='https://github.com/Lasindu248/Assistant-Bot')
        ]]
)

@app.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_photo(
        START_STICKER,
        caption=START_TEXT,
        reply_markup=START_BUTTON,
        parse_mode=ParseMode.MARKDOWN,
        quote=True
)

@app.on_message(filters.private & filters.command(["help"]))
async def start(bot, update):
    await update.reply_photo(
        HELP_STICKER,
        caption=HELP_TEXT,
        reply_markup=HELP_BUTTON,
        parse_mode=ParseMode.MARKDOWN,
        quote=True
)   

app.start()
LOGGER.info("DTSongBot is online.")
idle()
