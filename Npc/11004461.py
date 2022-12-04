""" 11004461: Safehold Guardsman """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1227192907012070$
        # - All's well!
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012071$
            # - All's well!
            return 10
        elif self.index == 1:
            # $script:1227192907012072$
            # - Two months out from retirement, and I get assigned here. Just my luck.
            return 10
        elif self.index == 2:
            # $script:1227192907012073$
            # - Forget justice and duty! I want to go home!
            if pick == 0:
                # $script:1227192907012074$
                # - Stick with it, soldier!
                return 11
            return -1
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012075$
            # - No way. I don't have what it takes to be a hero! I just want to go hide under my bunk!
            return 11
        elif self.index == 1:
            # $script:1227192907012076$
            # - Don't tell Condor about this, by the way. If he hears I've been talking like this, I'm done for!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.NEXT
        elif (self.state, self.index) == (10, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.NEXT
        elif (self.state, self.index) == (11, 1):
            return Option.CLOSE
        return Option.NONE
