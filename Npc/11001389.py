""" 11001389: Dalan """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217193307005389$
        # - Why's he so worried all the time?
        return None # TODO

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:1223165107005563$
            # - I have this friend named $npcName:11001396[gender:1]$. She has a house, but she practically lives out in the desert...
            return 40
        elif self.index == 1:
            # $script:1223165107005564$
            # - She had a chance to get a good job in $map:02010002$, but she let it slip through her fingers. She could've been enjoying the finer things in life by now...
            return 40
        elif self.index == 2:
            # $script:1223165107005565$
            # - She's always talking about ruins and secrets. Why does she let such silly nonsense weigh her down? She tried to tell me about it, but honestly, it's so boring I forgot it already...
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.NEXT
        elif (self.state, self.index) == (40, 2):
            return Option.CLOSE
        return Option.NONE
