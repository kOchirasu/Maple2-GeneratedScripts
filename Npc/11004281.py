""" 11004281: Unmarked Sarcophagus """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0911203207011294$
        # - <font color="#909090">(This sarcophagus has no name engraved upon it. Does an ancient lumarigon slumber within?)</font>
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0911203207011295$
            # - <font color="#909090">(This sarcophagus has no name engraved upon it. Does an ancient lumarigon slumber within?)</font>
            return 10
        elif self.index == 1:
            # $script:0913151207011307$
            # - <font color="#909090">(It's covered in a thick layer of dust. Still, the elaborate carvings are the work of a master artisan.)</font>
            return 10
        elif self.index == 2:
            # $script:0913151207011308$
            # - <font color="#909090">(As you gaze upon the sarcophagus, you're overcome by a sudden feeling of melancholy.)</font>
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.NEXT
        elif (self.state, self.index) == (10, 2):
            return Option.CLOSE
        return Option.NONE
