""" 11001706: Tinchai """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0728022507006958$
        # - Mm? Yes?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0728024507006980$
        # - It's good to see you, $MyPCName$. Is there something I can get for you?
        if pick == 0:
            # $script:0804030507007003$
            # - What is this artifact we're after?
            return 40
        elif pick == 1:
            # $script:0804030507007004$
            # - Should we be looking for the master?
            return 50
        return -1

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:0804030507007005$
            # - I don't know exactly what it is, but supposedly Lone Spirit, the founder of Guidance, left behind a treasure that would grant enlightenment to his true heir. It was passed down through generations... until the eleventh Munakra vanished with it.
            return 40
        elif self.index == 1:
            # $script:0804030507007006$
            # - Some people think it was destroyed. Others think that all of its power was drained, and it's been placed in hiding until it can recharge. Others say that Lone Spirit reincarnated and claimed it for himself. Who knows which theory, if any, is true?
            return 40
        elif self.index == 2:
            # $script:0804030507007007$
            # - The only reliable information on the artifact is told through word-of-mouth, so the only one who would really know is the master. What if... what if $npcName:11001559[gender:0]$ came to Halo Mountain for the artifact?
            return 40
        elif self.index == 3:
            # $script:0804030507007008$
            # - That must be it. I'm sure he said something about an artifact when he attacked us...
            #   <font color="#909090">($npcName:11001706[gender:1]$ is lost in thought.)</font>
            if pick == 0:
                # $script:0804030507007009$
                # - Let's talk about something else.
                return 30
            return -1
        return -1

    def __50(self, pick: int) -> int:
        # $script:0804030507007010$
        # - The master can fend for himself. Don't worry, all right?
        #   <font color="#909090">(Even as she comforts you, worry is etched in her face.)</font>
        if pick == 0:
            # $script:0804030507007011$
            # - Let's talk about something else.
            return 30
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.NEXT
        elif (self.state, self.index) == (40, 2):
            return Option.NEXT
        elif (self.state, self.index) == (40, 3):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        return Option.NONE
