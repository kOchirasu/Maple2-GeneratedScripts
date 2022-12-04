""" 11001630: Vasara Chen """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0516130207006132$
        # - What brings you here?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0531170907006286$
        # - What is it now?
        if pick == 0:
            # $script:0531170907006287$
            # - Did you know about $npcName:11001629[gender:0]$'s plan?
            return 30
        return -1

    def __30(self, pick: int) -> int:
        # $script:0531170907006288$
        # - Not that I think you'll believe me, but no, I didn't. Even if I did know, so what? It's not my job to stop him.
        if pick == 0:
            # $script:0531170907006289$
            # - Then you're no better than $npcName:11001629[gender:0]$.
            return 40
        return -1

    def __40(self, pick: int) -> int:
        # $script:0531170907006290$
        # - Listen. My old man and I don't always see eye to eye, but he built Blackstar from the ground up. You gotta be ruthless to succeed in this town, and he's earned my respect.
        if pick == 0:
            # $script:0531170907006291$
            # - Old man... You're $npcName:11001629[gender:0]$'s son?!
            return 50
        return -1

    def __50(self, pick: int) -> int:
        # $script:0531170907006292$
        # - I didn't tell you? Must've slipped my mind. $npcName:11001630[gender:0]$, son of $npcName:11001629[gender:0]$, at your service.
        if pick == 0:
            # $script:0531170907006293$
            # - Slipped your mind. Sure.
            return 60
        return -1

    def __60(self, pick: int) -> int:
        # $script:0531170907006294$
        # - Hey, where's it written that I have to tell every idiot who stumbles in here who my dad is? Now, get out of my face before I get mad.
        if pick == 0:
            # $script:0531170907006295$
            # - I'm not done with you.
            return 70
        return -1

    def __70(self, pick: int) -> int:
        # $script:0531170907006296$
        # - Me neither. I got a feeling we'll be fighting again real soon. And next time, I'll beat you fair and square. No tricks.
        if pick == 0:
            # $script:0531170907006297$
            # - I'll see you in the ring.
            return 80
        return -1

    def __80(self, pick: int) -> int:
        # $script:0531170907006298$
        # - Count on it.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (60, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (70, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (80, 0):
            return Option.CLOSE
        return Option.NONE
