""" 11004252: Arte """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0829171107010964$
        # - Looks like another day with no luck. Hm? Who are you?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0829171107010965$
        # - Looks like another day with no luck. Hm? Who are you?
        if pick == 0:
            # $script:0831123907010999$
            # - No one important. I'm just passing through.
            return 11
        return -1

    def __11(self, pick: int) -> int:
        # $script:0831123907011000$
        # - You're either brave or real dumb, to come all the way out here. Anyway, my name's $npcName:11004252[gender:1]$. I'm here observing.
        if pick == 0:
            # $script:0831123907011001$
            # - Observing what?
            return 12
        return -1

    def __12(self, pick: int) -> int:
        # $script:0831123907011002$
        # - Observing the movements of $npcName:11001813[gender:0]$'s army. He's one of the Seven Commanders, you know, and I have it on good authority that he often sends his troops through $map:03000115$ and $map:03000118$.
        if pick == 0:
            # $script:0831123907011003$
            # - Are you sure that's wise?
            return 13
        return -1

    def __13(self, pick: int) -> int:
        # $script:0831123907011004$
        # - Pfft, I'm not scared. I have family in Maple World, and I'll do anything I can to keep them safe, including marching right up to $npcName:11001813[gender:0]$ and stopping him right here and now.
        if pick == 0:
            # $script:0831143807011039$
            # - Thanks.
            return 14
        return -1

    def __14(self, pick: int) -> int:
        # $script:0831143807011040$
        # - No need to thank me. I'm happy if my family is happy. You should keep it up, too.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (13, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (14, 0):
            return Option.CLOSE
        return Option.NONE
