""" 11003414: Hero's Tomb """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0623153207008575$
        # - <i>Here lies Sharp Claw, the war chief who rebuilt $map:02000051$. His kind heart and dedicated work uplifted our people during our time of need, and for that he will always be remembered.</i>
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0623180607008577$
        # - <i>Here lies Sharp Claw, the war chief who rebuilt $map:02000051$. His kind heart and dedicated work uplifted our people during our time of need, and for that he will always be remembered.</i>
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
