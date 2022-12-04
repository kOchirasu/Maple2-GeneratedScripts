""" 11004324: Lennon """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1010140307011492$
        # - What is she thinking?!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1010140307011493$
        # - Sigh. Once $npcName:11004323[gender:1]$ sets her mind to something, there's little hope of changing it.
        if pick == 0:
            # $script:1010140307011494$
            # - What's the matter?
            return 20
        return -1

    def __20(self, pick: int) -> int:
        if self.index == 0:
            # $script:1010140307011495$
            # - Oh, $MyPCName$. Fancy meeting you here.
            return 20
        elif self.index == 1:
            # $script:1010140307011496$
            # - After not seeing $npcName:11004323[gender:1]$ for a few days I got worried. I asked around and found out she came here all alone. So, I dropped everything and followed her here.
            return 20
        elif self.index == 2:
            # $script:1010140307011497$
            # - I asked her what's going on, but she won't tell me anything. Maybe she doesn't think she can depend on me...
            return 20
        elif self.index == 3:
            # $script:1010140307011498$
            # - In any case, this is no place for her to be running off to alone! She needs to go home.
            if pick == 0:
                # $script:0111232407012693$
                # - That seems like a conversation you should have with her.
                return 21
            return -1
        return -1

    def __21(self, pick: int) -> int:
        # $script:0111232407012694$
        # - I've tried! Maybe you can talk some sense into her?
        return -1

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0109125407012659$
            # - I'm worried...
            return 30
        elif self.index == 1:
            # $script:0109125407012660$
            # - How can I get $npcName:11004323[gender:1]$ to change her mind? We should be in Victoria Island, not here!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (20, 0):
            return Option.NEXT
        elif (self.state, self.index) == (20, 1):
            return Option.NEXT
        elif (self.state, self.index) == (20, 2):
            return Option.NEXT
        elif (self.state, self.index) == (20, 3):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (21, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.CLOSE
        return Option.NONE
