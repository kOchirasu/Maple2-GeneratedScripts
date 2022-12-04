""" 11000322: Clara """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001285$
        # - How may I help you?
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180407001289$
        # - $MyPCName$, are you an adventurer? Have you ever seen a rainbow?
        if pick == 0:
            # $script:0831180407001290$
            # - Yep.
            return 41
        elif pick == 1:
            # $script:0831180407001291$
            # - Nope.
            return 42
        return -1

    def __41(self, pick: int) -> int:
        # $script:0831180407001292$
        # - Whoa! What does it look like? $npcName:11000174[gender:1]$ says there's always a big rainbow over the dam!
        if pick == 0:
            # $script:0831180407001293$
            # - Who is $npcName:11000174[gender:1]$?
            return 43
        elif pick == 1:
            # $script:0831180407001294$
            # - Where is the dam?
            return 44
        return -1

    def __42(self, pick: int) -> int:
        # $script:0831180407001295$
        # - Hmm, really? $npcName:11000174[gender:1]$ wrote to me in a letter that there's always a rainbow over the dam!
        if pick == 0:
            # $script:0831180407001296$
            # - Who is $npcName:11000174[gender:1]$?
            return 43
        elif pick == 1:
            # $script:0831180407001297$
            # - Where is the dam?
            return 44
        return -1

    def __43(self, pick: int) -> int:
        # $script:0831180407001298$
        # - $npcName:11000174[gender:1]$ is my cousin living near the dam. She used to live here until her father had to move there for work. I wish I had to move out there too...
        return -1

    def __44(self, pick: int) -> int:
        # $script:0831180407001299$
        # - Mm, I don't know exactly. $MyPCName$, do you think you could find it? I'd give anything to see it!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (42, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (43, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (44, 0):
            return Option.CLOSE
        return Option.NONE
