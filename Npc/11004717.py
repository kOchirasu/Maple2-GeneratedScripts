""" 11004717: Karkamelle """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0828194707015119$
        # - Oh oh, what have I gotten myself into in my old age? 
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0828194607015110$
            # - Guard the cauldron. Deal with customers. Deal with customers. Guard the cauldron... 
            return 30
        elif self.index == 1:
            # $script:0828194607015111$
            # - $npcName:11000304[gender:1]$, that dratted old bat! Well, at least I don't have to worry about getting lonely...
            if pick == 0:
                # $script:0828194607015112$
                # - Who's $npcName:11000304[gender:1]$?
                return 31
            elif pick == 1:
                # $script:0828194607015113$
                # - What's with the cauldron?
                return 32
            return -1
        return -1

    def __31(self, pick: int) -> int:
        # $script:0828194607015114$
        # - She's only her exalted fancy-warts, the grand bossy-britches of all the witches! Oh, we were friends once, back in the day. But I wasted my time when she was mastering her grimoires, and... Well, no point regretting it now!
        if pick == 0:
            # $script:0828194607015115$
            # - What happened?
            return 33
        return -1

    def __32(self, pick: int) -> int:
        if self.index == 0:
            # $script:0828194607015116$
            # - This old thing? You see, once a year, a deep shadow covers the world, and all the demons and spirits rise from the netherworld to cavort and caper in the mortal realm. I think you humans call it Halloween. 
            return 32
        elif self.index == 1:
            # $script:0828194607015117$
            # - Anyway, this is the one time of the year when we can get all the ingredients for witch stew! And we witches, we've got to have our witch stew. It gives our magic that extra little OOMPH that makes us so wonderful.
            return -1
        return -1

    def __33(self, pick: int) -> int:
        # $script:0828194607015118$
        # - It's a long story. And an ugly one! Instead of nosing into my painful memories, why don't you help me with this cauldron?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.NEXT
        elif (self.state, self.index) == (32, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (33, 0):
            return Option.CLOSE
        return Option.NONE
