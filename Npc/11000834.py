""" 11000834: Cathy Mart Employee """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([40, 50, 60])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003051$
        # - Welcome to Cathy Mart.
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180407003055$
        # - When is the next shift going to show up? I really have to go to the bathroom! ...Oh, shoot! Please excuse me, um, how may I help you?
        return -1

    def __50(self, pick: int) -> int:
        # $script:0831180407003056$
        # - You can pay for your items at the cashier over there.
        return -1

    def __60(self, pick: int) -> int:
        # $script:0831180407003057$
        # - Cathy Mart sells only the highest-quality products. If you find any items that don't seem to meet our standards, please don't hesitate to let me know.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (60, 0):
            return Option.CLOSE
        return Option.NONE
