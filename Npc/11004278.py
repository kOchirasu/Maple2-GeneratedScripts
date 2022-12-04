""" 11004278: Shadow Dragon Statue """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0911203207011283$
        # - <font color="#909090">(You feel an ominous chill as you gaze upon the dragon statue.)</font>
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0911203207011284$
            # - <font color="#909090">(You feel an ominous chill as you gaze upon the dragon statue.)</font>
            return 10
        elif self.index == 1:
            # $script:0911203207011285$
            # - <font color="#909090">(This statue was once a grand piece of architecture, proudly displaying the spirit of the dragons. However, it's been altered by darkness.)</font>
            return 10
        elif self.index == 2:
            # $script:0911203207011286$
            # - <font color="#909090">(The power of the dragons of light which once protected Nazkar is completely gone. Now, all avoid this once-sacred area.)</font>
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.NEXT
        elif (self.state, self.index) == (10, 2):
            return Option.CLOSE
        return Option.NONE
