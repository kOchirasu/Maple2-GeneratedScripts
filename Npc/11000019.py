""" 11000019: Terry """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000090$
        # - Hm hm hmmm, hm! Those marching songs always get stuck in my head.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000093$
        # - Hey there. First time in $map:02000062$?
        if pick == 0:
            # $script:0831180407000094$
            # - Yep!
            return 31
        return -1

    def __31(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000095$
            # - Well, if you're trying to get to $map:02000001$, I've got some bad news for you.. We just had a big earthquake that split the road there in half. No one can make the journey now.
            return 31
        elif self.index == 1:
            # $script:0831180407000096$
            # - As if that weren't bad enough, rough seas are preventing ships from entering or leaving the harbor. We're all stuck here!
            if pick == 0:
                # $script:0831180407000097$
                # - Is there no other way to get to $map:02000001$?
                return 32
            elif pick == 1:
                # $script:0831180407000098$
                # - What about by air?
                return 33
            return -1
        return -1

    def __32(self, pick: int) -> int:
        # $script:0831180407000099$
        # - I've heard there's a wilderness path that connects $map:02000115$ and $map:02000116$, but no one's been taking it. Supposedly it's a bit... dangerous.
        if pick == 0:
            # $script:1111011307007374$
            # - Where's the path?
            return 34
        return -1

    def __33(self, pick: int) -> int:
        # $script:0831180407000100$
        # - Uhh... Lith isn't that kind of port, buddy.
        return -1

    def __34(self, pick: int) -> int:
        # $script:1111011407007374$
        # - It's through a mountain path northwest of $map:02000062$. The path's been closed for ages, though. Too treacherous for most folks. I'd forget about it if I were you.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.NEXT
        elif (self.state, self.index) == (31, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (33, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (34, 0):
            return Option.CLOSE
        return Option.NONE
