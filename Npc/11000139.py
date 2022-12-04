""" 11000139: Lailai """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([40, 50])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000565$
        # - Bah, what now?
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180407000569$
        # - Hmph, this used to be a really nice place to live before that gigantic hotel dropped from the sky. It's been attracting all kinds of things and making our lives miserable.
        return -1

    def __50(self, pick: int) -> int:
        # $script:0831180407000570$
        # - Well, I'm not fighting those monsters. It's not that they're too scary... I just don't want to be bothered.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.CLOSE
        return Option.NONE
