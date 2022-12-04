""" 11001714: Tinchai """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0728022507006966$
        # - Hello there.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0805021607007090$
        # - None of us are okay right now. All the more reason to stay strong.
        if pick == 0:
            # $script:0805021607007091$
            # - (Nod your head.)
            return 40
        return -1

    def __40(self, pick: int) -> int:
        # $script:0805021607007092$
        # - You know, I... Oh, never mind.
        #   <font color="#909090">($npcName:11001714[gender:1]$ looks you in the eye, but stops herself from saying more.)</font>
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
