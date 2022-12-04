""" 11004382: Lydia """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1109213607011803$
        # - I will find love this winter!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1109213607011804$
        # - I confessed my love to someone during the holidays last year...
        if pick == 0:
            # $script:1109213607011805$
            # - What happened?
            return 11
        return -1

    def __11(self, pick: int) -> int:
        # $script:1109213607011806$
        # - The very next day, he gave it away. This year, I'll give it to someone special...
        if pick == 0:
            # $script:1109213607011807$
            # - Well, happy holidays!
            return 12
        return -1

    def __12(self, pick: int) -> int:
        # $script:1109213607011808$
        # - You listen to me, find your true love before the year ends!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.CLOSE
        return Option.NONE
