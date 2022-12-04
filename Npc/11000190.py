""" 11000190: Mr. Hofmann """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000837$
        # - What brings you here?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000840$
        # - Do you know what's good about these black pine mushrooms?
        if pick == 0:
            # $script:0831180407000841$
            # - Nope.
            return 31
        elif pick == 1:
            # $script:0831180407000842$
            # - I don't really care.
            return 32
        return -1

    def __31(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000843$
            # - Of course you don't. I'm sure you haven't seen them before, either. They're that rare. They're good for... Good for... 
            return 31
        elif self.index == 1:
            # $script:0831180407000844$
            # - Ah... Mm... I can't remember all of a sudden. I've been so forgetful lately. I don't know what's wrong with me. 
            return -1
        return -1

    def __32(self, pick: int) -> int:
        # $script:0831180407000845$
        # - Is... that so? Well, I guess young folks like you usually don't take much interest in herbs, but... This is embarrassing. Ha ha ha.
        return -1

    def __40(self, pick: int) -> int:
        # $script:0831180407000846$
        # - Do you have a house?
        if pick == 0:
            # $script:0831180407000847$
            # - Yes.
            return 41
        elif pick == 1:
            # $script:0831180407000848$
            # - No.
            return 44
        return -1

    def __41(self, pick: int) -> int:
        # $script:0831180407000849$
        # - Are you comfortable in your home?
        if pick == 0:
            # $script:0831180407000850$
            # - Yeah.
            return 42
        elif pick == 1:
            # $script:0831180407000851$
            # - No.
            return 43
        return -1

    def __42(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000852$
            # - I see. Good for you. I've got a house, too. And a wife and children. But I'm not comfortable in my own home.
            return 42
        elif self.index == 1:
            # $script:0831180407000853$
            # - My sons never listen. They run wild all the time, screaming and fighting. And my wife nags at me all day long. At home, I can't rest for even a moment.
            return -1
        return -1

    def __43(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000854$
            # - I see. You're just like me then. I'm not comfortable in my own home either.
            return 43
        elif self.index == 1:
            # $script:0831180407000855$
            # - My sons never listen. They run wild all the time, screaming and fighting. And my wife nags at me all day long. At home, I can't rest for even a moment.
            return -1
        return -1

    def __44(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000856$
            # - I see. I've got a house. And a wife and children. But I'm not comfortable in my own home.
            return 44
        elif self.index == 1:
            # $script:0831180407000857$
            # - My sons never listen. They run wild all the time, screaming and fighting. And my wife nags at me all day long. At home, I can't rest for even a moment.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.NEXT
        elif (self.state, self.index) == (31, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (42, 0):
            return Option.NEXT
        elif (self.state, self.index) == (42, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (43, 0):
            return Option.NEXT
        elif (self.state, self.index) == (43, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (44, 0):
            return Option.NEXT
        elif (self.state, self.index) == (44, 1):
            return Option.CLOSE
        return Option.NONE
