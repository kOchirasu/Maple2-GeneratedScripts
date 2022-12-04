""" 11003788: Nairin """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1213192607009646$
        # - All systems are operational!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1213192607009647$
        # - How may I help you today, $male:Sir,female:Ma'am$?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
