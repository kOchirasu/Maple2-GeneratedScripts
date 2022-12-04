""" 11004071: Deluded Frog """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0619202207010155$
        # - Woe is me, woe is me...
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0619202207010156$
            # - Woe is me, woe is me...
            return 10
        elif self.index == 1:
            # $script:0619202207010157$
            # - Oh... Hey! You! Help me!
            if pick == 0:
                # $script:0619202207010158$
                # - What's going on?
                return 31
            return -1
        return -1

    def __31(self, pick: int) -> int:
        # $script:0619202207010159$
        # - Just hear me out, okay? I'm actually a noble from Tria! A mage cursed me to become a frog, until... Well, perhaps you could help me break the curse.
        if pick == 0:
            # $script:0619202207010160$
            # - Don't tell me you want me to kiss you.
            return 32
        return -1

    def __32(self, pick: int) -> int:
        # $script:0619202207010161$
        # - But it's the only way to break the curse!
        if pick == 0:
            # $script:0619202207010162$
            # -  Has anyone else tried breaking the curse yet?
            return 33
        return -1

    def __33(self, pick: int) -> int:
        # $script:0619202207010163$
        # - Of course. Obviously, I haven't found the <i>right</i> human to break the curse...
        if pick == 0:
            # $script:0619202207010164$
            # - Are you really cursed?
            return 34
        return -1

    def __34(self, pick: int) -> int:
        # $script:0619202207010165$
        # - That's what my ma used to tell me when I wouldn't eat my flies. The old frog must've taken me in when I was really little.
        if pick == 0:
            # $script:0619202207010166$
            # - Ah. Well, I'll pass. Thanks, though.
            return 35
        return -1

    def __35(self, pick: int) -> int:
        # $script:0619202207010167$
        # - Don't be so picky. I'll shower you with riches when I'm back in my rightful form! I just know in my guts that you can break this curse.
        if pick == 0:
            # $script:0619202207010168$
            # - You keep telling yourself that. I'm out of here.
            return 36
        return -1

    def __36(self, pick: int) -> int:
        # $script:0619202207010169$
        # - Where, oh where will I find someone to break my curse? Woe is me!
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
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (35, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (36, 0):
            return Option.CLOSE
        return Option.NONE
