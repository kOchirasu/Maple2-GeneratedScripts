""" 11004221: Agent S """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806222707010788$
        # - I can't really talk right now.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806222707010789$
        # - Can't talk, secret mission. I told $npc:11004220[gender:0]$ to meet right here by the balloons. Where is he? You don't think <i>they</i> got to him first, do you...?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
