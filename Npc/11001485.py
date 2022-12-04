""" 11001485: Araxis """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0106143407005788$
        # - So, how can I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0106143407005791$
        # - So... what do you think about demons?
        if pick == 0:
            # $script:0106143407005792$
            # - They must be vanquished!
            return 40
        elif pick == 1:
            # $script:0106143407005793$
            # - I hadn't really thought about them.
            return 50
        return -1

    def __40(self, pick: int) -> int:
        # $script:0106143407005794$
        # - Indeed? That's what most people think about demons. I don't believe vanquishing them is the best solution. At the very least, we should learn more about their abilities first.
        if pick == 0:
            # $script:0106143407005795$
            # - What kinds of abilities do they have?
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:0106143407005796$
        # - Oh, many kinds indeed. Most involve temptations used to trick mortals into doing their bidding. The problem is the way those abilities are used, not the demons themselves. There are ways to use demonic abilities for good.
        if pick == 0:
            # $script:0106143407005797$
            # - How can you do that?
            return 42
        return -1

    def __42(self, pick: int) -> int:
        # $script:0106143407005798$
        # - Well... I can't really say yet. There's so much left unexplained about demons. And even if I found ways to use their powers, I'm not sure I could use them without dire consequences.
        return -1

    def __50(self, pick: int) -> int:
        # $script:0106143407005799$
        # - What a shame! I can tell by your aura that you're strong enough to handle demons. But if you're not interested, it hardly matters. Remember, there are always demons around us.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (42, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.CLOSE
        return Option.NONE
