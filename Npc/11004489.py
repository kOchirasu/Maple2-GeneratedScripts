""" 11004489: Leppens """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1227192907012303$
        # - Oh, hello. You must be here for my report. I'm afraid it's not very good...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1227192907012304$
        # - Oh, hello. You must be here for my report. I'm afraid it's not very good...
        if pick == 0:
            # $script:1227192907012305$
            # - Something wrong?
            return 11
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012306$
            # - I'm looking into the soil contamination that started spreading around here not too long ago.
            return 11
        elif self.index == 1:
            # $script:1227192907012307$
            # - What do you know about the mechanical monster that roams this area?
            if pick == 0:
                # $script:1227192907012308$
                # - I know all about it!
                return 12
            elif pick == 1:
                # $script:1227192907012309$
                # - Not a whole lot.
                return 13
            return -1
        return -1

    def __12(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012313$
            # - Then you're aware of how big a problem Gigantica is for us.
            return 12
        elif self.index == 1:
            # $script:1227192907012314$
            # - Wherever Gigantica appears, the soil becomes tainted. We've actually had to abandoned a camp because the toxins got so bad!
            return 12
        elif self.index == 2:
            # $script:1227192907012315$
            # - That's why I'm needed. If I can analyze the contamination, we may be able to counteract it—or, at the very least, predict where Gigantica will go next.
            return -1
        return -1

    def __13(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012310$
            # - Really? You must not read the crew newsletter. Our efforts to explore Kritias have been hindered by this giant robotic worm. We call it Gigantica.
            return 13
        elif self.index == 1:
            # $script:1227192907012311$
            # - Wherever Gigantica appears, the soil becomes tainted. We've actually had to abandon a camp because the toxins got so bad!
            return 13
        elif self.index == 2:
            # $script:1227192907012312$
            # - That's why I'm needed. If I can analyze the contamination, we may be able to counteract it—or, at the very least, predict where Gigantica will go next.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.NEXT
        elif (self.state, self.index) == (11, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.NEXT
        elif (self.state, self.index) == (12, 1):
            return Option.NEXT
        elif (self.state, self.index) == (12, 2):
            return Option.CLOSE
        elif (self.state, self.index) == (13, 0):
            return Option.NEXT
        elif (self.state, self.index) == (13, 1):
            return Option.NEXT
        elif (self.state, self.index) == (13, 2):
            return Option.CLOSE
        return Option.NONE
