""" 11003415: Hero's Tomb """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0623153207008576$
        # - <i>Here lies Red Fox, courageous warrior of $map:02000051$. He laid down his life while defending our people from the forces of darkness, and for that he will always be remembered.</i>
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0623180607008578$
        # - <i>Here lies Red Fox, courageous warrior of $map:02000051$. He laid down his life while defending our people from the forces of darkness, and for that he will always be remembered.</i>
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
