""" 11001080: Yovo """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1216233107005208$
        # - The desert hides many secrets, and I'm going to uncover them all!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1216233107005211$
        # - You can feel it, too, can't you? There's something wrong here. You have sharp senses for a human.
        if pick == 0:
            # $script:1216233107005212$
            # - What is this strange energy?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:1216233107005213$
        # - I wouldn't get too curious about it if I were you. In fact, keep your distance unless you have some good info for me. I don't have time to answer questions for ignoramuses.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        return Option.NONE
