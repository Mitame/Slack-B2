__author__ = "MrMindImplosion"

from engines import Engine
from bot.constants import event, message_subtype

class CensorshipEngine(Engine):
    name = "censorship"
    version = 0.1
    confName = None
    depends = []
    supplies = []
    conflicts = []

    def __init__(self, bot, conf):
        """
        :type bot bot.slack.Bot
        :param conf configparser.ConfigParser
        :return:
        """
        Engine.__init__(self, bot, conf)
        self.bot = bot
        self.conf = conf

        self.bot.add_listener(event.message, self.message_listener)

    def message_listener(self, message, *args, **kwargs):
        if not hasattr(message, "subtype"):
            return

        if message.subtype == message_subtype.message_deleted:
            self.bot.send_PrivMsg(self.bot.getUserFromName("levi"), "A message was deleted from %s." % message.channel)

