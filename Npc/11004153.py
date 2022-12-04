""" 11004153: Yentayo """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806025707010577$
        # - What seems to be the problem?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806025707010578$
        # - There are chests hidden all over Maple World, but the ones in $map:02000499$ are... different. Hehe, you'll see!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
