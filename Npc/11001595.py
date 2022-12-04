""" 11001595: Asimov """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0504151707006083$
        # - How may I help you?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0515180307006132$
        # - $npcName:11001229[gender:0]$'s body may be asleep, but I don't think his mind is. He'll return to us soon. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
