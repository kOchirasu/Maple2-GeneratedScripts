""" 11004275: Numero """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0911203207011264$
        # - Ugh, this sucks. When can I get out of here?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0911203207011265$
        # - Ugh, this sucks. When can I get out of here?
        if pick == 0:
            # $script:0911203207011266$
            # - What's wrong?
            return 11
        return -1

    def __11(self, pick: int) -> int:
        # $script:0911203207011267$
        # - Who are you, and why is that any of your business?
        if pick == 0:
            # $script:0911203207011268$
            # - C'mon. Just tell me what's bothering you.
            return 12
        return -1

    def __12(self, pick: int) -> int:
        # $script:0911203207011269$
        # - If you must know, I'm upset because I'm trapped here. There's no way out, and...
        if pick == 0:
            # $script:0913151207011304$
            # - Maybe I can help you get free!
            return 13
        return -1

    def __13(self, pick: int) -> int:
        if self.index == 0:
            # $script:0913151207011305$
            # - What? 
            return 13
        elif self.index == 1:
            # $script:0911203207011270$
            # - Never mind. It's not worth explaining to you. Just move along.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (13, 0):
            return Option.NEXT
        elif (self.state, self.index) == (13, 1):
            return Option.CLOSE
        return Option.NONE
