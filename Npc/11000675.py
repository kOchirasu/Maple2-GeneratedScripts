""" 11000675: Khan """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 50

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002743$
        # - What brings you here?
        return None # TODO

    def __50(self, pick: int) -> int:
        # $script:0831180407002744$
        # - Mm? Are you here to challenge me? You can never defeat me, no matter how many times you try. You'd better give up before you get seriously hurt.
        if pick == 0:
            # $script:0831180407002745$
            # - I want to challenge you.
            return 51
        elif pick == 1:
            # $script:0831180407002746$
            # - What's the $map:65000001$?
            return 52
        return -1

    def __51(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407002747$
            # - Heh. Interesting. You challenge the undefeated champion of $map:65000001$, the victor of 47 consecutive matches. Very well. I shall give you what you desire.
            return 51
        elif self.index == 1:
            # $script:0831180407002748$
            # - But not right now. We gladiators fight only inside the ring. That's our rule.
            return 51
        elif self.index == 2:
            # $script:0831180407002749$
            # - As you can also see, I'm quite busy. Perhaps while I attend to my business, you can start to make a name for yourself. Why not go prove your strength at the $map:65000001$?
            return -1
        return -1

    def __52(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407002750$
            # - You must not have heard about the $map:65000001$. All right, I shall do you the honor of hearing $npcName:11000675[gender:0]$'s own explanation. So listen.
            return 52
        elif self.index == 1:
            # $script:0831180407002751$
            # - The $map:65000001$ is a place of battle where up to 10 warriors can take turns battling one on one, until only one remains. The order of their fights is random.
            return 52
        elif self.index == 2:
            # $script:0831180407002752$
            # - Unlucky fighters may be eliminated in their very first match. But those who are truly strong, truly deserving, will triumph over fortune and faith.
            return 52
        elif self.index == 3:
            # $script:0831180407002753$
            # - I should know. I've done it countless times. Now... Do you still want to challenge me?
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (51, 0):
            return Option.NEXT
        elif (self.state, self.index) == (51, 1):
            return Option.NEXT
        elif (self.state, self.index) == (51, 2):
            return Option.CLOSE
        elif (self.state, self.index) == (52, 0):
            return Option.NEXT
        elif (self.state, self.index) == (52, 1):
            return Option.NEXT
        elif (self.state, self.index) == (52, 2):
            return Option.NEXT
        elif (self.state, self.index) == (52, 3):
            return Option.CLOSE
        return Option.NONE
