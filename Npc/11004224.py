""" 11004224: Richelle """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806222707010796$
        # - Can I help you?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806222707010797$
        # - Hey, thanks for listening! We're Riot at the Danceclub. We all met during an audition and decided to form a band, kindred spirits and all that. We picked stage names to riff off the band name.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
