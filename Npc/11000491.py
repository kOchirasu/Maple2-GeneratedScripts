""" 11000491: Cathy Catalina """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40, 70, 80])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002150$
        # - Can I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407002153$
        # - Right now, Goldus Group is the biggest company in $map:02000100$, but that'll soon change. I'll be crushing $npcName:11000252[gender:0]$ under my heel before you know it.
        return -1

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407002154$
            # - What? You want to know if I'm single?
            return 40
        elif self.index == 1:
            # $script:0831180407002155$
            # - Hah! I don't need a man. All men are narcissistic, chauvinist pigs. I hate them!
            return -1
        return -1

    def __70(self, pick: int) -> int:
        # $script:0831180407002156$
        # - Can't you see I'm busy? If it's not urgent, then scram.
        return -1

    def __80(self, pick: int) -> int:
        # $script:0831180407002157$
        # - I don't sell anything on credit. I trust money more than I trust people.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (70, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (80, 0):
            return Option.CLOSE
        return Option.NONE
