""" 11003092: Franz """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0113173307007775$
        # - Hello, how may I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0113173307007778$
        # - Hello, how may I help you?
        if pick == 0:
            # $script:0113173307007779$
            # - How can I play music in $map:02000064$?
            return 31
        elif pick == 1:
            # $script:0113173307007780$
            # - How can I get to the stage?
            return 33
        elif pick == 2:
            # $script:0113173307007781$
            # - How can I cheer during a performance?
            return 34
        return -1

    def __31(self, pick: int) -> int:
        # $script:0113173307007782$
        # - All you have to do to perform in $map:02000064$ is apply! Just press the request button. If someone else has already applied, you'll need to wait 10 minutes and then apply again when they're done.
        if pick == 0:
            # $script:0113173307007783$
            # - How can I play as a group?
            return 32
        return -1

    def __32(self, pick: int) -> int:
        if self.index == 0:
            # $script:0113173307007784$
            # - For ensemble performances, form a party with someone who has applied to perform. After that you can all take the stage together.
            return 32
        elif self.index == 1:
            # $script:0113173307007785$
            # - It's super easy to perform in a group! So, is there anything else you want to know?
            if pick == 0:
                # $script:0113173307007786$
                # - How can I get to the stage?
                return 33
            elif pick == 1:
                # $script:0113173307007787$
                # - How can I cheer during a performance?
                return 34
            elif pick == 2:
                # $script:0113173307007788$
                # - No, I think I'm good.
                return 35
            return -1
        return -1

    def __33(self, pick: int) -> int:
        if self.index == 0:
            # $script:0113173307007789$
            # - We'll let you up on stage if you're going to perform. Just hit the apply button and we'll let you know when it's time.
            return 33
        elif self.index == 1:
            # $script:0113173307007790$
            # - If you want to leave the stage, just hit the same button you used to get up there. That was an easy one. Anything else?
            if pick == 0:
                # $script:0113173307007791$
                # - How can I play music in $map:02000064$?
                return 31
            elif pick == 1:
                # $script:0113173307007792$
                # - How can I cheer during a performance?
                return 34
            elif pick == 2:
                # $script:0113173307007793$
                # - No, I think I'm good.
                return 35
            return -1
        return -1

    def __34(self, pick: int) -> int:
        if self.index == 0:
            # $script:0113173307007794$
            # - Everyone in $map:02000064$ can hear performances from the stage. Show your appreciation by lighting firecrackers, waving glowsticks, or just clapping!
            return 34
        elif self.index == 1:
            # $script:0113173307007795$
            # - Cheers and applause encourage the performers, so let 'em have it! Anything else you want to know?
            if pick == 0:
                # $script:0113173307007796$
                # - How can I play music in $map:02000064$?
                return 31
            elif pick == 1:
                # $script:0113173307007797$
                # - How can I get to the stage?
                return 33
            elif pick == 2:
                # $script:0113173307007798$
                # - No, I think I'm good.
                return 35
            return -1
        return -1

    def __35(self, pick: int) -> int:
        # $script:0113173307007799$
        # - Great! Come on back if you have any more questions about performing in $map:02000064$.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.NEXT
        elif (self.state, self.index) == (32, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (33, 0):
            return Option.NEXT
        elif (self.state, self.index) == (33, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (34, 0):
            return Option.NEXT
        elif (self.state, self.index) == (34, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (35, 0):
            return Option.CLOSE
        return Option.NONE
