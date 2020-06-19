"""QuotLy: Avaible commands: .تحويل
"""
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern="تحويل ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```الرد على أي رسالة مستخدم.```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit("```الرد على رسالة.```")
       return
    chat = "@QuotLyBot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("```الرد على رسالة المستخدمين```")
       return
    await event.edit("```جاري عمل...```")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1031952739))
              await event.client.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```الرجاء الغاء الحظر (@QuotLyBot) ```")
              return
          if response.text.startswith("Hi!"):
             await event.edit("```هل يمكنك تعطيل إعدادات الخصوصية إلى الأمام للحصول على plox جيد؟```")
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)
