""" 11003504: Wooji """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0816160115008990$
        # - What is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0816160115008993$
        # - There are lots of hungry $itemPlural:61000002$ here. I'm here to capture one as a pet.
        if pick == 0:
            # $script:0816160115008994$
            # - Who's your little friend?
            return 31
        elif pick == 1:
            # $script:0816160115008995$
            # - Did you come here alone?
            return 32
        return -1

    def __31(self, pick: int) -> int:
        # $script:0816160115008996$
        # - This is my $item:61000005$. We're traveling together. Say hello, $item:61000005$.
        if pick == 0:
            # $script:0816160115008997$
            # - Hello, Duckling.
            return 34
        elif pick == 1:
            # $script:0816160115008998$
            # - Why are you traveling with a duckling?
            return 35
        return -1

    def __32(self, pick: int) -> int:
        # $script:0816160115008999$
        # - No, it's just me and my $item:61000005$ on the open road! Though I did bump into my childhood friend $npcName:11003506[gender:1]$. Small world, isn't it?
        return -1

    def __34(self, pick: int) -> int:
        # $script:0816160115009000$
        # - I guess my little $item:61000005$ is feeling shy.
        return -1

    def __35(self, pick: int) -> int:
        # $script:0816160115009001$
        # - $item:61000005$ and I are training. I'm going to be a great pet master someday!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (34, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (35, 0):
            return Option.CLOSE
        return Option.NONE
