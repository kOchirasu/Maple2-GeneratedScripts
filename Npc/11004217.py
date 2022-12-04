""" 11004217: Jenna """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806222707010773$
        # - Do you have business with me?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806222707010774$
        # - Haha, let's get this party started! Pew pew! That's the sound of me blowing everyone away with the power of my cannon!
        return -1

    def __20(self, pick: int) -> int:
        # $script:0806222707010775$
        # - If you want to be happy, there's one rule to live by: figure out what you wanna do, and do it! In my case, that's listening my cannon purr as it pumps out hundreds of rounds a minute.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
