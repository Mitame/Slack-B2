__author__ = 'MrMindImplosion'

from engines.commands import PermissionEngine

permissionLevels = PermissionEngine.levels

class Command:
    callname = "command"
    permissionLevel = permissionLevels.NONE
    msg_subtype = None
    syntax = ""

    def __init__(self, engine):
        self.engine = engine
        self.bot = self.engine.bot
        self.engine.registerCommand(self, None)

    def on_call(self, message, *args, **kwargs):
        pass

