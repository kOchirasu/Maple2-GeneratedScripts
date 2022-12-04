""" 11004381: Puccini """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1109213607011801$
        # - Why does everyone have to get all lovey-dovey for the holidays? It's gross for the rest of us.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1109213607011802$
        # - Why does everyone have to get all lovey-dovey for the holidays? It's gross for the rest of us.
        return -1

    def __40(self, pick: int) -> int:
        # $script:1120173007011874$
        # - Why does everyone have to get all lovey-dovey for the holidays? It's gross for the rest of us.
        if pick == 0:
            # $script:1120173007011875$
            # - Did you see $npcName:11004345[gender:1]$'s family?
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:1120173007011876$
        # - I saw $npcName:11004346[gender:0]$ heading for $map:63000073$ early this morning. He goes there every day, you know. He's always got his face stuffed in a book, ignoring his adorable little sister $npcName:11004345[gender:1]$. I'd never let her get bored... So what's his problem?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        return Option.NONE
