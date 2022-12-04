""" 11004321: Tara """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 30])

    def select(self) -> int:
        return random.choice([0, 20])

    def __0(self, pick: int) -> int:
        # $script:1102172107011625$
        # - This won't do...
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:1010140307011458$
        # - This won't do...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1102172107011626$
        # - It's hard to get my bearings in a weird place like this.
        return -1

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:1010140307011459$
            # - Huh?
            return 30
        elif self.index == 1:
            # $script:1010140307011460$
            # - Ah! It's you! How have you been?
            if pick == 0:
                # $script:1010140307011461$
                # - I'm doing pretty well, thanks.
                return 40
            return -1
        return -1

    def __40(self, pick: int) -> int:
        # $script:1010140307011462$
        # - That's good to hear. So what brings you here?
        if pick == 0:
            # $script:1010140307011463$
            # - I came here on an investigation.
            return 50
        return -1

    def __50(self, pick: int) -> int:
        if self.index == 0:
            # $script:1010140307011464$
            # - I see, you too... Sigh.
            return 50
        elif self.index == 1:
            # $script:1010140307011465$
            # - We're here researching the dark dragons that Biset used to talk about.
            if pick == 0:
                # $script:1010140307011466$
                # - How did you get here?
                return 60
            return -1
        return -1

    def __60(self, pick: int) -> int:
        if self.index == 0:
            # $script:1010140307011467$
            # - $npcName:11004319[gender:1]$ brought us here with her dragon power. It seems she's come a long way.
            return 60
        elif self.index == 1:
            # $script:1010140307011468$
            # - So far this new land seems like an amazing place, but some of us are having a harder time adjusting than others. $npcName:11004320[gender:0]$'s not acting like himself. Do you think you could offer him some words of encouragement?
            if pick == 0:
                # $script:1010140307011469$
                # - I'll see what I can do.
                return 70
            return -1
        return -1

    def __70(self, pick: int) -> int:
        # $script:1010140307011470$
        # - Thanks! I'm counting on you!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (50, 0):
            return Option.NEXT
        elif (self.state, self.index) == (50, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (60, 0):
            return Option.NEXT
        elif (self.state, self.index) == (60, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (70, 0):
            return Option.CLOSE
        return Option.NONE
