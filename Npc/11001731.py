""" 11001731: Informant M """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0728022507006976$
        # - Did you find me?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0804172907007069$
        # - You see me? You have exceptionally sharp senses.
        if pick == 0:
            # $script:0804172907007070$
            # - What are you doing here?
            return 40
        return -1

    def __40(self, pick: int) -> int:
        # $script:0804172907007071$
        # - Where's it written I've got to tell you anything?
        if pick == 0:
            # $script:0804172907007072$
            # - Just curious.
            return 41
        elif pick == 1:
            # $script:0804172907007073$
            # - Come on, tell me!
            return 42
        return -1

    def __41(self, pick: int) -> int:
        # $script:0804172907007074$
        # - You may have enough free time to bug strangers, but I don't. Scram.
        return -1

    def __42(self, pick: int) -> int:
        # $script:0804172907007075$
        # - Let me think... No.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (42, 0):
            return Option.CLOSE
        return Option.NONE
