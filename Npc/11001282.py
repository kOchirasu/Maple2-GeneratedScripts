""" 11001282: Tracker """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1209020507004852$
        # - How may I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1209020507004855$
        # - You're $npcName:11001267[gender:0]$'s student, aren't you? So the rumors were wrong...
        if pick == 0:
            # $script:1209020507004856$
            # - Rumors? What rumors?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:1209020507004857$
        # - W-well... No, I shouldn't. I don't want to upset you.
        if pick == 0:
            # $script:1209020507004858$
            # - Don't tell me and see how upset I get!
            return 32
        return -1

    def __32(self, pick: int) -> int:
        if self.index == 0:
            # $script:1209020507004859$
            # - Fair enough. They say $npcName:11001267[gender:0]$ has one critical weakness: his student.
            return 32
        elif self.index == 1:
            # $script:1209020507004860$
            # - They say his student is stubborn, arrogant, and too reckless to be trusted with any important task.
            if pick == 0:
                # $script:1209020507004861$
                # - Well, I don't care <i>what</i> they say!
                return 33
            return -1
        return -1

    def __33(self, pick: int) -> int:
        # $script:1209020507004862$
        # - Good. You shouldn't. You're definitely a worthy student to a man of his stature.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.NEXT
        elif (self.state, self.index) == (32, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (33, 0):
            return Option.CLOSE
        return Option.NONE
