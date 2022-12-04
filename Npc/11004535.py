""" 11004535: Barricade Patrolman """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0104170807012603$
        # - I'm sick of fighting! Is there no end to them?! <b>Oh...!</b> Hello, $male:Sir,female:Ma'am$! I didn't see you there!
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0104170807012604$
            # - I'm sick of fighting! Is there no end to them?! <b>Oh...!</b> Hello, $male:Sir,female:Ma'am$! I didn't see you there!
            return 10
        elif self.index == 1:
            # $script:0104170807012605$
            # - This is the biggest road to and from $map:02020041$. Maybe that's why the enemy keeps hammering us here.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.CLOSE
        return Option.NONE
