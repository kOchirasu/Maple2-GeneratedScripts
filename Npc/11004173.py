""" 11004173: Tara """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806025707010608$
        # - Mm?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806025707010609$
        # - Sorry, I've already got a squad. See? There's the guy selling churros, the girl strutting around over there, and that guy shooting finger-guns.  I couldn't ask for better teammates.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
