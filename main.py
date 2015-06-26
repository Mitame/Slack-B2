#!/usr/bin/env python3
from bot import Bot
from engines import censorship, commands
from config import getConfiguration


newbot = Bot(getConfiguration("bot"))

newbot.loadEngine(censorship.CensorshipEngine)
newbot.loadEngine(commands.PermissionEngine)
newbot.loadEngine(commands.CommandsEngine)

cmds = []

from commands.basic import Say, Help, Die, cnJoke, Ping
cmds.extend((Say, Help, Die, cnJoke, Ping))

from commands.fun import asciiClock, cowsay, slap
cmds.extend((asciiClock, cowsay, slap))

from commands.taiiwoport import cleverbot, findIP, FindPhone, Love, Moustache, WolframAlpha
cmds.extend((cleverbot, findIP, FindPhone, Love, Moustache, WolframAlpha))

from commands.utils import Permission
cmds.extend([Permission])

for cmd in cmds:
    cmd(newbot.getEngine("commands"))

newbot.start(1/30)