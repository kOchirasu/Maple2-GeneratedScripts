""" 11001409: Fubo """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217205907005406$
        # - No exceptions. Not even for humans!
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:1222203907005486$
        # - You want to be strong, like the Meerkat Patrol? Then join our training!
        if pick == 0:
            # $script:1222203907005487$
            # - That sounds <i>adorable</i>. Sign me up!
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:1222203907005488$
        # - Don't underestimate us. If you cry and give up halfway through, you'll never live it down!
        if pick == 0:
            # $script:1222203907005489$
            # - I can handle anything you throw at me!
            return 42
        return -1

    def __42(self, pick: int) -> int:
        # $script:1222203907005490$
        # - Heh... I'll see to it that you run away with your tail between your legs!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (42, 0):
            return Option.CLOSE
        return Option.NONE
