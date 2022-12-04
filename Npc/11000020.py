""" 11000020: Marina """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000101$
        # - How may I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000104$
        # - I still can't believe that the road to $map:02000001$ is out. All the supplies for the empress's court have been sent along that road. Do you think anyone fell in when the ground opened up? Yeesh.
        return -1

    def __40(self, pick: int) -> int:
        # $script:0831180407000105$
        # - The open court of the empress is just around the corner, and yet bad things are happening constantly around here. First the supply carriage was robbed, and then the earthquake happened. All I wanted was for all this to go smoothly.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
