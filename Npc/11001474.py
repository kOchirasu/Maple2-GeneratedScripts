""" 11001474: Fabid """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1224110207005585$
        # - W-what?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1228134707005721$
        # - M-m-must stay calm. I'm n-n-not scared...
        if pick == 0:
            # $script:0913170607011310$
            # - What's wrong?
            return 40
        return -1

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:0913170607011311$
            # - <b>AH!!</b> Jeez, you almost gave me a heart attack...
            return 40
        elif self.index == 1:
            # $script:0913170607011312$
            # - You aren't headed into the $dungeonTitle:20016002$, are you? I was researching the ruins there when I saw... one of "them!"
            return 40
        elif self.index == 2:
            # $script:0913170607011313$
            # - How did the temple of the divine lumarigons come to house such frightening creatures? It's enough to make a man quake in his boots.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.NEXT
        elif (self.state, self.index) == (40, 2):
            return Option.CLOSE
        return Option.NONE
