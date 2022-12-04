""" 11000235: Tracy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001000$
        # - Sigh...
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180407001004$
        # - Mm? You're not the person I saw.
        if pick == 0:
            # $script:0831180407001005$
            # - What are you doing?
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:0831180407001006$
        # - I don't know. I don't know why I'm doing this, so please stop talking to me.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        return Option.NONE
