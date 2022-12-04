""" 11004263: The Sea Siren """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0911203207011182$
        # - <font color="#909090">(You see a large ship, which looks like it drifted here long, long ago.)</font>
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0911203207011183$
            # - <font color="#909090">(You see a large ship, which looks like it drifted here long, long ago.)</font>
            return 10
        elif self.index == 1:
            # $script:0911203207011184$
            # - <font color="#909090">(Its name is written on the side, faded by age and the elements. "The Sea Siren," it says. Then, in smaller text, "Fairy of the seas, protect our way.")</font>
            return 10
        elif self.index == 2:
            # $script:0911203207011185$
            # - <font color="#909090">(Scattered chests litter the area, and you spy some items not native to Karkar. It must have been a merchant vessel.)</font>
            return 10
        elif self.index == 3:
            # $script:0911203207011186$
            # - <font color="#909090">(Amidst the upheaval, you notice a large deformation on the side of the ship... and broken bones everywhere.)</font>
            return 10
        elif self.index == 4:
            # $script:0911203207011187$
            # - <font color="#909090">(Could some terrible creature of the seas have caused all this mayhem and destruction?)</font>
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.NEXT
        elif (self.state, self.index) == (10, 2):
            return Option.NEXT
        elif (self.state, self.index) == (10, 3):
            return Option.NEXT
        elif (self.state, self.index) == (10, 4):
            return Option.CLOSE
        return Option.NONE
