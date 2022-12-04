""" 11000995: Maruchi """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003416$
        # - Ah, what is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407003419$
            # - Some people say I don't look like an adventurer. They think I would look more relaxed sitting behind a desk, reading and daydreaming.
            return 30
        elif self.index == 1:
            # $script:0831180407003420$
            # - That means they don't know me. I prefer seeing things for myself rather than reading them from books. That's why I'm so happy about this job with the Adventurer's Guild.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.CLOSE
        return Option.NONE
