""" 11003254: Kaitlyn """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0403155707008175$
        # - What is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0403155707008176$
            # - I don't know what you did to impress $npcName:11003250[gender:0]$, but I'm not convinced. So, how are you going to prove that you're worth my time? 
            return 30
        elif self.index == 1:
            # $script:0403155707008177$
            # - <font color="#909090">($npc:11003254[gender:1]$'s voice drops to a whisper.)</font>
            #   <font size='20'>This is all for Professor $npc:11003148[gender:0]$...</font>
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.CLOSE
        return Option.NONE
