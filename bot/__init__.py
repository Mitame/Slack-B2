__author__ = "MrMindImplosion"

import bot.constants as constants
from bot.slack import RTMHandler, getAllChannels, getAllGroups, getAllUsers
from slacker import Slacker
from config import getConfiguration

class Bot(RTMHandler):
    """A slack bot containing calls for Real Time Messaging."""

    def __init__(self, confBlock):
        """Create a new bot.
        :type confBlock configparser.ConfigParser
        """

        self.callSign = confBlock["bot"]["callname"]
        apikey = confBlock["bot"]["apikey"]
        self.slack = Slacker(apikey)

        RTMHandler.__init__(self, self.slack.rtm.start().body["url"])

        self.users = getAllUsers(self.slack)
        self.groups = getAllGroups(self.slack)
        self.channels = getAllChannels(self.slack)

        self.engines = {}
        self.enginesSupplied = {}

    def send_PrivMsg(self, user, message):
        """Send a private message to a user
        :type user bot.slack.User
        :type message str
        """

        print(user)
        if type(user) == str:
            user = self.getObjFromID(user)

        imId = user.getImID(self.slack)
        return self.send_message(imId, message)

    def send_Reply(self, event, message):
        return self.send_message(event.channel, message)

    def send(self, name, message):
        """Send a message to either a channel, user or group.
        Starting name with '#' indicates to send it to a channel.
        Starting name with '@' indicates to send it to a user.
        Starting name with '$' indicates to send it to a group.
        :type name str
        :type message str
        """

        if name[0] == "#":
            "is a channel"
            self.send_message(name[1:], message)

        elif name[0] == "@":
            "is a name"
            self.send_PrivMsg(name[1:], message)

    def getUserFromName(self, name):
        """Return a user object when given its user name
        :type name str
        """
        for user in self.users.values():
            if user.name == name:
                return user
        else:
            return False

    def getChannelFromName(self, name):
        """Return a user object when given its name
        :type name str
        """

        for channel in self.channels.values():
            if channel.name == name:
                return channel
        else:
            return False

    def getGroupFromName(self, name):
        """Return a group object when given its name
        :type name str
        """

        for group in self.group.values():
            if group.name == name:
                return  group
        else:
            return False

    def getObjFromID(self, ID):
        """Return the obj for a channel/group/user given it's ID
        :type name str
        """
        if ID[0] == "U":
            "found a user"
            return self.users[ID]

        elif ID[0] == "C":
            "found a channel"
            return self.channels[ID]

        elif ID[0] == "G":
            "found a group"
            return self.channels[ID]

        else:
            raise ValueError("'%s' is not a valid ID." % ID)

    def loadEngine(self, newEngine):
        """ Loads a new engine into the bot.
        """

        # check for confilcts:
        for conflict in newEngine.conflicts:
            if conflict in self.engines.keys():
                raise ValueError("%s conflicts with %s." % (newEngine.name, self.engines[conflict].name))

        for depend in newEngine.depends:
            if depend not in self.enginesSupplied.keys():
                raise ValueError("%s depends on %s, but has not been supplied." % (newEngine.name, depend))

        # check configuration
        if newEngine.confName is not None:
            conf = getConfiguration(newEngine.confName)
            if int(conf["versioning"]["version"]) < newEngine.requiredConfVersion:
                raise RuntimeError("Configuration for '%s' is too far out of date." % newEngine.name)

        else:
            conf = None
        engine = newEngine(self, conf)
        self.engines[engine.name] = engine

        for supply in engine.supplies:
            self.enginesSupplied[supply] = engine

    def getEngine(self, supplies):
        try:
            return self.enginesSupplied[supplies]
        except:
            raise IndexError('%s has not been supplied.\
                              Check your configurations to make sure an engine is being loaded that supplies %s.' %
                             (supplies, supplies))


