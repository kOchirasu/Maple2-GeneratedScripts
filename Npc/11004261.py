""" 11004261: Ludaritz Palace """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0911203207011173$
        # - <font color="#909090">(There's a placard in front of the palace.)</font>
        #   <i>There exists on Karkar Island two grand mansions that the Aliba Foundation has invested in. $map:02010062$ is one of them.</i>
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0911203207011174$
            # - <font color="#909090">(There's a placard in front of the palace.)</font>
            #   <i>There exists on Karkar Island two grand mansions that the Aliba Foundation has invested in. $map:02010062$ is one of them.</i>
            return 10
        elif self.index == 1:
            # $script:0911203207011175$
            # - <i>This mansion features a wondrous garden and other amenities. Only those with the express permission of the Aliba Foundation can live here, regardless of wealth or social stature.</i>
            return 10
        elif self.index == 2:
            # $script:0911203207011176$
            # - <i>For a time, it became a popular tourist destination, with a cafe on the first floor and the terrace opened to the public. However, due to fans swarming the building anytime $npc:11000406[gender:0]$ visited for some much-deserved rest and relaxation, the house has now been closed to the public.</i>
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
