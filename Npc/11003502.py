""" 11003502: Ramda """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0816160115008982$
        # - How may I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0816160115008984$
        # - $npcName:11003501[gender:1]$ and I wanna be bigshots in Team Mushroom someday. But it'd be cool to work for Dryad Co., too... What should we do?
        return -1

    def __40(self, pick: int) -> int:
        # $script:0816160115008985$
        # - The Team Mushroom is a huge organization, you know!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
