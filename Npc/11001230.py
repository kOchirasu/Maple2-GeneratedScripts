""" 11001230: Landevian """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1125194807004469$
        # - We've got nothing but problems here.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1125194807004472$
        # - This is all that old coot Arazaad's fault. He's giving me work to do from beyond the grave!
        if pick == 0:
            # $script:1205185107004717$
            # - Was there bad blood between you and Arazard?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:1205185107004718$
        # - More like resentment. He was always bossing me around. "Practice your rune magic. Practice with your blade. Behave like a leader and set an example for the other Runeblades. Blah blah blah!" Even when $npcName:11001246[gender:0]$ and $npcName:11001231[gender:0]$ were there, the old man always singled me out.
        if pick == 0:
            # $script:1205185107004719$
            # - Sounds like you were Arazaad's most trusted student.
            return 32
        return -1

    def __32(self, pick: int) -> int:
        # $script:1205185107004720$
        # - W-what? No way. He was just a mean old man looking for an easy mark to pick on. Trust me, his favorite student was that jerk $npcName:11001231[gender:0]$, and boy did that one come back to bite him.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        return Option.NONE
