""" 11000406: Blake """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001642$
        # - What is it?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407001644$
        # - Sometimes I'm afraid to look in the mirror.
        if pick == 0:
            # $script:0831180407001645$
            # - Why?
            return 21
        return -1

    def __21(self, pick: int) -> int:
        # $script:0831180407001646$
        # - I might fall in love with myself!
        if pick == 0:
            # $script:0831180407001647$
            # - But I'm already in love with you!
            return 22
        elif pick == 1:
            # $script:0831180407001648$
            # - I'm just gonna pretend I didn't hear that.
            return 23
        return -1

    def __22(self, pick: int) -> int:
        # $script:0831180407001649$
        # - I know how difficult it is to resist my incredible charms. Don't hate me because I can't love you in return.
        return -1

    def __23(self, pick: int) -> int:
        # $script:0831180407001650$
        # - Hey, hey! What are you looking at? Look at me! Hello! Hey, can't you hear me?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (21, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (22, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (23, 0):
            return Option.CLOSE
        return Option.NONE
