""" 11004072: Suspicious Tree """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0619202207010170$
        # - ...
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0619202207010171$
            # - ...
            return 10
        elif self.index == 1:
            # $script:0619202207010172$
            # - ...
            if pick == 0:
                # $script:0619202207010173$
                # - ...
                return 31
            return -1
        return -1

    def __31(self, pick: int) -> int:
        # $script:0619202207010174$
        # - ...
        if pick == 0:
            # $script:0619202207010175$
            # - ...
            return 32
        return -1

    def __32(self, pick: int) -> int:
        # $script:0619202207010176$
        # - ...
        if pick == 0:
            # $script:0619202207010177$
            # - Huh. I didn't know trees could scream.
            return 33
        return -1

    def __33(self, pick: int) -> int:
        # $script:0619202207010178$
        # - Well obviously I'm not a tree! How did you even spot me? I'm here on a secret mission!
        if pick == 0:
            # $script:0619202207010179$
            # - You one of Frey's men?
            return 40
        elif pick == 1:
            # $script:0619202207010180$
            # - Did the empress send you?
            return 50
        elif pick == 2:
            # $script:0619202207010181$
            # - Liar.
            return 60
        return -1

    def __40(self, pick: int) -> int:
        # $script:0619202207010182$
        # - I'm trying to keep a low profile here. Can't you pretend you didn't see me and just move along?
        return -1

    def __50(self, pick: int) -> int:
        # $script:0619202207010183$
        # - You aren't worthy to even speak of her!
        return -1

    def __60(self, pick: int) -> int:
        # $script:0619202207010184$
        # - Stop blathering. I'm on duty. Get out of here now, before you regret it.
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
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (60, 0):
            return Option.CLOSE
        return Option.NONE
