""" 11001707: Tinchai """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0728022507006959$
        # - Mm? Yes?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0728024507006983$
        # - Hello again. Is there something you need?
        if pick == 0:
            # $script:0804030507007012$
            # - How is $npcName:11001715[gender:0]$?
            return 40
        elif pick == 1:
            # $script:0804030507007013$
            # - What do you think of $map:02000001$?
            return 50
        return -1

    def __40(self, pick: int) -> int:
        # $script:0804030507007014$
        # - You aren't actually <i>worried</i> about him, are you? He'll be soooo happy to hear that!
        if pick == 0:
            # $script:0804030507007015$
            # - I'm not worried! Just... concerned.
            return 41
        return -1

    def __41(self, pick: int) -> int:
        if self.index == 0:
            # $script:0804030507007016$
            # - Well, he'll appreciate your concern, anyway. I'm keeping a close eye on him, so you just leave him to me.
            return 41
        elif self.index == 1:
            # $script:0804030507007017$
            # - <font color="#909090">($npcName:11001707[gender:1]$ stops talking suddenly. She hesitates for a moment, then speaks.)</font>
            #   $MyPCName$... Thank you.
            if pick == 0:
                # $script:0804030507007018$
                # - What for?
                return 42
            return -1
        return -1

    def __42(self, pick: int) -> int:
        if self.index == 0:
            # $script:0804030507007019$
            # - $npcName:11001715[gender:0]$ has always been very hard on you. But you've stood by us through this crisis, when other students abandoned us for far less.
            return 42
        elif self.index == 1:
            # $script:0804030507007020$
            # - Now Halo Mountain has been burned to the ground and the master is gone. Guidance exists in name only. You have no real obligation to us. Why don't you wash your hands of this whole mess?
            if pick == 0:
                # $script:0804030507007021$
                # - I owe the master my life.
                return 43
            return -1
        return -1

    def __43(self, pick: int) -> int:
        # $script:0804030507007022$
        # - Maybe... But I want to thank you anyway. That's all.
        if pick == 0:
            # $script:0804030507007023$
            # - Let's talk about something else.
            return 30
        return -1

    def __50(self, pick: int) -> int:
        if self.index == 0:
            # $script:0804030507007024$
            # - This place is amazing! I've never seen such a big city before. It's loud and crowded and crazy, but I think I see why humans like it here.
            return 50
        elif self.index == 1:
            # $script:0804030507007025$
            # - I also get why students who completed their training came to live here. It's about as different from life on Halo Mountain as you can get.
            if pick == 0:
                # $script:0804030507007026$
                # - So, you think you'll be a city slicker from now on?
                return 51
            return -1
        return -1

    def __51(self, pick: int) -> int:
        if self.index == 0:
            # $script:0804030507007027$
            # - No, I don't think so. This place is amazing, but I'll always choose a peaceful life on Halo Mountain...
            #   <font color="#909090">(There's a far-off look in her eyes.)</font>
            return 51
        elif self.index == 1:
            # $script:0804030507007028$
            # - N-no need to dwell on the past, I guess! Let's talk about something else.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.NEXT
        elif (self.state, self.index) == (41, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (42, 0):
            return Option.NEXT
        elif (self.state, self.index) == (42, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (43, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (50, 0):
            return Option.NEXT
        elif (self.state, self.index) == (50, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (51, 0):
            return Option.NEXT
        elif (self.state, self.index) == (51, 1):
            return Option.CLOSE
        return Option.NONE
