""" 11000201: Noel """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000874$
        # - Hello.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000877$
        # - Hey $male:mister,female:lady$, do you want to play with us too? I have to play while I can. My mom will be here soon to pick me up.
        return -1

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000878$
            # - I can't believe how big this field is! The sunlight stings a little bit, but Mom said a little sun is good for you.
            return 40
        elif self.index == 1:
            # $script:0831180407000879$
            # - $map:02000023$ is nice and shady. Neal's going to come over to my house later. $male:Mister,female:Lady$, do you want to come?
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
