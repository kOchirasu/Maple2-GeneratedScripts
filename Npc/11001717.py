""" 11001717: Junta """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0728022507006968$
        # - You'd better have a good reason for interrupting my training.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0805021607007093$
        # - I've given it some thought, but I still don't understand why some of us would leave the master's guidance to live in human cities like $map:02000001$. $MyPCName$, do you like this place?
        if pick == 0:
            # $script:0805021607007094$
            # - It's not too bad. 
            return 31
        elif pick == 1:
            # $script:0805021607007095$
            # - It's too loud for me!
            return 40
        return -1

    def __31(self, pick: int) -> int:
        # $script:0805021607007096$
        # - Hmph. If you have time to enjoy the sights, then you have time to train!
        if pick == 0:
            # $script:0805021607007097$
            # - Let's talk about something else.
            return 30
        return -1

    def __40(self, pick: int) -> int:
        # $script:0805021607007098$
        # - Yes... Yes, it is, isn't it? It hasn't escaped my notice that you've been training hard lately. Don't strain yourself.
        if pick == 0:
            # $script:0805021607007099$
            # - Let's talk about something else.
            return 30
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        return Option.NONE
