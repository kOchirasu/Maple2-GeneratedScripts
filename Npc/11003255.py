""" 11003255: Kaitlyn """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0403155707008178$
        # - What is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0403155707008179$
            # - There's no shame in asking for my help. I am, after all, the smartest person you know.
            return 30
        elif self.index == 1:
            # $script:0403155707008180$
            # - When you're done here, go ahead and help Professor $npcName:11003148[gender:0]$ with his research. He's been on edge lately thanks to his migraines. Don't do anything to make them worse, will you?
            return 30
        elif self.index == 2:
            # $script:0403155707008181$
            # - <font color="#909090">($npcName:11003254[gender:1]$ whispers to herself.) </font>
            #   <font size='20'>I wish he wore glasses. He's so intelligent and sensitive... It would be perfect...</font>
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.NEXT
        elif (self.state, self.index) == (30, 2):
            return Option.CLOSE
        return Option.NONE
