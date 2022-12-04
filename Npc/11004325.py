""" 11004325: Blake """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1010140307011499$
        # - Breathtaking!
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:1010140307011500$
            # - Ahh... It's too beautiful.
            return 10
        elif self.index == 1:
            # $script:1010140307011501$
            # - Can't you feel it? The stunning aurora in the sky... The alien wildlife... This place is filling me with creative energy!
            return 10
        elif self.index == 2:
            # $script:1010140307011502$
            # - I feel it brewing inside. I'm ready to write a smash hit song!
            if pick == 0:
                # $script:1010140307011503$
                # - Since when do you write your own songs?
                return 20
            return -1
        return -1

    def __20(self, pick: int) -> int:
        if self.index == 0:
            # $script:1010140307011504$
            # - Forget the $npcName:11004325[gender:0]$ you used to know. From this day on, I'm reborn as a guy who totally writes his own songs!
            return 20
        elif self.index == 1:
            # $script:1010140307011505$
            # - You just wait. The new and improved $npcName:11004325[gender:0]$ is going to take the world by storm!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.NEXT
        elif (self.state, self.index) == (10, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (20, 0):
            return Option.NEXT
        elif (self.state, self.index) == (20, 1):
            return Option.CLOSE
        return Option.NONE
