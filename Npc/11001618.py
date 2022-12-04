""" 11001618: Wei Hong """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0516130207006121$
        # - What brings you here?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0531170907006264$
        # - You have something to say to me?
        if pick == 0:
            # $script:0531170907006265$
            # - The people your thugs took, are they safe?
            return 20
        return -1

    def __20(self, pick: int) -> int:
        if self.index == 0:
            # $script:0531170907006266$
            # - Who knows? The poor idiots are probably locked up somewhere. They don't respect the first rule of the streets: you give back as much as you take. Blackstar wants to make 'em pay up their fair share, that's all.
            return 20
        elif self.index == 1:
            # $script:0531170907006267$
            # - Why do you care, anyway? You friends with one of those vagrants?
            if pick == 0:
                # $script:0531170907006268$
                # - Their friends asked me to look into their disappearances.
                return 30
            return -1
        return -1

    def __30(self, pick: int) -> int:
        # $script:0531170907006269$
        # - Sticking your nose into matters that don't concern you, eh? That's a special kind of stupid. I'd say they better be paying you a fortune, but any friend of those deadbeats wouldn't have two mesos to rub together.
        if pick == 0:
            # $script:0531170907006270$
            # - I'm not in this for the money.
            return 40
        return -1

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:0531170907006271$
            # - <font color="#909090">($npc:11001623[gender:0]$ squints at you in disbelief.)</font>
            #   You don't know them and you don't care about getting paid?
            return 40
        elif self.index == 1:
            # $script:0531170907006272$
            # - You're one of those hero-types. That's fine with me. Go off and get yourself killed. One less idiot to get in my way.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (20, 0):
            return Option.NEXT
        elif (self.state, self.index) == (20, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.CLOSE
        return Option.NONE
