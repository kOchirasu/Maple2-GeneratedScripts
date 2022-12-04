""" 11003533: Veliche """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1126155107011958$
        # - The future is in our hands.
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:1126155107011959$
        # - Speak. I'm listening.
        if pick == 0:
            # $script:1126155107011960$
            # - Tell me about Tria's navy.
            return 31
        return -1

    def __31(self, pick: int) -> int:
        if self.index == 0:
            # $script:1126155107011961$
            # - After all this time, you haven't seen the famous navy of Tria?
            return 31
        elif self.index == 1:
            # $script:1126155107011962$
            # - I suppose that's not unreasonable. Tria's navy isn't in Tria at the moment, after all.
            return 31
        elif self.index == 2:
            # $script:1126155107011963$
            # - A few months before the empress's grand court, the main fleet was dispatched to an island far away. Not even I know where the command came from.
            return 31
        elif self.index == 3:
            # $script:1126155107011964$
            # - Fa—I mean, Admiral Martini didn't even take the time to tell me about the mission. They simply set sail, leaving myself and a few petty officers to command a skeleton fleet.
            return 31
        elif self.index == 4:
            # $script:1126155107011965$
            # - They don't appear on Sky Fortress's radar, either. I'm not sure what to make of the bulk of our military vanishing at a time like this...
            return 31
        elif self.index == 5:
            # $script:1126155107011966$
            # - I wonder if he's even still alive...
            return 31
        elif self.index == 6:
            # $script:1126155107011967$
            # - I've said too much. You can trust in Tria's naval forces. The entire empire is under my personal protection.
            return -1
        return -1

    def __40(self, pick: int) -> int:
        # $script:1126155107011968$
        # - Prove yourself to my officers, and I'll consider entrusting you with a mission for the Maple Alliance.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.NEXT
        elif (self.state, self.index) == (31, 1):
            return Option.NEXT
        elif (self.state, self.index) == (31, 2):
            return Option.NEXT
        elif (self.state, self.index) == (31, 3):
            return Option.NEXT
        elif (self.state, self.index) == (31, 4):
            return Option.NEXT
        elif (self.state, self.index) == (31, 5):
            return Option.NEXT
        elif (self.state, self.index) == (31, 6):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
