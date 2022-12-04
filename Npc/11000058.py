""" 11000058: Elmin """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40, 50])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000255$
        # - What is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000258$
        # - If I had stayed with Bella that day... 
        return -1

    def __40(self, pick: int) -> int:
        # $script:0831180407000259$
        # - I used to live here with my family, but... I'm the only one living in this house now. I miss them so much...
        return -1

    def __50(self, pick: int) -> int:
        # $script:0831180407000260$
        # - Sometimes I sit by the window, watching the stars fade away one by one, reminiscing about the good old days. I try not to recall the sad memories, but only the good, happy ones.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.CLOSE
        return Option.NONE
