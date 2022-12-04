""" 11000244: Mrs. Toulette """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([40, 50])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001037$
        # - Can I help you?
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180407001041$
        # - Why are you talking to me? What do you want?
        return -1

    def __50(self, pick: int) -> int:
        # $script:0831180407001042$
        # - People say that the richer you get, the pickier you get. Makes sense, since you can have whatever you want with enough money.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.CLOSE
        return Option.NONE
