""" 11000585: Seamus """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        # TODO: Job 1
        # TODO: RandomPick 40
        return 0 # Default

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180610000843$
        # - Ahoy!
        return None # TODO

    def __1(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180610000844$
            # - Welcome to the $map:02000124$ cruise ship!
            return 1
        elif self.index == 1:
            # $script:0831180610000845$
            # - $map:02000124$ is where the worst criminals of all get locked up. We run tours to show the free, law-abiding citizens why they should stay law-abiding.
            return 1
        elif self.index == 2:
            # $script:0831180610000846$
            # - It's <font color="#ffd200">1,000 mesos</font> to take a tour of the prison.
            #   Are you interested?
            return None # TODO
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180610000850$
        # - Hey there! You looking for the cruise ship to $map:02000124$?
        if pick == 0:
            # $script:0831180610000851$
            # - Yep!
            return 41
        elif pick == 1:
            # $script:0831180610000852$
            # - What is $map:02000124$?
            return 42
        return -1

    def __41(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180610000853$
            # - Hey, it's <font color="#ffd200">1,000 mesos</font> to take a tour of the prison. 
            return 41
        elif self.index == 1:
            # $script:0831180610000854$
            # - Looks like you're short on cash. Come on back when you've got it, because this tour is worth the money! You've never seen such suffering, such misery! It builds character.
            return -1
        return -1

    def __42(self, pick: int) -> int:
        # $script:0831180610000855$
        # - $map:02000124$ is where the worst criminals of all get locked up. We run tours to show the free, law-abiding citizens why they should stay law-abiding.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (1, 0):
            return Option.NEXT
        elif (self.state, self.index) == (1, 1):
            return Option.NEXT
        elif (self.state, self.index) == (1, 2):
            return Option.TAKE_BOAT
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.NEXT
        elif (self.state, self.index) == (41, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (42, 0):
            return Option.CLOSE
        return Option.NONE
