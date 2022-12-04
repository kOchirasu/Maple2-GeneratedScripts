""" 11000839: Pochi """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003069$
        # - Can I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407003072$
            # - Do you know who $npcName:11000614[gender:0]$ is? He's a friend of mine in $map:03000135$.
            return 30
        elif self.index == 1:
            # $script:0831180407003073$
            # - We first met in Katramus. The Lumina Liberation Army sprung us while we were being transferred to another prison, and we joined up together. 
            return 30
        elif self.index == 2:
            # $script:0831180407003074$
            # - We promised that we'd stick together like we did during our time in prison. That was the most difficult time of our lives.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.NEXT
        elif (self.state, self.index) == (30, 2):
            return Option.CLOSE
        return Option.NONE
