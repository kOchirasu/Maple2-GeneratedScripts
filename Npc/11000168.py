""" 11000168: Kay """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1103095507004409$
        # - Welcome to the Maple OX Quiz!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1103095507004412$
        # - How'd you like the quiz? Pretty tricky, right? Come back next time, because there's more where that came from!
        if pick == 0:
            # $script:1103095507004413$
            # - I lost. I <i>lost</i>. I <i>never</i> lose!
            return 31
        elif pick == 1:
            # $script:1103095507004414$
            # - So... what are the questions for the next quiz?
            return 32
        elif pick == 2:
            # $script:1103095507004415$
            # - Congratulations on being the host.
            return 33
        return -1

    def __31(self, pick: int) -> int:
        # $script:1103095507004416$
        # - Don't lose heart. You can always come back and try again next time. I'll be rooting for you, $MyPCName$!
        return -1

    def __32(self, pick: int) -> int:
        # $script:1103095507004417$
        # - You want me to help you cheat? No. No way. I can't believe you'd ask me that...
        return -1

    def __33(self, pick: int) -> int:
        # $script:1103095507004418$
        # - Thank you! It's a dream come true, to be honest. A dream come true...
        #   <font color="#909090">(He starts weeping.)</font>
        if pick == 0:
            # $script:1103095507004419$
            # - Don't cry, little raccoon guy.
            return 34
        return -1

    def __34(self, pick: int) -> int:
        # $script:1103095507004420$
        # - I-I won't! Sorry. I just wasn't expecting anyone to congratulate me. I'll do my best not to let you down as a host, $MyPCName$!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (33, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (34, 0):
            return Option.CLOSE
        return Option.NONE
