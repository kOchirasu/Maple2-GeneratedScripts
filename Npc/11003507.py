""" 11003507: Karyan """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0816160115009007$
        # - What is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0816160115009008$
        # - I'm a member of Team Mushroom, but I'm also a freelance pet-tamer.
        if pick == 0:
            # $script:0816160115009009$
            # - Can I hire you?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0816160115009010$
        # - Not now. I'm on vacation.
        return -1

    def __40(self, pick: int) -> int:
        # $script:0816211415009058$
        # - Apparently, Dryad Co. set their R&D department loose on monsters' tastebuds and developed these new monster candies. The $itemPlural:63000000$ are pretty popular.
        if pick == 0:
            # $script:0816211415009059$
            # - Where can I get these monster candies?
            return 41
        elif pick == 1:
            # $script:0816211415009060$
            # - Tell me about Dryad Co.
            return 42
        return -1

    def __41(self, pick: int) -> int:
        # $script:0816211415009061$
        # - Most major supply shops should carry $itemPlural:63000000$. I'm pretty sure $npcName:11003506[gender:1]$ has some in stock.
        return -1

    def __42(self, pick: int) -> int:
        # $script:0816211415009062$
        # - I don't really know much, myself. It's a tech giant with lots of next-gen products. Rumor has it one of the founders of Dryad Co. recently retired, but nobody really knows much about them, or even what they look like.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (42, 0):
            return Option.CLOSE
        return Option.NONE
