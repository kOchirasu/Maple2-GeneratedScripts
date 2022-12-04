""" 11004254: Inscribed Totem """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0829171107010968$
        # - <font color="#909090">(The water in the "Demonspring", for which the surrounding area is named, is neither red nor black as one might expect, but rather a sickly translucent green.)</font>
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0829171107010969$
            # - <font color="#909090">(The water in the "Demonspring", for which the surrounding area is named, is neither red nor black as one might expect, but rather a sickly translucent green.)</font>
            return 10
        elif self.index == 1:
            # $script:0831140807011011$
            # - <font color="#909090">(It's said that the spring was tainted long ago by the blood of the goddess of darkness. It is <i>also</i> said that this spring contains the blood of an ancient turtle. No one knows the truth of the matter.)</font>
            return 10
        elif self.index == 2:
            # $script:0831140807011012$
            # - <font color="#909090">(Nevertheless, it's probably best not to let the liquid touch you.)</font>
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
