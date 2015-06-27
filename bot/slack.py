__author__ = "MrMindImplosion"

import time
import websocket
import json

class RTMHandler:
    events = ["hello", "message", "user_typing", "channel_marked",
              "channel_created", "channel_joined", "channel_left", "channel_deleted",
              "channel_rename", "channel_archive", "channel_unarchive", "channel_history_changed",
              "im_created", "im_open", "im_close", "im_marked",
              "im_history_changed", "group_joined", "group_left", "group_open",
              "group_close", "group_archive", "group_unarchive", "group_rename",
              "group_marked", "group_history_changed", "file_created", "file_shared",
              "file_unshared", "file_public", "file_private", "file_change",
              "file_deleted", "file_comment_added", "file_comment_edited", "file_comment_deleted",
              "pin_added", "pin_removed", "presence_change", "manual_presence_change",
              "pref_change", "user_change", "team_join", "star_added",
              "star_removed", "emoji_changed", "commands_changed", "team_plan_change",
              "team_pref_change", "team_rename", "team_domain_change", "email_domain_changed",
              "bot_added", "bot_changed", "accounts_changed", "team_migration_started",
              "reply_to"]

    def __init__(self, url):
        self.ws = websocket.create_connection(url)

        self.handlers = {}
        self.listeners = {}

        for event in self.events:
            self.handlers[event] = getattr(self, "_on_"+event)
            self.listeners[event] = []

        self.msgId = 0
        self.msgStack = []

    # define all websocket message handlers (there's a lot...)
    def _on_hello(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_message(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_user_typing(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_channel_marked(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_channel_created(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_channel_joined(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_channel_left(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_channel_deleted(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_channel_rename(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_channel_archive(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_channel_unarchive(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_channel_history_changed(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_im_created(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_im_open(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_im_close(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_im_marked(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_im_history_changed(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_group_joined(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_group_left(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_group_open(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_group_close(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_group_archive(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_group_unarchive(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_group_rename(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_group_marked(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_group_history_changed(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_file_created(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_file_shared(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_file_unshared(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_file_public(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_file_private(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_file_change(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_file_deleted(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_file_comment_added(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_file_comment_edited(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_file_comment_deleted(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_pin_added(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_pin_removed(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_presence_change(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_manual_presence_change(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_pref_change(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_user_change(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_team_join(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_star_added(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_star_removed(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_emoji_changed(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_commands_changed(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_team_plan_change(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_team_pref_change(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_team_rename(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_team_domain_change(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_email_domain_changed(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_bot_added(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_bot_changed(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_accounts_changed(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_team_migration_started(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_reply_to(self, msg):
        for listener in self.listeners[msg.type]:
            listener[0](msg, *listener[1], **listener[2])

    def _on_any(self, msg):
        pass

    def _on_other(self, msg):
        pass

    # create methods for listening to events
    def on_hello(self, msg):
        pass

    def on_message(self, msg):
        pass

    def on_user_typing(self, msg):
        pass

    def on_channel_marked(self, msg):
        pass

    def on_channel_created(self, msg):
        pass

    def on_channel_joined(self, msg):
        pass

    def on_channel_left(self, msg):
        pass

    def on_channel_deleted(self, msg):
        pass

    def on_channel_rename(self, msg):
        pass

    def on_channel_archive(self, msg):
        pass

    def on_channel_unarchive(self, msg):
        pass

    def on_channel_history_changed(self, msg):
        pass

    def on_im_created(self, msg):
        pass

    def on_im_open(self, msg):
        pass

    def on_im_close(self, msg):
        pass

    def on_im_marked(self, msg):
        pass

    def on_im_history_changed(self, msg):
        pass

    def on_group_joined(self, msg):
        pass

    def on_group_left(self, msg):
        pass

    def on_group_open(self, msg):
        pass

    def on_group_close(self, msg):
        pass

    def on_group_archive(self, msg):
        pass

    def on_group_unarchive(self, msg):
        pass

    def on_group_rename(self, msg):
        pass

    def on_group_marked(self, msg):
        pass

    def on_group_history_changed(self, msg):
        pass

    def on_file_created(self, msg):
        pass

    def on_file_shared(self, msg):
        pass

    def on_file_unshared(self, msg):
        pass

    def on_file_public(self, msg):
        pass

    def on_file_private(self, msg):
        pass

    def on_file_change(self, msg):
        pass

    def on_file_deleted(self, msg):
        pass

    def on_file_comment_added(self, msg):
        pass

    def on_file_comment_edited(self, msg):
        pass

    def on_file_comment_deleted(self, msg):
        pass

    def on_pin_added(self, msg):
        pass

    def on_pin_removed(self, msg):
        pass

    def on_presence_change(self, msg):
        pass

    def on_manual_presence_change(self, msg):
        pass

    def on_pref_change(self, msg):
        pass

    def on_user_change(self, msg):
        pass

    def on_team_join(self, msg):
        pass

    def on_star_added(self, msg):
        pass

    def on_star_removed(self, msg):
        pass

    def on_emoji_changed(self, msg):
        pass

    def on_commands_changed(self, msg):
        pass

    def on_team_plan_change(self, msg):
        pass

    def on_team_pref_change(self, msg):
        pass

    def on_team_rename(self, msg):
        pass

    def on_team_domain_change(self, msg):
        pass

    def on_email_domain_changed(self, msg):
        pass

    def on_bot_added(self, msg):
        pass

    def on_bot_changed(self, msg):
        pass

    def on_accounts_changed(self, msg):
        pass

    def on_team_migration_started(self, msg):
        pass

    def on_reply_to(self, msg):
        pass

    def add_listener(self, event, function, *args, **kwargs):
        self.listeners[event].append((function, args, kwargs))

    def remove_listener(self, event, index):
        self.listeners[event].remove(index)

    def replace_handler(self, event, function):
        self.handlers[event] = function

    # create methods for handling sending
    def send_message(self, channel, text, wait=True):
        jsonString = json.dumps({"id": self.msgId,
                                 "type": "message",
                                 "channel": channel,
                                 "text": text
                                 })
        self.ws.send(jsonString)

        self.msgId += 1
        if wait:
            status = self.wait_for_reply(self.msgId - 1)
            return status

    def wait_for_reply(self, Id):
        while 1:
            msg = self._parseMsg(self._recv())
            if hasattr(msg, "reply_to") and msg.reply_to == Id:
                return msg.ok
            else:
                self.msgStack.append(msg)
            time.sleep(1/30)

    def _onrecv(self, msg):
        if type(msg) != Message:
            parse = self._parseMsg(msg)
        else:
            parse = msg
        self._on_any(parse)

        try:
            if hasattr(parse, "message"):
                self.handlers[parse.type](parse.message)
            self.handlers[parse.type](parse)
        except ValueError:
            print("Error parsing message:", msg)
            self._on_other(parse)

    def _parseMsg(self, msg):
        return Message(json.loads(msg))

    def _recv(self):
        return self.ws.recv()

    def start(self, scanInterval=1):
        try:
            while 1:
                try:
                    self._onrecv(self.ws.recv())

                    # work through the message stack if it built up while waiting
                    while len(self.msgStack) != 0:
                        self._onrecv(self.msgStack.pop())

                    time.sleep(scanInterval)
                except TimeoutError:
                    print("Connection lost.")
                    break
        except KeyboardInterrupt or SystemExit:
            pass


class dictObj():
    def __init__(self, Dict):
        for a, b in Dict.items():
            if isinstance(b, (list, tuple)):
                setattr(self, a, [type(self)(x) if isinstance(x, dict) else x for x in b])
            else:
                setattr(self, a, type(self)(b) if isinstance(b,dict) else b)

class Message(dictObj):
    type = None
    channel = None
    user = None
    text = None
    ts = None

    def __init__(self, Dict):
        dictObj.__init__(self, Dict)
        self.raw = Dict


class User(dictObj):
    def getImID(self, slack):
        """get the instant messaging ID for the user
        :type slack slacker.Slacker
        """
        if not hasattr(self, "imID"):
            im = slack.im.open(self.id).body
            if im["ok"] is True:
                self.imID = im["channel"]["id"]
        return self.imID


class Group(dictObj):
    pass


class Channel(dictObj):
    pass


def getAllUsers(slack):
    userObjs = {}
    users = slack.users.list().body["members"]
    for x in users:
        userObjs[x["id"]] = User(x)

    return userObjs

def getAllGroups(slack):
    groupObjs = {}
    users = slack.groups.list().body["groups"]
    for x in users:
        groupObjs[x["id"]] = Group(x)

    return groupObjs

def getAllChannels(slack):
    channelObjs = {}
    users = slack.channels.list().body["channels"]
    for x in users:
        channelObjs[x["id"]] = Channel(x)

    return channelObjs