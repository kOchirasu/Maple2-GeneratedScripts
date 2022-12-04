""" 11000317: Jonn """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001205$
        # - What is it?
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180407001209$
        # - Ah, are you an adventurer? So am I!
        if pick == 0:
            # $script:0831180407001210$
            # - Don't you lie to me!
            return 41
        elif pick == 1:
            # $script:0831180407001211$
            # - What is an adventurer to you?
            return 42
        return -1

    def __41(self, pick: int) -> int:
        # $script:0831180407001212$
        # - I-I'm not lying! I mean it!
        if pick == 0:
            # $script:0831180407001213$
            # - What do you think an adventurer is?
            return 42
        return -1

    def __42(self, pick: int) -> int:
        # $script:0831180407001214$
        # - An adventurer is someone who embarks on adventures around the world! I've even been to $map:02000023$, you know. My next destination is $map:02000051$!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (42, 0):
            return Option.CLOSE
        return Option.NONE
