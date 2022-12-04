""" 11000185: Ms. Kim """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 50

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000773$
        # - Can I help you?
        return None # TODO

    def __50(self, pick: int) -> int:
        # $script:0831180407000778$
        # - $map:2000123$. How may I help you?
        if pick == 0:
            # $script:0831180407000781$
            # - What's been happening lately?
            return 53
        elif pick == 1:
            # $script:0831180407000782$
            # - I was wondering how you're doing.
            return 54
        return -1

    def __53(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000799$
            # - You mean the news? If I had good information, do you think I'd share it with you?
            return 53
        elif self.index == 1:
            # $script:0831180407000800$
            # - Well, I would. Instead of seeking immediate gains, I invest for the future. That's my philosophy.
            return 53
        elif self.index == 2:
            # $script:0831180407000801$
            # - Money or trust... which do you think is better for me in the long run? Heh, I'm still weighing my options.
            return -1
        return -1

    def __54(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000805$
            # - What is this? Are you hitting on me? I'm sorry, but I don't answer questions that have nothing to do with my work.
            return 54
        elif self.index == 1:
            # $script:0831180407000806$
            # - I'm aware of the rumors about me. One of them says I'm divorced. Another says I'm a widow. 
            return 54
        elif self.index == 2:
            # $script:0831180407000807$
            # - Some even say I'm the only daughter of Chairman Goldus. Ha, geez...
            return 54
        elif self.index == 3:
            # $script:0831180407000808$
            # - I refuse to be gossip fodder. Don't these people have anything better to do with their lives?
            return 54
        elif self.index == 4:
            # $script:0831180407000809$
            # - I'm sorry... I got carried away for a moment. Now, if you'll excuse me, I have developments to inspect.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (53, 0):
            return Option.NEXT
        elif (self.state, self.index) == (53, 1):
            return Option.NEXT
        elif (self.state, self.index) == (53, 2):
            return Option.CLOSE
        elif (self.state, self.index) == (54, 0):
            return Option.NEXT
        elif (self.state, self.index) == (54, 1):
            return Option.NEXT
        elif (self.state, self.index) == (54, 2):
            return Option.NEXT
        elif (self.state, self.index) == (54, 3):
            return Option.NEXT
        elif (self.state, self.index) == (54, 4):
            return Option.CLOSE
        return Option.NONE
