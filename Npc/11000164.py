""" 11000164: Vale """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000694$
        # - What seems to be the problem?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000697$
        # - Sigh... I knew this was a dangerous job, but I volunteered anyway because it pays twice as much as other jobs I've had. Maybe I shouldn't have taken it, though. I would've been safer hauling fish at the harbor.
        return -1

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000698$
            # - If not for the earthquake, the Royal Road wouldn't have been destroyed and I could've been in $map:02000001$ by now. I'd be done with my delivery, and kicking back while waiting for the court to open.
            return 40
        elif self.index == 1:
            # $script:0831180407000699$
            # - Actually, if the supplies for the court weren't stolen to begin with, the palace wouldn't have needed the replacements in such a hurry. This is a mess.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.CLOSE
        return Option.NONE
