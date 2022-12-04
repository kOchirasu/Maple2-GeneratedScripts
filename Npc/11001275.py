""" 11001275: Branko """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1207123607004824$
        # - The air here is cleaner than in $map:2000270$.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1207123607004827$
        # - Yes? What do you want?
        if pick == 0:
            # $script:1207123607004828$
            # - I heard you're Maccan's assistant.
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:1207123607004829$
        # - Yes. What of it? If you want to ask <i>why</i> I'm still working as Dr. $npcName:11001276[gender:0]$'s assistant, save your breath.
        if pick == 0:
            # $script:1207123607004830$
            # - Why are you sti— Oh.
            return 32
        return -1

    def __32(self, pick: int) -> int:
        # $script:1207123607004831$
        # - I knew it! Some people just can't open their mouths without letting a stupid question slip out.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        return Option.NONE
