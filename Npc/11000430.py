""" 11000430: Antoine """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40, 41])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001791$
        # - I'm so glad I decided to come to the beach.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407001793$
        # - $map:02000111$ is such a beautiful place to be! Except for the turtles. They're awful.
        return -1

    def __40(self, pick: int) -> int:
        # $script:0831180407001794$
        # - Mm?
        if pick == 0:
            # $script:0831180407001795$
            # - $npcName:11000362[gender:0]$'s special...
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:0831180407001796$
        # - Not interested.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        return Option.NONE
