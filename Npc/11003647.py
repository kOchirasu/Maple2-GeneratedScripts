""" 11003647: Olive """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1109121007009186$
        # - So much to do, so much mortal danger...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1109121007009187$
        # - What's have we here? A foreigner, in a place like this?
        if pick == 0:
            # $script:1109121007009188$
            # - I'm here on business.
            return 11
        return -1

    def __11(self, pick: int) -> int:
        # $script:1109121007009189$
        # - In that case, $npcName:11003535[gender:1]$ must have sent you. I see she can't be bothered to visit me in person... as usual.
        if pick == 0:
            # $script:1109121007009190$
            # - Uh, she tells me that you're doing very important work.
            return 12
        return -1

    def __12(self, pick: int) -> int:
        # $script:1109121007009191$
        # - That's kind of you to say, but I know the truth. Anyway, please tell her that I said, "Parrot. Shoes. Perfume."
        if pick == 0:
            # $script:1109121007009192$
            # - I'll make sure she gets the messsage.
            return 13
        return -1

    def __13(self, pick: int) -> int:
        # $script:1109121007009193$
        # - Please remind her that us agents get lonely sometimes, would you?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (13, 0):
            return Option.CLOSE
        return Option.NONE
