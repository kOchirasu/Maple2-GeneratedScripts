""" 11004271: Burgundia """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0911203207011241$
        # - <font color="#909090">(This squat desert plant drips with a brilliant red sap.)</font>
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0911203207011242$
            # - <font color="#909090">(This squat desert plant drips with a brilliant red sap.)</font>
            return 10
        elif self.index == 1:
            # $script:0911203207011243$
            # - <font color="#909090">(You're pretty sure you've seen this shade of red in the clothes and makeup worn by the people of Karkar.)</font>
            return 10
        elif self.index == 2:
            # $script:0911203207011244$
            # - <font color="#909090">(You've seen plants like this all over Karkar, but they're especially plentiful here.)</font>
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.NEXT
        elif (self.state, self.index) == (10, 2):
            return Option.CLOSE
        return Option.NONE
