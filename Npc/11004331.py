""" 11004331: Orde """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 30])

    def select(self) -> int:
        return random.choice([0, 20])

    def __0(self, pick: int) -> int:
        # $script:1102172107011633$
        # - Those four... It can't be...
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:1010140307011551$
        # - Those four... It can't be...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1102172107011634$
        # - Children of the dragon... here? Am I dreaming?
        return -1

    def __30(self, pick: int) -> int:
        # $script:1010140307011552$
        # - Children of the dragon... here? Am I dreaming?
        if pick == 0:
            # $script:1010140307011553$
            # - (Tap her gently on the shoulder.)
            return 40
        return -1

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:1010140307011554$
            # - Ahh! Don't sneak up on a girl like that!
            return 40
        elif self.index == 1:
            # $script:1010140307011555$
            # - Oh, it's you. I didn't expect to run into you here.
            return 40
        elif self.index == 2:
            # $script:1010140307011556$
            # - I'm busy right now. Can we talk later?
            if pick == 0:
                # $script:1010140307011557$
                # - What are you doing?
                return 50
            return -1
        return -1

    def __50(self, pick: int) -> int:
        if self.index == 0:
            # $script:1010140307011558$
            # - It's top-secret!
            return 50
        elif self.index == 1:
            # $script:1010140307011559$
            # - Actually, you'll never believe it. Those kids raised by the last dragon master? They're <b>here</b>!
            return 50
        elif self.index == 2:
            # $script:1010140307011560$
            # - I heard the rumors. That's the only reason I was willing to come schlep all the way here with $npcName:11004332[gender:1]$. But it turns out they were true!
            return 50
        elif self.index == 3:
            # $script:1010140307011561$
            # - See that girl with the blonde hair, way over there? I can smell her dragon juju from here. Unless I'm imagining things...
            return 50
        elif self.index == 4:
            # $script:1010140307011562$
            # - What I would give for an interview with them! Just to hear them talk about the lumarigons...
            if pick == 0:
                # $script:0111232407012697$
                # - Same old Orde.
                return 60
            return -1
        return -1

    def __60(self, pick: int) -> int:
        # $script:0111232407012698$
        # - Hey, you know them don't you? Do you think you could introduce me? Please? Hey, where are you going?!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.NEXT
        elif (self.state, self.index) == (40, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (50, 0):
            return Option.NEXT
        elif (self.state, self.index) == (50, 1):
            return Option.NEXT
        elif (self.state, self.index) == (50, 2):
            return Option.NEXT
        elif (self.state, self.index) == (50, 3):
            return Option.NEXT
        elif (self.state, self.index) == (50, 4):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (60, 0):
            return Option.CLOSE
        return Option.NONE
