""" 11004329: Jorge """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 30])

    def select(self) -> int:
        return random.choice([0, 20])

    def __0(self, pick: int) -> int:
        # $script:1102172107011629$
        # - I see... What a novel approach.
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:1010140307011535$
        # - I see... What a novel approach.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1102172107011630$
        # - I see... What a novel approach.
        return -1

    def __30(self, pick: int) -> int:
        # $script:1010140307011536$
        # - I see... What a novel approach.
        if pick == 0:
            # $script:1010140307011537$
            # - What are you working on there?
            return 40
        return -1

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:1010140307011538$
            # - Hm? Oh, I'm doing research on the magic of this continent!
            return 40
        elif self.index == 1:
            # $script:1010140307011539$
            # - The rumors have already spread as far as $map:02000023$ that the people of this continent practice a form of magic we've never seen.
            return 40
        elif self.index == 2:
            # $script:1010140307011540$
            # - There's no way that I would miss such a tantalizing opportunity for self-edification.
            return 40
        elif self.index == 3:
            # $script:1010140307011541$
            # - Just you wait! I'm on the verge of a groundbreaking discovery, one for the history books!
            if pick == 0:
                # $script:0111232407012695$
                # - I look forward to hearing all about it.
                return 50
            return -1
        return -1

    def __50(self, pick: int) -> int:
        # $script:0111232407012696$
        # - Indeed!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.NEXT
        elif (self.state, self.index) == (40, 2):
            return Option.NEXT
        elif (self.state, self.index) == (40, 3):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (50, 0):
            return Option.CLOSE
        return Option.NONE
