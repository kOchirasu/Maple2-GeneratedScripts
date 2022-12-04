""" 11004380: Rufina """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1109213607011795$
        # - You won't know love if you don't express it. Confess your love to your crush for the holidays! It's the perfect gift!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1109213607011796$
        # - The holidays are all about looooove.
        if pick == 0:
            # $script:1109213607011797$
            # - ...
            return 11
        return -1

    def __11(self, pick: int) -> int:
        # $script:1109213607011798$
        # - I have a pair of skates I really love... so much so that I don't want to take them out of the box.
        if pick == 0:
            # $script:1109213607011799$
            # - You skate with them still inside the box? Sounds kind of dangerous.
            return 12
        return -1

    def __12(self, pick: int) -> int:
        # $script:1109213607011800$
        # - No way! I've never even worn them! I wonder what it'd be like to skate with them... Maybe that's what love is, taking risks.
        return -1

    def __40(self, pick: int) -> int:
        # $script:1120173007011871$
        # - The holidays are all about looooove.
        if pick == 0:
            # $script:1120173007011872$
            # - Did you see $npcName:11004345[gender:1]$'s family?
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:1120173007011873$
        # - I know $npcName:11004348[gender:0]$, he's $npcName:11004345[gender:1]$'s father. I saw him last night at the gardening club meeting. But I didn't see him today. I bet he's just at home... He mentioned wanting to decorate his holiday tree.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        return Option.NONE
