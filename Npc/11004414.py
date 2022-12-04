""" 11004414: Frosty Fairfolk """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1120173007011883$
        # - Don't you want to taste a fairfolk cake?
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:1120173007011886$
            # - There are many people who hunger for the fairfolk's cake. But it seems no two people have the same reaction to it! Isn't that interesting?
            return 10
        elif self.index == 1:
            # $script:1120173007011887$
            # - Some say it has no taste, others claim it's the most flavorful food they've ever eaten. Maybe it simply causes madness?
            return 10
        elif self.index == 2:
            # $script:1120173007011888$
            # - In any event, try some! Go on, eat it up!
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
