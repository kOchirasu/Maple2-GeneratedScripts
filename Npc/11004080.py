""" 11004080: Blacksmith's Workbench """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0620203007010268$
        # - <font color="#909090">(This workbench is particularly cluttered.)</font>
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0620203007010269$
            # - <font color="#909090">(This workbench is particularly cluttered.)</font>
            return 10
        elif self.index == 1:
            # $script:0620203007010270$
            # - <font color="#909090">(Many weapon parts are scattered across the top of the bench. Everything on it is coated with a fine layer of onyx dust. It appears Ophelia's skill is the result of countless hours of practice.)</font>
            return 10
        elif self.index == 2:
            # $script:0620203007010271$
            # - <font color="#909090">(On the corner of the workbench, there's a fancy business card that seems out of place. <i>"Unload Your Unused Trash! Ophelia's Hardware Store! We Buy All Scrap Metal. Call Us! 902-555-3959")</i></font>
            return 10
        elif self.index == 3:
            # $script:0625140507010368$
            # - <font color='#909090'>(Is the enchanting business not working out? What a strange turn of events...)</font>
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
