""" 11000001: Manovich """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000001$
        # - $MyPCName$, what is it?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180407000003$
        # - ...And this knucklehead, where in the world is he?
        if pick == 0:
            # $script:0831180407000004$
            # - What is it?
            return 11
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000005$
            # - My son is a bit... no, he's very hard-headed. I lost my patience with him, and well... He stormed out of the house and hasn't returned yet.
            return 11
        elif self.index == 1:
            # $script:0831180407000006$
            # - Sigh... People are right when they say parenting is the world's hardest job.
            return -1
        return -1

    def __20(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000007$
            # - It's a beautiful day today. Hopefully it'll stay that way... 
            return 20
        elif self.index == 1:
            # $script:0831180407000008$
            # - As the elder of this village, I'm doing my best to keep its residents safe. But there's little I could do about the seal of the Land of Darkness breaking, and now something terrible seems to happen every day.
            return 20
        elif self.index == 2:
            # $script:0831180407000009$
            # - The only wish I have now is for peace. $MyPCName$, I'm relying on you for that.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.NEXT
        elif (self.state, self.index) == (11, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.NEXT
        elif (self.state, self.index) == (20, 1):
            return Option.NEXT
        elif (self.state, self.index) == (20, 2):
            return Option.CLOSE
        return Option.NONE
