""" 11001148: Danpa """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0915221607003971$
        # - What? If it's not urgent, come back later.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0915221607003974$
        # - See the fortress over there? It's got to be full of all kinds of amazing stuff worth collecting. Say, would you be interested in checking it out?
        if pick == 0:
            # $script:0915221607003975$
            # - I don't think there's much of value left in that abandoned fortress.
            return 31
        elif pick == 1:
            # $script:0915221607003976$
            # - I'm a little more worried about the monsters guarding it.
            return 32
        return -1

    def __31(self, pick: int) -> int:
        # $script:0915221607003977$
        # - <font color="#909090">(He chuckles.)</font>
        #   Well I do! It's gotta be chock full of treasure. I can tell, just by the look of it. I guess we'll see which of us is right.
        return -1

    def __32(self, pick: int) -> int:
        # $script:0915221607003978$
        # - No kidding. Why do you think I haven't gone inside? I wish someone would take care of them for me...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        return Option.NONE
