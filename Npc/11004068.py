""" 11004068: Springs Totem """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0619202207010140$
        # - <font color="#909090">(The bubbling water behind this statue is just the right temperature. There's a plaque on the totem.)</font>
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0619202207010141$
            # - <font color="#909090">(The bubbling water behind this statue is just the right temperature. There's a plaque on the totem.)</font>
            return 10
        elif self.index == 1:
            # $script:0619202207010142$
            # - <i>Dealing with aches? Pains? Fatigue? Skin blemishes? Then take a soak at these world-renown hot springs! A five minute soak in these naturally heated waters is all you need to feel like a new person!</i>
            return 10
        elif self.index == 2:
            # $script:0625111007010361$
            # - <i>The people of Perion know that nothing is better after a long day of hunting than a dip on the springs. And best of all, it's free to use!</i>
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
