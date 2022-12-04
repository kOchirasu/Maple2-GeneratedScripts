""" 11004066: Mysterious Luditionist """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0619202207010127$
        # - ...
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0619202207010128$
            # - ...
            return 10
        elif self.index == 1:
            # $script:0619202207010129$
            # - Tch! Don't tell me I got caught... Your senses are sharp, I'll give you that.
            if pick == 0:
                # $script:0619202207010130$
                # - Why are you hiding here?
                return 31
            return -1
        return -1

    def __31(self, pick: int) -> int:
        # $script:0619202207010131$
        # - This place, the $map:02000262$, was created by us, the luditionists. I'm taking a quick peek to ensure everything is running smoothly. And by smoothly, I mean with lots of exciting incidents.
        return -1

    def __32(self, pick: int) -> int:
        # $script:0619202207010132$
        # - A world without incidents is boring, hmm? We don't want a boring world.
        if pick == 0:
            # $script:0619202207010133$
            # - What does a luditionist do?
            return 33
        return -1

    def __33(self, pick: int) -> int:
        # $script:0619202207010134$
        # - Hush, now. Don't ask too many questions or you'll get hurt. Let's just say that we're trying to make things more fun.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (33, 0):
            return Option.CLOSE
        return Option.NONE
