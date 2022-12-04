""" 11004322: Startz """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 30])

    def select(self) -> int:
        return random.choice([0, 20])

    def __0(self, pick: int) -> int:
        # $script:1102172107011627$
        # - Hm...
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:1010140307011471$
        # - Hm...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1102172107011628$
        # - That might look good on my menu...
        return -1

    def __30(self, pick: int) -> int:
        # $script:1010140307011472$
        # - Hmm?
        if pick == 0:
            # $script:1010140307011473$
            # - Good to see you! It's been a while.
            return 40
        return -1

    def __40(self, pick: int) -> int:
        # $script:1010140307011474$
        # - Yeah, whatever.
        if pick == 0:
            # $script:1010140307011475$
            # - What are you doing here?
            return 50
        return -1

    def __50(self, pick: int) -> int:
        # $script:1010140307011476$
        # - $npcName:11004319[gender:1]$ dragged us here to search for dark dragons.
        if pick == 0:
            # $script:1010140307011477$
            # - Really? Have you found anything?
            return 60
        return -1

    def __60(self, pick: int) -> int:
        if self.index == 0:
            # $script:1010140307011478$
            # - I have actually. <b>New ingredients.</b>
            return 60
        elif self.index == 1:
            # $script:1010140307011479$
            # - This place is littered with ingredients Maple World has never seen before!
            return 60
        elif self.index == 2:
            # $script:1010140307011480$
            # - When I integrate them into my menu, it'll blow people's minds. You should stop by my restaurant some time.
            if pick == 0:
                # $script:0111224807012689$
                # - I'll definitely pay you a visit.
                return 70
            return -1
        return -1

    def __70(self, pick: int) -> int:
        # $script:0111224807012690$
        # - Cool.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (60, 0):
            return Option.NEXT
        elif (self.state, self.index) == (60, 1):
            return Option.NEXT
        elif (self.state, self.index) == (60, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (70, 0):
            return Option.CLOSE
        return Option.NONE
