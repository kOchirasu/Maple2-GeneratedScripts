""" 11004210: Ruru """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806045807010666$
        # - Yaaaaaawn...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806045807010667$
        # - You want to try out some high-caliber mushsplosives? Just pick up a bomb and throw it.
        if pick == 0:
            # $script:0806052007010672$
            # - Right... And how do I pick stuff up again?
            return 11
        return -1

    def __11(self, pick: int) -> int:
        # $script:0806052107010672$
        # - You don't know? Just stand next to a bomb and the words "Pick Up" will pop up in the air as if by magic. Just press the corresponding button and you're ready to unleash the cleansing power of fire!
        if pick == 0:
            # $script:0806052107010673$
            # - ...None of that seems strange to you?
            return 12
        return -1

    def __12(self, pick: int) -> int:
        # $script:0806052107010674$
        # - No stranger than the voices in my head that tell me to burn things!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.CLOSE
        return Option.NONE
