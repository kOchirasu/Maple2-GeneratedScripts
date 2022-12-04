""" 11001412: Sumsum """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217205907005409$
        # - So... much... pain...
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:1222203907005501$
        # - C-can't... talk... Too... busy... pain...
        if pick == 0:
            # $script:1222203907005502$
            # - Where does it hurt?
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:1222203907005503$
        # - Leave me alone... you dummy... I need to rest...
        if pick == 0:
            # $script:1222203907005504$
            # - Hey, I'm just trying to help!
            return 42
        return -1

    def __42(self, pick: int) -> int:
        # $script:1222203907005505$
        # - G-go away... I don't want... your help... 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (42, 0):
            return Option.CLOSE
        return Option.NONE
