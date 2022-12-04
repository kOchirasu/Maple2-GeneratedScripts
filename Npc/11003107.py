""" 11003107: QuietMinds Guild Leader """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0119135307007855$
        # - There's nothing like a glass of something sweet to drink away your stress.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0119135307007858$
        # - Are you stressed out? I formed the QuietMinds guild to help people escape from the many stresses of life.
        if pick == 0:
            # $script:0119135307007859$
            # - I totally want to join your guild!
            return 31
        elif pick == 1:
            # $script:0119135307007860$
            # - Not really my scene, but thanks.
            return 32
        return -1

    def __31(self, pick: int) -> int:
        # $script:0119135307007861$
        # - Oh! I'm sorry, but my guild is already full. Hm... Well, I'm sure I'm not the only one who formed a guild to relax. There has to be another chill guild somewhere. Or you could start your own.
        return -1

    def __32(self, pick: int) -> int:
        # $script:0119135307007862$
        # - Ah, you must be quite content with your life. You're always welcome to visit if you need a place to rest and escape from reality.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        return Option.NONE
