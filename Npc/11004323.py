""" 11004323: Eve """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1010140307011481$
        # - ...
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:1010140307011482$
            # - You...
            return 10
        elif self.index == 1:
            # $script:1010140307011483$
            # - What are you doing here? Have you come to try and convince me to go home too?
            if pick == 0:
                # $script:1010140307011484$
                # - Nothing like that.
                return 20
            return -1
        return -1

    def __20(self, pick: int) -> int:
        # $script:1010140307011485$
        # - ...Really?
        if pick == 0:
            # $script:1010140307011486$
            # - You don't look well. Are you feeling all right?
            return 30
        return -1

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:1010140307011487$
            # - You're not the first person to say that.
            return 30
        elif self.index == 1:
            # $script:1010140307011488$
            # - Something $npcName:11000044[gender:0]$ said was bothering me. I came here hoping to find answers.
            return 30
        elif self.index == 2:
            # $script:1010140307011489$
            # - Somehow $npcName:11004324[gender:0]$ figured out where I was going and came after me.
            return 30
        elif self.index == 3:
            # $script:1010140307011490$
            # - All he's done since is nag, sigh.
            return 30
        elif self.index == 4:
            # $script:1010140307011491$
            # - I'm not going to let anyone stop me from finding out what $npcName:11000044[gender:0]$ told me was true.
            if pick == 0:
                # $script:0111232407012691$
                # - Good for you!
                return 31
            return -1
        return -1

    def __31(self, pick: int) -> int:
        # $script:0111232407012692$
        # - Thanks! I appreciate your support.
        return -1

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:0109125407012657$
            # - Sigh...
            return 40
        elif self.index == 1:
            # $script:0109125407012658$
            # - $npcName:11004324[gender:0]$ is sweet, but sometimes I just need to be by myself.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (20, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.NEXT
        elif (self.state, self.index) == (30, 2):
            return Option.NEXT
        elif (self.state, self.index) == (30, 3):
            return Option.NEXT
        elif (self.state, self.index) == (30, 4):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.CLOSE
        return Option.NONE
