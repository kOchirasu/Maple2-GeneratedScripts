""" 11004075: Chee the Caterpillar """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0619202207010200$
        # - Uh... Um...
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0619202207010201$
            # - Uh... Um...
            return 10
        elif self.index == 1:
            # $script:0619202207010202$
            # - Okay, I'm just gonna do it. I'm going to ask. Hey, human! Tell me something...
            if pick == 0:
                # $script:0619202207010203$
                # - Know what?
                return 31
            return -1
        return -1

    def __31(self, pick: int) -> int:
        # $script:0619202207010204$
        # - What am I? I mean, what do you think I'm gonna be when I grow up?
        if pick == 0:
            # $script:0619202207010205$
            # - What do you mean?
            return 32
        return -1

    def __32(self, pick: int) -> int:
        # $script:0619202207010206$
        # - Am I gonna be a moth? A butterfly? Maybe a beetle?
        if pick == 0:
            # $script:0619202207010207$
            # - You're a beetle, for sure.
            return 40
        elif pick == 1:
            # $script:0619202207010208$
            # - Oh, you're definitely a moth.
            return 41
        elif pick == 2:
            # $script:0619202207010209$
            # - Hmm. Maybe a butterfly?
            return 42
        return -1

    def __40(self, pick: int) -> int:
        # $script:0619202207010210$
        # - R-really? I guess beetles are pretty cool...
        return -1

    def __41(self, pick: int) -> int:
        # $script:0619202207010211$
        # - Wow... A moth? So the butterflies were telling the truth... I might as well just end it now. Sniff...
        return -1

    def __42(self, pick: int) -> int:
        # $script:0619202207010212$
        # - That's a relief! The butterflies said I was a moth, but I want to become a beautiful butterfly!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (42, 0):
            return Option.CLOSE
        return Option.NONE
