""" 11001280: Eupheria """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1208234507004843$
        # - I-I'm not... strong enough...
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1208234507004846$
        # - Gah! I failed to avenge Master Arazaad. Again!
        if pick == 0:
            # $script:1208234507004847$
            # - You'll get your chance.
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:1208234507004848$
        # - Just wait. Perhaps I'm not strong enough now, but I'll keep training. And someday, I'll rend $npcName:11001231[gender:0]$ asunder!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        return Option.NONE
