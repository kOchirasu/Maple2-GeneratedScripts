""" 11001192: Pirollo """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1016202007004172$
        # - Grah! Writer's block, my mortal enemy!
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:1016202007004175$
            # - <font color="#909090"> (He sighs.)</font>
            #   Am I really qualified to be a TV writer...? Hey, you there! Can I ask you a question?
            return 30
        elif self.index == 1:
            # $script:1016210507004209$
            # - Do you think people should pursue jobs they <i>want</i> to do, or just ones they're good at?
            if pick == 0:
                # $script:1016210507004210$
                # - I'm not sure... What do you think?
                return 31
            elif pick == 1:
                # $script:1016210507004211$
                # - Why? Do you not like your job?
                return 32
            return -1
        return -1

    def __31(self, pick: int) -> int:
        # $script:1016202007004178$
        # - What I want to do, of course! I would give anything to be good at what I <i>want</i> to be doing...
        return -1

    def __32(self, pick: int) -> int:
        # $script:1016202007004179$
        # - That's not it. This has been my dream job for as long as I can remember. It's just... not the job I expected.
        #   <font color="#909090">(He sighs.)</font>
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
