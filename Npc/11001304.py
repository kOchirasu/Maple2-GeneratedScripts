""" 11001304: Asimov """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1215203907005023$
        # - How may I help you?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1228222807005745$
        # - I haven't been in $map:02000001$ for a long, long time. The air is... dustier than I remember. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
