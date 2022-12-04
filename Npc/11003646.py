""" 11003646: Nikki """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1109121007009176$
        # - Hop hop!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1109121007009177$
        # - Hi-hi! I'm $npcName:11003646$ the Bunny!
        if pick == 0:
            # $script:1109121007009178$
            # - Hello there, fluffy rabbit!
            return 11
        return -1

    def __11(self, pick: int) -> int:
        # $script:1109121007009179$
        # - Ahem. Youse the mug Schatten sent? Here's the code phrase: "The square looks at the flower twice."
        if pick == 0:
            # $script:1109121007009180$
            # - Uh... What?
            return 12
        return -1

    def __12(self, pick: int) -> int:
        # $script:1109121007009181$
        # - Hop hop!
        if pick == 0:
            # $script:1109121007009182$
            # - W-wait... What did you say?
            return 13
        return -1

    def __13(self, pick: int) -> int:
        # $script:1109121007009183$
        # - I didn't say anything, you silly goose! Run along now!
        if pick == 0:
            # $script:1109121007009184$
            # - Uh...
            return 14
        return -1

    def __14(self, pick: int) -> int:
        # $script:1109121007009185$
        # - Hop hop!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (13, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (14, 0):
            return Option.CLOSE
        return Option.NONE
