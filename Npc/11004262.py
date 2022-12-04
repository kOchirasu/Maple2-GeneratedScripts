""" 11004262: Small Pond """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0911203207011177$
        # - <font color="#909090">(This pleasant little pond holds a prominent position in $npcName:11001350[gender:0]$'s estate.)</font>
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0911203207011178$
            # - <font color="#909090">(This pleasant little pond holds a prominent position in $npcName:11001350[gender:0]$'s estate.)</font>
            return 10
        elif self.index == 1:
            # $script:0911203207011179$
            # - <font color="#909090">(The fish look like golden bladefish, a species unique to the island.)</font>
            return 10
        elif self.index == 2:
            # $script:0911203207011180$
            # - <font color="#909090">(Their scales shimmer beautifully in the sunlight. The interplay of light brings a sense of peace to your mind...)</font>
            return 10
        elif self.index == 3:
            # $script:0911203207011181$
            # - <font color="#909090">(Maybe it's time you got some fish of your own.)</font>
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.NEXT
        elif (self.state, self.index) == (10, 2):
            return Option.NEXT
        elif (self.state, self.index) == (10, 3):
            return Option.CLOSE
        return Option.NONE
