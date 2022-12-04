""" 11000531: Zorba """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002284$
        # - How may I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407002287$
        # - Cough, cough... It's so dusty in here! I've had it with all these old books. 
        if pick == 0:
            # $script:0831180407002288$
            # - Are you really going to close your bookstore?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0831180407002289$
        # - Well, I'm certainly thinking about it. Ha ha... My bookstore is the oldest business on $map:02000147$, you know. I'd rather keep it open, but I'm getting too old to run it on my own.
        return -1

    def __40(self, pick: int) -> int:
        # $script:0831180407002290$
        # - Do you like books?
        if pick == 0:
            # $script:0831180407002291$
            # - Yep!
            return 41
        elif pick == 1:
            # $script:0831180407002292$
            # - Nope!
            return 42
        return -1

    def __41(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407002293$
            # - Ha, do you? People like you amaze me. I've owned this store for over thirty years, but reading always puts me right to sleep. It's so boring.
            return 41
        elif self.index == 1:
            # $script:0831180407002294$
            # - I'm glad not everyone feels like I do. I'd have long since shut down, ha!
            return -1
        return -1

    def __42(self, pick: int) -> int:
        # $script:0831180407002295$
        # - You don't? Ha, you're just like me. I've owned this store for over thirty years, but reading always puts me right to sleep. It's so boring. Just between you and me, I've never finished a single book in my whole life.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.NEXT
        elif (self.state, self.index) == (41, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (42, 0):
            return Option.CLOSE
        return Option.NONE
