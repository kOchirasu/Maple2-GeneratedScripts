""" 11004370: Claus """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1109213607011783$
        # - If you're looking for a classic holiday tree, go evergreen or go home.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1109213607011784$
        # - If you're looking for a classic holiday tree, go evergreen or go home.
        if pick == 0:
            # $script:1120173007011855$
            # - Ooh, an evergreen?
            return 11
        return -1

    def __11(self, pick: int) -> int:
        # $script:1120173007011856$
        # - There's nothing quite like it! Tall, bushy, and wonderfully scented... And if you're looking for the most beautiful tree, you'd need to get a Korean fir tree.
        if pick == 0:
            # $script:1120173007011857$
            # - The Korean fir tree, you say? Hmm...
            return 12
        return -1

    def __12(self, pick: int) -> int:
        # $script:1120173007011858$
        # - It grows on Mount Halla, and it's simply divine. A shame they're becoming harder to find these days. Climate change, you know.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.CLOSE
        return Option.NONE
