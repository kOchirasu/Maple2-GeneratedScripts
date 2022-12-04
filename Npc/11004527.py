""" 11004527: Richard """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 50])

    def select(self) -> int:
        return random.choice([0, 40])

    def __0(self, pick: int) -> int:
        # $script:0103163407012512$
        # - Oh?!
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0104140207012578$
        # - Aaaah.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0103163407012513$
        # - Ah... Hello there.
        if pick == 0:
            # $script:0103163407012514$
            # - How's the research going?
            return 20
        return -1

    def __20(self, pick: int) -> int:
        if self.index == 0:
            # $script:0103163407012515$
            # - V-very well. As you can see, I'm burning the midnight oil. Eheheh...
            return 20
        elif self.index == 1:
            # $script:0103163407012516$
            # - If you could see our results, why, they'd knock your socks off!
            return 20
        elif self.index == 2:
            # $script:0103163407012517$
            # - S-so you go and tell $npcName:11004438[gender:0]$ that we're working hard, okay?
            if pick == 0:
                # $script:0103163407012518$
                # - It doesn't look like you're working <i>that</i> hard.
                return 30
            return -1
        return -1

    def __30(self, pick: int) -> int:
        # $script:0103163407012519$
        # - I-I am, and I have the overtime sheets to show it! L-later. I'll have them later. You'll see...
        return -1

    def __50(self, pick: int) -> int:
        # $script:0104140207012579$
        # - Isn't this place lovely? I get to enjoy this wonderful nature while I work.
        if pick == 0:
            # $script:0104140207012580$
            # - I see the "enjoy" part, but what about the "work" part?
            return 60
        return -1

    def __60(self, pick: int) -> int:
        # $script:0104140207012581$
        # - I can't help it if I have resting "relaxed" face. Trust me when I say that we're working hard over here.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (20, 0):
            return Option.NEXT
        elif (self.state, self.index) == (20, 1):
            return Option.NEXT
        elif (self.state, self.index) == (20, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (60, 0):
            return Option.CLOSE
        return Option.NONE
