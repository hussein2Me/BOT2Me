# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
"""
This module updates the userbot based on chtream revision
"""

from os import remove, execl
import sys

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError

from userbot import CMD_HELP, bot, HEROKU_MEMEZ, HEROKU_API_KEY, HEROKU_APP_NAME
from userbot.events import register


async def gen_chlog(repo, diff):
    ch_log = ''
    d_form = "%d/%m/%y"
    for c in repo.iter_commits(diff):
        ch_log += f'•[{c.committed_datetime.strftime(d_form)}]: {c.summary} <{c.author}>\n'
    return ch_log


async def is_off_br(br):
    off_br = ['master']
    for k in off_br:
        if k == br:
            return 1
    return


@register(outgoing=True, pattern="^.chl(?: |$)(.*)")
async def chtream(ch):
    "For .update command, check if the bot is up to date, update if specified"
    await ch.edit("`جاري التحقق من التحديثات ، يرجى الانتظار ....`")
    conf = ch.pattern_match.group(1).lower()
    off_repo = 'https://github.com/hussein2Me/Bot2Me.git'

    try:
        txt = "`عفوًا .. لا يمكن للمحدث المتابعة نظرًا لحدوث بعض المشكلات`\n\n**LOGTRACE:**\n"
        repo = Repo()
    except NoSuchPathError as error:
        await ch.edit(f'{txt}\n`directory {error} غير موجود`')
        return
    except GitCommandError as error:
        await ch.edit(f'{txt}\n`الفشل المبكر! {error}`')
        return
    except InvalidGitRepositoryError:
        repo = Repo.init()
        await ch.edit(
            "`تحذير: فرض المزامنة على أحدث رمز ثابت`\
            \قد أفقد الملفات التي تم تنزيلها أثناء هذا التحديث."
        )
        origin = repo.create_remote('chtream', off_repo)
        origin.fetch()
        repo.create_head('master', origin.refs.master)
        repo.heads.master.checkout(True)

    ac_br = repo.active_branch.name
    if not await is_off_br(ac_br):
        await ch.edit(
            f'**[UPDATER]:**` يبدو أنك تستخدم الفرع المخصص الخاص بك ({ac_br}). \
            في هذه الحالة ، يتعذر على Updater تحديد الفرع الذي سيتم دمجه. \
            يرجى الخروج إلى أي فرع رسمي`')
        return

    try:
        repo.create_remote('chtream', off_repo)
    except BaseException:
        pass

    ch_rem = repo.remote('chtream')
    ch_rem.fetch(ac_br)
    changelog = await gen_chlog(repo, f'HEAD..chtream/{ac_br}')

    if not changelog:
        await ch.edit(f'\n`WEW Your BOT is` **up-to-date** `with` **{ac_br}**\n')
        return

    if conf != "w":
        changelog_str = f'**New UPDATE available for [{ac_br}]:\n\nCHANGELOG:**\n`{changelog}`'
        if len(changelog_str) > 4096:
            await ch.edit("`عفوا التغير كبير جدًا ، يتم إرساله كملف.`")
            file = open("output.txt", "w+")
            file.write(changelog_str)
            file.close()
            await ch.client.send_file(
                ch.chat_id,
                "output.txt",
                reply_to=ch.id,
            )
            remove("output.txt")
        else:
            await ch.edit(changelog_str)
        await ch.respond(
            "`do \".update now \" to update\nif using Heroku`")
        return

    await ch.edit('`تم العثور على تحديث جديد ، جارٍ التحديث ...`')
    ch_rem.fetch(ac_br)
    await ch.edit('`تم التحديث بنجاح!\n'
                   'جاري إعادة التشغيل ... انتظر لحظة!`')
    await install_requirements()
    await bot.disconnect()
    # Spin a new instance of bot
    execl(sys.executable, sys.executable, *sys.argv)
    # Shut the existing one down
    exit()


CMD_HELP.update({
    'update':
    ".chl\
\nUsage: Checks if the main userbot repository has any updates and shows a changelog if so.\
\n\n.update\
\nUsage: Updates your userbot, if there are any updates in the main userbot repository."
})
