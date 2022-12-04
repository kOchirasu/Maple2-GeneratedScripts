""" 11001434: Pardore """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1216230507005197$
        # - They have to be around here somewhere.
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:1216230507005201$
        # - It's peaceful out here, isn't it? Of course, it'd be more peaceful without all the monsters.
        if pick == 0:
            # $script:1216230507005202$
            # - What can you tell me about the place?
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:1216230507005203$
        # - Minar Desert used to be the home of the dragons, or so they say. Whether or not that's true, there are plenty of legends about this place... Such as the legend of the sacred tribe.
        if pick == 0:
            # $script:1216230507005204$
            # - What sacred tribe?
            return 42
        return -1

    def __42(self, pick: int) -> int:
        # $script:1216230507005205$
        # - Do you know about the snow leopards? There are only a few of them. The younger leopards look human, but as they grow, so does their sacred power. They grow bestial and lose the ability to speak. They're no ordinary spirits; some believe they're closer to gods.
        if pick == 0:
            # $script:1216230507005206$
            # - Have you ever seen a snow leopard?
            return 43
        return -1

    def __43(self, pick: int) -> int:
        # $script:1216230507005207$
        # - I caught a glimpse of one once. Of course, most folks think I dreamed it, but I know that's not true. I'm determined to uncover the secret of the snow leopards. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (42, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (43, 0):
            return Option.CLOSE
        return Option.NONE
