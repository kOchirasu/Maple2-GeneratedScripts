""" 11004085: Oath Marker """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0622133907010290$
        # - <font color="#909090">(This enchanted marker has been warded against the ages. Ancient writing has been etched into it.)</font>
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0622133907010291$
            # - <font color="#909090">(This enchanted marker has been warded against the ages. Ancient writing has been etched into it.)</font>
            return 10
        elif self.index == 1:
            # $script:0622133907010292$
            # - <i>When our world was young, the goddess of light faded away. It became the responsibility of us fairfolk to carry what remained of her work into the future.</i>
            return 10
        elif self.index == 2:
            # $script:0622133907010293$
            # - <i>The taint of the darkness remained. Without our goddess, it fell to us to seal it away.</i>
            return 10
        elif self.index == 3:
            # $script:0622133907010294$
            # - <i>Someday, we believe that our goddess will return to us in mortal form. Until then, we wait and stand watch against the shadows.</i>
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.NEXT
        elif (self.state, self.index) == (10, 2):
            return Option.NEXT
        elif (self.state, self.index) == (10, 3):
            return Option.CLOSE
        return Option.NONE
