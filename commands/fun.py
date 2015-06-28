import time
import os
import shlex
import pyfiglet
import random

from commands.base import Command, permissionLevels


class slap(Command):
    permissionLevel = permissionLevels.ADMIN
    callname = "slap"

    def on_call(self, message, *args, **kwargs):
        self.bot.send_Reply(message, "*slapped %s*" % args[0])


class asciiClock(Command):
    permissionLevel = permissionLevels.NORMAL
    callname = "time"

    def on_call(self, message, *args, **kwargs):
        font = pyfiglet.Figlet()
        x = font.renderText(str(time.ctime()).split(" ")[3])
        self.bot.send_Reply(message, "```"+x+"```")


class cowsay(Command):
    permissionLevel = permissionLevels.NORMAL
    callname = "cowsay"

    withArguments = ["-e", "-f", "-T", "-W"]
    withoutArguments = ["-b", "-d", "-g", "-h", "-l", "-L", "-n", "-N", "-p", "-s", "-t", "-w", "-y"]

    def on_call(self, message, *args, **kwargs):
        args = list(args)
        newArgs = []
        text = []
        while len(args) != 0:
            arg = args.pop(0)
            if arg[0:2] in self.withArguments:
                newArgs.append(arg[0:2])
                if arg not in self.withArguments:  # check for arguments without space
                    newArgs.append(arg[2:])
                else:
                    newArgs.append(args.pop(0))
            elif arg in self.withoutArguments:
                newArgs.append(arg)
            elif arg[0] == "-":
                self.bot.send_PrivMsg(message.user, "Invalid argument '%s'." % arg)
            else:
                text.append(arg)
        print("Executing %s." % ("cowsay " + " ".join(newArgs) + " " + shlex.quote(" ".join(text))))
        y = os.popen("cowsay " + " ".join(newArgs) + " " + shlex.quote(" ".join(text)))
        self.bot.send_Reply(message, "```" + y.read() + "```")


class Dice(Command):
    callname = "r"
    permissionLevel = permissionLevels.NORMAL

    def on_call(self, message, *args, **kwargs):
        if len(args) == 0:
            self.on_call(message, "6", "1")
            return
        elif len(args) == 1:
            self.on_call(message, args[0], "1")
            return

        try:
            sides = int(args[0])
            rolls = int(args[1])
        except ValueError or IndexError:
            self.bot.send_PrivMsg(message.user, "Incorrect syntax: '!r [<SIDES_ON_DICE> [<NUMBER_OF_ROLLS>]]")
            return

        if sides * rolls > 20 and self.engine.perms.get_permission_level(message.user) < permissionLevels.BOT_OP:
            self.bot.send_PrivMsg(message.user, "Only the bot operators can roll that much.")
            return

        if rolls == 1:
            value = random.randint(1, sides)
            self.bot.send_Reply(message, "Rolled a %s" % str(value))
            return

        results = [0]*sides
        for roll in range(rolls):
            results[random.randint(0, sides-1)] += 1

        text = "```side | roll\n"
        for index in range(len(results)):
            text += (str(index + 1) + " ").rjust(5, " ") + "| "+str(results[index]).ljust(5, " ") + "\n"
        text += "```"

        self.bot.send_Reply(message, text)
