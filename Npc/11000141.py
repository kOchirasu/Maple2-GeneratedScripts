""" 11000141: Morren """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000571$
        # - Can I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000574$
        # - Whoever you are, please help me! My... My boss was taken by them. Please save him!
        if pick == 0:
            # $script:0831180407000575$
            # - Don't worry, I'll save him.
            return 31
        return -1

    def __31(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000576$
            # - Thank you so much! I'm here alone and I didn't know what to do until you came along. I've been watching them, and there's a few things you need to know.
            return 31
        elif self.index == 1:
            # $script:0831180407000577$
            # - First, don't step on the floor sensors marked red. They'll trip the alarm and you'll be in a world of hurt. I think if I hack into their security system, I should be able to turn off the alarm. Hm... 
            return 31
        elif self.index == 2:
            # $script:0831180407000578$
            # - If you beat up a Blackdrake gang foot soldier, they're sure to call a superior for help. I suggest tossing an Energy Bomb at them, and then finishing them off quickly while they're stunned.
            return 31
        elif self.index == 3:
            # $script:0831180407000579$
            # - Please, save my boss!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.NEXT
        elif (self.state, self.index) == (31, 1):
            return Option.NEXT
        elif (self.state, self.index) == (31, 2):
            return Option.NEXT
        elif (self.state, self.index) == (31, 3):
            return Option.CLOSE
        return Option.NONE
