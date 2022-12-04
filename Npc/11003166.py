""" 11003166: Joddy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0516084007008466$
        # - I sure hope $npcName:11003163[gender:0]$ comes back soon.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0516084007008469$
        # - I hear $npcName:11003163[gender:0]$ is one of the most dutiful, most devoted, most loving sons in all of Maple World.
        if pick == 0:
            # $script:0516084007008470$
            # - He's a devoted... son?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0516084007008471$
        # - Yeah! He's always off visiting his sick ma, who lives really far away. When I finally graduate, I'm gonna be a good son, too!
        if pick == 0:
            # $script:0516084007008472$
            # - Why wait until then?
            return 32
        return -1

    def __32(self, pick: int) -> int:
        # $script:0516084007008473$
        # - If my mom and dad saw me the way I am now, they'd die of shame. Gotta prove myself, first!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        return Option.NONE
