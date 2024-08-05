from pyrogram import filters
from devgagan import app
from devgagan.core import script
from devgagan.core.func import subscribe
from config import OWNER_ID
from telethon import events, Button
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

# ------------------- Start-Buttons ------------------- #

buttons = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("Join Channel", url="https://t.me/TBots_Father"),
        InlineKeyboardButton("Buy Premium", url="https://t.me/BinaryBandiT69")]
    ]
)

@app.on_message(filters.command("start"))
async def start(_, message):
    join = await subscribe(_, message)
    if join == 1:
        return
    await message.reply_photo(photo="https://graph.org/file/b0c891545d4adb77a4f95.jpg",
                              caption=script.START_TXT.format(message.from_user.mention), 
                              reply_markup=buttons)



HELP_TEXT = """
HELP SECTION 📝

🛠️ /settings - Open settings to set your requirements.

🔒 /login - Login to your userbot session.

📦 /batch - Download bulk links in a systematic way.

⛔ /cancel - Stop batch processing.

FOR PUBLIC CHANNELS OR GROUPS:
- First, Login.
- Then send the message link of any channel that you've joined in your login account.

FOR BOT:
- Send the link in this format: https://t.me/b/bot_username/message_id (use Plus Messenger for message_id)

FOR GROUP TOPIC:
- (For Private Group) Group topic link is like: https://t.me/c/xxxxxxxxx/first_id/second_id
But, send it like this: https://t.me/c/xxxxxxx/second_id (remove first id and one /)

- (For Public Group) Follow the private link step but also remove "/c" from the link.
Ex: https://t.me/c/username/first_id/second_id Will Be https://t.me/username/second_id

#FAQ:

- If the bot says "Have you joined the channel?" then just log in again to the bot and try.

- If your batch is stuck, then use /cancel.

""" 


@app.on(events.NewMessage(pattern='/help'))
async def help_command(event):
    await event.respond(HELP_TEXT, buttons=buttons, link_preview=False)