""" 11000283: Duomo """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 50])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001102$
        # - What are you curious about now?
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407001105$
            # - Let me introduce myself. I am a great prophet. I can tell you of future events with unerring accuracy. Ignorant people call me a mere fortune teller or a con artist. It's their loss, really.
            return 30
        elif self.index == 1:
            # $script:0831180407001106$
            # - Why, you ask? Because even people like them need something to believe in. When everything else fails them, they'll come to me. They always do. Now, how'd you like to know your fortune? 
            return -1
        return -1

    def __50(self, pick: int) -> int:
        # $script:0831180407001107$
        # - Want to know your destiny? Want to see your future? Then ask me! I can tell you anything you want. For a price, of course.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.CLOSE
        return Option.NONE
