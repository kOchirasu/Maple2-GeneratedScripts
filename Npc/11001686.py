""" 11001686: Zabeth """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0629000607006484$
        # - What're you staring at? You want a piece of me?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0629000607006487$
        # - You need something, go bother $npcName:11001545[gender:0]$ instead. He likes to hear himself talk, and I got real work to do.
        if pick == 0:
            # $script:0706173707006645$
            # - What's your rank in Blackstar?
            return 40
        return -1

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:0706173707006646$
            # - I'm a henchman, plain and simple. $npcName:11001678[gender:0]$ has big ideas about moving up in the organization, but I don't care what they call me as long as I get to bash heads in.
            return 40
        elif self.index == 1:
            # $script:0706173707006647$
            # - Boss. Lackey. It doesn't matter. All that matters is how strong you are. $npcName:11001678[gender:0]$ can try to rise as much as he wants, but he's got a glass jaw. A weakling like him just ain't officer material.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.CLOSE
        return Option.NONE
