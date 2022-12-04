""" 11004070: Moonlight Wolf Statue """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0619202207010151$
        # - <font color="#909090">(This statue marks the final resting place of a great warrior from Perion.)</font>
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0619202207010152$
            # - <font color="#909090">(This statue marks the final resting place of a great warrior from Perion.)</font>
            return 10
        elif self.index == 1:
            # $script:0619202207010153$
            # - <i>Even on the darkest night, the great Guardian of Wolfclaw Canyon fought without a hint of fear in his heart.</i>
            return 10
        elif self.index == 2:
            # $script:0619202207010154$
            # - <i>Oh, brave warrior of Perion! Death is not the end. Though you are no longer in this world, your heart will be with the tribes always.</i>
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
