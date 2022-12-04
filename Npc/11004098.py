""" 11004098: Chocolate Waffle Waterfall """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0623132607010349$
        # - <font color="#909090">(This chocolate waterfall puts off an overwhelmingly sweet aroma.)</font>
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0623132607010350$
            # - <font color="#909090">(This chocolate waterfall puts off an overwhelmingly sweet aroma.)</font>
            return 10
        elif self.index == 1:
            # $script:0623132507010346$
            # - <font color="#909090">(The rich chocolate of this waterfall is enough to drive some children sugar-crazy.)</font>
            return 10
        elif self.index == 2:
            # $script:0623132507010347$
            # - <font color="#909090">(The chocolate found in $map:02000257$ is favored by dessert chefs everywhere. Some say it's even Empress $npcName:11001969[gender:1]$'s favorite chocolate.)</font>
            return 10
        elif self.index == 3:
            # $script:0623132507010348$
            # - <font color="#909090">(In fact, rumor has it the empire's vaults are full of the stuff...)</font>
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
