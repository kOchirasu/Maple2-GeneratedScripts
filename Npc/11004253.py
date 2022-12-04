""" 11004253: Bill """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0829171107010966$
        # - Everything seems fine today, but if those monsters dare to return... I'll show them!
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0829171107010967$
            # - Everything seems fine today, but if those monsters dare to return... I'll show them!
            return 10
        elif self.index == 1:
            # $script:0831140807011005$
            # - I've never seen you around these parts before. You're not up to any funny business, are you?
            if pick == 0:
                # $script:0831140807011006$
                # - Nah, just passing through. What's up with this place anyway?
                return 11
            return -1
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831140807011007$
            # - This place, $map:03000165$, used to be infested with monsters. But it wasn't the castle who cleaned it up, oh no! Let me tell you, it was us folks from the Lumina Liberation Army! And to think, this place didn't even have any roads!
            return 11
        elif self.index == 1:
            # $script:0831140807011008$
            # - We keep the peace here now. Can't rely on those castle folk, you know?
            if pick == 0:
                # $script:0831140807011009$
                # - ...You realize this place is totally infested with violent pig-folk right?
                return 12
            return -1
        return -1

    def __12(self, pick: int) -> int:
        # $script:0831140807011010$
        # - Compared to before, this is nothing! I admit it's still a work in progress, but one day soon we'll be rid of all those monsters!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.NEXT
        elif (self.state, self.index) == (11, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.CLOSE
        return Option.NONE
