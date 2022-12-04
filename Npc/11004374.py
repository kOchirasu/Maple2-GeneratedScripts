""" 11004374: Bobo """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1109213607011785$
        # - You want presents? Hee hee.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1109213607011786$
        # - You want presents? Hee hee.
        if pick == 0:
            # $script:1120173007011859$
            # - Never mind, I don't want it.
            return 11
        elif pick == 1:
            # $script:1120173007011860$
            # - I want it.
            return 12
        return -1

    def __11(self, pick: int) -> int:
        # $script:1120173007011861$
        # - $npcName:11004349[gender:0]$ do better now. $npcName:11004349[gender:0]$ is sad.
        return -1

    def __12(self, pick: int) -> int:
        # $script:1120173007011862$
        # - What want? $npcName:11004349[gender:0]$ do best!
        if pick == 0:
            # $script:1120173007011863$
            # - $npcName:11004349[gender:0]$'s big heart is enough.
            return 13
        elif pick == 1:
            # $script:1120173007011864$
            # - How about a million mesos?
            return 14
        return -1

    def __13(self, pick: int) -> int:
        # $script:1120173007011865$
        # - $MyPCName$... better than Santa! $npcName:11004349[gender:0]$ happy!
        return -1

    def __14(self, pick: int) -> int:
        # $script:1120173007011866$
        # - Sorry... $npcName:11004349[gender:0]$ no money. Sniff... Sorry. Very sorry.
        if pick == 0:
            # $script:1120173007011867$
            # - $npcName:11004349[gender:0]$'s big heart is enough.
            return 13
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (12, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (13, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (14, 0):
            return Option.SELECTABLE_DISTRACTOR
        return Option.NONE
