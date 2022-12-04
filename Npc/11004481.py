""" 11004481: Macrandra """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1227192907012212$
        # - Hm? I didn't expect to see anyone outside the safety of the outpost.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1227192907012213$
        # - Hm? I didn't expect to see anyone outside the safety of the outpost.
        if pick == 0:
            # $script:1227192907012214$
            # - What are you doing here?
            return 11
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012215$
            # - Oh, well I was sent out to look for aetherine samples, but I found this weird machine. I'm pretty sure it's related to aetherine somehow, but I haven't quite worked it out.
            return 11
        elif self.index == 1:
            # $script:1227192907012216$
            # - It's weak, but that ring is drawing aetherine power into its center. I took some initial scans, and I think it's actually capable of storing vast amounts of the stuff.
            if pick == 0:
                # $script:1227192907012217$
                # - That's strange.
                return 12
            return -1
        return -1

    def __12(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012218$
            # - Isn't it? But I have theories!
            return 12
        elif self.index == 1:
            # $script:1227192907012219$
            # - Based on the data I've collected so far, I have two ideas. Either this device is gathering aetherine and transporting it somewhere...
            return 12
        elif self.index == 2:
            # $script:1227192907012220$
            # - Or it's a dimensional portal that's connected to a place far, far away.
            return 12
        elif self.index == 3:
            # $script:1227192907012221$
            # - What kind of people live here, that they can make all this wild technology?
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.NEXT
        elif (self.state, self.index) == (11, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.NEXT
        elif (self.state, self.index) == (12, 1):
            return Option.NEXT
        elif (self.state, self.index) == (12, 2):
            return Option.NEXT
        elif (self.state, self.index) == (12, 3):
            return Option.CLOSE
        return Option.NONE
