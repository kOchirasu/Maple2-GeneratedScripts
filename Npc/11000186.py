""" 11000186: Jack """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([50, 60])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000810$
        # - How may I help you?
        return None # TODO

    def __50(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000813$
            # - I live with my grandma. She said that when I was young, my parents were taken away by demons. Also, my sister was frozen solid alongside the rest of the villagers. You could say my family's had a rough go of it.
            return 50
        elif self.index == 1:
            # $script:0831180407000814$
            # - She also said the empire's forces are no better than those demons. They brought ice elementals to fight the demons, but tons of innocent people were frozen during the fight.
            return -1
        return -1

    def __60(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000815$
            # - See those red maple trees there? When Grandma planted them, they were seeds as big as your thumbnail. She says they grew twice as fast as I did.
            return 60
        elif self.index == 1:
            # $script:0831180407000816$
            # - I've heard only the warmth of $itemPlural:30000028$ can thaw the people frozen below.
            return 60
        elif self.index == 2:
            # $script:0831180407000817$
            # - That's because red maple trees are born from the energy of the fire elementals that fell in that terrible battle. I don't know if that's true.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (50, 0):
            return Option.NEXT
        elif (self.state, self.index) == (50, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (60, 0):
            return Option.NEXT
        elif (self.state, self.index) == (60, 1):
            return Option.NEXT
        elif (self.state, self.index) == (60, 2):
            return Option.CLOSE
        return Option.NONE
