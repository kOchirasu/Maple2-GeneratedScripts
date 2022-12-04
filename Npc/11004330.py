""" 11004330: Kaitlyn """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 30])

    def select(self) -> int:
        return random.choice([0, 20])

    def __0(self, pick: int) -> int:
        # $script:1102172107011631$
        # - Sigh...
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:1010140307011542$
        # - Sigh...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1102172107011632$
        # - Will he be okay without me? Maybe I should go back...
        return -1

    def __30(self, pick: int) -> int:
        # $script:1010140307011543$
        # - Sigh...
        if pick == 0:
            # $script:1010140307011544$
            # - Why the long face?
            return 40
        return -1

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:1010140307011545$
            # - $MyPCName$? It seems like I can't go anywhere without bumping into you.
            return 40
        elif self.index == 1:
            # $script:1010140307011546$
            # - When I heard about the discovery of a new continent from somewhere else, I rushed over in order to study their unique magical practices. But I'm afraid I haven't learned much.
            return 40
        elif self.index == 2:
            # $script:1010140307011547$
            # - It seems $npcName:11004329[gender:0]$ is, to the contrary, already deep into his research.
            return 40
        elif self.index == 3:
            # $script:1010140307011548$
            # - I was hoping to find something that would improve Professor $npcName:11000032[gender:0]$'s condition.
            if pick == 0:
                # $script:1010140307011549$
                # - I believe in you.
                return 50
            return -1
        return -1

    def __50(self, pick: int) -> int:
        # $script:1010140307011550$
        # - Ahem! W-well I'm not going to make any progress sitting around talking to you! Excuse me.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.NEXT
        elif (self.state, self.index) == (40, 2):
            return Option.NEXT
        elif (self.state, self.index) == (40, 3):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (50, 0):
            return Option.CLOSE
        return Option.NONE
