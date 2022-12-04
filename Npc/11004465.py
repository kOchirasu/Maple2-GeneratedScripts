""" 11004465: Richmonde Guard """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1227192907012093$
        # - Who goes there? Enemy?!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1227192907012095$
        # - Who goes there? Enemy?!
        if pick == 0:
            # $script:0111125107012684$
            # - Hey, I'm on your side.
            return 11
        return -1

    def __11(self, pick: int) -> int:
        # $script:1227192907012096$
        # - Hm? Your clothes are strange, but you look like you can hold your own. You ever consider a career in freedom fighting?
        if pick == 0:
            # $script:1227192907012097$
            # - Sorry, but I've got other obligations.
            return 12
        return -1

    def __12(self, pick: int) -> int:
        # $script:1227192907012098$
        # - Tch... What a waste of talent. Well, if you change your mind, it's not like we can afford to be picky...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.CLOSE
        return Option.NONE
