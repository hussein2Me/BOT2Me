# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
# credits to @AvinashReddy3108
#
"""
This module updates the userbot based on Upstream revision
"""

from os import remove, execle, path, makedirs, getenv, environ
from shutil import rmtree
import asyncio
import sys

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError

from userbot import CMD_HELP, bot, HEROKU_API_KEY, HEROKU_APP_NAME, UPSTREAM_REPO_URL, HEROKU_MEMEZ
from userbot.events import register

requirements_path = path.join(
    path.dirname(path.dirname(path.dirname(__file__))), 'requirements.txt')


async def gen_chlog(repo, diff):
    ch_log = ''
    d_form = "%d/%m/%y"
    for c in repo.iter_commits(diff):
        ch_log += f'•[{c.committed_datetime.strftime(d_form)}]: {c.summary} <{c.author}>\n'
    return ch_log


async def update_requirements():
    reqs = str(requirements_path)
    try:
        process = await asyncio.create_subprocess_shell(
            ' '.join([sys.executable, "-m", "pip", "install", "-r", reqs]),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE)
        await process.communicate()
        return process.returncode
    except Exception as e:
        return repr(e)


@register(outgoing=True, pattern="^\.update(?: |$)(.*)")
async def upstream(ups):
    "بالنسبة لأمر .update ، تحقق مما إذا كان البوت مُحدّثًا ، حدّث إذا كان محددًا"
    await ups.edit("`جاري التحقق من التحديثات ، يرجى الانتظار ....`")
    conf = ups.pattern_match.group(1)
    off_repo = UPSTREAM_REPO_URL
    force_update = False

    try:
        txt = "`عفوًا .. لا يمكن للمحدث المتابعة بسبب"
        txt += "حدثت بعض المشاكل`\n\n**LOGTRACE:**\n"
        repo = Repo()
    except NoSuchPathError as error:
        await ups.edit(f'{txt}\n`الدليل {error} لم يتم العثور`')
        repo.__del__()
        return
    except GitCommandError as error:
        await ups.edit(f'{txt}\n`الفشل المبكر! {error}`')
        repo.__del__()
        return
    except InvalidGitRepositoryError as error:
        if conf != "now":
            await ups.edit(
                f"`لسوء الحظ ، لا يبدو أن الدليل {error} هو مستودع git.\
            \n ولكن يمكننا إصلاح ذلك عن طريق فرض تحديث برنامج المستخدم باستخدام .update now.`"
            )
            return
        repo = Repo.init()
        origin = repo.create_remote('upstream', off_repo)
        origin.fetch()
        force_update = True
        repo.create_head('master', origin.refs.master)
        repo.heads.master.set_tracking_branch(origin.refs.master)
        repo.heads.master.checkout(True)

    ac_br = repo.active_branch.name
    if ac_br != 'master':
        await ups.edit(
            f'** [محدث]: ** `يبدو أنك تستخدم فرعك المخصص ({ac_br}). '
            'في هذه الحالة ، يتعذر على Updater تحديد'
            'أي فرع سيتم دمجه.'
            'يرجى الخروج إلى أي فرع رسمي`')
        repo.__del__()
        return

    try:
        repo.create_remote('upstream', off_repo)
    except BaseException:
        pass

    ups_rem = repo.remote('upstream')
    ups_rem.fetch(ac_br)

    changelog = await gen_chlog(repo, f'HEAD..upstream/{ac_br}')

    if not changelog and not force_update:
        await ups.edit(
            f'\n`Your BOT is`  **up-to-date**  `with`  **{ac_br}**\n')
        repo.__del__()
        return

    if conf != "now" and not force_update:
        changelog_str = f'**New UPDATE available for [{ac_br}]:\n\nCHANGELOG:**\n`{changelog}`'
        if len(changelog_str) > 4096:
            await ups.edit("`التغييرات كبيرة جدًا ، اعرض الملف لرؤيته.`")
            file = open("output.txt", "w+")
            file.write(changelog_str)
            file.close()
            await ups.client.send_file(
                ups.chat_id,
                "output.txt",
                reply_to=ups.id,
            )
            remove("output.txt")
        else:
            await ups.edit(changelog_str)
        await ups.respond('`do \".update now\" to update`')
        return

    if force_update:
        await ups.edit(
            '`فرض المزامنة لأحدث رمز مستقر لبرنامج المستخدم ، يرجى الانتظار ...`')
    else:
        await ups.edit('`جاري تحديث برنامج userbot ، يرجى الانتظار ....`')
    # We're in a Heroku Dyno, handle it's memez.
    if HEROKU_API_KEY is not None:
        import heroku3
        heroku = heroku3.from_key(HEROKU_API_KEY)
        heroku_app = None
        heroku_applications = heroku.apps()
        if not HEROKU_APP_NAME:
            await ups.edit(
                '`يرجى إعداد متغير HEROKU_APP_NAME لتتمكن من تحديث userbot.`'
            )
            repo.__del__()
            return
        for app in heroku_applications:
            if app.name == HEROKU_APP_NAME:
                heroku_app = app
                break
        if heroku_app is None:
            await ups.edit(
                f'{txt} \ n` بيانات اعتماد Heroku غير صالحة لتحديث userbot dyno.`'
            )
            repo.__del__()
            return
        await ups.edit('`جارٍ إنشاء Userbot ، يرجى الانتظار لمدة 5 دقائق فقط حتى يكتمل.`'
                       )
        ups_rem.fetch(ac_br)
        repo.git.reset("--hard", "FETCH_HEAD")
        heroku_git_url = heroku_app.git_url.replace(
            "https://", "https://api:" + HEROKU_API_KEY + "@")
        if "heroku" in repo.remotes:
            remote = repo.remote("heroku")
            remote.set_url(heroku_git_url)
        else:
            remote = repo.create_remote("heroku", heroku_git_url)
        try:
            remote.push(refspec="HEAD:refs/heads/master", force=True)
        except GitCommandError as error:
            await ups.edit(f'{txt} \n`إليك سجل الأخطاء: \n {error}`')
            repo.__del__()
            return
        await ups.edit('`تم التحديث بنجاح!\n'
                       'إعادة التشغيل ، يرجى الانتظار ...`')
    else:
        # Classic Updater, pretty straightforward.
        try:
            ups_rem.pull(ac_br)
        except GitCommandError:
            repo.git.reset("--hard", "FETCH_HEAD")
        reqs_upgrade = await update_requirements()
        await ups.edit('`تم التحديث بنجاح!\n'
                       'جاري إعادة التشغيل ... انتظر لحظة!`')
        # Spin a new instance of bot
        args = [sys.executable, "-m", "userbot"]
        execle(sys.executable, *args, environ)
        return


CMD_HELP.update({
    'update':
    ".update\
\nUsage: Checks if the main userbot repository has any updates and shows a changelog if so.\
\n\n.update now\
\nUsage: Updates your userbot, if there are any updates in the main userbot repository."
})
