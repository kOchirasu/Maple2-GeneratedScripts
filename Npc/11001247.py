""" 11001247: Rejan """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1125194807004500$
        # - Hm? You're awake!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1125194807004503$
        # - Five of the Eight Blades have betrayed us. Are we sure we can trust the remaining three?
        if pick == 0:
            # $script:1205185107004725$
            # - Who are the remaining three Blades?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:1205185107004726$
        # - If you can't remember that, maybe you're in worse shape than I thought... There's $npcName:11001246[gender:0]$, your teacher, $npcName:11001230[gender:0]$, the current leader of Terrun Calibre, and Vaharin, who's been missing for a pretty long while.
        if pick == 0:
            # $script:1205185107004727$
            # - And the five turncoat Blades?
            return 32
        return -1

    def __32(self, pick: int) -> int:
        # $script:1205185107004728$
        # - Well, there's my teacher and Arazaad's murderer, $npcName:11001231[gender:0]$, and his sworn brothers Zurile, Dalt, Kirisika, and Kahm. They're all in Jibricia and have very little love for the Pelgia sect.
        if pick == 0:
            # $script:1205185107004729$
            # - Is their association with Jibricia a problem?
            return 33
        return -1

    def __33(self, pick: int) -> int:
        # $script:1205185107004730$
        # - You really are your teacher's student, aren't you? While $npcName:11001246[gender:0]$ has always argued in favor of a strong, united Terrun Calibre, it's always seemed most Runeblades disagree with him, and this recent turn of events proves it.
        return -1

    def __34(self, pick: int) -> int:
        # $script:1205185107004731$
        # - The man that $npcName:11001231[gender:0]$ killed was both the leader of the Pelgia sect and Terrun Calibre as a whole. While not all of the Jibricia have turned against us entirely turned against us, his actions have us teetering on the edge of civil war.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (33, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (34, 0):
            return Option.CLOSE
        return Option.NONE
