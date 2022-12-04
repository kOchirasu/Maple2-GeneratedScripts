""" 11003163: Nelph """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0310134607008074$
        # - Welcome to the $map:52000116$. I am $npcName:11003163[gender:0]$. If you have any questions regarding the caravans, feel free to ask.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0310134607008077$
        # - My job is to make sure $npcName:11000075[gender:1]$ and the other members of the royal family have everything they desire. I'm always busy, but I take pride in my position and my service to $map:02000025$.
        return -1

    def __31(self, pick: int) -> int:
        # $script:0310134607008078$
        # - These matters are not normally my responsibility, of course, but $npcName:11003165[gender:0]$ asked for me personally due to the... sensitive nature.
        return -1

    def __40(self, pick: int) -> int:
        # $script:0310134607008079$
        # - Have you been to $map:02000076$? My mother lives there. I really should visit her, but I've been so busy that I haven't had the time since preparations began. 
        return -1

    def __41(self, pick: int) -> int:
        # $script:0310134607008080$
        # - Once my work here is done, I'll go and visit her first thing! I've been sending her letters, it's just... she can't see. A disease took her eyesight. Sigh... 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        return Option.NONE
