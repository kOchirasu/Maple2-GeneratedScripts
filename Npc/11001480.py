""" 11001480: Tara """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0106111607005767$
        # - What?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0106111607005768$
        # - Light and darkness... The war between the Lumarigons and the Kargons isn't over yet.
        #   All hope lies on $npcName:11001472[gender:1]$ recovering soon. She alone can save the Lumarigons.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
