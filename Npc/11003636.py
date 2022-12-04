""" 11003636: JCH-2YS """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1109121007009064$
        # - Identity confirmed... $MyPCName$...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1109121007009065$
        # - Initiating light banter protocol. I am just passing through town, stranger.
        if pick == 0:
            # $script:1109121007009066$
            # - Aren't you a polite robot?
            return 11
        return -1

    def __11(self, pick: int) -> int:
        # $script:1109121007009067$
        # - Rhetorical question detected. Response: Can I help you with something?
        if pick == 0:
            # $script:1109121007009068$
            # - No, no, I'm good.
            return 12
        return -1

    def __12(self, pick: int) -> int:
        # $script:1109121007009069$
        # - Detecting trace amounts of $npcName:11003535[gender:1]$ pheromones... Special encoders enabled. Message: "Code EK-LOVE."
        if pick == 0:
            # $script:1109121007009070$
            # - You're an agent...?
            return 13
        return -1

    def __13(self, pick: int) -> int:
        # $script:1109121007009071$
        # - Resuming normal operations. Have a nice day.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (13, 0):
            return Option.CLOSE
        return Option.NONE
