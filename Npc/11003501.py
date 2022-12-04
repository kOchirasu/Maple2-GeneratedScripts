""" 11003501: Rosa """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 50])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0816160115008978$
        # - How may I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0816160115008979$
        # - If I'm going to get into Team Mushroom, I've got to study hard!
        return -1

    def __50(self, pick: int) -> int:
        # $script:0816160115008981$
        # - I want to be best friends with all kinds of monsters. That's what Team Mushroom is all about, right?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.CLOSE
        return Option.NONE
