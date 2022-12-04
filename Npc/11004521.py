""" 11004521: Mayu """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0102174210002228$
        # - If you need a lift back to $map:02000001$, I'm your gal!
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0102174210002229$
            # - If you need a lift back to $map:02000001$, I'm your gal!
            return 10
        elif self.index == 1:
            # $script:0102174210002230$
            # - We're heading out straight away. If you miss this place, you can always use the <i>Lumiwind</i> to come back. Are you ready to return to $map:02000001$?
            if pick == 0:
                # $script:0102174210002231$
                # - Take me to $map:02000001$!
                return 11
            return -1
        return -1

    def __11(self, pick: int) -> int:
        # functionID=1 
        # $script:0102174210002232$
        # - All right. Away we go!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.CLOSE
        return Option.NONE
