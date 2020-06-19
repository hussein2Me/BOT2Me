# Lots of lub to @r4v4n4 for gibing the base <3
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.utils import admin_cmd,register

@borg.on(admin_cmd("scan ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```الرد على أي رسالة مستخدم.```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.media:
       await event.edit("```الرد على رسالة وسائط```")
       return
    chat = "@DrWebBot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("```الرد على رسالة المستخدمين الفعلية.```")
       return
    await event.edit(" `Sliding my tip, of fingers over it`")
    async with borg.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=161163358))
              await borg.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```يرجى إلغاء حظر sangmatainfo_bot@ والمحاولة مرة أخرى```")
              return
          if response.text.startswith("Forward"):
             await event.edit("```هل يمكنك تعطيل إعدادات الخصوصية للأمام؟```")
          else:
          	if response.text.startswith("Select"):
          		await event.edit("`يرجى الانتقال إلى `DrWebBot@` واختيار لغتك.`") 
          	else: 
          			await event.edit(f"**تم الانتهاء من فحص مكافحة الفيروسات.  حصلت على النتائج النهائية.**\n {response.message.message}")
