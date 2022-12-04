""" 11001277: Krend """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1208175407004832$
        # - Shush! You'll scare them off.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1208175407004835$
        # - Sorry, but now isn't a good time. As you can see, I'm busy.
        if pick == 0:
            # $script:1208175407004836$
            # - What are you up to?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:1208175407004837$
        # - I'm collecting special materials. I'm a specialist in restoring old documents, antiques, and what have you. The secretions of the $npcNamePlural:21000074$ are important in my line of work. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        return Option.NONE
