""" 11001406: Gree """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217205907005403$
        # - You've got guts, walking around a place like this.
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:1222203907005471$
        # - Go away! We're on a mission!!
        if pick == 0:
            # $script:1222203907005472$
            # - You're awfully excited for someone on a mission.
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:1222203907005473$
        # - We aren't playing, if that's what you're trying to say! We don't get to play all day like you! We're on a very, very important <i>training</i> mission!!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        return Option.NONE
