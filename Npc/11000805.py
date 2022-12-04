""" 11000805: Hozzie """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002966$
        # - H-how can I...? 
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407002968$
        # - I don't care who you are. Just stop talking to me. They'll beat me up if they see me talking to you.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
