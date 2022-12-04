""" 11004476: Ludwigia """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1227192907012167$
        # - Sigh... I'm sick of these ration packs they have us all eating. I miss the gourmet restaurants of Tria!
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012168$
            # - They didn't warn us that Kritias doesn't have any proper eateries. What's a foodie supposed to do in a place like this?
            return 10
        elif self.index == 1:
            # $script:1227192907012169$
            # - I would kill for a bowl of blue mushroom slime soup in cornelian cherry sauce...
            return 10
        elif self.index == 2:
            # $script:1227192907012170$
            # - Ugh, talking about it just makes it worse! I'm going to be too hungry to sleep tonight...
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
