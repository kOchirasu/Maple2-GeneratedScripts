""" 11001611: Ishura """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0509213707006098$
        # - <font color="#909090">(He's sound asleep.)</font>
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0511194807006105$
        # - I miss the master. I still hear his voice in my head...
        return -1

    def __20(self, pick: int) -> int:
        # $script:0515180407006106$
        # - $npcName:11001229[gender:0]$... Will he ever wake up?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
