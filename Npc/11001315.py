""" 11001315: Amorro """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1215203907005034$
        # - It's a beautiful day, isn't it? 
        return None # TODO

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227194507005691$
            # - People are always asking me if I'm okay living with my gramps. Well, I am!
            return 40
        elif self.index == 1:
            # $script:1227194507005692$
            # - I don't care if you think he's a screaming old fart. If you ask me, he's a great man!
            if pick == 0:
                # $script:1227194507005693$
                # - Your grandpa isn't popular, is he?
                return 41
            return -1
        return -1

    def __41(self, pick: int) -> int:
        # $script:1227194507005694$
        # - They're just jealous of how great he is! Gramps talks loud so people can hear him clearly. Isn't that nice? 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        return Option.NONE
