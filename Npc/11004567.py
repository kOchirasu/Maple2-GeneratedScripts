""" 11004567: Vasara Chen """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0220211107014547$
        # - Really?
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0220211107014548$
            # - Hm?
            return 10
        elif self.index == 1:
            # $script:0220211107014549$
            # - You look strong. Almost as strong as someone I know...
            if pick == 0:
                # $script:0220211107014550$
                # - You're one to talk.
                return 11
            return -1
        return -1

    def __11(self, pick: int) -> int:
        # $script:0220211107014551$
        # - Hey, you ever hear of the Gray Wolf?
        if pick == 0:
            # $script:0220211107014552$
            # - I may have heard the name.
            return 12
        return -1

    def __12(self, pick: int) -> int:
        # $script:0220211107014553$
        # - I have a feeling the Gray Wolf will be here. We've got unfinished business...
        return -1

    def __20(self, pick: int) -> int:
        # $script:0220211107014554$
        # - Hey, Gray Wolf.
        if pick == 0:
            # $script:0220211107014555$
            # - Vasara Chen?
            return 21
        return -1

    def __21(self, pick: int) -> int:
        if self.index == 0:
            # $script:0220211107014556$
            # - I knew you'd be here. A fighter like you can't resist the ring for long.
            return 21
        elif self.index == 1:
            # $script:0220211107014557$
            # - That's why I signed up. Figured it's a good chance for us to duke it out.
            if pick == 0:
                # $script:0220211107014558$
                # - This is getting interesting.
                return 22
            return -1
        return -1

    def __22(self, pick: int) -> int:
        # $script:0220211107014559$
        # - I hope you haven't slacked off in your training. I haven't.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (21, 0):
            return Option.NEXT
        elif (self.state, self.index) == (21, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (22, 0):
            return Option.CLOSE
        return Option.NONE
