""" 11004313: Condor """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0928133807011352$
        # - Back in my day, we knew a thing or two about duty!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0928133807011353$
        # - I'm here, but most of my men are tied up defending Victoria Island. I hate being benched!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
