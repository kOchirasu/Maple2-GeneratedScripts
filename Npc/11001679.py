""" 11001679: Bravos """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0629000607006447$
        # - You need anything, you just call out my name. Not that I'll come running, but maybe it'll give you good luck.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0629000607006450$
        # - Do you know why I'm called $npcName:11001545[gender:0]$?
        if pick == 0:
            # $script:0629000607006451$
            # - You want to ask me that? Right now?
            return 40
        return -1

    def __40(self, pick: int) -> int:
        # $script:0629000607006453$
        # - You're no fun. Forget it.
        if pick == 0:
            # $script:0706165507006639$
            # - How are you feeling?
            return 50
        return -1

    def __50(self, pick: int) -> int:
        if self.index == 0:
            # $script:0629000607006454$
            # - Wh-what? You worried about me? Don't! Look... You're giving me goosebumps!
            return 50
        elif self.index == 1:
            # $script:0629000607006456$
            # - What's with the intense stare? Spit it out or sc-scram!
            #   <font color="#909090">(He's blushing.)</font>
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (50, 0):
            return Option.NEXT
        elif (self.state, self.index) == (50, 1):
            return Option.CLOSE
        return Option.NONE
