""" 11003257: Cheshire Carmen Bella Jr. II """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40, 50, 60])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0403155707008184$
        # - Meow!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0403155707008185$
        # - What're you staring at? Never see a talking cat before?
        if pick == 0:
            # $script:0403155707008186$
            # - Guh...
            return 31
        elif pick == 1:
            # $script:0403155707008187$
            # - Are you a magic kitty?
            return 32
        return -1

    def __31(self, pick: int) -> int:
        # $script:0403155707008188$
        # - Meheh! You're an old-fashioned one, talking animals are all the rage these days! I forgive your ignorance, though... so long as you bring me snacks next time.
        return -1

    def __32(self, pick: int) -> int:
        # $script:0403155707008189$
        # - Yep! A magical kitty for a magical place. This is $map:02000023$ after all, land of wonder and imagination. Welcome!
        return -1

    def __40(self, pick: int) -> int:
        # $script:0403155707008190$
        # - What's with the sour face?
        if pick == 0:
            # $script:0530154407008542$
            # - Send me to $npcName:11003254[gender:1]$.
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:0530154407008543$
        # - Has my magic failed? Impossible!
        if pick == 0:
            # $script:0530154407008544$
            # - Hurry it up!
            return 42
        return -1

    def __42(self, pick: int) -> int:
        # functionID=1 
        # $script:0530154407008545$
        # - I'm trying! Close your eyes. It'll work for sure this time!
        return -1

    def __50(self, pick: int) -> int:
        # $script:0530154407008546$
        # - There's something... dark blocking my magic. There's no way to get to Ellinel right now. 
        return -1

    def __60(self, pick: int) -> int:
        # $script:0530154407008547$
        # - What's with the sour face?
        if pick == 0:
            # $script:0808093807008794$
            # - I'm lost.
            return 61
        elif pick == 1:
            # $script:0808122107008796$
            # - I'm not depressed.
            return 62
        return -1

    def __61(self, pick: int) -> int:
        # $script:0808122107008797$
        # - On to the next portal! Since you've passed through the gate to $map:02000023$, the portal there will open new paths to you. But if there's nowhere to go, the portal won't work.
        return -1

    def __62(self, pick: int) -> int:
        # $script:0808122107008798$
        # - You look worried. Go ahead, put your feet up and tell me your troubles.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (42, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (60, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (61, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (62, 0):
            return Option.CLOSE
        return Option.NONE
