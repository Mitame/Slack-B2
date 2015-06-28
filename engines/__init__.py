__author__ = 'MrMindImplosion'


class Engine:
    name = "baseEngine"
    version = 0.1
    confName = "base"
    requiredConfVersion = 1
    depends = []
    supplies = ["base"]
    conflicts = []

    def __init__(self, bot, conf):
        """
        :type bot bot.Bot
        :type conf: configparser.ConfigParser
        """
        self.bot = bot
        if type(self) == Engine:
            raise RuntimeError("Base engine was run. Please check your configuration.")
