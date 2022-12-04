""" 11004074: Overheating Dog """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0619202207010189$
        # - Ah, it's hot... Even hotter than yesterday...
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0619202207010190$
            # - Ah, it's hot... Even hotter than yesterday...
            return 10
        elif self.index == 1:
            # $script:0619202207010191$
            # - <i>Another</i> human? Phew. You guys really don't mind this heat?
            if pick == 0:
                # $script:0619202207010192$
                # - What's the matter?
                return 31
            return -1
        return -1

    def __31(self, pick: int) -> int:
        # $script:0619202207010193$
        # - Don't laugh! I've got heatstroke. I think. I came up here because it's cooler, and now I can't go back down because it's too hot.
        if pick == 0:
            # $script:0619202207010194$
            # - You... do realize you're a fire dog, right?
            return 32
        return -1

    def __32(self, pick: int) -> int:
        # $script:0619202207010195$
        # - You think I don't know how weird it is that I hate the heat? Maybe it's because I was born in winter...
        if pick == 0:
            # $script:0619202207010196$
            # - I thought you guys needed fire to stay alive.
            return 33
        return -1

    def __33(self, pick: int) -> int:
        # $script:0619202207010197$
        # - No, no more fire! I can't go back down there. I gotta shake this heatstroke...
        if pick == 0:
            # $script:0619202207010198$
            # - Eating something spicy might take your mind off the heat.
            return 34
        return -1

    def __34(self, pick: int) -> int:
        # $script:0619202207010199$
        # - You're just like all those people napping down there. No help. No help at all...
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
        elif (self.state, self.index) == (33, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (34, 0):
            return Option.CLOSE
        return Option.NONE
