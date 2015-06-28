__author__ = 'MrMindImplosion'

from commands.base import Command, permissionLevels


class Permission(Command):
    callname = "getperm"
    permissionLevel = permissionLevels.ADMIN

    def on_call(self, message, *args, **kwargs):
        username = args[0]
        x = self.bot.getUserFromName(username)
        self.bot.send_Reply(message, "%s has permission level %s" % (x.name, self.bot.getEngine("permission").get_permission_level(x.id)))


class DeleteLastMessage(Command):
    callname = "delmessage"
    permissionLevel = permissionLevels.BOT_OWNER

    def on_call(self, message, *args, **kwargs):

        # if chat is IM
        if message.channel[0] == "D":
            history = self.bot.slack.im.history(message.channel).body

        # if chat is group
        elif message.channel[0] == "G":
            history = self.bot.slack.groups.history(message.channel).body

        # if chat is channel
        elif message.channel[0] == "C":
            history = self.bot.slack.channels.history(message.channel).body

        # everything borked
        else:
            return

        ID = self.bot.slack.auth.test().body["user_id"]

        timestamps = []
        for oldMessage in history["messages"]:
            if oldMessage["type"] == "message" and \
               oldMessage["user"] == ID:
                timestamps.append(oldMessage["ts"])

        timestamps.sort()
        self.bot.slack.chat.delete(message.channel, timestamps[-1])
