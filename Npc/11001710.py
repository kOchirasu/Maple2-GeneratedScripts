""" 11001710: Tinchai """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0728022507006962$
        # - Mm?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0728024507006992$
        # - Were your contacts any good this time?
        if pick == 0:
            # $script:0805021607007084$
            # - Your informants are little cuties.
            return 31
        elif pick == 1:
            # $script:0805021607007085$
            # - Is their information reliable?
            return 40
        return -1

    def __31(self, pick: int) -> int:
        # $script:0805021607007086$
        # - I suppose they are! Don't judge them by their looks, though. They've got a knack for gathering information.
        if pick == 0:
            # $script:0805021607007087$
            # - Let's talk about something else.
            return 30
        return -1

    def __40(self, pick: int) -> int:
        # $script:0805021607007088$
        # - I can't think of any reason it wouldn't be. If you're worried, I'll vouch for them personally. They've never failed me in the past.
        if pick == 0:
            # $script:0805021607007089$
            # - Let's talk about something else.
            return 30
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        return Option.NONE
