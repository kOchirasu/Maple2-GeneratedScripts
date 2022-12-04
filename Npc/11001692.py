""" 11001692: Hub Computer """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([5, 10, 11, 12, 13, 14, 15, 20, 30, 40, 50, 60])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0629000607006502$
        # - Connecting to the BeyondLink database...
        return None # TODO

    def __5(self, pick: int) -> int:
        # $script:0728011907006927$
        # - Connecting to the BeyondLink database... Error: Invalid credentials.
        return -1

    def __10(self, pick: int) -> int:
        # $script:0629000607006503$
        # - Connecting to the BeyondLink database... Connection established.
        if pick == 0:
            # $script:0705132707006621$
            # - (View Code 0.)
            return 11
        return -1

    def __11(self, pick: int) -> int:
        # $script:0705132707006622$
        # - Code 0
        #   Project Hand: Summoning System/Transdimensional Implementation
        if pick == 0:
            # $script:0705132707006623$
            # - (View Code 1.)
            return 12
        return -1

    def __12(self, pick: int) -> int:
        # $script:0705132707006624$
        # - Code 1
        #   Project Mantra: Narubashan purification rate is normal. Mental and physical changes detected during administration.
        if pick == 0:
            # $script:0705132707006625$
            # - (Next page.)
            return 13
        return -1

    def __13(self, pick: int) -> int:
        # $script:0705132707006626$
        # - More sample data is required. Out of 100 personnel supplied by Katramus through the Red Cape, only half can move on to phase 2. Conversion to phase 3 requires the restoration of the missing prototype.
        if pick == 0:
            # $script:0705132707006627$
            # - (View Code 2.)
            return 14
        return -1

    def __14(self, pick: int) -> int:
        # $script:0705132707006628$
        # - Code 2
        #   Project Katramus: Linking $map:03000145$ data not necessary. Code 1 is the highest priority.
        if pick == 0:
            # $script:0705132707006629$
            # - (Next page.)
            return 15
        return -1

    def __15(self, pick: int) -> int:
        # $script:0705132707006630$
        # - Code 1 Support Proposal: Move Dr. Rokel's project. Given current situation, highly likely that Code 2 will be terminated.
        return -1

    def __20(self, pick: int) -> int:
        # $script:0728011907006928$
        # - Confirming connection to BeyondLink... Please scan your iris to verify your credentials.
        return -1

    def __30(self, pick: int) -> int:
        # $script:0728011907006929$
        # - You must first verify your credentials before accessing files. You may only access files for which your account has access permission.
        return -1

    def __40(self, pick: int) -> int:
        # $script:0728011907006947$
        # - <font color="#ffd200">Confirm Target: Lost Child</font>
        if pick == 0:
            # $script:0805105407007103$
            # - <font color="#909090">(Your vision blurs and you feel dizzy.)</font>
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # functionID=1 
        # $script:0804163407007059$
        # - System Command: Absorb target's energy.
        return -1

    def __50(self, pick: int) -> int:
        # $script:0805105407007104$
        # - Connecting to the BeyondLink database... Connection established.
        if pick == 0:
            # $script:0805105407007105$
            # - (View Code 0.)
            return 51
        return -1

    def __51(self, pick: int) -> int:
        # $script:0805105407007106$
        # - Code 0
        #   Project Hand: Summoning System/Transdimensional Implementation
        if pick == 0:
            # $script:0805105407007107$
            # - (View Code 1.)
            return 52
        return -1

    def __52(self, pick: int) -> int:
        # $script:0805105407007108$
        # - Code 1
        #   Project Mantra: Narubashan purification rate is normal. Mental and physical changes detected during administration.
        if pick == 0:
            # $script:0805105407007109$
            # - (Next page.)
            return 53
        return -1

    def __53(self, pick: int) -> int:
        # $script:0805105407007110$
        # - More sample data is required. Out of 100 personnel supplied by Katramus through the Red Cape, only half can move on to phase 2. Conversion to phase 3 requires the restoration of the missing prototype.
        if pick == 0:
            # $script:0805105407007111$
            # - (View Code 2.)
            return 54
        return -1

    def __54(self, pick: int) -> int:
        # $script:0805105407007112$
        # - Code 2
        #   Project Katramus: Linking $map:03000145$ data not necessary. Code 1 is the highest priority.
        if pick == 0:
            # $script:0805105407007113$
            # - (Next page.)
            return 55
        return -1

    def __55(self, pick: int) -> int:
        # $script:0805105407007114$
        # - Code 1 Support Proposal: Move Dr. Rokel's project. Given current situation, highly likely that Code 2 will be terminated.
        return -1

    def __60(self, pick: int) -> int:
        # $script:0805105407007115$
        # - Connecting to the BeyondLink database... Connection established.
        if pick == 0:
            # $script:0805105407007116$
            # - (View Code 0.)
            return 61
        return -1

    def __61(self, pick: int) -> int:
        # $script:0805105407007117$
        # - Code 0
        #   Project Hand: Summoning System/Transdimensional Implementation
        if pick == 0:
            # $script:0805105407007118$
            # - (View Code 1.)
            return 62
        return -1

    def __62(self, pick: int) -> int:
        # $script:0805105407007119$
        # - Code 1
        #   Project Mantra: Narubashan purification rate is normal. Mental and physical changes detected during administration.
        if pick == 0:
            # $script:0805105407007120$
            # - (Next page.)
            return 63
        return -1

    def __63(self, pick: int) -> int:
        # $script:0805105407007121$
        # - More sample data is required. Out of 100 personnel supplied by Katramus through the Red Cape, only half can move on to phase 2. Conversion to phase 3 requires the restoration of the missing prototype.
        if pick == 0:
            # $script:0805105407007122$
            # - (View Code 2.)
            return 64
        return -1

    def __64(self, pick: int) -> int:
        # $script:0805105407007123$
        # - Code 2
        #   Project Katramus: Linking $map:03000145$ data not necessary. Code 1 is the highest priority.
        if pick == 0:
            # $script:0805105407007124$
            # - (Next page.)
            return 65
        return -1

    def __65(self, pick: int) -> int:
        # $script:0805105407007125$
        # - Code 1 Support Proposal: Move Dr. Rokel's project. Given current situation, highly likely that Code 2 will be terminated.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (5, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (13, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (14, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (15, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (51, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (52, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (53, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (54, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (55, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (60, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (61, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (62, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (63, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (64, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (65, 0):
            return Option.CLOSE
        return Option.NONE
