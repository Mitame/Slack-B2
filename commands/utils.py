__author__ = 'leviwright'

from commands.base import Command, permissionLevels

class Permission(Command):
    callname = "perm"
    permissionLevel = permissionLevels.ADMIN

    def on_call(self, message, *args, **kwargs):
        username = args[0]
        x = self.bot.getUserFromName(username)
        self.bot.send_Reply(message, "%s has permission level %s" % (x.name, self.bot.getEngine("permission").get_permission_level(x.id)))
