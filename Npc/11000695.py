""" 11000695: Bazette """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 50

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002802$
        # - What brings you here?
        return None # TODO

    def __50(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407002806$
            # - Making potions is very difficult. The first priority is preparing the ingredients. You need very specific ingredients to make effective potions.
            return 50
        elif self.index == 1:
            # $script:0831180407002807$
            # - Some people compare potion brewing to cooking. They're crazy if they think potions are as easy to make as food.
            return 50
        elif self.index == 2:
            # $script:0831180407002808$
            # - Here, I'll give you an example. Say you're making fried rice. You can put in just about anything you want. Ham, peppers, carrots, anything you want.
            return 50
        elif self.index == 3:
            # $script:0831180407002809$
            # - When you're making a potion, however, you must add the ingredients in the correct order, at the correct time. You can't take your eyes off the cauldron.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (50, 0):
            return Option.NEXT
        elif (self.state, self.index) == (50, 1):
            return Option.NEXT
        elif (self.state, self.index) == (50, 2):
            return Option.NEXT
        elif (self.state, self.index) == (50, 3):
            return Option.CLOSE
        return Option.NONE
