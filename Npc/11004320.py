""" 11004320: Dunba """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 30])

    def select(self) -> int:
        return random.choice([0, 20])

    def __0(self, pick: int) -> int:
        # $script:1102172107011623$
        # - This place is super weird...
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:1010140307011449$
        # - This place is super weird...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1102172107011624$
        # - I don't like this place... It's new and scary...
        return -1

    def __30(self, pick: int) -> int:
        # $script:1010140307011450$
        # - Ahh! You scared me!
        if pick == 0:
            # $script:1010140307011451$
            # - What's gotten into you?
            return 40
        return -1

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:1010140307011452$
            # - Oh... It's only you. Phew.
            return 40
        elif self.index == 1:
            # $script:1010140307011453$
            # - This place has me on edge. Everything's so different.
            return 40
        elif self.index == 2:
            # $script:1010140307011454$
            # - It seems like I'm the only one having any trouble fitting in. $npcName:11004322[gender:0]$ is so absorbed in his search for new ingredients. And it seems like $npcName:11004321[gender:1]$ has run out of all patience for me... Sniff.
            return 40
        elif self.index == 3:
            # $script:1010140307011455$
            # - I want to be of help tracking down traces of the dragons, but I'm just so anxious. I should've just stayed home.
            if pick == 0:
                # $script:1010140307011456$
                # - That's crazy! I'm sure your friends are glad to have you here.
                return 50
            return -1
        return -1

    def __50(self, pick: int) -> int:
        # $script:1010140307011457$
        # - You really think so? Thanks... That means a lot. I'm sure I can muster up the courage to keep going.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.NEXT
        elif (self.state, self.index) == (40, 2):
            return Option.NEXT
        elif (self.state, self.index) == (40, 3):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (50, 0):
            return Option.CLOSE
        return Option.NONE
