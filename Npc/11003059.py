""" 11003059: Ravole """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0102155907007626$
        # - It's nice to meet you!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0102155907007629$
        # - Nice to meet you, $MyPCName$! 
        if pick == 0:
            # $script:0102155907007630$
            # - Why did you come here?
            return 31
        elif pick == 1:
            # $script:0102155907007631$
            # - What does the supply crew do around here?
            return 32
        return -1

    def __31(self, pick: int) -> int:
        # $script:0102155907007632$
        # - I came here with the supply crew, of course. We're here to keep the guards out here from turning into popsicles. But me... I'm here for another reason.
        if pick == 0:
            # $script:0102155907007633$
            # - So, why are you REALLY here?
            return 33
        return -1

    def __32(self, pick: int) -> int:
        # $script:0102155907007634$
        # - We keep the guards fed and clothed so they don't freeze or complain too much. Veterans like me handle supplies since we've learned what kind of gear we'll need. Honestly though, there's another reason I'm here.
        if pick == 0:
            # $script:0102155907007635$
            # - So, why are you REALLY here?
            return 33
        return -1

    def __33(self, pick: int) -> int:
        if self.index == 0:
            # $script:0102155907007636$
            # - I'm here to study a kingdom that once stood in this snowfield. It was a peaceful kingdom, but no one knows why it vanished into history. The survivors scattered, and none of them will talk to me, so I came here myself.
            return 33
        elif self.index == 1:
            # $script:0206154107007917$
            # - I've heard there's a shrine hidden somewhere in the snowfield kingdom. It was meant only for their kings and queens, to hold their most precious treasure. That means if I can get in there, I'll be rich! 
            return 33
        elif self.index == 2:
            # $script:0206154107007918$
            # - Hey, this is all completely grounded in fact! That's what my gut tells me, anyway. You look like you can handle a little adventure. If you come across the shrine, you gotta let me know!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (33, 0):
            return Option.NEXT
        elif (self.state, self.index) == (33, 1):
            return Option.NEXT
        elif (self.state, self.index) == (33, 2):
            return Option.CLOSE
        return Option.NONE
