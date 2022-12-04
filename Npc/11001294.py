""" 11001294: Dunba """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1215203907005008$
        # - Sigh... I should have left well enough alone...
        return None # TODO

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227194507005634$
            # - Ugh... He's the champ for a reason...
            return 40
        elif self.index == 1:
            # $script:1227194507005635$
            # - If he'd gone all-out...
            if pick == 0:
                # $script:1227194507005636$
                # - What happened to you?
                return 41
            return -1
        return -1

    def __41(self, pick: int) -> int:
        # $script:1227194507005637$
        # - Vasara Chen happened... He's the champion of the underground fighting circuit, and the son of Wei Hong. You know, the mob boss of Blackstar? He promised... promised that if I beat him, Blackstar would leave me alone...
        if pick == 0:
            # $script:0131151207007895$
            # - Soooooooo... the results?
            return 42
        return -1

    def __42(self, pick: int) -> int:
        # $script:0131151207007896$
        # - It ended with my utter defeat, as you can see. He said he had fun and that the Blackstars wouldn't bother me if I stayed down. Well, all it took was a single punch and I was done. I don't deserve to be the champion of Ludari Arena.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (42, 0):
            return Option.CLOSE
        return Option.NONE
