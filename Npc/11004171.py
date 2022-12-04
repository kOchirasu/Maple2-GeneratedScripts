""" 11004171: Startz """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806025707010599$
        # - Order now or get a face full of burning oil. Your choice. 
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806025707010600$
        # - Don't get the wrong idea. I'm not here selling churros because my restaurant is doing poorly, I'm just here to enjoy myself.
        if pick == 0:
            # $script:0806025707010601$
            # - So then why ARE you selling churros?
            return 11
        elif pick == 1:
            # $script:0806025707010602$
            # - Can I have a churro?
            return 12
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:0806025707010603$
            # - Huh? Because I like to cook, obviously.
            return 11
        elif self.index == 1:
            # $script:0806025707010604$
            # - Well... If I'm being honest, we all trekked all the way here to $map:02000499$ to take a vacation, but we ran out of money to pay for lodging.
            return -1
        return -1

    def __12(self, pick: int) -> int:
        # $script:0806025707010605$
        # - They're not done yet. Come back later.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.NEXT
        elif (self.state, self.index) == (11, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (12, 0):
            return Option.CLOSE
        return Option.NONE
