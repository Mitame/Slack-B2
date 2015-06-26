import time
import os
import shlex

from commands.base import Command, permissionLevels
import pyfiglet


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
        print(str(time.ctime()).split(" "))
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
                if arg not in self.withArguments: #check for arguments without space
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
        self.bot.send_Reply("```" + str(y.read(), "utf8") + "```")
