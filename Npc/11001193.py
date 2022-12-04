""" 11001193: Illuna """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1016202007004180$
        # - I wish I could find a story my colleague $npcName:11001191[gender:1]$ would be excited to cover.
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:1016202007004183$
            # - Hehehe! This is so much fun! <font color="#C66455" size="22">Pfft... Are you kidding me? This is awful.</font> 
            #   No, no. Don't say that.
            #   <font color="#909090">(...Is she arguing with herself?)</font>
            return 30
        elif self.index == 1:
            # $script:1016210507004212$
            # - ...?! Ahh! How long have you been standing there? You didn't hear what I said, did you?
            if pick == 0:
                # $script:1016210507004213$
                # - Uhh... Were you just talking to yourself?
                return 31
            elif pick == 1:
                # $script:1016210507004214$
                # - I didn't hear a thing.
                return 32
            return -1
        return -1

    def __31(self, pick: int) -> int:
        # $script:1016202007004186$
        # - W-what? I'm not crazy, you're crazy! <font color="#C66455" size="22">I didn't say anything, got it?</font>
        #   <font color="#909090">(After an awkward silence, Illuna sighs in resignation.)</font>
        return -1

    def __32(self, pick: int) -> int:
        # $script:1016202007004187$
        # - Hah... Hahaha! 
        #   <font color="#C66455" size="22">Good, good.</font>
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        return Option.NONE
