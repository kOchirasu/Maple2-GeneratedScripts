""" 11004319: Mika """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 30])

    def select(self) -> int:
        return random.choice([0, 20])

    def __0(self, pick: int) -> int:
        # $script:1102172107011621$
        # - I've got a bad feeling...
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:1010140307011441$
        # - I've got a bad feeling...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1102172107011622$
        # - I sense draconic power... Did I finally find them?
        return -1

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:1010140307011442$
            # - Oh, it's you!
            return 30
        elif self.index == 1:
            # $script:1010140307011443$
            # - It's been a while! What're you doing here?
            if pick == 0:
                # $script:1010140307011444$
                # - What are you doing here?
                return 40
            return -1
        return -1

    def __40(self, pick: int) -> int:
        # $script:1010140307011445$
        # - A few days ago I sensed an unusual energy coming from this place, so I came to investigate.
        if pick == 0:
            # $script:1010140307011446$
            # - Did you find anything?
            return 50
        return -1

    def __50(self, pick: int) -> int:
        if self.index == 0:
            # $script:1010140307011447$
            # - Did I ever! As soon as I arrived, I felt it—that familiar aura... The traces of dragons!
            return 50
        elif self.index == 1:
            # $script:1010140307011448$
            # - There's no question about it, dragons once lived in this land! I got to thinking that maybe they were related to the dark dragons that Biset told me about.
            return 50
        elif self.index == 2:
            # $script:1010141507011602$
            # - Now I'm just waiting for my next big clue.
            if pick == 0:
                # $script:0111224807012687$
                # - Well, good luck!
                return 60
            return -1
        return -1

    def __60(self, pick: int) -> int:
        # $script:0111224807012688$
        # - Thank you!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (50, 0):
            return Option.NEXT
        elif (self.state, self.index) == (50, 1):
            return Option.NEXT
        elif (self.state, self.index) == (50, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (60, 0):
            return Option.CLOSE
        return Option.NONE
