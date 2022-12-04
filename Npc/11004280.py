""" 11004280: Pillar of Light """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0911203207011291$
        # - <font color="#909090">(A bright light shines through a crack in the wall.)</font>
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0911203207011292$
            # - <font color="#909090">(A bright light shines through a crack in the wall.)</font>
            return 10
        elif self.index == 1:
            # $script:0911203207011293$
            # - <font color="#909090">(This passageway was blocked off long ago, but something on the other side still shines brilliantly.)</font>
            return 10
        elif self.index == 2:
            # $script:0913151207011306$
            # - <font color="#909090">(You can sense a different sort of power beyond the crack in the wall.)</font>
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.NEXT
        elif (self.state, self.index) == (10, 2):
            return Option.CLOSE
        return Option.NONE
