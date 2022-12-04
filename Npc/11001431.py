""" 11001431: Ruche """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217205907005428$
        # - ...?
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:1222203907005516$
        # - ...
        if pick == 0:
            # $script:1222203907005517$
            # - I heard you talk!
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:1222203907005518$
        # - <font color="#909090">($npcName:11001431[gender:0]$ tilts his head.)</font>
        if pick == 0:
            # $script:1222203907005519$
            # - Maybe I'm hearing things...
            return 42
        return -1

    def __42(self, pick: int) -> int:
        # $script:1222203907005520$
        # - ...Heh.
        #   <font color="#909090">(Did $npcName:11001431[gender:0]$ just giggle...?)</font>
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (42, 0):
            return Option.CLOSE
        return Option.NONE
