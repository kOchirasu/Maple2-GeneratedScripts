""" 11004300: Ghost """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1002141907011395$
        # - What do you want?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1002141907011398$
        # - I don't gotta answer to you. Now scram, before I get angry.
        if pick == 0:
            # $script:1002141907011399$
            # - What brings you here?
            return 31
        elif pick == 1:
            # $script:1002141907011400$
            # - I'm not here to fight, friend.
            return 32
        return -1

    def __31(self, pick: int) -> int:
        # $script:1002141907011401$
        # - Blackstar goes where the money is! Here's some free advice: keep your nose outta things where it don't belong.
        if pick == 0:
            # $script:1002141907011402$
            # - How'd you become a ghost?
            return 33
        return -1

    def __32(self, pick: int) -> int:
        # $script:1002141907011403$
        # - I ain't your friend, pal! You think you can talk down to me 'cause I'm a ghost? Is that it?
        if pick == 0:
            # $script:1002141907011404$
            # - How'd you become a ghost?
            return 33
        return -1

    def __33(self, pick: int) -> int:
        # $script:1002141907011405$
        # - To tell the truth... I got no idea. Boss sent me here on a job, and next thing I know... Pow! Ghost.
        if pick == 0:
            # $script:1002141907011406$
            # - There, there. It's okay.
            return 34
        return -1

    def __34(self, pick: int) -> int:
        if self.index == 0:
            # $script:1002141907011407$
            # - I don't want your stinkin' pity! Anyway, this place ain't so bad. It's real cushy, and I got tons of books to read.
            return 34
        elif self.index == 1:
            # $script:1002141907011408$
            # - Come to think of it, there were some real important-looking papers in one of the books I read the other day. Weird, huh?
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (33, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (34, 0):
            return Option.NEXT
        elif (self.state, self.index) == (34, 1):
            return Option.CLOSE
        return Option.NONE
