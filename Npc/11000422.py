""" 11000422: Roanna's Tombstone """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001763$
        # - <font color="#909090">(The headstone is old and worn, and there is an epitaph inscribed upon it.)</font>
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180407001764$
        # - <i>Here lies Roanna Levematri. She leaves behind her lover Alberto, whose heart will never heal.</i>
        return -1

    def __20(self, pick: int) -> int:
        # $script:0831180407001765$
        # - <i>Here lies Roanna Levematri. She leaves behind her lover Alberto, whose heart will never heal.</i>
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
