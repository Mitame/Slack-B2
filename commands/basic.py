__author__ = 'MrMindImplosion'

from commands.base import Command, permissionLevels
import requests
import json
from urllib.parse import unquote


class Say(Command):
    callname = "say"
    permissionLevel = permissionLevels.ADMIN

    def on_call(self, message, *args, **kwargs):
        self.bot.send_Reply(message, " ".join(args))


class Ping(Command):
    callname = "ping"
    permissionLevel = permissionLevels.NONE

    def on_call(self, message, *args, **kwargs):
        self.bot.send_Reply(message.user, "PONG")


class Die(Command):
    callname = "die"
    permissionLevel = permissionLevels.BOT_OWNER

    def on_call(self, event, *args):
        raise SystemExit


class cnJoke(Command):
    callname = "cnjoke"
    permissionLevel = permissionLevels.NORMAL

    def on_call(self, message, *args):
        x = requests.get("http://api.icndb.com/jokes/random")
        z = x.text
        try:
            a = json.loads(z)
            self.bot.send_Reply(message, unquote(a["value"]["joke"]))
        except ValueError:
            pass

    # this is useless right now
    def on_fail(self, message):
        self.bot.send_PrivMsg(message.user,
                              "You failed to type the command correctly puny human." +
                              "\nChuck Norris will roundhouse kick you in the face shortly." % self.callName+" " +
                              str(self.arguments))


class Help(Command):
    permissionLevel = permissionLevels.NONE
    callname = "help"

    def __init__(self, engine):
        Command.__init__(self, engine)

    def on_call(self, message, *args, **kwargs):
        commands = []
        for x in list(self.engine.commands.items()):
            if x[1]["command"].permissionLevel <= self.engine.perms.get_permission_level(message.user):
                commands.append(x[0])
        commands.sort()

        text = "---Commands avaliable to you---\n"
        for cmd in commands:
            text += self.engine.commandPrefix+cmd+"\n"
        text += "-------------------------------"

        self.bot.send_PrivMsg(message.user, text)
