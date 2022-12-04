""" 11000023: Toomy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000125$
        # - What's up?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180407000126$
        # - Are you also trying to attend the court? I was on my way there... stopping to sample some delicious food along the way, of course... and had my plans dashed by this wretched rift! I suppose I could try the forest, but it's fairly frightening.
        if pick == 0:
            # $script:0831180407000127$
            # - Wait, can you get around the rift through the forest?
            return 11
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000128$
            # - That's what I heard! Follow the path between the trees over there to $map:02000116$, and then keep on until you get to $map:02000001$.
            return 11
        elif self.index == 1:
            # $script:0831180407000129$
            # - I wouldn't try it if I were you, though. A few folks have faced the forest... but none have returned from $map:02000116$.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.NEXT
        elif (self.state, self.index) == (11, 1):
            return Option.CLOSE
        return Option.NONE
