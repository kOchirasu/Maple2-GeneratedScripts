""" 11000331: Brandon """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001339$
        # - Can I help you?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407001341$
        # - Hm... Have you ever felt like you're being watched? You get this itchy feeling on the back of your neck when that happens. I've been feeling it a lot lately. Why do you think that is?
        return -1

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407001342$
            # - Excuse me, have you seen a girl around here who looks like me? She has blond hair and blue eyes, just like I do. I don't remember what she was wearing, though.
            return 30
        elif self.index == 1:
            # $script:0831180407001343$
            # - She's my sister. She went to do her hair and never came back. Does it take women a long time to do their hair? Huh... maybe she was getting it dyed.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.CLOSE
        return Option.NONE
