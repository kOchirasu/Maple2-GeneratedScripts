""" 11001410: Dona """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217205907005407$
        # - You came to gawk at the Meerkat Patrols? 
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:1222203907005494$
        # - We all trust and rely on each other in the Meerkat Patrol. You could say we're a big happy family.
        if pick == 0:
            # $script:1222203907005495$
            # - What's the secret to your camaraderie?
            return 41
        return -1

    def __41(self, pick: int) -> int:
        if self.index == 0:
            # $script:1222203907005496$
            # - It's all thanks to our hardworking captain. We all look up to good old Captain $npcName:11001408[gender:0]$! 
            return 41
        elif self.index == 1:
            # $script:1222203907005497$
            # - Since you're here, you should say hi to him. I bet he'll have some good advice for you.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.NEXT
        elif (self.state, self.index) == (41, 1):
            return Option.CLOSE
        return Option.NONE
