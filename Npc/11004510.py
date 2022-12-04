""" 11004510: Mannstad Patrolman """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1228182607012457$
        # - What're you, a tourist? You wanna get tombstoned? This is a warzone! Not that $map:02020030$ is any better...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1228182607012458$
        # - What're you, a tourist? You wanna get tombstoned? This is a warzone! Not that $map:02020030$ is any better...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
