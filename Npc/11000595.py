""" 11000595: Scott """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 50

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002385$
        # - Hm... That's... 
        return None # TODO

    def __50(self, pick: int) -> int:
        # $script:0831180407002389$
        # - Mm? Are you a traveler?
        if pick == 0:
            # $script:0831180407002390$
            # - What are you doing here?
            return 51
        return -1

    def __51(self, pick: int) -> int:
        # $script:0831180407002391$
        # - Oh, me? I'm studying these creatures we call the fairfolk. All kinds of fairfolk inhabit forests like this.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (51, 0):
            return Option.CLOSE
        return Option.NONE
