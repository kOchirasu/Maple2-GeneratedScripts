""" 11001730: Informant B """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0728022507006975$
        # - I'm here!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0804172407007060$
        # - I've been waiting for you!
        if pick == 0:
            # $script:0804172407007061$
            # - Why are you here?
            return 40
        elif pick == 1:
            # $script:0804172407007062$
            # - See anything interesting lately?
            return 41
        return -1

    def __40(self, pick: int) -> int:
        # $script:0804172407007063$
        # - Heh heh... Most humans can't comprehend the importance of my work here. Don't look down on me just 'cause I'm small!
        return -1

    def __41(self, pick: int) -> int:
        # $script:0804172407007064$
        # - But I can tell that you're more sensible then the other humans. You value meerkat ingenuity, yes? Not a thing happens here that we don't see.
        if pick == 0:
            # $script:0804172407007065$
            # - So, what have you seen lately?
            return 42
        return -1

    def __42(self, pick: int) -> int:
        # $script:0804172407007066$
        # - All kinds of people come through here, raising all sorts of ruckus. Sometimes they make angry noises at us because they can't get their security deposits back. Once time, I saw the guards drag away a human male because he wouldn't leave the pretty human female.
        if pick == 0:
            # $script:0804172407007067$
            # - $male:Which pretty human female?,female:You mean me?$
            return 43
        return -1

    def __43(self, pick: int) -> int:
        # $script:0804172407007068$
        # - $male:Lessee...,female:Nuh-uh!$ $npcName:11000515[gender:1]$. You know her? You better steer clear. She's pretty, but she's got thorns!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (41, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (42, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (43, 0):
            return Option.CLOSE
        return Option.NONE
