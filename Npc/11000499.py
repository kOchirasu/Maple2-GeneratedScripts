""" 11000499: Gogh """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002172$
        # - Did... Did you come to see me?
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407002175$
            # - I thought that if we went deeper into the forest, we could keep $npcName:11000751[gender:1]$ safer...
            return 30
        elif self.index == 1:
            # $script:0831180407002176$
            # - Others pointed their fingers and called us cowards, but we didn't care. We just wanted to keep our charge safe... 
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.CLOSE
        return Option.NONE
