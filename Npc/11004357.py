""" 11004357: Evelyn """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1109213607011767$
        # - What a relief.
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:1109213607011768$
            # - Thank you very much for helping us, $MyPCName$.
            return 10
        elif self.index == 1:
            # $script:1120173007011847$
            # - And... forgive $npcName:11004349[gender:0]$. I was the one who messed up, venting my anger in my diary...
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.CLOSE
        return Option.NONE
