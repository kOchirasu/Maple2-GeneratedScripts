""" 11000015: Oska """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000074$
        # - How may I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000077$
        # - What brings you to this place?
        if pick == 0:
            # $script:0831180407000078$
            # - I came to see you.
            return 31
        elif pick == 1:
            # $script:0831180407000079$
            # - I came to $map:02000076$ to see the elder.
            return 41
        elif pick == 2:
            # $script:0831180407000080$
            # - I have business here.
            return 51
        elif pick == 3:
            # $script:0831180407000081$
            # - That's none of your business.
            return 61
        return -1

    def __31(self, pick: int) -> int:
        # $script:0831180407000082$
        # - Do you have a reason for coming to see me?
        if pick == 0:
            # $script:0831180407000083$
            # - I just thought I'd say hi.
            return 32
        elif pick == 1:
            # $script:0831180407000084$
            # - Nope.
            return 33
        return -1

    def __32(self, pick: int) -> int:
        # $script:0831180407000085$
        # - Oh. Well. Hi.
        return -1

    def __33(self, pick: int) -> int:
        # $script:0831180407000086$
        # - Well, you're just being ridiculous. I've no time for that. Excuse me. 
        return -1

    def __41(self, pick: int) -> int:
        # $script:0831180407000087$
        # - $npcName:11000001[gender:0]$'s house is on the hill behind the clock tower in the center of the village. He's always there, keeping an eye on everyone.
        return -1

    def __51(self, pick: int) -> int:
        # $script:0831180407000088$
        # - I see. All I'll say then is that if you need help, the militia is always here.
        return -1

    def __61(self, pick: int) -> int:
        # $script:0831180407000089$
        # - I hope I didn't upset you. You certainly don't have to explain yourself. But if you do, the rest of the militia and I may be able to help.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (33, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (51, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (61, 0):
            return Option.CLOSE
        return Option.NONE
