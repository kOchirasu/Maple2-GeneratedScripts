""" 11004081: Strange Tombstone """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0619202207010249$
        # - <font color="#909090">(You faintly make out the cries of a woman. She somehow sounds far away and close at the same time.)</font>
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0619202207010250$
            # - <font color="#909090">(You faintly make out the cries of a woman. She somehow sounds far away and close at the same time.)</font>
            return 10
        elif self.index == 1:
            # $script:0619202207010251$
            # - My child... My child... Where are you...?
            return 10
        elif self.index == 2:
            # $script:0619202207010252$
            # - Come back to me... Come out of the cold... Your mama is waiting...
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
