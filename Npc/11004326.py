""" 11004326: Manager """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1010140307011506$
        # - Never thought I'd wind up in a place like this...
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:1010140307011507$
            # - Keep your distance, chump!
            return 10
        elif self.index == 1:
            # $script:1010140307011508$
            # - Hold on. You're one of those Sky Fortress people. Sorry, I thought you were another stalker.
            if pick == 0:
                # $script:1010140307011509$
                # - Why is $npcName:11004325[gender:0]$ here, anyway?
                return 20
            return -1
        return -1

    def __20(self, pick: int) -> int:
        if self.index == 0:
            # $script:1010140307011510$
            # - About that... Come closer, okay? I don't want to exactly shout this out.
            return 20
        elif self.index == 1:
            # $script:1010140307011511$
            # - $npcName:11004325[gender:0]$ isn't so popular these days. He's getting a little old for the gig, and there's lots of hot young talent in the idol game.
            return 20
        elif self.index == 2:
            # $script:1010140307011512$
            # - Some stars are able to keep working into their old age. But these stars can compose and write their own songs. $npcName:11004325[gender:0]$ can't do neither.
            return 20
        elif self.index == 3:
            # $script:1010140307011513$
            # - But my boy here heard about this strange new land and thought he might take a vacation to find his muse.
            return 20
        elif self.index == 4:
            # $script:1010140307011514$
            # - He wouldn't take no for an answer. Lucky for us, the president of his fan club has an in with Sky Fortress and we were able to hitch a ride.
            if pick == 0:
                # $script:1010140307011515$
                # - Who's this fan club president?
                return 30
            return -1
        return -1

    def __30(self, pick: int) -> int:
        # $script:1010140307011516$
        # - I can't exactly say. Confidentiality, you see. But between you and me, she's pretty high up in the Sky Fortress food chain, if you catch my drift.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (20, 0):
            return Option.NEXT
        elif (self.state, self.index) == (20, 1):
            return Option.NEXT
        elif (self.state, self.index) == (20, 2):
            return Option.NEXT
        elif (self.state, self.index) == (20, 3):
            return Option.NEXT
        elif (self.state, self.index) == (20, 4):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
