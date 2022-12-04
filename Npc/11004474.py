""" 11004474: Wentid """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1227192907012151$
        # - Hey, do you see that huge ship? I'm not imagining it, am I?
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012152$
            # - Hey, do you see that huge ship? I'm not imagining it, am I?
            return 10
        elif self.index == 1:
            # $script:1227192907012153$
            # - It's so big... How can something that big float up in the sky like that?
            if pick == 0:
                # $script:1227192907012154$
                # - Didn't you ride Sky Fortress to get here?
                return 11
            return -1
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012155$
            # - Sure, but I couldn't exactly tell how big it is from the inside. Seeing it now, away from the buildings in Tria... It's unreal!
            return 11
        elif self.index == 1:
            # $script:1227192907012156$
            # - Do you know? How does it fly like that?
            if pick == 0:
                # $script:1227192907012157$
                # - $npcName:24100101$ would tell you it's the power of science.
                return 12
            return -1
        return -1

    def __12(self, pick: int) -> int:
        # $script:1227192907012158$
        # - $npcName:24100101$? Is that the name of one of the Sky Fortress big wigs? She sounds intimidating...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.NEXT
        elif (self.state, self.index) == (11, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.CLOSE
        return Option.NONE
