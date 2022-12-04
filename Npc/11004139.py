""" 11004139: Einos """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806025707010549$
        # - How may I help you?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806025707010550$
        # - It is all well and good to forget one's troubles in a cheerful place such as this, but we cannot lose sight of what's real. A dark storm gathers over Maple World. Now more than ever, we need heroes. Will you answer the call?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
