__author__ = "MrMindImplosion"

from engines import Engine
from bot.constants import event

class PermissionEngine(Engine):
    name = "permission"
    version = 0.1
    confName = "permission"
    requiredConfVersion = 1
    depends = []
    supplies = ["permission"]
    conflicts = []

    class levels:
        BOT_OWNER = 7
        PRIMARY_OWNER = 6
        OWNER = 5
        ADMIN = 4
        BOT_OP = 3
        NORMAL = 2
        RESTRICTED = 1
        NONE = 0

    def __init__(self, bot, conf):
        Engine.__init__(self, bot, conf)
        self.owners = tuple(x.strip() for x in conf["permission"]["owners"].split(","))
        self.ops = tuple(x.strip() for x in conf["permission"]["ops"].split(","))

    def get_permission_level(self, userID):
        user = self.bot.getObjFromID(userID)

        if user.name in self.owners:
            return self.levels.BOT_OWNER
        elif user.is_primary_owner:
            return self.levels.PRIMARY_OWNER
        elif user.is_owner:
            return self.levels.OWNER
        elif user.is_admin:
            return self.levels.ADMIN
        elif user.name in self.ops:
            return self.levels.BOT_OP
        elif not user.is_restricted:
            return self.levels.NORMAL
        elif user.is_restricted:
            return self.levels.RESTRICTED
        else:
            return self.levels.NONE


class CommandsEngine(Engine):
    name = "commands"
    version = 0.1
    confName = "commands"
    requiredConfVersion = 1
    depends = ["permission"]
    supplies = ["commands"]
    conflicts = []

    class spaces:
        DIRECT_MESSAGE = 1
        GROUP = 2
        CHANNEL = 3

    def __init__(self, bot, conf):
        Engine.__init__(self, bot, conf)
        self.commandPrefix = conf["command"]["commandPrefix"]

        # register listener
        self.bot.add_listener(event.message, self.on_any_message)

        # create dict to hold commands
        self.commands = {}

        # get permissions engine from bot
        self.perms = self.bot.enginesSupplied["permission"]

    def get_space(self, message):
        chat = message.channel
        if chat[0] == "D":
            return self.spaces.DIRECT_MESSAGE, chat
        elif chat[0] == "C":
            return self.spaces.CHANNEL, chat
        elif chat[0] == "G":
            return self.spaces.GROUP, chat

    def on_any_message(self, message):
        if message.channel is None or message.text is None:
            print(message.raw)
            return

        space = self.get_space(message)[0]

        if space == self.spaces.DIRECT_MESSAGE:
            self.on_direct_message(message)
        elif space == self.spaces.CHANNEL:
            self.on_channel_message(message)
        elif space == self.spaces.GROUP:
            self.on_group_message(message)

    def on_channel_message(self, message):
        channel = message.channel

        if message.text == "":
            return

        if message.text[0] == self.commandPrefix:
            command = message.text.split(" ")[0].strip("!")
            if command in self.commands:
                return self.doCommand(self.commands[command], message)

    def on_group_message(self, message):
        group = message.channel

        # catch empty messages
        if message.text == "":
            return

        if message.text[0] == self.commandPrefix:
            command = message.text.split(" ")[0].strip("!")
            if command in self.commands:
                return self.doCommand(self.commands[command], message)

    def on_direct_message(self, message):
        dm = message.channel

        if message.text == "":
            self.bot.send_Reply(message, "No command specified")
            return False, "no command"

        x = message.text.lstrip("!")

        cmd = x.split(" ")[0]

        if cmd in self.commands:
            return self.doCommand(self.commands[cmd], message)
        else:
            return False, "command not found"

    def registerCommand(self, commandObject, spaces, *args, **kwargs):
        self.commands[commandObject.callname] = {"command": commandObject,
                                                 "spaces": spaces,
                                                 "args": args,
                                                 "kwargs": kwargs
                                                 }

    def doCommand(self, command, message):
        space = self.get_space(message)

        # check command can be used in this space
        if command["spaces"] is not None and not (space[0] in command["spaces"] or space[1] in command["spaces"]):
            return False, ("private", "command is not valid in this space")

        # check command is allowed to be used by the sender
        print(message.user, self.perms.get_permission_level(message.user))
        if command["command"].permissionLevel > self.perms.get_permission_level(message.user):
            print(command["command"].permissionLevel, self.perms.get_permission_level(message.user))
            return False, ("private", "You are not permitted to run the '%s' command." % command["command"].callname)

        args = message.text.split(" ")[1:]
        args.extend(command["args"])

        return command["command"].on_call(message, *args, **command["kwargs"])


