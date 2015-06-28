__author__ = 'leviwright'

from commands.base import Command, permissionLevels


class Vote(Command):
    """ DON'T USE THIS YET"""
    arguments = ["str", "str"]
    permissionLevel = -1
    permitExtraArgs = True
    manArgCheck = True
    defaultArgs = []
    callName = "vote"

    class poll:
        def __init__(self, *args):
            self.votes = {}
            self.voteids = {}
            self.voted = []
            for vote in args:
                self.votes[vote] = 0
                self.voteids[args.index(vote)] = vote

        def getVote(self, ID, data="name"):
            if data == "name":
                return self.voteids[ID]
            elif data == "score":
                return self.votes[self.voteids[ID]]

    def __init__(self, bot):
        Command.__init__(self, bot)
        self.polls = {}
        self.pollids = {}
        self.currentPoll = ""

    def createPoll(self, event, name, question, *options):
        self.currentPoll = name
        self.polls[name] = self.poll(*options)
        self.polls[len(self.polls.keys())] = name
        self.pubMsg(event, """%s has started a poll!""" % event.source.nick)
        self.pubMsg(event, "---%s---" % question)

        for x in range(len(self.polls[name].voteids)):
            self.pubMsg(event, str(x)+" :\t"+self.polls[name].getVote(x))

        self.pubMsg(event, "To vote, type in '%s:vote #', where '#' is your vote." % self.bot.callsign)
        self.pubMsg(event, "---Note, you can't change your mind after you have voted, so think carefully.")

    def castVote(self, event, *args):
        if self.currentPoll == "":
            self.bot.sendPubMsg(event, "Sorry %s, there is not vote running currently." % event.source.nick)
            return

        curpoll = self.polls[self.currentPoll]
        if event.source.nick in curpoll.voted:
            self.bot.sendPubMsg(event, "Sorry %s, you can't vote again." % event.source.nick)
            return

        curpoll = self.polls[self.currentPoll]
        curpoll.votes[curpoll.voteids[int(args[0])]] += 1
        alert = ("%s voted for '" + self.polls[self.currentPoll].voteids[int(args[0])]+"'!") % event.source.nick

        curpoll.voted.append(event.source.nick)
        self.bot.sendPubMsg(event, alert)

    def checkPermissions(self, event, *args):
        if len(args) == 0:
            return True
        base = args[0]
        if base in ("create", "results", "close"):
            if self.bot.getPermLevel(event) >= 1:
                return True
            else:
                return False
        else:
            if base.isdecimal() and (0 <= int(base) < len(self.polls[self.currentPoll].voteids)):
                return True
            else:
                return False

    @staticmethod
    def checkArgs(*args):
        if len(args) == 0:
            return 0
        return True

    def getResults(self, event, *args):
        if self.currentPoll == "":
            self.bot.sendPubMsg(event, "Sorry %s, there is not vote running currently." % event.source.nick)
            return

        self.bot.sendPubMsg(event, "---Current poll results---")
        for ID in self.polls[self.currentPoll].voteids:
            x = self.polls[self.currentPoll].voteids[ID]

            self.bot.sendPubMsg(event, ("    '%s': " + str(self.polls[self.currentPoll].votes[x])+" votes.") % x)
        self.bot.sendPubMsg(event, "--------------------------")

    def closePoll(self, event, name):
        self.pubMsg(event, "The voting has now ended. The final results are:")
        for ID in self.polls[self.currentPoll].voteids:
            x = self.polls[self.currentPoll].voteids[ID]

            self.bot.sendPubMsg(event, ("    '%s': "+str(self.polls[self.currentPoll].votes[x])+" votes.") % x)
        self.bot.sendPubMsg(event, "--------------------------")

        self.currentPoll = ""

    def on_call(self, event, *args):
        if args[0] == "create":
            args = " ".join(args[1:]).split(", ")
            self.createPoll(event, args[0], args[1], *args[2:])
        elif args[0] == "results":
            self.getResults(event)
        elif args[0] == "close":
            try:
                self.closePoll(event, self.currentPoll)
            except NameError:
                self.pubMsg("No poll to close.")
        else:
            if args[0].isdecimal():
                self.castVote(event, int(args[0]))
