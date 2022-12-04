""" 11001678: Bravos """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0629000607006437$
        # - You need anything, you just call out my name. Not that I'll come running, but maybe it'll give you good luck.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0629000607006440$
        # - Do you know why I'm called $npcName:11001545[gender:0]$?
        if pick == 0:
            # $script:0629000607006441$
            # - No clue.
            return 40
        elif pick == 1:
            # $script:0629000607006442$
            # - Yes.
            return 50
        elif pick == 2:
            # $script:0706165507006635$
            # - Let's talk about something else.
            return 60
        return -1

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:0629000607006443$
            # - I'm so great I deserve a standing ovation! Haw! I can't believe you never heard of me. Well, remember me for next time.
            return 40
        elif self.index == 1:
            # $script:0629000607006444$
            # - What, you come here to stare at me? Unless you have something else to say, scram!
            return -1
        return -1

    def __50(self, pick: int) -> int:
        if self.index == 0:
            # $script:0629000607006445$
            # - You probably already heard this, but listen anyway. They call me Bravos 'cause I'm so great I deserve a standing ovation! Get it?
            return 50
        elif self.index == 1:
            # $script:0629000607006446$
            # - What, you come here to stare at me? Unless you have something else to say, scram!
            return -1
        return -1

    def __60(self, pick: int) -> int:
        # $script:0706165507006636$
        # - Yeah, what do you want to talk about?
        if pick == 0:
            # $script:0706165507006637$
            # - What's your standing in Blackstar, exactly?
            return 70
        return -1

    def __70(self, pick: int) -> int:
        # $script:0706165507006638$
        # - Isn't it obvious? There's a reason I'm always picked for the best missions. The boss trusts me. I'll be an officer in no time, and then idiots like $npcName:11001686[gender:0]$ will have to do whatever I say.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.NEXT
        elif (self.state, self.index) == (50, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (60, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (70, 0):
            return Option.CLOSE
        return Option.NONE
