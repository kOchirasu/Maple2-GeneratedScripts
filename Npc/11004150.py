""" 11004150: Harry """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806025707010571$
        # - What is it?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806025707010572$
        # - Are you here to participate in Mushking Royale too? I'm afraid we've already got a squad of four. I'll see you on the battlefield!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
