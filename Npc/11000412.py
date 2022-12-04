""" 11000412: 50 Meso """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001737$
        # - Wassup?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407001739$
        # - Sup, man? You wanna talk art? What do you think is the soul of art?
        if pick == 0:
            # $script:0831180407001740$
            # - I don't... know?
            return 21
        elif pick == 1:
            # $script:0831180407001741$
            # - Heart
            return 22
        elif pick == 2:
            # $script:0831180407001742$
            # - Talent
            return 23
        elif pick == 3:
            # $script:0831180407001743$
            # - Swag
            return 24
        return -1

    def __21(self, pick: int) -> int:
        # $script:0831180407001744$
        # - Then lemme educate you, man! A real artist uses their tools to show the world their heart. That's the whole point, yo!
        return -1

    def __22(self, pick: int) -> int:
        # $script:0831180407001745$
        # - That's right! You're on point today!
        return -1

    def __23(self, pick: int) -> int:
        # $script:0831180407001746$
        # - Talent? Man, anyone can train up talent. That's not what's important. 
        return -1

    def __24(self, pick: int) -> int:
        # $script:0831180407001747$
        # - Seriously? Man, I don't want to talk to you anymore.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (21, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (22, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (23, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (24, 0):
            return Option.CLOSE
        return Option.NONE
