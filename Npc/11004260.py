""" 11004260: Skate Fan """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0911203207011164$
        # - Stupid, stupid, stupid! Where is he?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0911203207011165$
        # - Stupid, stupid, stupid! Where is he?
        if pick == 0:
            # $script:0911203207011166$
            # - Where is who?
            return 11
        return -1

    def __11(self, pick: int) -> int:
        # $script:0911203207011167$
        # - Oh. Um. Just this guy who skateboards around here sometimes. He looks sooooo cool. I've been waiting for him.
        if pick == 0:
            # $script:0911203207011168$
            # - Oh, were you guys meeting up here? Is he late? Tsk, tsk.
            return 12
        return -1

    def __12(self, pick: int) -> int:
        if self.index == 0:
            # $script:0911203207011169$
            # - Um... I haven't actually officially met him yet. But that's what I've been waiting around for! I want to ask him for his name and number!
            return 12
        elif self.index == 1:
            # $script:0911203207011170$
            # - Seriously, though, a girl's got limits. I've been waiting here every day for a week, and he hasn't showed up once! Now my legs hurt. Maybe I should give up.
            if pick == 0:
                # $script:0911203207011171$
                # - Aww, just wait a little longer. Never give up!
                return 13
            return -1
        return -1

    def __13(self, pick: int) -> int:
        # $script:0911203207011172$
        # - Ugh, fine, I'll give him <b>one</b> more day. I mean, he is, like, super hot.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.NEXT
        elif (self.state, self.index) == (12, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (13, 0):
            return Option.CLOSE
        return Option.NONE
