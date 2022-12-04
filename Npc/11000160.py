""" 11000160: Napolie """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 60, 70])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000674$
        # - Yes? How may I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000677$
        # - How may I help you, $MyPCName$?
        if pick == 0:
            # $script:0831180407000678$
            # - How can I increase my job rank?
            return 31
        elif pick == 1:
            # $script:0831180407000679$
            # - I don't know where I am.
            return 32
        return -1

    def __31(self, pick: int) -> int:
        # $script:0831180407000680$
        # - You can talk to the Job Instructors for assistance. They've gathered in $map:02000188$, which you can reach through the entrance right behind me.
        return -1

    def __32(self, pick: int) -> int:
        # $script:0831180407000681$
        # - Oh! Well, that's an easy fix. Just press M to see all of Maple World at a glance in your World Map.
        return -1

    def __60(self, pick: int) -> int:
        # $script:0303111207007963$
        # - How may I help you, $MyPCName$?
        if pick == 0:
            # $script:0303111207007964$
            # - I don't know where I am.
            return 61
        elif pick == 1:
            # $script:0303111207007965$
            # - I'm bored.
            return 62
        return -1

    def __61(self, pick: int) -> int:
        # $script:0303111207007966$
        # - Oh! Well, that's an easy fix. Just press M to see all of Maple World at a glance in your World Map.
        return -1

    def __62(self, pick: int) -> int:
        if self.index == 0:
            # $script:0303111207007967$
            # - Oh, I'm sorry. Hmm... how'd you like to make some friends? I know it can be awkward, but you'll never know what kind of cool people you can meet until you try it. You can also visit houses and leave a message in their Guestbook.
            return 62
        elif self.index == 1:
            # $script:0303111207007968$
            # - You can invite your friends over to your house for a party, explore dungeons, fish, and play music with them. Everything's more fun when you do it with friends!
            return -1
        return -1

    def __70(self, pick: int) -> int:
        # $script:1215102107009677$
        # - Oh my, $MyPCName$! What brings you here?
        if pick == 0:
            # $script:1215102107009678$
            # - Do you know anything about the rumors going around?
            return 71
        return -1

    def __71(self, pick: int) -> int:
        # $script:1215102107009679$
        # - Funny, that knight earlier asked me about the same thing. Well, I guess these days that rumor is all anyone wants to talk about.
        if pick == 0:
            # $script:1215102107009680$
            # - Details, please!
            return 72
        return -1

    def __72(self, pick: int) -> int:
        # $script:1215102107009681$
        # - It's like a giant shadow that darkens the skies. It looked like... a giant winged airship. Something about it gives me the heebie jeebies.
        if pick == 0:
            # $script:1215102107009682$
            # - How come?
            return 73
        return -1

    def __73(self, pick: int) -> int:
        if self.index == 0:
            # $script:1215102107009683$
            # - I don't know. It just feels ominous, like something horrible is about to happen. Disaster seems to follow anywhere that shadow is spotted!
            return 73
        elif self.index == 1:
            # $script:1215102107009684$
            # - I'm frightened.
            if pick == 0:
                # $script:1215102107009685$
                # - Don't worry. I'll protect you.
                return 74
            return -1
        return -1

    def __74(self, pick: int) -> int:
        # $script:1215102107009686$
        # - Really? Thanks, $MyPCName$.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (60, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (61, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (62, 0):
            return Option.NEXT
        elif (self.state, self.index) == (62, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (70, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (71, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (72, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (73, 0):
            return Option.NEXT
        elif (self.state, self.index) == (73, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (74, 0):
            return Option.CLOSE
        return Option.NONE
