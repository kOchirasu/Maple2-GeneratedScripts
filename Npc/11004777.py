""" 11004777: Snowleaf Fairfolk """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1122135407015958$
        # - Travel to the festively-decorated <font color="#ffd200">$map:63000072$</font> using the <font color="#00a2ed">Go to Event Map</font> button!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1122135407015959$
        # - Click on the <font color="#00a2ed">Go to Event Map</font> button to go to <font color="#ffd200">$map:63000072$</font>.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
