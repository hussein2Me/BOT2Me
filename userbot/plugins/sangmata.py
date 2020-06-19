
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from uniborg.util import admin_cmd




@borg.on(admin_cmd("email ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```الرد ع رسالة المستخدم```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit("```رجاء الرد ع رسالة.```")
       return
    chat = "@fakemailbot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("```الرد على رسالة المستخدمين.```")
       return
    await event.edit("```جاري ...```")
    async with borg.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=177914997))
              await borg.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```رجاء الغاء الحظر @sangmatainfo_bot و اعادة المحاولة```")
              return
          if response.text.startswith("send"):
             await event.edit("```هل يمكنك تعطيل إعدادات الخصوصية؟```")
          else: 
             await event.edit(f"{response.message.message}")

@borg.on(admin_cmd("gid ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```رجاء الرد ع رسالة مستخدم```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit("```رجاء الرد ع رسالة.```")
       return
    chat = "@getidsbot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("```رجاء الرد ع رسالة المستخدمين```")
       return
    await event.edit("```جاري ...```")
    async with borg.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=186675376))
              await borg.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```send```")
              return
          if response.text.startswith("Hello,"):
             await event.edit("```هل يمكنك تعطيل إعدادات الخصوصية؟```")
          else: 
             await event.edit(f"{response.message.message}")