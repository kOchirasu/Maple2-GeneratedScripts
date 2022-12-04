""" 11000514: Belma """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([40, 50])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002195$
        # - What brings you here?
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180407002199$
        # - Maybe you don't realize this, but I'm the warden of this prison. I don't take walk-ins.
        if pick == 0:
            # $script:0831180407002200$
            # - I'm here to make amends for my deeds.
            return 41
        elif pick == 1:
            # $script:0831180407002201$
            # - I'm just a tourist!
            return 42
        return -1

    def __41(self, pick: int) -> int:
        # $script:0831180407002202$
        # - All misdeeds must be punished. The punishment must fit the crime, or else we risk the criminal committing their crimes again.
        if pick == 0:
            # $script:0831180407002203$
            # - How can I reduce my sentence?
            return 43
        return -1

    def __42(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407002207$
            # - See the prisoners in here? Remember that you can always end up the same if you fail to heed the law.
            return 42
        elif self.index == 1:
            # $script:0831180407002208$
            # - And that's the reason I have a tourist program here. You could learn a thing or two.
            return -1
        return -1

    def __43(self, pick: int) -> int:
        # $script:0831180407002204$
        # - How bold! You realize I don't issue pardons...
        if pick == 0:
            # $script:0831180407002205$
            # - I'll do anything. ANYTHING.
            return 44
        return -1

    def __44(self, pick: int) -> int:
        # $script:0831180407002206$
        # - Will you, now? Hmm... I like the sound of that. In some cases, hard labor can substitute for time served. How about you pull the weeds in the prison yard? Do a good job, and I'll consider reducing your sentence.
        return -1

    def __50(self, pick: int) -> int:
        # $script:1210061907004881$
        # - Maybe you don't realize this, but I'm the warden of this prison. I don't take walk-ins.
        if pick == 0:
            # $script:1210061907004882$
            # - Do you know someone named $npcName:11001231[gender:0]$?
            return 51
        return -1

    def __51(self, pick: int) -> int:
        # $script:1210061907004883$
        # - Who? You can't expect me to remember every rodent who comes in and out of $map:2000124$.
        if pick == 0:
            # $script:1210061907004884$
            # - Trust me, you'd remember this guy.
            return 52
        return -1

    def __52(self, pick: int) -> int:
        # $script:1210061907004885$
        # - <font color="#909090">(She listens begrudgingly as you describe $npcName:11001231[gender:0]$.)</font>
        #   As a matter of fact, I do remember him. There was something mysterious about the man.
        if pick == 0:
            # $script:1210061907004886$
            # - Do you know why he was here?
            return 53
        return -1

    def __53(self, pick: int) -> int:
        # $script:1210061907004887$
        # - Only two kinds of people come to $map:2000124$: tourists and convicts. Since he's not rotting in one of our cells, I suppose he must have been a tourist.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (42, 0):
            return Option.NEXT
        elif (self.state, self.index) == (42, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (43, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (44, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (51, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (52, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (53, 0):
            return Option.CLOSE
        return Option.NONE
