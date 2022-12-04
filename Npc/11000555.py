""" 11000555: Shadow Tombstone """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180610000801$
        # - <font color="#909090">(Someone left a message.)</font>
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180610000806$
        # - <font color="#909090">(There's dark energy billowing and swirling all around this tombstone! It's making it impossible to read the message.)</font>
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
