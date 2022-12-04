""" 11004560: Rovey """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0220211107014495$
        # - Hm.
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0220211107014496$
            # - And who might you be?
            return 10
        elif self.index == 1:
            # $script:0220211107014497$
            # - I haven't seen you before, but you seem like a formidable opponent.
            if pick == 0:
                # $script:0220211107014498$
                # - And you are?
                return 11
            return -1
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:0220211107014499$
            # - Ahem! I am Rovey, drillmaster for the Royal Knights.
            return 11
        elif self.index == 1:
            # $script:0220211107014500$
            # - I've trained many knights around your age. In fact, you remind me of one particular fool whom I once taught...
            return 11
        elif self.index == 2:
            # $script:0220211107014501$
            # - Well, I shan't waste any more words on you. I will see you in the rumble.
            return -1
        return -1

    def __20(self, pick: int) -> int:
        if self.index == 0:
            # $script:0220211107014502$
            # - !!
            return 20
        elif self.index == 1:
            # $script:0220211107014503$
            # - You...
            if pick == 0:
                # $script:0220211107014504$
                # - $npcName:11004560[gender:0]$?!
                return 21
            return -1
        return -1

    def __21(self, pick: int) -> int:
        # $script:0220211107014505$
        # - I'm surprised that foolish sense of justice hasn't gotten you killed. Why did you come here?
        if pick == 0:
            # $script:0220211107014506$
            # - I'm here to fight.
            return 22
        return -1

    def __22(self, pick: int) -> int:
        # $script:0220211107014507$
        # - It's been some time since we last sparred. I'm curious to see how you've grown.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.NEXT
        elif (self.state, self.index) == (11, 1):
            return Option.NEXT
        elif (self.state, self.index) == (11, 2):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.NEXT
        elif (self.state, self.index) == (20, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (21, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (22, 0):
            return Option.CLOSE
        return Option.NONE
