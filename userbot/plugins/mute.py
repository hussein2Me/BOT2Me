from userbot.plugins.sql_helper.mute_sql import is_muted, mute, unmute
import asyncio

@command(outgoing=True, pattern=r"^.mute ?(\d+)?", allow_sudo=True)
async def startmute(event):
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
        return await event.edit("يرجى الرد على مستخدم ليتم كتمه.")
    chat_id = event.chat_id
    chat = await event.get_chat()
    if "admin_rights" in vars(chat) and vars(chat)["admin_rights"] is not None: 
        if chat.admin_rights.delete_messages is True:
            pass
        else:
            return await event.edit("لا يمكنك كتم شخص ما إذا لم يكن لديك إذن حذف الرسائل")
    elif "creator" in vars(chat):
        pass
    elif private == True:
        pass
    else:
        return await event.edit("لا يمكنك كتم شخص بدون حقوق المسؤول")
    if is_muted(userid, chat_id):
        return await event.edit("هذا المستخدم موجود بالفعل في هذه الدردشة")
    try:
        mute(userid, chat_id)
    except Exception as e:
        await event.edit("حدث خطأ! n\ خطأ" + str(e))
    else:
        await event.edit("تم كتم هذا الشخص بنجاح")

@command(outgoing=True, pattern=r"^.unmute ?(\d+)?", allow_sudo=True)
async def endmute(event):
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
        return await event.edit("يرجى الرد على مستخدم أو إضافته إلى الأمر لإلغاء كتمه.")
    chat_id = event.chat_id
    if not is_muted(userid, chat_id):
        return await event.edit("هذا المستخدم لم يتم كتم في هذه المحادثة")
    try:
        unmute(userid, chat_id)
    except Exception as e:
        await event.edit("حدث خطأ! n\ خطأ" + str(e))
    else:
        await event.edit("تم إلغاء كتم هذا الشخص بنجاح")

@command(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, event.chat_id):
        await event.delete()

from userbot.plugins.sql_helper.mute_sql import is_muted, mute, unmute
import asyncio

@command(outgoing=True, pattern=r"^.mute ?(\d+)?")
async def startmute(event):
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
        return await event.edit("يرجى الرد على مستخدم ليتم كتمه.")
    chat_id = event.chat_id
    chat = await event.get_chat()
    if "admin_rights" in vars(chat) and vars(chat)["admin_rights"] is not None: 
        if chat.admin_rights.delete_messages is True:
            pass
        else:
            return await event.edit("لا يمكنك كتم شخص ما إذا لم يكن لديك إذن حذف الرسائل")
    elif "creator" in vars(chat):
        pass
    elif private == True:
        pass
    else:
        return await event.edit("لا يمكنك كتم شخص بدون حقوق المسؤول")
    if is_muted(userid, chat_id):
        return await event.edit("هذا المستخدم بالفعل مكتوم في هذه الدردشة")
    try:
        mute(userid, chat_id)
    except Exception as e:
        await event.edit("حدث خطأ! n\ خطأ" + str(e))
    else:
        await event.edit("تم كتم هذا الشخص بنجاح")

@command(outgoing=True, pattern=r"^.unmute ?(\d+)?")
async def endmute(event):
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
        return await event.edit("يرجى الرد على مستخدم أو إضافته إلى الأمر لإلغاء كتمه.")
    chat_id = event.chat_id
    if not is_muted(userid, chat_id):
        return await event.edit("هذا المستخدم لم يتم كتم في هذه المحادثة")
    try:
        unmute(userid, chat_id)
    except Exception as e:
        await event.edit("حدث خطأ! n\ خطأ" + str(e))
    else:
        await event.edit("تم إلغاء كتم هذا الشخص بنجاح")

@command(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, event.chat_id):
        await event.delete()
