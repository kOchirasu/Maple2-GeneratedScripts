""" 11003196: Katvan """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0404083307008224$
        # - $npcName:11003216[gender:0]$... That fool!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0404083307008225$
        # - I won't give up until $npcName:11003216[gender:0]$ pays for his crimes. I just wish $npcName:11000069[gender:1]$ would understand that I'm doing this for her...
        return -1

    def __20(self, pick: int) -> int:
        # $script:0516084007008486$
        # - I told you! As long as $npcName:11003216[gender:0]$ is alive, $npcName:11000069[gender:1]$ isn't safe.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
