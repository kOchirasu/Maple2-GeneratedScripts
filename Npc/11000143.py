""" 11000143: Boen """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000581$
        # - Hello.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000584$
        # - Sigh... See that big hotel on the cliff? It dropped from the sky one day, literally out of the blue. Since then, monsters have been swarming the area. It's getting impossible to do anything.
        return -1

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000585$
            # - Huh? You think my name is funny. I disagree. 
            return 40
        elif self.index == 1:
            # $script:0831180407000586$
            # - Boen is easy to remember and rolls off the tongue beautifully. Go to the top of that cliff and shout my name. It'll echo for a long time.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.CLOSE
        return Option.NONE
