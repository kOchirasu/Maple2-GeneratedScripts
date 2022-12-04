""" 11001408: Dali """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217205907005405$
        # - Welcome to <i>our</i> territory, human. 
        return None # TODO

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:1222203907005480$
            # - We don't usually let our clients in here. Seeing us train and tend to our wounded makes them realize that we, too, are mortal. It's bad for the brand, see?
            return 40
        elif self.index == 1:
            # $script:1222203907005481$
            # - We like humans, of course, but we know better than to count them as friends. We once relied on our humans for happiness. That... didn't end well for us.
            return 40
        elif self.index == 2:
            # $script:1222203907005482$
            # - Anyway, now that you've seen our base, you have to promise never to tell anyone about it. Only you and your closest friends are welcome here.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.NEXT
        elif (self.state, self.index) == (40, 2):
            return Option.CLOSE
        return Option.NONE
