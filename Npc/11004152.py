""" 11004152: Tina """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806025707010575$
        # - Can I help you?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806025707010576$
        # - The scenery here is breathtaking, but if you want the best view in $map:02000499$, you should try hanging from $npcName:11004165$.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
