""" 11001232: Eupheria """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1125194807004474$
        # - Even with the draft in effect, we still don't have enough soldiers.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1125194807004477$
        # - $MyPCName$, if I'm not mistaken? You're that reckless student of $npc:11001244[gender:0]$'s I've heard so much about.
        if pick == 0:
            # $script:1205185107004721$
            # - Where did you hear that?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:1205185107004722$
        # - You'll be hard-pressed to find a Runeblade within Terrun Calibre that hasn't heard of you. Though lately, your name has been cropping up more and more.
        if pick == 0:
            # $script:1205185107004723$
            # - What do you mean by that?
            return 32
        return -1

    def __32(self, pick: int) -> int:
        # $script:1205185107004724$
        # - You don't know? Your teacher, $npc:11001246[gender:0]$, is one of the Eight Blades, the most magnificent warriors in all of Terrun Calibre. Learning from him is an honor, yet your approach to your studies have been a bit... unconventional. It's no wonder why there are many Runeblades who are jealous and resentful of you.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        return Option.NONE
