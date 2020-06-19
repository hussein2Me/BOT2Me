from userbot.plugins.sql_helper.mute_sql import is_muted, mute, unmute
import asyncio

@command(outgoing=True, pattern=r"^.gmute ?(\d+)?")
async def startgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("قد تحدث مشاكل غير متوقعة أو أخطاء قبيحة!")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit("يرجى الرد على مستخدم أو إضافته إلى الأمر لكتم صوته.")
    chat_id = event.chat_id
    chat = await event.get_chat()
    if is_muted(userid, "gmute"):
        return await event.edit("هذا المستخدم محجوب بالفعل")
    try:
        mute(userid, "gmute")
    except Exception as e:
        await event.edit("حدث خطأ! n\ خطأ" + str(e))
    else:
        await event.edit("تم بنجاح  كتم هذا الشخص")

@command(outgoing=True, pattern=r"^.ungmute ?(\d+)?")
async def endgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("قد تحدث مشكلات غير متوقعة أو أخطاء قبيحة!")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit("يرجى الرد على مستخدم أو إضافة إلى الأمر إلى Ungmute .")
    chat_id = event.chat_id
    if not is_muted(userid, "gmute"):
        return await event.edit("هذا المستخدم غير مكتوم")
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await event.edit("حدث خطأ! n\ خطأ" + str(e))
    else:
        await event.edit("تم بنجاح الغاء كتم هذا الشخص")

@command(outgoing=True, pattern=r"^.gmute ?(\d+)?", allow_sudo=True)
async def startgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("قد تحدث مشكلات غير متوقعة أو أخطاء قبيحة!")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit("يرجى الرد على مستخدم أو إضافة إلى الأمر إلى gmute .")
    chat_id = event.chat_id
    chat = await event.get_chat()
    if is_muted(userid, "gmute"):
        return await event.edit("هذا المستخدم مكتوم بالفعل")
    try:
        mute(userid, "gmute")
    except Exception as e:
        await event.edit("حدث خطأ! n\ خطأ" + str(e))
    else:
        await event.edit("تم بنجح  كتم هذا الشخص")

@command(outgoing=True, pattern=r"^.ungmute ?(\d+)?", allow_sudo=True)
async def endgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("قد تحدث مشكلات غير متوقعة أو أخطاء قبيحة!")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit("يرجى الرد على مستخدم أو إضافة إلى الأمر إلى Ungmute .")
    chat_id = event.chat_id
    if not is_muted(userid, "gmute"):
        return await event.edit("هذا المستخدم غير مكتوم")
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await event.edit("حدث خطأ! n\ خطأ" + str(e))
    else:
        await event.edit("تم بنجاح الغاء كتم هذا الشخص")

@command(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, "gmute"):
        await event.delete()
