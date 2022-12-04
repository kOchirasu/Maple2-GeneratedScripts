""" 11001911: Battle Sim Researcher """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1115191007007385$
        # - How may I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1115191007007388$
        # - Welcome to the $map:63000047$. How may I help you?
        if pick == 0:
            # $script:1115191007007389$
            # - Sell me on this $map:63000047$ business.
            return 31
        elif pick == 1:
            # $script:1115191007007390$
            # - You simulate battles here?
            return 32
        elif pick == 2:
            # $script:1115191007007391$
            # - Who created all this?
            return 33
        return -1

    def __31(self, pick: int) -> int:
        if self.index == 0:
            # $script:1115191007007392$
            # - The $map:63000047$ is home of the Chaotic Raid Battle Sim, where you can experience the most realistic virtual battles in Maple World. All the great heroes come here sooner or later.
            return 31
        elif self.index == 1:
            # $script:1116121707007396$
            # - Do you have any more questions? 
            if pick == 0:
                # $script:1116121707007397$
                # - You simulate battles here?
                return 32
            elif pick == 1:
                # $script:1116121707007398$
                # - Who created all this?
                return 33
            elif pick == 2:
                # $script:1116121707007399$
                # - Thank you for your time.
                return 34
            return -1
        return -1

    def __32(self, pick: int) -> int:
        if self.index == 0:
            # $script:1115191007007393$
            # - The Chaotic Raid Battle Sim is a full-immersion virtual combat simulator that Dr. Gelimer created after decades of collecting combat data. You can use it to prepare for any kind of conflict situation.
            return 32
        elif self.index == 1:
            # $script:1115191007007394$
            # - The simulations are so good, they're more dangerous than the real thing! On that note, you should definitely make sure you and your group are prepared before trying it out.
            return 32
        elif self.index == 2:
            # $script:1116121707007400$
            # - Do you have any more questions? 
            if pick == 0:
                # $script:1116121707007401$
                # - Sell me on this $map:63000047$ business.
                return 31
            elif pick == 1:
                # $script:1116121707007402$
                # - Who created all this?
                return 33
            elif pick == 2:
                # $script:1116121707007403$
                # - Thank you for your time.
                return 34
            return -1
        return -1

    def __33(self, pick: int) -> int:
        if self.index == 0:
            # $script:1115191007007395$
            # - This place was created by my teacher, the great Dr. Gelimer. It is a masterpiece containing combat data taken from monsters throughout Maple World.
            return 33
        elif self.index == 1:
            # $script:1116121707007404$
            # - Do you have any more questions? 
            if pick == 0:
                # $script:1116121707007405$
                # - Sell me on this $map:63000047$ business.
                return 31
            elif pick == 1:
                # $script:1116121707007406$
                # - You simulate battles here?
                return 32
            elif pick == 2:
                # $script:1116121707007407$
                # - Thank you for your time.
                return 34
            return -1
        return -1

    def __34(self, pick: int) -> int:
        # $script:1116121707007408$
        # - If you have any more questions, you know where to find me.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.NEXT
        elif (self.state, self.index) == (31, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.NEXT
        elif (self.state, self.index) == (32, 1):
            return Option.NEXT
        elif (self.state, self.index) == (32, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (33, 0):
            return Option.NEXT
        elif (self.state, self.index) == (33, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (34, 0):
            return Option.CLOSE
        return Option.NONE
