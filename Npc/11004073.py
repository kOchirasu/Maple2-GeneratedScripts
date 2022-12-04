""" 11004073: Fire Dragon Remains """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0619202207010185$
        # - <font color="#909090">(These are the remains of a dragon. They appear to be very old.)</font>
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0619202207010186$
            # - <font color="#909090">(These are the remains of a dragon. They appear to be very old.)</font>
            return 10
        elif self.index == 1:
            # $script:0619202207010187$
            # - <font color="#909090">(Judging from the skeletal structure, you can tell that this was a distant cousin to the modern girant breed of dragon. It wasn't very big, but its thick jaw suggests it had a powerful bite.)</font>
            return 10
        elif self.index == 2:
            # $script:0619202207010188$
            # - <font color="#909090">(You've also noticed that the fire dogs are steering clear of these remains. Did this dragon once prey on those mutts?)</font>
            return 10
        elif self.index == 3:
            # $script:0625131207010362$
            # - <font color='#909090'>(One particularly long bone tells you that this dragon was male. Its 10-meter-long horn bone, to be precise.)</font>
            return 10
        elif self.index == 4:
            # $script:0620224307010272$
            # - <font color="#909090">(As you examine the snout of the skull, you note a lack of flame canals present in the dragons of today. While it was obviously flame resistant, this dragon did not actually breathe fire.)</font>
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.NEXT
        elif (self.state, self.index) == (10, 2):
            return Option.NEXT
        elif (self.state, self.index) == (10, 3):
            return Option.NEXT
        elif (self.state, self.index) == (10, 4):
            return Option.CLOSE
        return Option.NONE
