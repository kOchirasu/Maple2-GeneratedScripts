""" 11000354: Chairman Goldus """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40, 50])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001472$
        # - Grr...
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407001475$
        # - Ah, I'm finally safe! You're my savior.
        return -1

    def __40(self, pick: int) -> int:
        # $script:0831180407001476$
        # - I thought I was going to die. I used to think I was untouchable. But after they took me so easily...
        return -1

    def __50(self, pick: int) -> int:
        # $script:0831180407001477$
        # - I can't believe you came to save me... Thank you. I'll live an honest life from now on. I'll donate to charities, pay all my taxes, and volunteer at the soup kitchens.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.CLOSE
        return Option.NONE
