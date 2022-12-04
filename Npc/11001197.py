""" 11001197: Ropey """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1016142906000509$
        # - Only those who know the true value of Trophies can appreciate the value I offer.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1016142906000512$
        # - What's this? What business do you have with the Trophy expert? Are you interested in Trophies?
        if pick == 0:
            # $script:1016142906000513$
            # - Isn't everyone interested in Trophies?
            return 31
        elif pick == 1:
            # $script:1016142906000514$
            # - I don't have time for useless junk like Trophies.
            return 34
        return -1

    def __31(self, pick: int) -> int:
        # $script:1016142906000515$
        # - Ah, another Trophy connoisseur like myself! If you aspire to be an expert in Trophies like me, you'd better work hard. It'll take you a long time to become as savvy as I!
        if pick == 0:
            # $script:1016142906000516$
            # - What do I get if I have a lot of Trophies?
            return 32
        return -1

    def __32(self, pick: int) -> int:
        if self.index == 0:
            # $script:1016142906000517$
            # - Hmpf! Collecting Trophies is about more than just what you can get! Of course, there are precious few who collect for the sheer joy of it anymore.
            return 32
        elif self.index == 1:
            # $script:1016142906000518$
            # - In any case, I have some Trophies, and I'm always looking for more. You can never have enough Trophies, you know! If you happen to find any, I'll trade something equally valuable for them.
            if pick == 0:
                # $script:1016142906000519$
                # - Do you even have something equally valuable?
                return 33
            return -1
        return -1

    def __33(self, pick: int) -> int:
        # $script:1016142906000520$
        # - Of course I do! I've got all kinds of treasures from traveling around Maple World. I can't believe you doubt me.
        return -1

    def __34(self, pick: int) -> int:
        # $script:1016142906000521$
        # - How dare you call my beautiful Trophies junk! Insulting my trophies is like personally insulting me, the Trophy expert! You should be ashamed of yourself for being so insulting!
        if pick == 0:
            # $script:1016142906000522$
            # - All right! All right! I'm sorry! I shouldn't have called them junk.
            return 35
        return -1

    def __35(self, pick: int) -> int:
        # $script:1016142906000523$
        # - Hmpf! I suppose I'll forgive you this time. Not everyone understands the true beauty of Trophies, after all. But don't let it happen again! Trophy experts demand respect, I tell you!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.NEXT
        elif (self.state, self.index) == (32, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (33, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (34, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (35, 0):
            return Option.CLOSE
        return Option.NONE
