""" 11001591: Einos """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0504151707006079$
        # - Hello.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0515180307006130$
        # - $npcName:11001229[gender:0]$ is strong. He'll recover. Until then, the Life Lapenta will protect him.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
