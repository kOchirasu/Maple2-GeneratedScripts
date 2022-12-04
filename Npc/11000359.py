""" 11000359: Hendel """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001489$
        # - May I help you?
        return None # TODO

    def __20(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407001491$
            # - Are you traveling? You look like you're about my son's age.
            return 20
        elif self.index == 1:
            # $script:0831180407001492$
            # - $npcName:11000360[gender:0]$ is my only child. He left home recently, wanting to strike out on his own. If only he knew how much that hurt his mother.
            return 20
        elif self.index == 2:
            # $script:0831180407001493$
            # - The day before yesterday I got a letter from $npcName:11000360[gender:0]$. He must've written it somewhere around here... even the edges are singed. So I bought an ice pack to keep him cool.
            return 20
        elif self.index == 3:
            # $script:0831180407001494$
            # - My son, $npcName:11000360[gender:0]$ is on the other side of all that lava. I wanted to visit him, but I'm just too scared to cross it myself.
            return -1
        return -1

    def __30(self, pick: int) -> int:
        # $script:0831180407001495$
        # - My son, $npcName:11000360[gender:0]$ is on the other side of all that lava. I wanted to visit him, but I'm just too scared to cross it myself.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.NEXT
        elif (self.state, self.index) == (20, 1):
            return Option.NEXT
        elif (self.state, self.index) == (20, 2):
            return Option.NEXT
        elif (self.state, self.index) == (20, 3):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
