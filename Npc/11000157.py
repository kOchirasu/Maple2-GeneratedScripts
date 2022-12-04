""" 11000157: Paul """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000663$
        # - What seems to be the problem?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407000665$
        # - I don't know what caused the recent earthquake. It was so strong, it tore the Royal Road in half. This could be a serious problem.
        return -1

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0116162507009762$
            # - It's really you! $MyPCName$, in the flesh!
            return 30
        elif self.index == 1:
            # $script:0116162507009763$
            # - It's an honor to meet you!
            if pick == 0:
                # $script:0116162507009764$
                # - You know me?
                return 31
            return -1
        return -1

    def __31(self, pick: int) -> int:
        # $script:0116162507009765$
        # - You're the hero of the Siege of $map:02000001$. Of course I know you! You're a hero to all of us here.
        if pick == 0:
            # $script:0116162507009766$
            # - I was just doing my duty.
            return 32
        return -1

    def __32(self, pick: int) -> int:
        # $script:0116162507009767$
        # - You're so humble. Wow! Listen, if there's anything I can do to help you, just say the word.
        if pick == 0:
            # $script:0116162507009768$
            # - I'm looking into rumors about hot places. Like, super hot.
            return 33
        return -1

    def __33(self, pick: int) -> int:
        # $script:0116162507009769$
        # - Hot places, huh? Like unseasonably hot places?
        if pick == 0:
            # $script:0116162507009770$
            # - That's one example.
            return 34
        return -1

    def __34(self, pick: int) -> int:
        # $script:0116162507009771$
        # - Now that you mention it, I did hear a rumor from one of the merchants with the Barrota Trading Company. You heard about their new air trade routes, didn't you?
        if pick == 0:
            # $script:0116162507009772$
            # - I may have heard a thing or two.
            return 35
        return -1

    def __35(self, pick: int) -> int:
        if self.index == 0:
            # $script:0116162507009773$
            # - Well, a few of their routes pass over the ruins of Orbis. They say that the airships passing through the area get so hot, you can fry an egg on their decks.
            return 35
        elif self.index == 1:
            # $script:0116162507009774$
            # - Interesting, right?
            if pick == 0:
                # $script:0116162507009775$
                # - Fascinating.
                return 36
            return -1
        return -1

    def __36(self, pick: int) -> int:
        # $script:0116170407009788$
        # - That's all I know.
        if pick == 0:
            # $script:0116170407009789$
            # - It was a big help.
            return 37
        return -1

    def __37(self, pick: int) -> int:
        # $script:0116162507009776$
        # - I can't believe <i>I</i> am getting to talk to <i>you</i> about real important official business! Don't worry, $male:sir,female:ma'am$, I'll do my best to keep $map:02000001$ safe, too!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (33, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (34, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (35, 0):
            return Option.NEXT
        elif (self.state, self.index) == (35, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (36, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (37, 0):
            return Option.CLOSE
        return Option.NONE
