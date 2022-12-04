""" 11001587: Ishura """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0504151707006075$
        # - Ah, $MyPCName$!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0515180307006123$
        # - There must be something about the power $npcName:11001231[gender:0]$  seeks in our ancestors' records.
        if pick == 0:
            # $script:0515180307006124$
            # - Why are you so sure?
            return 11
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:0515180307006125$
            # - I encountered Holstatt in the Land of Darkness once. He said that Arazaad had kept a secret from us. That the real legacy of our ancestors was elsewhere. 
            return 11
        elif self.index == 1:
            # $script:0515180307006126$
            # - I don't know if he was lying or not. But if he wasn't, then the old records, which only Arazaad could read, must hold clue about the secret. Something to point us towards this so-called legacy. 
            return -1
        return -1

    def __20(self, pick: int) -> int:
        # $script:0517210007006136$
        # - Why are you staring at me?
        if pick == 0:
            # $script:0517210007006137$
            # - I just wanted to see you.
            return 21
        elif pick == 1:
            # $script:0517210007006138$
            # - I missed you so much!
            return 22
        elif pick == 2:
            # $script:0517210007006139$
            # - Play with me.
            return 23
        elif pick == 3:
            # $script:0517210007006140$
            # - There's something I need to tell you.
            return 24
        return -1

    def __21(self, pick: int) -> int:
        # $script:0517210007006141$
        # - Ha... Weirdo... 
        return -1

    def __22(self, pick: int) -> int:
        # $script:0517210007006142$
        # - Y-you did? So did I. Ahem.
        return -1

    def __23(self, pick: int) -> int:
        # $script:0517210007006143$
        # - Now is <i>not</i> the time for such things!
        return -1

    def __24(self, pick: int) -> int:
        # $script:0517210007006144$
        # - I'm a little busy right now.
        return -1

    def __30(self, pick: int) -> int:
        # $script:0524142307006216$
        # - There must be something about the power $npcName:11001231[gender:0]$ seeks in our ancestors' records.
        if pick == 0:
            # $script:0524142307006217$
            # - Why are you so sure?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0524142307006218$
        # - I encountered Holstatt in the Land of Darkness once. He said that Arazaad had kept a secret from us. That the real legacy of our ancestors was elsewhere. 
        return -1

    def __32(self, pick: int) -> int:
        # $script:0524142307006219$
        # - I don't know if he was lying or not. But if he wasn't, then the old records, which only Arazaad could read, must hold some clue about the secret. Something to point us towards this so-called legacy. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.NEXT
        elif (self.state, self.index) == (11, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (21, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (22, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (23, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (24, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        return Option.NONE
