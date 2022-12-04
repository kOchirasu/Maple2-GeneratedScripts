""" 11001124: Hanu """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0910171307003840$
        # - Did you come to see me?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0915113107003932$
        # - I've been studying artificial intelligence. Androids in particular. Do you think that my androids are capable of thinking like we do?
        if pick == 0:
            # $script:0915113107003933$
            # - I don't see why not.
            return 31
        elif pick == 1:
            # $script:0915113107003934$
            # - I don't think so.
            return 32
        return -1

    def __31(self, pick: int) -> int:
        # $script:0915113107003935$
        # - Haha! I wasn't expecting a real answer. After all, it's a question I struggle with myself.
        return -1

    def __32(self, pick: int) -> int:
        # $script:0915113107003936$
        # - Hmm? You can't just say something like that and leave it at that! Then tell me, what do you think I should do to make my androids as smart as you and me?
        if pick == 0:
            # $script:0915113107003937$
            # - Data isn't enough. They have to learn through experience.
            return 33
        elif pick == 1:
            # $script:0915113107003938$
            # - Just cram them full of as much data as you can.
            return 34
        elif pick == 2:
            # $script:0915113107003939$
            # - (Mumble inaudibly.)
            return 35
        return -1

    def __33(self, pick: int) -> int:
        # $script:0915113107003940$
        # - Don't you think I tried that already? Well, thanks for your input in any case. As a professional in the field of android research, I'm sure I'll come up with a solution on my own.
        return -1

    def __34(self, pick: int) -> int:
        # $script:0915113107003941$
        # - Yes, I've thought much the same. Perhaps if I build a database based on what my androids learn from various stimuli, much as humans learn from their own experience. Thanks for your input, in any case.
        return -1

    def __35(self, pick: int) -> int:
        # $script:0915113107003942$
        # - What? Hmph. I really thought you had something of value to say on the topic. Next time someone asks for your opinion, you should just be honest with them.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (33, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (34, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (35, 0):
            return Option.CLOSE
        return Option.NONE
