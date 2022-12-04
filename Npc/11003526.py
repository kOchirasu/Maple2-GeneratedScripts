""" 11003526: Rain """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0816160115009037$
        # - What is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0816160115009038$
        # - Sh. I'm trying to think of a melody. Can you give me a minute?
        if pick == 0:
            # $script:0816160115009039$
            # - Yeah, goodbye.
            return 36
        elif pick == 1:
            # $script:0816160115009040$
            # - (Wait.)
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0816160115009041$
        # - ♬ Compelled to capture every pet! You and I, together! ♬
        if pick == 0:
            # $script:0816160115009042$
            # - Yeah, goodbye.
            return 36
        elif pick == 1:
            # $script:0816160115009043$
            # - (Wait a little more.)
            return 32
        return -1

    def __36(self, pick: int) -> int:
        # $script:0816170815009057$
        # - ♬ I wish for unparalleled skill... ♬
        return -1

    def __32(self, pick: int) -> int:
        # $script:0816160115009044$
        # - A fan, are you? Want my autograph? An advanced copy of my album? Well, it's coming out soon, so you'll just have to wait!
        if pick == 0:
            # $script:0816160115009045$
            # - I'd like to hear a song.
            return 33
        elif pick == 1:
            # $script:0816160115009046$
            # - I want to know about your pet.
            return 34
        return -1

    def __33(self, pick: int) -> int:
        # $script:0816160115009047$
        # - My new song is a secret! You'll have to wait for the single, like everybody else.
        return -1

    def __34(self, pick: int) -> int:
        # $script:0816160115009048$
        # - This one... this one cannot be tamed. It's special.
        if pick == 0:
            # $script:0816160115009049$
            # - Where can I get one?
            return 35
        return -1

    def __35(self, pick: int) -> int:
        # $script:0816160115009050$
        # - That's my secret!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (36, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (33, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (34, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (35, 0):
            return Option.CLOSE
        return Option.NONE
