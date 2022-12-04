""" 11001665: Karl """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0617211107006378$
        # - So, it's you.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0617211107006379$
        # - The empress has placed her faith in you.
        return -1

    def __20(self, pick: int) -> int:
        # $script:0617211107006380$
        # - Your eyes speak volumes about your character, $MyPCName$. I believe I can trust you. We are depending on you to protect the peace of Maple World.
        return -1

    def __30(self, pick: int) -> int:
        # $script:0426090007008441$
        # - What does Her Highness see in this stranger...?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
