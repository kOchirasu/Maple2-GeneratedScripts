""" 11003503: Ranshu """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40, 50])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0816160115008986$
        # - What is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0816160115008987$
        # - The Team Mushroom has people all over the world. You'll find them wherever you find monsters!
        return -1

    def __40(self, pick: int) -> int:
        # $script:0816160115008988$
        # - Team Mushroom and Dryad Co. don't have much in common. Dryad sells the tools of the pet-taming trade. Team Mushroom is working to protect the world from devastation, and unite all peoples across the nation!
        return -1

    def __50(self, pick: int) -> int:
        # $script:0816160115008989$
        # - I work alone, but I'll be in need of a partner in the future.
        if pick == 0:
            # $script:0816211715009063$
            # - What about me?
            # TODO: goto 51,52
            self.close()
            return -1
        return -1

    def __51(self, pick: int) -> int:
        # $script:0816211715009064$
        # - Hey... Are you serious...?
        return -1

    def __52(self, pick: int) -> int:
        # $script:0816211715009065$
        # - Not right now. But... maybe later.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (51, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (52, 0):
            return Option.CLOSE
        return Option.NONE
