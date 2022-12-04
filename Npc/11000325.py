""" 11000325: Gordon """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001312$
        # - Hello. 
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407001315$
        # - Welcome to the Tuning Motors Showroom! Are you looking for something in particular?
        if pick == 0:
            # $script:0909184507003771$
            # - I want to know about mounts.
            return 38
        elif pick == 1:
            # $script:0909184507003772$
            # - I came to see the cars.
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0831180407001316$
        # - I'm here to help you find the perfect car for your style and needs. What kind of car do you like?
        if pick == 0:
            # $script:0831180407001317$
            # - Rugged 4-wheel-drives.
            # TODO: goto 33,37
            # TODO: gotoFail 34
            return 34
        elif pick == 1:
            # $script:0831180407001318$
            # - Luxurious sports cars.
            return 35
        elif pick == 2:
            # $script:0831180407001319$
            # - No cage for me! I want a bike.
            return 36
        return -1

    def __33(self, pick: int) -> int:
        if self.index == 0:
            # functionID=1 
            # $script:0831180407001320$
            # - Ooh, you've got excellent taste! 4-wheel-drive vehicles are designed to handle a wider variety of terrain, including fields, swamps, sand, slopes, and so on.
            return 33
        elif self.index == 1:
            # openTalkReward=True 
            # $script:0831180407001321$
            # - Lucky for you, I've got one 4-wheel-drive model brochure left. Would you like to take a look?
            return -1
        return -1

    def __34(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407001322$
            # - Ooh, you've got excellent taste! 4-wheel-drive vehicles are designed to handle a wider variety of terrain, including fields, swamps, sand, slopes, and so on. Lucky for you, I've got one 4-wheel-drive model brochure left.
            return 34
        elif self.index == 1:
            # $script:0831180407001323$
            # - Oh dear, you don't seem to have enough room in your bag for this brochure. It must be completely stuffed! Make some room if you'd like it, please.
            return -1
        return -1

    def __35(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407001324$
            # - I knew it! You had that look that says "I've got a need... for speed".
            return 35
        elif self.index == 1:
            # $script:0831180407001325$
            # - The Tuning Motors Enpilar series features a high-performance engine slotted into a low-riding, stable chassis to minimize air resistance and give more power to the speed-sensitive steering and brakes. $MyPCName$, it won't disappoint you!
            return -1
        return -1

    def __36(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407001326$
            # - Ooh, we're kindred spirits! With a bike, you can fly through narrow alleyways and congested freeways at high speed. And don't forget the sense of freedom that you don't get in a car!  
            return 36
        elif self.index == 1:
            # $script:0831180407001327$
            # - The Tuning Motors Chopper series is the king of Maple World touring bikes, and it's been the most popular bike on the market for years. It has a much larger displacement than street bikes, and its engine makes a throaty roar that you can't help but love!
            return -1
        return -1

    def __37(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407001328$
            # - Ooh, you've got excellent taste! 4-wheel-drive vehicles are designed to handle a wider variety of terrain, including fields, swamps, sand, slopes, and so on.
            return 37
        elif self.index == 1:
            # $script:0831180407001329$
            # - Good, you already have our 4-wheel-drive model brochure. Read through it, and let me know if you have any questions. And it wouldn't hurt to have a look at our other models, too.
            return -1
        return -1

    def __38(self, pick: int) -> int:
        # $script:0909184507003773$
        # - Mounts? I'll tell you anything you want to know. What'll it be?
        if pick == 0:
            # $script:0909184507003774$
            # - What exactly are mounts?
            return 39
        elif pick == 1:
            # $script:0909184507003775$
            # - Where can I get mounts?
            return 40
        elif pick == 2:
            # $script:0909184507003776$
            # - How do I use my mounts?
            return 41
        return -1

    def __39(self, pick: int) -> int:
        # $script:0909184507003777$
        # - Mounts are very convenient modes of transportation. Riding a mount is faster than running, and much more convenient too! Plus, there's a wide variety of mounts to choose from. So... which one looks good to you?
        if pick == 0:
            # $script:0910171307003816$
            # - I need to ask something else.
            return 42
        return -1

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:0909184507003778$
            # - You can buy cute animal mounts from the Mount Merchant in town. I've heard some animal mounts can even swim. There's also some pretty awesome cars and bikes available for purchase on the Meret Market.
            return 40
        elif self.index == 1:
            # $script:0909184507003779$
            # - You can buy mounts with all kinds of currencies, including mesos, treva, valor tokens, and merets. But to get an extremely fast rare mount, you'll need to earn certain Trophies.
            if pick == 0:
                # $script:0910171307003817$
                # - I need to ask something else.
                return 42
            return -1
        return -1

    def __41(self, pick: int) -> int:
        if self.index == 0:
            # $script:0909184507003780$
            # - You can use a mount by double-clicking it in your inventory, or by adding it to a quickslot. Mounts perform a special action when you press the Basic Attack key while riding them. You'll have a lot of fun just checking out all the different special actions.
            return 41
        elif self.index == 1:
            # $script:0910171307003818$
            # - But there's a catch... the special actions activated by the Basic Attack key consume stamina every time they're used. But it won't be a problem as long as you use them in moderation.
            if pick == 0:
                # $script:0910171307003819$
                # - I need to ask something else.
                return 42
            return -1
        return -1

    def __42(self, pick: int) -> int:
        # $script:0910171307003820$
        # - Is there anything else you want to know about mounts?
        if pick == 0:
            # $script:0910171307003821$
            # - What exactly are mounts?
            return 39
        elif pick == 1:
            # $script:0910171307003822$
            # - Where can I get mounts?
            return 40
        elif pick == 2:
            # $script:0910171307003823$
            # - How do I use my mounts?
            return 41
        elif pick == 3:
            # $script:0910171307003824$
            # - I need to be going.
            return 43
        return -1

    def __43(self, pick: int) -> int:
        # $script:0910171307003825$
        # - While you're here, why don't you peruse the vehicles on display?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (33, 0):
            return Option.NEXT
        elif (self.state, self.index) == (33, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (34, 0):
            return Option.NEXT
        elif (self.state, self.index) == (34, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (35, 0):
            return Option.NEXT
        elif (self.state, self.index) == (35, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (36, 0):
            return Option.NEXT
        elif (self.state, self.index) == (36, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (37, 0):
            return Option.NEXT
        elif (self.state, self.index) == (37, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (38, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (39, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.NEXT
        elif (self.state, self.index) == (41, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (42, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (43, 0):
            return Option.CLOSE
        return Option.NONE
