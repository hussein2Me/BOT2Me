"""Emoji

Available Commands:

.load
.square
.up
.round
.anim
.fnl
.monkey
.hand"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 100)

    input_str = event.pattern_match.group(1)

    if input_str == "load":

        await event.edit(input_str)

        animation_chars = [

            "▮",

            "▯",

            "▬",

            "▭"
            "‎"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 4])


"""Emoji

Available Commands:

.emoji shrug

.emoji apple

.emoji :/

.emoji -_-"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 100)

    input_str = event.pattern_match.group(1)

    if input_str == "square":

        await event.edit(input_str)

        animation_chars = [

            "◧",

            "◨",

            "◧",

            "◨"
            "‎"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 4])



@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 100)

    input_str = event.pattern_match.group(1)

    if input_str == "up":

        await event.edit(input_str)

        animation_chars = [

            "╹",

            "╻",

            "╹",

            "╻"
            "‎"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 4])

@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 100)

    input_str = event.pattern_match.group(1)

    if input_str == "round":

        await event.edit(input_str)

        animation_chars = [

            "⚫",

            "⬤",

            "●",

            "∘"
            "‎"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 4])


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "anim":

        await event.edit(input_str)

        animation_chars = [

            "😁",

            "😧",

            "😡",

            "😢",

            "‎**مقدمة بواسطة @TEAM2ME**",
 
            "😁",

            "😧",

            "😡",

            "😢",

            "‎t.me/team2me",

            "__**حقوق @GcGcY**__"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 6)

    input_str = event.pattern_match.group(1)

    if input_str == "fnl":

        await event.edit(input_str)

        animation_chars = [

            "😁🏿",

            "😁🏾",

            "😁🏽",

            "😁🏼",

            "‎😁",

            "**حقوق الكتابة @GcGcY**"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 6])


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 6)

    input_str = event.pattern_match.group(1)

    if input_str == "monkey":

        await event.edit(input_str)

        animation_chars = [

            "🐵",

            "🙉",

            "🙈",

            "🙊",

            "🖕‎🐵🖕",

            "**مقدمة بواسطة @TEAM2ME**"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 6])

            
@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 14)

    input_str = event.pattern_match.group(1)

    if input_str == "hand":

        await event.edit(input_str)

        animation_chars = [

            "👈",

            "👉",

            "☝️",

            "👆",

            "🖕",

            "👇",

            "✌️",

            "🤞",

            "🖖",

            "🤘",

            "🤙",

            "🖐️",

            "👌"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 14])


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 13)

    input_str = event.pattern_match.group(1)

    if input_str == "cnt":

        await event.edit(input_str)

        animation_chars = [

            "🔟",

            "9️⃣",

            "8️⃣",

            "7️⃣",

            "6️⃣",

            "5️⃣",

            "4️⃣",

            "3️⃣",

            "2️⃣",

            "1️⃣",

            "0️⃣",

            "🆘"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 13])
