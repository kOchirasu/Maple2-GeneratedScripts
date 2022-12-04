""" 11000044: Katvan """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000209$
        # - Let's get to business.
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000212$
            # - I'll admit, not everyone in Dark Wind was happy when I took over. Many were loyal to Captain Winn, not the organization. After he passed away, $npcName:11000006[gender:0]$ took some of our best agents and left.
            return 30
        elif self.index == 1:
            # $script:0831180407000213$
            # - But I have my own principles to follow and I intend to lead Dark Wind in my own way. Winn Stilton was a great man, but we won't live in his shadow.
            return 30
        elif self.index == 2:
            # $script:0831180407000214$
            # - The others may not be on board yet, but they'll come around. Eventually.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.NEXT
        elif (self.state, self.index) == (30, 2):
            return Option.CLOSE
        return Option.NONE
