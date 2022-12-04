""" 11001262: Ripert """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1203182807004698$
        # - Strength will win a fight. Information will win a war. 
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1206005307004737$
        # - What do you wa—I mean, welcome, valued customer! What kind of information can I help you with today?
        if pick == 0:
            # $script:1206005307004738$
            # - What do you do here, exactly?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:1206005307004739$
        # - This $map:52000020$ exists to provide only the most reliable information handpicked by the hundreds and thousands of members of the Barrota Trading Company, Victoria Island's largest community of traveling merchants.
        if pick == 0:
            # $script:1206005307004740$
            # - Okay, you've caught my attention.
            return 32
        return -1

    def __32(self, pick: int) -> int:
        if self.index == 0:
            # $script:1206010607004771$
            # - Of course! Our information is divided into five classes for your convenience: S, A, B, C, and D. The class varies with the quality and price of the information. Class D information starts from 1,000 mesos, while Class S information is a steal at 50 million mesos.
            return 32
        elif self.index == 1:
            # $script:1206010607004772$
            # - Now, what kind of information do you want?
            if pick == 0:
                # $script:1206010607004773$
                # - Class D please!
                return 33
            elif pick == 1:
                # $script:1206010607004774$
                # - Class S! Only the best for me!
                return 34
            elif pick == 2:
                # $script:1206010607004775$
                # - Oh, I was just browsing.
                return 35
            elif pick == 3:
                # $script:1206011307004791$
                # - I'll come back later.
                return 38
            return -1
        return -1

    def __33(self, pick: int) -> int:
        # $script:1206010607004776$
        # - What're you, a cheapskate? Look, I don't got time for... I mean, sorry, but I don't have any appointments available!
        if pick == 0:
            # $script:1206010607004777$
            # - I need to ask something else.
            return 36
        return -1

    def __34(self, pick: int) -> int:
        # $script:1206010607004778$
        # - Absolutely! May I offer you a cup of tea? Or perhaps a moist towelette?
        if pick == 0:
            # $script:1206010607004779$
            # - Actually, I just remembered I've got other things to do.
            return 37
        return -1

    def __35(self, pick: int) -> int:
        # $script:1206010607004780$
        # - This isn't an art gallery! Is wasting my time entertaining to you?
        if pick == 0:
            # $script:1206010607004781$
            # - I need to ask something else.
            return 36
        return -1

    def __36(self, pick: int) -> int:
        # $script:1206010607004782$
        # - Which class of information would you like?
        if pick == 0:
            # $script:1206010607004783$
            # - Class D please!
            return 33
        elif pick == 1:
            # $script:1206010607004784$
            # - Class S! Only the best for me!
            return 34
        elif pick == 2:
            # $script:1206010607004785$
            # - Oh, I was just browsing.
            return 35
        elif pick == 3:
            # $script:1206011307004792$
            # - I'll come back later.
            return 38
        return -1

    def __37(self, pick: int) -> int:
        # $script:1206010607004786$
        # - Wait! If you'd just give me a moment... Bah!
        return -1

    def __38(self, pick: int) -> int:
        # $script:1206011307004793$
        # - Yes, well, please come again!
        #   <font color="#909090">(He looks a bit crestfallen.)</font>
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.NEXT
        elif (self.state, self.index) == (32, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (33, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (34, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (35, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (36, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (37, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (38, 0):
            return Option.CLOSE
        return Option.NONE
