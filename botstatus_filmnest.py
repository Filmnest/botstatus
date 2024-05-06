from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import asyncio
import datetime
import pytz
import os

app = Client(
    name="botstatus_teletips",
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"],
    session_string=os.environ["SESSION_STRING"]
)
TIME_ZONE = os.environ["TIME_ZONE"]
BOT_LIST = [i.strip() for i in os.environ.get("BOT_LIST").split(' ')]
CHANNEL_OR_GROUP_ID = int(os.environ["CHANNEL_OR_GROUP_ID"])
MESSAGE_ID = int(os.environ["MESSAGE_ID"])

async def main_teletips():
    async with app:
        while True:
            print("Checking...")
            xxx_teletips = f"〠 | **𝐑𝐞𝐚𝐥-𝐓𝐢𝐦𝐞 𝐌𝐢𝐠𝐮𝐞𝐥 𝐋𝐞𝐞𝐜𝐡 𝐁𝐨𝐭𝐬 𝐒𝐭𝐚𝐭𝐮𝐬**"
            for bot in BOT_LIST:
                try:
                    yyy_teletips = await app.send_message(bot, "/start")
                    aaa = yyy_teletips.id
                    await asyncio.sleep(20)
                    zzz_teletips = app.get_chat_history(bot, limit=1)
                    async for ccc in zzz_teletips:
                        bbb = ccc.id
                    if aaa == bbb:
                        xxx_teletips += f"\n\n유  @{bot}\n        └ **ᴅᴇᴀᴅ** ❌"
                        await app.read_chat_history(bot)
                    else:
                        xxx_teletips += f"\n\n유  @{bot}\n        └ **ᴡᴏʀᴋɪɴɢ** ✅"
                        await app.read_chat_history(bot)
                except FloodWait as e:
                    await asyncio.sleep(e.x)
            time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
            last_update = time.strftime(f"%d %b %Y at %I:%M %p")
            xxx_teletips += f"\n\n<i>✔ ᴄʜᴇᴄᴋᴇᴅ ᴏɴ: {last_update} ({TIME_ZONE})</i>\n\n✇ ʀᴇꜰʀᴇꜱʜ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴀꜰᴛᴇʀ 1 ʜᴏᴜʀ"
            await app.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, xxx_teletips)
            print(f"ᴄʜᴇᴄᴋᴇᴅ ᴏɴ: {last_update}")
            await asyncio.sleep(3600)

app.run(main_teletips())
