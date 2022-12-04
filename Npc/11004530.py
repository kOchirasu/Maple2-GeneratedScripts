""" 11004530: Reika """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 50])

    def select(self) -> int:
        return random.choice([0, 40])

    def __0(self, pick: int) -> int:
        # $script:0103163407012522$
        # - I see you there.
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0104140207012582$
        # - I can't stand the noise here...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0103163407012523$
        # - Can I help you?
        if pick == 0:
            # $script:0103163407012524$
            # - I'm just checking in on things.
            return 20
        return -1

    def __20(self, pick: int) -> int:
        if self.index == 0:
            # $script:0103163407012525$
            # - $npcName:11004437[gender:0]$ sent you, then. As you can see, nothing's changed.
            return 20
        elif self.index == 1:
            # $script:0103163407012526$
            # - We're still getting shot at by wild robots. We're still dealing with these ridiculous dust clouds. And we're still getting motion sickness when that machine over there sends out tremors...
            return 20
        elif self.index == 2:
            # $script:0103163407012527$
            # - I miss the forest.
            return 20
        elif self.index == 3:
            # $script:0103163407012528$
            # - ...
            return 20
        elif self.index == 4:
            # $script:0103163407012529$
            # - When you get back to the outpost, let them know we need reinforcements to help with the killer machines here.
            if pick == 0:
                # $script:0103163407012530$
                # - Will do.
                return 30
            return -1
        return -1

    def __30(self, pick: int) -> int:
        # $script:0103163407012531$
        # - Thanks. You're a life saver!
        return -1

    def __50(self, pick: int) -> int:
        if self.index == 0:
            # $script:0104140207012583$
            # - The dust here is unreal... I should have brought a face mask.
            return 50
        elif self.index == 1:
            # $script:0104140207012584$
            # - I'm going to get a lung disease from my time in this place. Hopefully it's all just in my head...
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (20, 0):
            return Option.NEXT
        elif (self.state, self.index) == (20, 1):
            return Option.NEXT
        elif (self.state, self.index) == (20, 2):
            return Option.NEXT
        elif (self.state, self.index) == (20, 3):
            return Option.NEXT
        elif (self.state, self.index) == (20, 4):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.NEXT
        elif (self.state, self.index) == (50, 1):
            return Option.CLOSE
        return Option.NONE
