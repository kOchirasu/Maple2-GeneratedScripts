""" 11004335: Brighton """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1010140307011590$
        # - Now, isn't this something?
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:1010140307011591$
            # - I've gotta admit, I'm impressed.
            return 10
        elif self.index == 1:
            # $script:1010140307011592$
            # - This whole place is, like, the opposite of Maple World. No wonder the boss was so eager to check it out.
            return 10
        elif self.index == 2:
            # $script:1010140307011593$
            # - I didn't believe a word of it, of course. But $npcName:11004334[gender:1]$ insisted, and... Wow. Just wow.
            return 10
        elif self.index == 3:
            # $script:1010140307011594$
            # - $npcName:11003191[gender:0]$ doesn't know what he's missing!
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
