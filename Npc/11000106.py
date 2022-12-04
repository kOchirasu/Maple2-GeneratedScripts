""" 11000106: Cecilia """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40, 50])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000433$
        # - What?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000436$
        # - Don't talk to me.
        return -1

    def __40(self, pick: int) -> int:
        # $script:0831180407000437$
        # - Eww. Stranger danger!
        return -1

    def __50(self, pick: int) -> int:
        if self.index == 0:
            # $script:1215101207009666$
            # - What?
            return 50
        elif self.index == 1:
            # $script:1215101207009667$
            # - Don't talk to me.
            if pick == 0:
                # $script:1215101207009668$
                # - What can you tell me about trading airships?
                return 51
            return -1
        return -1

    def __51(self, pick: int) -> int:
        # $script:1215101207009669$
        # - Airships? I don't know anything about that.
        if pick == 0:
            # $script:1215101207009670$
            # - Are you sure you haven't heard <i>ANYTHING</i>?
            return 52
        return -1

    def __52(self, pick: int) -> int:
        # $script:1215101207009671$
        # - Ugh, how annoying. That weird guy from earlier was asking the same questions.
        if pick == 0:
            # $script:1215101207009672$
            # - I'm going to keep bothering you until you talk to me...
            return 53
        return -1

    def __53(self, pick: int) -> int:
        if self.index == 0:
            # $script:1215101207009673$
            # - Ugh! Fine! There are some rumors flying around about airships going missing, but I don't remember any of the details because they were boring. 
            return 53
        elif self.index == 1:
            # $script:1215101207009674$
            # - I don't even know if they're the same airships you're talking about, just that some have supposedly gone missing. There, are you happy?
            if pick == 0:
                # $script:1215101207009675$
                # - Thanks. You've been a <i>biiig</i> help.
                return 54
            return -1
        return -1

    def __54(self, pick: int) -> int:
        # $script:1215101207009676$
        # - Don't act like we're friends now.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.NEXT
        elif (self.state, self.index) == (50, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (51, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (52, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (53, 0):
            return Option.NEXT
        elif (self.state, self.index) == (53, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (54, 0):
            return Option.CLOSE
        return Option.NONE
