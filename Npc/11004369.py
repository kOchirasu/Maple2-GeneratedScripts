""" 11004369: Claus """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1109213607011781$
        # - I grow my own trees to decorate, you know. My commitment to the holidays cannot be questioned.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1109213607011782$
        # - My favorite memory from my childhood is decorating our tree every year. Now that I tend the garden myself, it can be even grander.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
