""" 11004522: Friendly Soldieretto """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 50])

    def select(self) -> int:
        return random.choice([0, 40])

    def __0(self, pick: int) -> int:
        # $script:0103163407012492$
        # - Beeep... Beeep...
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0104140207012576$
        # - Beeep... Beeep...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0103163407012493$
        # - Initiating greeting protocol! The weather is nice today, is it not?
        if pick == 0:
            # $script:0103163407012494$
            # - How's your work coming?
            return 20
        return -1

    def __20(self, pick: int) -> int:
        if self.index == 0:
            # $script:0103163407012495$
            # - Initiating reassurance protocol! We soldierettos are doing our best. You can count upon us.
            return 20
        elif self.index == 1:
            # $script:0103163407012496$
            # - Initiating gratitude protocol! We are grateful to the humans who gave us new purpose.
            return 20
        elif self.index == 2:
            # $script:0103163407012497$
            # - Initiating brusque farewell protocol! This time has been very pleasant, but I have over one hundred tasks remaining for today. Please excuse me.
            if pick == 0:
                # $script:0103163407012498$
                # - I'll leave you to it, then.
                return 30
            return -1
        return -1

    def __30(self, pick: int) -> int:
        # $script:0103163407012499$
        # - Scanning records on aetherine air brake experiment... Scan complete.
        return -1

    def __50(self, pick: int) -> int:
        # $script:0104140207012577$
        # - Initiating excitement protocols! Oh, I have uncovered records about Vanheim. Archiving now.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (20, 0):
            return Option.NEXT
        elif (self.state, self.index) == (20, 1):
            return Option.NEXT
        elif (self.state, self.index) == (20, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.CLOSE
        return Option.NONE
