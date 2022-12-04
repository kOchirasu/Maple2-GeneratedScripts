""" 11004413: Frosty Fairfolk """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1120173007011877$
        # - Come visit $map:63000072$!
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:1120173007011880$
            # - $map:63000072$ is bursting with joyous holiday cheer! People are happy! Fairfolk are happy! And it's SNOWING!!
            return 10
        elif self.index == 1:
            # $script:1120173007011881$
            # - Board this toy train if you want to go to $map:63000072$! Toot, toot!
            return 10
        elif self.index == 2:
            # $script:1120173007011882$
            # - The toy train is completely free because it's run by the fairfolk! We barely even know what money is! Come along to $map:63000072$!
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
