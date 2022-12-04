""" 11004069: Cheez """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0619202207010143$
        # - It's breezy up here!
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0619202207010144$
            # - It's breezy up here!
            return 10
        elif self.index == 1:
            # $script:0619202207010145$
            # - Huh? What do <i>you</i> want?
            if pick == 0:
                # $script:0619202207010146$
                # - $npcName:11000367$'s owner is worried...
                return 31
            return -1
        return -1

    def __31(self, pick: int) -> int:
        # $script:0619202207010147$
        # - That's too bad. $npcName:11000367$ and I were meant for each other. It was fate.
        if pick == 0:
            # $script:0619202207010148$
            # - How'd you two meet, anyway?
            return 32
        return -1

    def __32(self, pick: int) -> int:
        if self.index == 0:
            # $script:0619202207010149$
            # - How is that any of your business? Let's just say that Skittle saved me from a really tough situation.
            return 32
        elif self.index == 1:
            # $script:0619202207010150$
            # - You should just wish us happiness, okay?
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.NEXT
        elif (self.state, self.index) == (32, 1):
            return Option.CLOSE
        return Option.NONE
