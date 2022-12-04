""" 11003505: Rieve """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0816160115009002$
        # - See the hungry $itemPlural:61000002$ over there? This place is getting crowded because of them...
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0816160115009003$
        # - You're way too green to cut it in Team Mushroom.
        return -1

    def __40(self, pick: int) -> int:
        # $script:0816160115009004$
        # - Tamed monsters are called 'combat pets.' Don't forget that, 'cause it might be on the test!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
