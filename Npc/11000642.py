""" 11000642: Prisoner 150124 """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([40, 50])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002617$
        # - Did you call me?
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180407002621$
        # - I know all the guards, and you ain't one of them.
        if pick == 0:
            # $script:0831180407002622$
            # - How did you end up in here?
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:0831180407002623$
        # - I made a T-shirt with a sexy picture on it, so what? That's not a crime!
        return -1

    def __50(self, pick: int) -> int:
        # $script:1210061907004906$
        # - I know all the guards, and you ain't one of them.
        if pick == 0:
            # $script:1210061907004907$
            # - Do you know someone named $npcName:11001231[gender:0]$?
            return 51
        return -1

    def __51(self, pick: int) -> int:
        # $script:1210061907004908$
        # - What's it to you?
        #   <font color="#909090">(He narrows his eyes at you.)</font>
        if pick == 0:
            # $script:1210061907004909$
            # - I'm working with him.
            return 52
        return -1

    def __52(self, pick: int) -> int:
        # $script:1210061907004910$
        # - Hm... Yeah, you don't look like no ordinary tourist. Tell him not to worry. Everything's right on schedule.
        if pick == 0:
            # $script:1210061907004911$
            # - I need to see the supervisor.
            return 53
        return -1

    def __53(self, pick: int) -> int:
        # $script:1210061907004912$
        # - Yeah, yeah, sure. That's $npcName:11000651[gender:0]$. But he won't talk to you unless you know the password.
        if pick == 0:
            # $script:1210061907004913$
            # - What's the password?
            return 54
        return -1

    def __54(self, pick: int) -> int:
        if self.index == 0:
            # $script:1210061907004914$
            # - Hold your horses. I wrote it down somewhere...
            return 54
        elif self.index == 1:
            # $script:1210061907004915$
            # - Here we go. "Thick shadows have been cast..." ...something something... "...illuminate light..." Dang, who smudged up the password?
            return 54
        elif self.index == 2:
            # $script:1210061907004916$
            # - Sorry, $male:buddy,female:lady$. You got to get the rest from someone else.
            if pick == 0:
                # $script:1214232607004979$
                # - Why can't I just talk to the supervisor?
                return 55
            return -1
        return -1

    def __55(self, pick: int) -> int:
        # $script:1214232607004980$
        # - Listen, the supervisor won't even talk to <i>me</i> without the password. You don't stand a chance without it.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (51, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (52, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (53, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (54, 0):
            return Option.NEXT
        elif (self.state, self.index) == (54, 1):
            return Option.NEXT
        elif (self.state, self.index) == (54, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (55, 0):
            return Option.CLOSE
        return Option.NONE
