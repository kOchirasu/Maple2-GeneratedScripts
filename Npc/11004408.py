""" 11004408: Veliche """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1113161307011833$
        # - The future is in our hands.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1113161307011834$
        # - Especially at times like these, we must maintain our composure.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
