"""Check if userbot alive."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "hussein @GcGcY"
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**`انا على قيد تشغيل سيدي`**\n\n"
                     "**✅Telethon version:- 6.9.0**\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n**✅Python: 3.7.3**\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n"
                     "**✅بوت مصنوع من:- @TEAM2ME\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n**"
                     "**✅حالة قاعدة البيانات: قواعد البيانات تعمل بشكل طبيعي!!**\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n💞دائما معك يا سيد \n`"
                     f"dev: {DEFAULTUSER}\n"
                     "[Channel](https://t.me/GcGcZ)")
