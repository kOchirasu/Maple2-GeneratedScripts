""" 11001306: Livanda """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1215203907005025$
        # - Are you here for my father? 
        return None # TODO

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227194507005647$
            # - Dad's a thoughtful and affection man, if you get to know him.
            return 40
        elif self.index == 1:
            # $script:1227194507005648$
            # - There's more to him than he lets on.
            #   <font color="#909090">(There are tears in her eyes.)</font>
            if pick == 0:
                # $script:1227194507005649$
                # - Are you okay?
                return 41
            return -1
        return -1

    def __41(self, pick: int) -> int:
        # $script:1227194507005650$
        # - I'll be okay...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        return Option.NONE
