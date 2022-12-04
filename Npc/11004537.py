""" 11004537: Barricade Defender """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0104170807012611$
        # - We're doing our best to defend $map:02020041$!
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0104170807012612$
            # - We're doing our best to defend $map:02020041$!
            return 10
        elif self.index == 1:
            # $script:0104170807012613$
            # - Send me to where the fighting's thickest! I'll crush any enemy in my path!
            return 10
        elif self.index == 2:
            # $script:0104170807012614$
            # - Umm... Would you mind taking a few of them out while you're here? N-not that I can't take them myself, of course!
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
