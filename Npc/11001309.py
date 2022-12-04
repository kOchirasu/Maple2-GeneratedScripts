""" 11001309: Devin """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1215203907005028$
        # - Ugh, my head...
        return None # TODO

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227194507005659$
            # - I've got more cases on my plate than I could ever solve in a single lifetime.
            return 40
        elif self.index == 1:
            # $script:1227194507005660$
            # - Sure, I'm happy that $map:02010002$ is growing. But does the crime have to grow with it? Our prison is bursting at the seams!
            return 40
        elif self.index == 2:
            # $script:1227194507005661$
            # - This isn't police work. It's war! But somebody's got to protect the city, right?
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.NEXT
        elif (self.state, self.index) == (40, 2):
            return Option.CLOSE
        return Option.NONE
