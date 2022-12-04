""" 11001397: Akamorro """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40, 50])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217193307005397$
        # - What brings you here?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1226235907005601$
        # - I like quiet places. Real quiet places.
        if pick == 0:
            # $script:1226235907005602$
            # - Why's that?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:1226235907005603$
        # - I've got my reasons.
        if pick == 0:
            # $script:1226235907005604$
            # - Such as...?
            return 32
        return -1

    def __32(self, pick: int) -> int:
        # $script:1226235907005605$
        # - I like quiet places because then I don't have to deal with nosy people like you. But I guess it's time for me to look for a new quiet place.
        return -1

    def __40(self, pick: int) -> int:
        # $script:1227015507005609$
        # - Hm? Who are you?
        if pick == 0:
            # $script:1227015507005610$
            # - $npcName:11001396[gender:1]$ wants this slab translated.
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:1227015507005611$
        # - Oh, yes, I remember her. Clever girl. It didn't even occur to her that I might not be able to translate this.
        if pick == 0:
            # $script:1227015507005612$
            # - You can't do it?
            return 42
        return -1

    def __42(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227015507005613$
            # - I didn't say that! Child's play, mere child's play. Now be quiet while I work...
            return 42
        elif self.index == 1:
            # $script:1227015507005614$
            # - Yes... Mm-hmm... Now, that is interesting.
            if pick == 0:
                # $script:1227015507005615$
                # - What is?!
                return 43
            return -1
        return -1

    def __43(self, pick: int) -> int:
        # $script:1227015507005616$
        # - Be quiet, you! Your jabbering is distracting.
        if pick == 0:
            # $script:1227015507005617$
            # - (Make an exaggerated lip-zipping motion.)
            return 44
        return -1

    def __44(self, pick: int) -> int:
        # $script:1227015507005618$
        # - Yes, I see. This will be quite helpful... I've got something for you. Wait just a while longer. 
        if pick == 0:
            # $script:1227015507005619$
            # - (Wait several moments.)
            return 45
        return -1

    def __45(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227015507005620$
            # - If I do this, then... Is the formula off? Then I should try this, and...
            return 45
        elif self.index == 1:
            # $script:1227015507005621$
            # - It is done! I don't know who made this slab, but it contained the answer to a new formula I've been trying to perfect.
            return 45
        elif self.index == 2:
            # $script:1227015507005622$
            # - This record describes a method for stimulating the nerves and triggering a transformation in the body. I reverse-engineered the method to create a restorative tincture!
            if pick == 0:
                # $script:1227015507005623$
                # - Yes, and?
                return 46
            return -1
        return -1

    def __46(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227015507005624$
            # - So impertinent! I was just getting to the good part. In short...
            return 46
        elif self.index == 1:
            # $script:1227015507005625$
            # - I've created a potion that can alleviate the ailments that $npcName:11001396[gender:1]$ told me about. Note that I am being most humble here. When I say alleviate, I mean completely cure.
            if pick == 0:
                # $script:1227015507005626$
                # - Thank you.
                # TODO: goto 47
                # TODO: gotoFail 48
                return 48
            return -1
        return -1

    def __47(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:1227015507005627$
        # - Take this to $npcName:11001396[gender:1]$. And tell her she's welcome.
        return -1

    def __48(self, pick: int) -> int:
        # $script:1230110007005751$
        # - I don't think you have enough space in your bag. Lighten your load first.
        return -1

    def __50(self, pick: int) -> int:
        # $script:1227033507005628$
        # - Is there anything else you need?
        if pick == 0:
            # $script:1227033507005629$
            # - No.
            return 51
        return -1

    def __51(self, pick: int) -> int:
        # $script:1227033507005630$
        # - Good, good. You may leave.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (42, 0):
            return Option.NEXT
        elif (self.state, self.index) == (42, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (43, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (44, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (45, 0):
            return Option.NEXT
        elif (self.state, self.index) == (45, 1):
            return Option.NEXT
        elif (self.state, self.index) == (45, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (46, 0):
            return Option.NEXT
        elif (self.state, self.index) == (46, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (47, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (48, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (51, 0):
            return Option.CLOSE
        return Option.NONE
