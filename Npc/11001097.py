""" 11001097: Triz """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003688$
        # - How may I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407003691$
            # - If I had to pick my most popular invention, it would be NSD 3200. It's a device that dismantles equipment and extracts onyx from it.
            return 30
        elif self.index == 1:
            # $script:0831180407003692$
            # - People think the blacksmiths of the Nerman Forge came up with it, but I was brought in to design it for them. I was compensated for my services, of course, but if I knew it'd become so popular I would've asked for more royalties!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.CLOSE
        return Option.NONE
