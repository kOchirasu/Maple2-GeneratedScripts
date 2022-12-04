""" 11004360: Aiden """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1109213607011771$
        # - Is it so much to ask that we have a normal celebration this year?
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:1109213607011772$
            # - I've got a reputation as a know-it-all, but I can't imagine why anyone would do this to our family...
            return 10
        elif self.index == 1:
            # $script:1120173007011848$
            # - I rely on science to explain things... but how can it explain <i>this</i>...
            if pick == 0:
                # $script:1120173007011849$
                # - You should focus on helping $npcName:11004345[gender:1]$ out here.
                return 11
            return -1
        return -1

    def __11(self, pick: int) -> int:
        # $script:1120173007011850$
        # - I'm not so sure about that, honestly.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.CLOSE
        return Option.NONE
