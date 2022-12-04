""" 11003180: Marco """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0316101907008107$
        # - All's well!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0323170507008126$
        # - You don't look like the usual beach bums we get around here. What do you want?
        if pick == 0:
            # $script:0426090007008442$
            # - I'm part of the caravan escort.
            return 31
        elif pick == 1:
            # $script:0426090007008443$
            # - I'm just passing through.
            return 32
        return -1

    def __31(self, pick: int) -> int:
        # $script:0426090007008444$
        # - You're just in time! Check in with the others in the $map:52000116$ behind me.
        return -1

    def __32(self, pick: int) -> int:
        # $script:0426090007008445$
        # - You're a tourist? Oh, okay. In that case, enjoy your stay. I'm new to this whole guardsman thing, so I wasn't sure what you were up to. Now I know you're cool, so... cool!
        if pick == 0:
            # $script:0426090007008446$
            # - Thank you.
            return 33
        return -1

    def __33(self, pick: int) -> int:
        # $script:0426090007008447$
        # - Just doing my job, $male:sir,female:ma'am$! But it does feel good to be thanked. I wish more folk were like you.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (33, 0):
            return Option.CLOSE
        return Option.NONE
