""" 11004251: Faint Writings """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0829171107010962$
        # - <font color="#909090">(Something is crudely scratched here.)</font>
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0829171107010963$
            # - <font color="#909090">(Something is crudely scratched here.)</font>
            return 10
        elif self.index == 1:
            # $script:0830163207010991$
            # - "That man is the root of all evil!"
            return 10
        elif self.index == 2:
            # $script:0830163207010992$
            # - "He appeared out of the blue, pale as a ghost. Even my cows were scared of him."
            return 10
        elif self.index == 3:
            # $script:0830173807010993$
            # - "But I couldn't kick him out. He seemed injured, and I was raised a gentleman. But letting him rest in my fields was a mistake. He pulled out a black bottle, grinned this sick little grin, then poured it all on the ground."
            return 10
        elif self.index == 4:
            # $script:0830173807010994$
            # - "Everything happened quickly after that. The dark shadow that blossomed out of the liquid..."
            return 10
        elif self.index == 5:
            # $script:0830173807010995$
            # - "My livestock were engulfed by darkness. They cried out as they transformed into monsters. The fields and streams turned black as ink. Even the people living on the farm became twisted."
            return 10
        elif self.index == 6:
            # $script:0830173807010996$
            # - "I tried to outrun the darkness, but I sense my time is short. I can feel the corruption of this forsaken ground crawling up my legs, slowly transforming me..."
            return 10
        elif self.index == 7:
            # $script:0830173807010997$
            # - "If you can read this, flee! Flee at once! This land is cursed. If you stay, in the end, you'll become... like me... IT IS TOO LATE!"
            return 10
        elif self.index == 8:
            # $script:0830174907010998$
            # - <font color="#909090">(Strange letters appear beneath that. You can't decipher them, but they send a chill down your spine.)</font>
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
            return Option.NEXT
        elif (self.state, self.index) == (10, 4):
            return Option.NEXT
        elif (self.state, self.index) == (10, 5):
            return Option.NEXT
        elif (self.state, self.index) == (10, 6):
            return Option.NEXT
        elif (self.state, self.index) == (10, 7):
            return Option.NEXT
        elif (self.state, self.index) == (10, 8):
            return Option.CLOSE
        return Option.NONE
