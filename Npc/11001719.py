""" 11001719: Junta """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0728022507006970$
        # - You have something to say to me?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0728024507007016$
        # - If things are to return to normal, then we must stay united. Don't forget that.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
