""" 11000586: Injured Guard """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([50, 60, 70, 80])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002370$
        # - Ugh... 
        return None # TODO

    def __50(self, pick: int) -> int:
        # $script:0831180407002375$
        # - H-help... 
        return -1

    def __60(self, pick: int) -> int:
        # $script:0831180407002376$
        # - Ugh... 
        return -1

    def __70(self, pick: int) -> int:
        # $script:0831180407002377$
        # - Ugh... No... 
        return -1

    def __80(self, pick: int) -> int:
        # $script:0831180407002378$
        # - I can't... die like this... 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (50, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (60, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (70, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (80, 0):
            return Option.CLOSE
        return Option.NONE
