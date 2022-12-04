""" 11001708: Tinchai """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0728022507006960$
        # - Mm? Yes?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0805021607007079$
        # - I feel... sluggish...
        if pick == 0:
            # $script:0805021607007080$
            # - Why's that?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0805021607007081$
        # - Do you know how long it's been since I had a good nap? Ever since we got here, I've been so busy that I haven't had time to train, let alone get my beauty sleep.
        if pick == 0:
            # $script:0805021607007082$
            # - Go take a nap now.
            return 32
        return -1

    def __32(self, pick: int) -> int:
        # $script:0805021607007083$
        # - It wouldn't do any good. I have to get myself good and tired from training, or I can't doze off. So it'll just have to wait!
        #   <font color="#909090">(She gives a cheerful laugh.)</font>
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        return Option.NONE
