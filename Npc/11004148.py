""" 11004148: Marina """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806025707010567$
        # - How may I help you?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806025707010568$
        # - Ever since we were little, it's always been me, $npcName:11004149$ and the sea, hehe!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
