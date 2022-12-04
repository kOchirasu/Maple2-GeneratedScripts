""" 11200005: Shuenji """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0518100907008515$
        # - The guild could use your help. You will be compensated!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0518100907008518$
        # - Complete this simple task, and you will get guild experience, funds, and some experience for yourself, too! Note that you can't start daily quests until you've been in the guild for a day, and you can't start weekly quests until you've been in the guild for a week.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
