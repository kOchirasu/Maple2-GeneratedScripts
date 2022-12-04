""" 11000482: Puzroon's Message """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002109$
        # - Judging by the rough handwriting, I think $npcName:11000441[gender:0]$ wrote this note.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180407002110$
        # - Judging by the rough handwriting, I think $npcName:11000441[gender:0]$ wrote this note.
        if pick == 0:
            # $script:0831180407002111$
            # - Check the note about the starting time.
            return 11
        elif pick == 1:
            # $script:0831180407002112$
            # - Check the note about how to play the game.
            return 12
        elif pick == 2:
            # $script:0831180407002113$
            # - Check the note about earning rewards.
            return 13
        return -1

    def __11(self, pick: int) -> int:
        # $script:0831180407002114$
        # - I know these folks aren't just here to see $npcName:11000441[gender:0]$. Don't worry, I'll start the game when we've got enough people.
        return -1

    def __12(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407002115$
            # - Step on the red tile to jump to the center of the cave. Once there, you can step on the blue tile there when you want to leave.
            return 12
        elif self.index == 1:
            # $script:0831180407002116$
            # - When the game begins, the tiles you're standing on will start disappearing. Last as long as you can without falling, and if you're the last one standing, you win! Easy, right?
            return -1
        return -1

    def __13(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407002117$
            # - In addition to mesos, the winners will get a special reward: $npcName:11000441[gender:0]$'s Blessing, which increases their Movement Speed for 15 seconds.
            return 13
        elif self.index == 1:
            # $script:0831180407002118$
            # - Do you want a reward? Then join up and complete the game!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (12, 0):
            return Option.NEXT
        elif (self.state, self.index) == (12, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (13, 0):
            return Option.NEXT
        elif (self.state, self.index) == (13, 1):
            return Option.CLOSE
        return Option.NONE
