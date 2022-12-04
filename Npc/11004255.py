""" 11004255: Mouse """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0829171107010970$
        # - Just look at that delicious candy and that sweet cream! How could anyone possibly resist? Hehe.
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0829171107010971$
            # - Just look at that delicious candy and that sweet cream! How could anyone possibly resist? Hehe.
            return 10
        elif self.index == 1:
            # $script:0831140807011013$
            # - So sweet! So very, very sweet. We're so blessed to eat such tastiness. Wouldn't you like to be blessed, too?
            if pick == 0:
                # $script:0831140807011014$
                # - Aren't you worried about getting fat?
                return 11
            return -1
        return -1

    def __11(self, pick: int) -> int:
        # $script:0831140807011015$
        # - Oh, no. Oh, no, no, no, never. Doesn't it just look irresistibly scrumptious? Don't you want to just take a lick?
        if pick == 0:
            # $script:0831140807011016$
            # - It can't be that great...
            return 12
        return -1

    def __12(self, pick: int) -> int:
        # $script:0831140807011017$
        # - You see those monsters over there? They're a long way from their natural habitat. They're all here because they're in love with these sweets. Such tasty, tasty treats.
        if pick == 0:
            # $script:0831140807011018$
            # - That actually sounds kind of dangerous.
            return 13
        return -1

    def __13(self, pick: int) -> int:
        # $script:0831140807011019$
        # - Dangerous? No way! Would we lie to you? There's nothing sweeter than to live life here amongst the world's tastiest treats.
        if pick == 0:
            # $script:0831140807011020$
            # - Uh, yeah. This is where I get the heck out of here.
            return 14
        return -1

    def __14(self, pick: int) -> int:
        # $script:0831140807011021$
        # - Where are you going? Have a taste!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (13, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (14, 0):
            return Option.CLOSE
        return Option.NONE
