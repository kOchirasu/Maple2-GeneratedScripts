""" 11004259: Ludified Water """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0829171107010978$
        # - <font color="#909090">(The water seems to be flowing all right, but it also appears rather... viscous.)</font>
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0829171107010979$
            # - <font color="#909090">(The water seems to be flowing all right, but it also appears rather... viscous.)</font>
            return 10
        elif self.index == 1:
            # $script:0831140807011036$
            # - Recently, this place has been transforming into ludibrium at a rapid pace. Once ludibrification starts, everything becomes mushy and then solidifies instantly.
            return 10
        elif self.index == 2:
            # $script:0831140807011037$
            # - <font color="#909090">(This ludibrification has been happening all over Maple World. There's no prevention, except to be careful.)</font>
            return 10
        elif self.index == 3:
            # $script:0831140807011038$
            # - <font color="#909090">(Will everything eventually become ludibrified?)</font>
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
            return Option.CLOSE
        return Option.NONE
