""" 11004091: Lucky Whale """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0622133907010325$
        # - <font color="#909090">(This mascot is the unofficial guardian of $map:02000377$.)</font>
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0622133907010326$
            # - <font color="#909090">(This mascot is the unofficial guardian of $map:02000377$.)</font>
            return 10
        elif self.index == 1:
            # $script:0622133907010327$
            # - <font color="#909090">(The local fishermen consider this whale lucky. They say that you'll catch a huge fish if you kiss the whale's cheek before heading out.)</font>
            return 10
        elif self.index == 2:
            # $script:0622133907010328$
            # - <font color="#909090">(It's also lucky for the villagers. If you have a dream about this whale, buy a lottery ticket the next day and you'll surely win. At least, that's what they tell you.)</font>
            return 10
        elif self.index == 3:
            # $script:0622133907010329$
            # - <font color="#909090">(Some people assume that this whale's name is Coco, given the name of the island. However, the creator of the whale insists that it isn't true.)</font>
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.NEXT
        elif (self.state, self.index) == (10, 2):
            return Option.NEXT
        elif (self.state, self.index) == (10, 3):
            return Option.CLOSE
        return Option.NONE
