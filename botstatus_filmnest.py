from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import asyncio
import datetime
import pytz
import os

app = Client(
    name="botstatus_filmnest",
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"],
    session_string=os.environ["SESSION_STRING"]
)
TIME_ZONE = os.environ["TIME_ZONE"]
BOT_LIST = [i.strip() for i in os.environ.get("BOT_LIST").split(' ')]
CHANNEL_OR_GROUP_ID = int(os.environ["CHANNEL_OR_GROUP_ID"])
MESSAGE_ID = int(os.environ["MESSAGE_ID"])
BOT_ADMIN_IDS = [int(i.strip()) for i in os.environ.get("BOT_ADMIN_IDS").split(' ')]

async def main_filmnest():
    async with app:
            while True:
                print("Checking...")
                xxx_filmnest = f"〠 | **ʀᴇᴀʟ-ᴛɪᴍᴇ ʙᴏᴛ ꜱᴛᴀᴛᴜꜱ**"
                for bot in BOT_LIST:
                    try:
                        yyy_filmnest = await app.send_message(bot, "/start")
                        aaa = yyy_filmnest.id
                        await asyncio.sleep(20)
                        zzz_filmnest = app.get_chat_history(bot, limit=1)
                        async for ccc in zzz_filmnest:
                            bbb = ccc.id
                        if aaa == bbb:
                            xxx_filmnest += f"\n\n유  @{bot}  ᘛ⁐̤ᕐᐶ  **ᴅᴇᴀᴅ** ❌"
                            for bot_admin_id in BOT_ADMIN_IDS:
                                try:
                                    await app.send_message(int(bot_admin_id), f"ꆛ **ʙᴇᴇᴘ! ʙᴇᴇᴘ!! @{bot} ɪꜱ ᴅᴏᴡɴ** ❌")
                                except Exception:
                                    pass
                            await app.read_chat_history(bot)
                        else:
                            xxx_filmnest += f"\n\n유  @{bot}  ᘛ⁐̤ᕐᐶ  **ᴡᴏʀᴋɪɴɢ** ✅"
                            await app.read_chat_history(bot)
                    except FloodWait as e:
                        await asyncio.sleep(e.x)            
                time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
                last_update = time.strftime(f"%d %b %Y at %I:%M %p")
                xxx_filmnest += f"\n\n✔ ᴄʜᴇᴄᴋᴇᴅ ᴏɴ: {last_update} ({TIME_ZONE})\n\n<i>✇ ʀᴇꜰʀᴇꜱʜᴇꜱ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ</i>"
                await app.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, xxx_filmnest)
                print(f"ᴄʜᴇᴄᴋᴇᴅ ᴏɴ: {last_update}")                
                await asyncio.sleep(3600)
                        
app.run(main_filmnest())
