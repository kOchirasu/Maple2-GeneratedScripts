""" 11000200: Neal """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000869$
        # - What is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000872$
        # - $npcName:11000202[gender:0]$ is really dumb. Did you see him standing there? He's punishing himself! 
        return -1

    def __40(self, pick: int) -> int:
        # $script:0831180407000873$
        # - $npcName:11000201[gender:0]$ is my friend from $map:02000023$. He's an elf. Isn't that awesome? 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
