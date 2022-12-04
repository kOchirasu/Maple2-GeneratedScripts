""" 11000024: Lydia """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000133$
        # - How may I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000136$
            # - Have you seen the Royal Road? Or rather, what's left of it? A huge earthquake tore right through it! Everyone who wants to get to $map:02000001$ is stuck here now.
            return 30
        elif self.index == 1:
            # $script:0831180407000137$
            # - $map:02000001$ is so close, and yet so far. Those who came by ship to attend the court are beyond disappointed. That's why we've decided to open the mountain path. To those who are authorized to use it, of course.
            return -1
        return -1

    def __40(self, pick: int) -> int:
        # $script:1215093407009645$
        # - Hm? How may I help you?
        if pick == 0:
            # $script:1215093407009646$
            # - What can you tell me about trading airships?
            return 41
        return -1

    def __41(self, pick: int) -> int:
        if self.index == 0:
            # $script:1215093407009647$
            # - Oh! Well, there was some kind of new-old technological development that recently opened the skies to trade. Flying boats, what a concept!
            return 41
        elif self.index == 1:
            # $script:1215093407009648$
            # - But, from what I've heard, only a fraction of the airships going out ever come back...
            if pick == 0:
                # $script:1215093407009649$
                # - What do you mean by that?
                return 42
            return -1
        return -1

    def __42(self, pick: int) -> int:
        # $script:1215093407009650$
        # - The airships vanish into... well, thin air! Once they set off for the skies, they just don't come back.
        if pick == 0:
            # $script:1215093407009651$
            # - Does anyone know what happens to them?
            return 43
        return -1

    def __43(self, pick: int) -> int:
        # $script:1215093407009652$
        # - I haven't the faintest idea. Anyway, that's all I know.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.NEXT
        elif (self.state, self.index) == (41, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (42, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (43, 0):
            return Option.CLOSE
        return Option.NONE
