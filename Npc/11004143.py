""" 11004143: Lian """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806025707010557$
        # - Hahaha!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806025707010558$
        # - $npcName:11001167[gender:0]$ likes to frighten us with scary stories, but now that I know better, I don't believe a word he says!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
