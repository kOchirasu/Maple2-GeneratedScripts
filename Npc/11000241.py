""" 11000241: Sally """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001019$
        # - Welcome.
        return None # TODO

    def __20(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407001021$
            # - Are you heading to $map:02000135$? It's famous for its beautiful scenery. At the very top you'll find the Cloud Cafe, famous among young couples. You can take the cable car all the way up to the top if you want to see it.
            return 20
        elif self.index == 1:
            # $script:0831180407001022$
            # - Our cable cars are made to last. They won't break, no matter how hard you jump! Please note that we won't be liable for injuries if you jump yourself right out of the car.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.NEXT
        elif (self.state, self.index) == (20, 1):
            return Option.CLOSE
        return Option.NONE
