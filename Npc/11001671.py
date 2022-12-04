""" 11001671: Junta """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0711210007006721$
        # - You have something to say to me?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0727223007006884$
        # - If you have something to say, just say it.
        if pick == 0:
            # $script:0727223007006885$
            # - Where have you been?
            return 40
        elif pick == 1:
            # $script:0727223007006886$
            # - You're hurt.
            return 50
        elif pick == 2:
            # $script:0727223007006887$
            # - What are these shadows?
            return 60
        return -1

    def __40(self, pick: int) -> int:
        # $script:0727223007006888$
        # - As I said, I saw one of those creatures while checking on the barrier stones. It led me into a trap, which took time to get myself out of. Do not worry... those who laid the trap will be laying no others.
        if pick == 0:
            # $script:0727233607006924$
            # - Let's talk about something else.
            return 30
        return -1

    def __50(self, pick: int) -> int:
        # $script:0727223007006889$
        # - Do not presume to tell me my business! I am the first student of Guidance, and those frail things could hardly lay a... a... whatever they have on me!
        if pick == 0:
            # $script:0727233607006925$
            # - Let's talk about something else.
            return 30
        return -1

    def __60(self, pick: int) -> int:
        # $script:0727223007006890$
        # - I have no idea. They aren't of nature, that much is obvious. And they are organized. Someone is behind this...
        if pick == 0:
            # $script:0727233607006926$
            # - Let's talk about something else.
            return 30
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (60, 0):
            return Option.SELECTABLE_DISTRACTOR
        return Option.NONE
