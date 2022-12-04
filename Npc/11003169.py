""" 11003169: Joddy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0516084007008474$
        # - This place is dark. And wet. Just the sort of place I'd do crimes if <i>I</i> was a bad guy.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0516084007008475$
        # - You saved me. Again. Jeez, I can't do anything right...
        if pick == 0:
            # $script:0516084007008476$
            # - You'll get the hang of it.
            return 11
        elif pick == 1:
            # $script:0516084007008477$
            # - Get a grip.
            return 12
        return -1

    def __11(self, pick: int) -> int:
        # $script:0516084007008478$
        # - Y-yeah! Next time, it's <i>my</i> turn to save <i>you</i>!
        return -1

    def __12(self, pick: int) -> int:
        # $script:0516084007008479$
        # - Y-yes, $male:sir,female:ma'am$. <font size='20'>Aw man...</font>
        return -1

    def __20(self, pick: int) -> int:
        # $script:0516084007008480$
        # - If I was stronger, you wouldn't have to go through so much trouble. I'm sorry I'm such a burden...
        return -1

    def __30(self, pick: int) -> int:
        # $script:0516084007008481$
        # - How'd you get to be so strong, $MyPCName$?
        if pick == 0:
            # $script:0516084007008482$
            # - The secret is hard work.
            return 31
        elif pick == 1:
            # $script:0516084007008483$
            # - What can I say? I was born this good.
            return 32
        return -1

    def __31(self, pick: int) -> int:
        # $script:0516084007008484$
        # - Hard work! I can do that. I'll start tomorrow! Or maybe next week...
        return -1

    def __32(self, pick: int) -> int:
        # $script:0516084007008485$
        # - It's all natural talent? Oh man. I guess there's no hope for me...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (12, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        return Option.NONE
