""" 11000318: Lionel """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 60

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001215$
        # - What is it?
        return None # TODO

    def __60(self, pick: int) -> int:
        # $script:0831180407001221$
        # - I don't recognize you. What do you want?
        if pick == 0:
            # $script:0831180407001222$
            # - I need directions.
            return 61
        elif pick == 1:
            # $script:0831180407001223$
            # - Nothing in particular.
            return 63
        return -1

    def __61(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407001224$
            # - You must be new to $map:02000001$, huh? Boy, I'd love to prank you, but you look like you're here to shop. Okay, I'll let you off... THIS time!
            return 61
        elif self.index == 1:
            # $script:0831180407001225$
            # - Follow that big road straight ahead.
            if pick == 0:
                # $script:0831180407001226$
                # - What's along the road?
                return 62
            return -1
        return -1

    def __62(self, pick: int) -> int:
        # $script:0831180407001227$
        # - Oh, I ran out of patience for you a while ago. Stop bothering me and move on.
        return -1

    def __63(self, pick: int) -> int:
        # $script:0831180407001228$
        # - Is that so? Strange... You really don't look familiar to me, and there's no way I can forget someone so ugly. Ha ha ha!
        if pick == 0:
            # $script:0831180407001229$
            # - Yeah, well... you're uglier!
            return 64
        elif pick == 1:
            # $script:0831180407001230$
            # - Uhh, pot to kettle...
            return 65
        return -1

    def __64(self, pick: int) -> int:
        # $script:0831180407001231$
        # - Heh. You've never seen a handsome man before, have you?
        if pick == 0:
            # $script:0831180407001232$
            # - This is ridiculous. I'm just going to leave.
            return 67
        return -1

    def __65(self, pick: int) -> int:
        # $script:0831180407001233$
        # - I can't hear you. 
        if pick == 0:
            # $script:0831180407001234$
            # - Takes one to know one, Buddy!
            return 66
        return -1

    def __66(self, pick: int) -> int:
        # $script:0831180407001235$
        # - I said, I can't hear you. 
        if pick == 0:
            # $script:0831180407001236$
            # - Right, that's about enough. Time to leave.
            return 67
        return -1

    def __67(self, pick: int) -> int:
        # $script:0831180407001237$
        # - Oh, come on, are you just going to leave?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (60, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (61, 0):
            return Option.NEXT
        elif (self.state, self.index) == (61, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (62, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (63, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (64, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (65, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (66, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (67, 0):
            return Option.CLOSE
        return Option.NONE
