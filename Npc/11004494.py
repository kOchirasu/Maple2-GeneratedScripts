""" 11004494: Pusilla """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1227192907012354$
        # - This place was a dense forest when we first got here...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1227192907012355$
        # - This place was a dense forest when we first got here...
        if pick == 0:
            # $script:1227192907012356$
            # - What happened?
            return 11
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012357$
            # - We set up camp just a day after the Daemon Army arrived. This is all that's left of the forest. The stream is totally dead now, too.
            return 11
        elif self.index == 1:
            # $script:1227192907012358$
            # - We've seen this kind of rapid transformation before. In the Land of Darkness...
            return 11
        elif self.index == 2:
            # $script:1227192907012359$
            # - As the Daemon Army expands, this massive die-off of nature will follow.
            if pick == 0:
                # $script:0114164507012725$
                # - That's bad news.
                return 12
            return -1
        return -1

    def __12(self, pick: int) -> int:
        # $script:0114164607012725$
        # - We need to stop them before they spread any further.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.NEXT
        elif (self.state, self.index) == (11, 1):
            return Option.NEXT
        elif (self.state, self.index) == (11, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.CLOSE
        return Option.NONE
