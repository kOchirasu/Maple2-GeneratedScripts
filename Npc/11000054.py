""" 11000054: Luke """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000232$
        # - What?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000235$
        # - Bah! $npcName:11000062[gender:1]$ said she would go attend the court with her dad. Why isn't my gramps saying anything? I want to go to see the empress too!
        return -1

    def __40(self, pick: int) -> int:
        # $script:0831180407000236$
        # - $npcName:11000056[gender:0]$ knows about a lot of things. If you have questions, you should ask him!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
