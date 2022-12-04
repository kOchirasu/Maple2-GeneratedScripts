""" 11001680: Bravos """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0629000607006457$
        # - You need anything, you just call out my name. Not that I'll come running, but maybe it'll give you good luck.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0629000607006460$
        # - Hm... Did I ever tell you why they call me $npcName:11001680[gender:0]$? I'm sure I told someone, but I can't remember if it was you.
        if pick == 0:
            # $script:0629000607006461$
            # - Why do you keep asking that question?
            return 40
        elif pick == 1:
            # $script:0629000607006462$
            # - Let's talk about something else.
            return 50
        return -1

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:0629000607006463$
            # - You got a problem with that? I'm my own man, and if I want to ask the same question over and over again, you can't stop me. Just for that, I'll tell you again!
            return 40
        elif self.index == 1:
            # $script:0629000607006465$
            # - They call me Bravos 'cause I'm so great I deserve a standing ovation! I hope you remember this time, 'cause there will be a test!
            return 40
        elif self.index == 2:
            # $script:0629000607006466$
            # - What, you come here to stare at me? Unless you have something else to say, scram!
            return -1
        return -1

    def __50(self, pick: int) -> int:
        # $script:0706165507006640$
        # - Yeah, what do you want to talk about?
        if pick == 0:
            # $script:0706165507006641$
            # - What was that clone in the video?
            return 51
        return -1

    def __51(self, pick: int) -> int:
        # $script:0706165507006642$
        # - Beats me. I never saw it before. This is a messed up thought, but could you imagine having 100 $npcNamePlural:11001688[gender:0]$ running around? Ugh, just having one of him is too much.
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
        elif (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (51, 0):
            return Option.CLOSE
        return Option.NONE
