""" 11004151: Lydia """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806025707010573$
        # - How may I help you?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806025707010574$
        # - $npcName:11004150$, $npcName:11004148$, $npcName:11004149$, and I are here in $map:02000499$ on vacation! Since we all grew up together, we've got some real synergy on the battlefield.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
