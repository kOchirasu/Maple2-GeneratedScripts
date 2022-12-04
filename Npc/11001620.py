""" 11001620: Jayce """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0516130207006123$
        # - Can I help you?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0531170907006273$
        # - Was there something you wanted to ask me?
        if pick == 0:
            # $script:0531170907006274$
            # - Tell me about the champion of $map:63000020$.
            return 20
        return -1

    def __20(self, pick: int) -> int:
        # $script:0531170907006275$
        # - $npcName:11001547[gender:0]$ is the champion and public face of $map:63000020$. Over the course of his career here, he's had 47 wins, zero losses, and one tie.
        if pick == 0:
            # $script:0607145407006338$
            # - Zero losses?
            return 30
        return -1

    def __30(self, pick: int) -> int:
        # $script:0531170907006276$
        # - His fights always end the same way: a single punch and his opponent is out like a light. He's built like a tank and moves like a panther. It's no wonder the crowds love him.
        if pick == 0:
            # $script:0531170907006277$
            # - You mentioned a tie.
            return 40
        return -1

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:0531170907006278$
            # - Yes, he tied. Once. His opponent wasn't even human—it was one of those animal men. He used a very strange technique in the ring. It almost looked like magic.
            return 40
        elif self.index == 1:
            # $script:0531170907006279$
            # - $map:63000020$ had never seen anything like him, and we haven't again since. Even $npcName:11001547[gender:0]$ was impressed.
            return 40
        elif self.index == 2:
            # $script:0531170907006280$
            # - The challenger left as soon as the match was over, mumbling something about being "pleased with the results of his training." What was his name again...?
            return 40
        elif self.index == 3:
            # $script:0531173507006320$
            # - Ah, that's right! The challenger's name was Junta. And that's everything I know about him.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (20, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.NEXT
        elif (self.state, self.index) == (40, 2):
            return Option.NEXT
        elif (self.state, self.index) == (40, 3):
            return Option.CLOSE
        return Option.NONE
