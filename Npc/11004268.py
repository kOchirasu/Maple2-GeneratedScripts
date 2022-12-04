""" 11004268: West Auto Bridge """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0911203207011222$
        # - <font color="#909090">(This bridge connects the city to the desert of Karkar. It plays a major role in the development of the island.)</font>
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0911203207011223$
            # - <font color="#909090">(This bridge connects the city to the desert of Karkar. It plays a major role in the development of the island.)</font>
            return 10
        elif self.index == 1:
            # $script:0911203207011224$
            # - <font color="#909090">(This wonderful bridge was co-designed by the genius architect brother Opath and Oparts. The younger brother, Oparts, was in charge of the western exchange. His flair for the fabulous is evident in the bridge's flashy lights.)</font>
            return 10
        elif self.index == 2:
            # $script:0911203207011225$
            # - <font color="#909090">(There are over 100 lights in use on the West Auto Bridge, and they symbolize the glamor and promise of the big city.)</font>
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
