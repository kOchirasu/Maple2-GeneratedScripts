""" 11000461: Isabel """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 50

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002048$
        # - Can I help you?
        return None # TODO

    def __50(self, pick: int) -> int:
        # $script:0831180407002051$
        # - Others say Chief Hairdresser $npcName:11000255[gender:1]$ is the best, but I like $npcName:11000253[gender:0]$'s style.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (50, 0):
            return Option.CLOSE
        return Option.NONE
