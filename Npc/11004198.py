""" 11004198: Wolf Heart """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806025707010644$
        # - May I help you?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806025707010645$
        # - Our yearly pilgrimage through the Vayar Mountains has made the warriors of Murpagoth mighty. Perhaps you will join us on our next journey? That is of course, after we have proven ourselves on the fields of Mushtopia.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
