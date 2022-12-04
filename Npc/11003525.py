""" 11003525: Rose """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0816160115009030$
        # - Can I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0816213215009068$
        # - We aren't open yet. Can you please come back later?
        if pick == 0:
            # $script:0816213215009069$
            # - Of course.
            return 32
        elif pick == 1:
            # $script:0816213215009070$
            # - When are you opening?
            return 31
        elif pick == 2:
            # $script:0816213215009071$
            # - Who runs this place?
            return 33
        elif pick == 3:
            # $script:0816213215009072$
            # - What's that music?
            return 34
        return -1

    def __31(self, pick: int) -> int:
        # $script:0816213215009073$
        # - We... don't have a date yet, actually. The boss wants to redecorate and... and hire more people.
        return -1

    def __32(self, pick: int) -> int:
        # $script:0816213215009074$
        # - Watch your step. It's slippery over there.
        return -1

    def __33(self, pick: int) -> int:
        # $script:0816213215009075$
        # - It seems the boss has strange tastes. He asked me to wear this outfit, even though we aren't open yet. It's so uncomfortable...
        return -1

    def __34(self, pick: int) -> int:
        if self.index == 0:
            # $script:0816213215009076$
            # - Isn't it cool? It's the $map:61000008$ theme song! The boss doesn't like it, but it's pretty popular these days.
            return 34
        elif self.index == 1:
            # $script:0816225215009078$
            # - Come to think of it, didn't the boss lose a game of $map:61000008$ the other day...?
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (33, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (34, 0):
            return Option.NEXT
        elif (self.state, self.index) == (34, 1):
            return Option.CLOSE
        return Option.NONE
