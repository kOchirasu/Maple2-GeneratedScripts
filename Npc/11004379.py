""" 11004379: Maximilian """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1109213607011793$
        # - I'll be honest, I didn't think this place was so merry until <i>you</i> showed up.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1109213607011794$
        # - I'll be honest, I didn't think this place was so merry until <i>you</i> showed up.
        return -1

    def __40(self, pick: int) -> int:
        # $script:1120173007011868$
        # - I'll be honest, I didn't think this place was so merry until <i>you</i> showed up.
        if pick == 0:
            # $script:1120173007011869$
            # - Did you see $npcName:11004345[gender:1]$'s family?
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:1120173007011870$
        # - $npcName:11004345[gender:1]$? That's $npcName:11004347[gender:1]$'s daughter. She's my boss, but she's off today. You sure she's not at home?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        return Option.NONE
