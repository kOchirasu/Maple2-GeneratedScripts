""" 11001403: Racafony """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217025910001349$
        # - Let's see, what else can I do for fun around here?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1223143510001425$
        # - Is there something I can do for you?
        if pick == 0:
            # $script:1223143510001426$
            # - I want to go to <font color="#ffd200">Victoria Island</font>.
            return 31
        elif pick == 1:
            # $script:1223143510001427$
            # - ...
            return 34
        return -1

    def __31(self, pick: int) -> int:
        # $script:1223143510001428$
        # - A-ha, you came to board the <i>Lumiwind</i>! Perfect timing... we're nearly done with maintenance. Did you want to depart right away?
        if pick == 0:
            # $script:1223143510001429$
            # - Yes.
            return 32
        elif pick == 1:
            # $script:1223143510001430$
            # - I'll come back later.
            return 33
        return -1

    def __32(self, pick: int) -> int:
        # functionID=1 
        # $script:1223143510001431$
        # - All right, bon voyage!
        return -1

    def __33(self, pick: int) -> int:
        # $script:1223143510001432$
        # - Huh? So you don't want to fly? Okay. Well, let me know if you change your mind.
        return -1

    def __34(self, pick: int) -> int:
        # $script:1223143510001433$
        # - Let me know if I can help.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (33, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (34, 0):
            return Option.CLOSE
        return Option.NONE
