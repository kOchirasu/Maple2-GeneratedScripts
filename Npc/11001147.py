""" 11001147: Magic Pot """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0916043407003991$
        # - Read $npcName:11001147$.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0916043407003992$
        # - <font color="#909090">($npcName:11001145[gender:0]$ brought this $npcName:11001147$ from home without telling his mom.)</font>
        return -1

    def __20(self, pick: int) -> int:
        # $script:0916043407003993$
        # - <font color="#909090">($npcName:11001145[gender:0]$ brought this $npcName:11001147$ from home without telling his mom.)</font>
        if pick == 0:
            # $script:0916043407003994$
            # - (Start cooking.)
            return 21
        return -1

    def __21(self, pick: int) -> int:
        # $script:0916043407003995$
        # - (Add the first ingredient.) 
        if pick == 0:
            # $script:0916043407003996$
            # - (Add 10 $itemPlural:30000390$.)
            # TODO: goto 41
            # TODO: gotoFail 28
            return 28
        elif pick == 1:
            # $script:0916043407003997$
            # - (Add 9 $itemPlural:30000390$.)
            # TODO: goto 42
            # TODO: gotoFail 28
            return 28
        elif pick == 2:
            # $script:0916043407003998$
            # - (Add 8 $itemPlural:30000390$.)
            # TODO: goto 22
            # TODO: gotoFail 28
            return 28
        elif pick == 3:
            # $script:0916043407003999$
            # - (Add 7 $itemPlural:30000390$.)
            # TODO: goto 44
            # TODO: gotoFail 28
            return 28
        return -1

    def __22(self, pick: int) -> int:
        # $script:0916043407004000$
        # - <font color="#909090">(Add the second ingredient.)</font> 
        if pick == 0:
            # $script:0916043407004001$
            # - (Add 10 $itemPlural:30000392$.)
            # TODO: goto 23
            # TODO: gotoFail 28
            return 28
        elif pick == 1:
            # $script:0916043407004002$
            # - (Add 9 $itemPlural:30000392$.)
            # TODO: goto 52
            # TODO: gotoFail 28
            return 28
        elif pick == 2:
            # $script:0916043407004003$
            # - (Add 8 $itemPlural:30000392$.)
            # TODO: goto 53
            # TODO: gotoFail 28
            return 28
        elif pick == 3:
            # $script:0916043407004004$
            # - (Add 7 $itemPlural:30000392$.)
            # TODO: goto 54
            # TODO: gotoFail 28
            return 28
        return -1

    def __23(self, pick: int) -> int:
        # $script:0916043407004005$
        # - <font color="#909090">(Add the third ingredient.)</font> 
        if pick == 0:
            # $script:0916043407004006$
            # - (Add 10 $itemPlural:30000391$.)
            # TODO: goto 61
            # TODO: gotoFail 28
            return 28
        elif pick == 1:
            # $script:0916043407004007$
            # - (Add 9 $itemPlural:30000391$.)
            # TODO: goto 62
            # TODO: gotoFail 28
            return 28
        elif pick == 2:
            # $script:0916043407004008$
            # - (Add 8 $itemPlural:30000391$.)
            # TODO: goto 63
            # TODO: gotoFail 28
            return 28
        elif pick == 3:
            # $script:0916043407004009$
            # - (Add 7 $itemPlural:30000391$.)
            # TODO: goto 24
            # TODO: gotoFail 28
            return 28
        return -1

    def __24(self, pick: int) -> int:
        # $script:0916043407004010$
        # - <font color="#909090">(Add the fourth ingredient.)</font> 
        if pick == 0:
            # $script:0916043407004011$
            # - (Add 10 $itemPlural:30000393$.)
            # TODO: goto 71
            # TODO: gotoFail 28
            return 28
        elif pick == 1:
            # $script:0916043407004012$
            # - (Add 9 $itemPlural:30000393$.)
            # TODO: goto 25
            # TODO: gotoFail 28
            return 28
        elif pick == 2:
            # $script:0916043407004013$
            # - (Add 8 $itemPlural:30000393$.)
            # TODO: goto 73
            # TODO: gotoFail 28
            return 28
        elif pick == 3:
            # $script:0916043407004014$
            # - (Add 7 $itemPlural:30000393$.)
            # TODO: goto 74
            # TODO: gotoFail 28
            return 28
        return -1

    def __25(self, pick: int) -> int:
        # $script:0916043407004015$
        # - <font color="#909090">(Continue cooking the dish.)</font>
        if pick == 0:
            # $script:0916043407004016$
            # - (Cook over high heat for 5 minutes.)
            return 35
        elif pick == 1:
            # $script:0916043407004017$
            # - (Cook over high heat for 3 minutes.)
            return 35
        elif pick == 2:
            # $script:0916043407004018$
            # - (Cook over low heat for 5 minutes.)
            # TODO: goto 26
            # TODO: gotoFail 27
            return 27
        elif pick == 3:
            # $script:0916043407004019$
            # - (Cook over low heat for 3 minutes.)
            return 35
        return -1

    def __26(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0916043407004020$
        # - <font color="#909090">(The syrupy candy crystallizes into a $item:30000395$ with a pop. 
        #   Quickly, remove the candy from the $npcName:11001147$!)</font>
        return -1

    def __27(self, pick: int) -> int:
        # $script:0916061207004048$
        # - <font color="#909090">(The candy syrup looks ready to collect, but all too late you realize your bag is full. The mixture inside the pot begins to boil, before inexplicably exploding into its original components. You collect the ingredients and place them in your bag.)</font>
        return -1

    def __28(self, pick: int) -> int:
        # $script:1027175907004302$
        # - <font color="#909090">(You don't have enough ingredients.)</font>
        return -1

    def __30(self, pick: int) -> int:
        # $script:1027182707004383$
        # - <font color="#909090">($npcName:11001145[gender:0]$ brought this $npcName:11001147$ from home without telling his mom.)</font>
        return -1

    def __35(self, pick: int) -> int:
        # $script:0916043407004041$
        # - <font color="#909090">(The $npcName:11001147$ spits out the ingredients with an angry hiss. <i>Did you make a mistake? You'd better read the $npcName:11001146$ again.</i>)
        return -1

    def __41(self, pick: int) -> int:
        # $script:1027181907004303$
        # - <font color="#909090">(Add the second ingredient.)</font> 
        if pick == 0:
            # $script:1027181907004304$
            # - (Add 10 $itemPlural:30000392$.)
            # TODO: goto 51
            # TODO: gotoFail 28
            return 28
        elif pick == 1:
            # $script:1027181907004305$
            # - (Add 9 $itemPlural:30000392$.)
            # TODO: goto 52
            # TODO: gotoFail 28
            return 28
        elif pick == 2:
            # $script:1027181907004306$
            # - (Add 8 $itemPlural:30000392$.)
            # TODO: goto 53
            # TODO: gotoFail 28
            return 28
        elif pick == 3:
            # $script:1027181907004307$
            # - (Add 7 $itemPlural:30000392$.)
            # TODO: goto 54
            # TODO: gotoFail 28
            return 28
        return -1

    def __42(self, pick: int) -> int:
        # $script:1027181907004308$
        # - <font color="#909090">(Add the second ingredient.)</font> 
        if pick == 0:
            # $script:1027181907004309$
            # - (Add 10 $itemPlural:30000392$.)
            # TODO: goto 51
            # TODO: gotoFail 28
            return 28
        elif pick == 1:
            # $script:1027181907004310$
            # - (Add 9 $itemPlural:30000392$.)
            # TODO: goto 52
            # TODO: gotoFail 28
            return 28
        elif pick == 2:
            # $script:1027181907004311$
            # - (Add 8 $itemPlural:30000392$.)
            # TODO: goto 53
            # TODO: gotoFail 28
            return 28
        elif pick == 3:
            # $script:1027181907004312$
            # - (Add 7 $itemPlural:30000392$.)
            # TODO: goto 54
            # TODO: gotoFail 28
            return 28
        return -1

    def __43(self, pick: int) -> int:
        # $script:1027181907004313$
        # - <font color="#909090">(Add the second ingredient.)</font> 
        if pick == 0:
            # $script:1027181907004314$
            # - (Add 10 $itemPlural:30000392$.)
            # TODO: goto 51
            # TODO: gotoFail 28
            return 28
        elif pick == 1:
            # $script:1027181907004315$
            # - (Add 9 $itemPlural:30000392$.)
            # TODO: goto 52
            # TODO: gotoFail 28
            return 28
        elif pick == 2:
            # $script:1027181907004316$
            # - (Add 8 $itemPlural:30000392$.)
            # TODO: goto 53
            # TODO: gotoFail 28
            return 28
        elif pick == 3:
            # $script:1027181907004317$
            # - (Add 7 $itemPlural:30000392$.)
            # TODO: goto 54
            # TODO: gotoFail 28
            return 28
        return -1

    def __44(self, pick: int) -> int:
        # $script:1027181907004318$
        # - <font color="#909090">(Add the second ingredient.)</font> 
        if pick == 0:
            # $script:1027181907004319$
            # - (Add 10 $itemPlural:30000392$.)
            # TODO: goto 51
            # TODO: gotoFail 28
            return 28
        elif pick == 1:
            # $script:1027181907004320$
            # - (Add 9 $itemPlural:30000392$.)
            # TODO: goto 52
            # TODO: gotoFail 28
            return 28
        elif pick == 2:
            # $script:1027181907004321$
            # - (Add 8 $itemPlural:30000392$.)
            # TODO: goto 53
            # TODO: gotoFail 28
            return 28
        elif pick == 3:
            # $script:1027181907004322$
            # - (Add 7 $itemPlural:30000392$.)
            # TODO: goto 54
            # TODO: gotoFail 28
            return 28
        return -1

    def __51(self, pick: int) -> int:
        # $script:1027181907004323$
        # - <font color="#909090">(Add the third ingredient.)</font> 
        if pick == 0:
            # $script:1027181907004324$
            # - (Add 10 $itemPlural:30000391$.)
            # TODO: goto 61
            # TODO: gotoFail 28
            return 28
        elif pick == 1:
            # $script:1027181907004325$
            # - (Add 9 $itemPlural:30000391$.)
            # TODO: goto 62
            # TODO: gotoFail 28
            return 28
        elif pick == 2:
            # $script:1027181907004326$
            # - (Add 8 $itemPlural:30000391$.)
            # TODO: goto 63
            # TODO: gotoFail 28
            return 28
        elif pick == 3:
            # $script:1027181907004327$
            # - (Add 7 $itemPlural:30000391$.)
            # TODO: goto 64
            # TODO: gotoFail 28
            return 28
        return -1

    def __52(self, pick: int) -> int:
        # $script:1027181907004328$
        # - <font color="#909090">(Add the third ingredient.)</font> 
        if pick == 0:
            # $script:1027181907004329$
            # - (Add 10 $itemPlural:30000391$.)
            # TODO: goto 61
            # TODO: gotoFail 28
            return 28
        elif pick == 1:
            # $script:1027181907004330$
            # - (Add 9 $itemPlural:30000391$.)
            # TODO: goto 62
            # TODO: gotoFail 28
            return 28
        elif pick == 2:
            # $script:1027181907004331$
            # - (Add 8 $itemPlural:30000391$.)
            # TODO: goto 63
            # TODO: gotoFail 28
            return 28
        elif pick == 3:
            # $script:1027181907004332$
            # - (Add 7 $itemPlural:30000391$.)
            # TODO: goto 64
            # TODO: gotoFail 28
            return 28
        return -1

    def __53(self, pick: int) -> int:
        # $script:1027181907004333$
        # - <font color="#909090">(Add the third ingredient.)</font> 
        if pick == 0:
            # $script:1027181907004334$
            # - (Add 10 $itemPlural:30000391$.)
            # TODO: goto 61
            # TODO: gotoFail 28
            return 28
        elif pick == 1:
            # $script:1027181907004335$
            # - (Add 9 $itemPlural:30000391$.)
            # TODO: goto 62
            # TODO: gotoFail 28
            return 28
        elif pick == 2:
            # $script:1027181907004336$
            # - (Add 8 $itemPlural:30000391$.)
            # TODO: goto 63
            # TODO: gotoFail 28
            return 28
        elif pick == 3:
            # $script:1027181907004337$
            # - (Add 7 $itemPlural:30000391$.)
            # TODO: goto 64
            # TODO: gotoFail 28
            return 28
        return -1

    def __54(self, pick: int) -> int:
        # $script:1027181907004338$
        # - <font color="#909090">(Add the third ingredient.)</font> 
        if pick == 0:
            # $script:1027181907004339$
            # - (Add 10 $itemPlural:30000391$.)
            # TODO: goto 61
            # TODO: gotoFail 28
            return 28
        elif pick == 1:
            # $script:1027181907004340$
            # - (Add 9 $itemPlural:30000391$.)
            # TODO: goto 62
            # TODO: gotoFail 28
            return 28
        elif pick == 2:
            # $script:1027181907004341$
            # - (Add 8 $itemPlural:30000391$.)
            # TODO: goto 63
            # TODO: gotoFail 28
            return 28
        elif pick == 3:
            # $script:1027181907004342$
            # - (Add 7 $itemPlural:30000391$.)
            # TODO: goto 64
            # TODO: gotoFail 28
            return 28
        return -1

    def __61(self, pick: int) -> int:
        # $script:1027181907004343$
        # - <font color="#909090">(Add the fourth ingredient.)</font> 
        if pick == 0:
            # $script:1027181907004344$
            # - (Add 10 $itemPlural:30000393$.)
            # TODO: goto 71
            # TODO: gotoFail 28
            return 28
        elif pick == 1:
            # $script:1027181907004345$
            # - (Add 9 $itemPlural:30000393$.)
            # TODO: goto 72
            # TODO: gotoFail 28
            return 28
        elif pick == 2:
            # $script:1027181907004346$
            # - (Add 8 $itemPlural:30000393$.)
            # TODO: goto 73
            # TODO: gotoFail 28
            return 28
        elif pick == 3:
            # $script:1027181907004347$
            # - (Add 7 $itemPlural:30000393$.)
            # TODO: goto 74
            # TODO: gotoFail 28
            return 28
        return -1

    def __62(self, pick: int) -> int:
        # $script:1027181907004348$
        # - <font color="#909090">(Add the fourth ingredient.)</font> 
        if pick == 0:
            # $script:1027181907004349$
            # - (Add 10 $itemPlural:30000393$.)
            # TODO: goto 71
            # TODO: gotoFail 28
            return 28
        elif pick == 1:
            # $script:1027181907004350$
            # - (Add 9 $itemPlural:30000393$.)
            # TODO: goto 72
            # TODO: gotoFail 28
            return 28
        elif pick == 2:
            # $script:1027181907004351$
            # - (Add 8 $itemPlural:30000393$.)
            # TODO: goto 73
            # TODO: gotoFail 28
            return 28
        elif pick == 3:
            # $script:1027181907004352$
            # - (Add 7 $itemPlural:30000393$.)
            # TODO: goto 74
            # TODO: gotoFail 28
            return 28
        return -1

    def __63(self, pick: int) -> int:
        # $script:1027181907004353$
        # - <font color="#909090">(Add the fourth ingredient.)</font> 
        if pick == 0:
            # $script:1027181907004354$
            # - (Add 10 $itemPlural:30000393$.)
            # TODO: goto 71
            # TODO: gotoFail 28
            return 28
        elif pick == 1:
            # $script:1027181907004355$
            # - (Add 9 $itemPlural:30000393$.)
            # TODO: goto 72
            # TODO: gotoFail 28
            return 28
        elif pick == 2:
            # $script:1027181907004356$
            # - (Add 8 $itemPlural:30000393$.)
            # TODO: goto 73
            # TODO: gotoFail 28
            return 28
        elif pick == 3:
            # $script:1027181907004357$
            # - (Add 7 $itemPlural:30000393$.)
            # TODO: goto 74
            # TODO: gotoFail 28
            return 28
        return -1

    def __64(self, pick: int) -> int:
        # $script:1027181907004358$
        # - <font color="#909090">(Add the fourth ingredient.)</font> 
        if pick == 0:
            # $script:1027181907004359$
            # - (Add 10 $itemPlural:30000393$.)
            # TODO: goto 71
            # TODO: gotoFail 28
            return 28
        elif pick == 1:
            # $script:1027181907004360$
            # - (Add 9 $itemPlural:30000393$.)
            # TODO: goto 72
            # TODO: gotoFail 28
            return 28
        elif pick == 2:
            # $script:1027181907004361$
            # - (Add 8 $itemPlural:30000393$.)
            # TODO: goto 73
            # TODO: gotoFail 28
            return 28
        elif pick == 3:
            # $script:1027181907004362$
            # - (Add 7 $itemPlural:30000393$.)
            # TODO: goto 74
            # TODO: gotoFail 28
            return 28
        return -1

    def __71(self, pick: int) -> int:
        # $script:1027181907004363$
        # - <font color="#909090">(Continue cooking the dish.)</font>
        if pick == 0:
            # $script:1027181907004364$
            # - (Cook over high heat for 5 minutes.)
            return 35
        elif pick == 1:
            # $script:1027181907004365$
            # - (Cook over high heat for 3 minutes.)
            return 35
        elif pick == 2:
            # $script:1027181907004366$
            # - (Cook over low heat for 5 minutes.)
            return 35
        elif pick == 3:
            # $script:1027181907004367$
            # - (Cook over low heat for 3 minutes.)
            return 35
        return -1

    def __72(self, pick: int) -> int:
        # $script:1027181907004368$
        # - <font color="#909090">(Continue cooking the dish.)</font>
        if pick == 0:
            # $script:1027181907004369$
            # - (Cook over high heat for 5 minutes.)
            return 35
        elif pick == 1:
            # $script:1027181907004370$
            # - (Cook over high heat for 3 minutes.)
            return 35
        elif pick == 2:
            # $script:1027181907004371$
            # - (Cook over low heat for 5 minutes.)
            return 35
        elif pick == 3:
            # $script:1027181907004372$
            # - (Cook over low heat for 3 minutes.)
            return 35
        return -1

    def __73(self, pick: int) -> int:
        # $script:1027181907004373$
        # - <font color="#909090">(Continue cooking the dish.)</font>
        if pick == 0:
            # $script:1027181907004374$
            # - (Cook over high heat for 5 minutes.)
            return 35
        elif pick == 1:
            # $script:1027181907004375$
            # - (Cook over high heat for 3 minutes.)
            return 35
        elif pick == 2:
            # $script:1027181907004376$
            # - (Cook over low heat for 5 minutes.)
            return 35
        elif pick == 3:
            # $script:1027181907004377$
            # - (Cook over low heat for 3 minutes.)
            return 35
        return -1

    def __74(self, pick: int) -> int:
        # $script:1027181907004378$
        # - <font color="#909090">(Continue cooking the dish.)</font>
        if pick == 0:
            # $script:1027181907004379$
            # - (Cook over high heat for 5 minutes.)
            return 35
        elif pick == 1:
            # $script:1027181907004380$
            # - (Cook over high heat for 3 minutes.)
            return 35
        elif pick == 2:
            # $script:1027181907004381$
            # - (Cook over low heat for 5 minutes.)
            return 35
        elif pick == 3:
            # $script:1027181907004382$
            # - (Cook over low heat for 3 minutes.)
            return 35
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (21, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (22, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (23, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (24, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (25, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (26, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (27, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (28, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (35, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (41, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (42, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (43, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (44, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (51, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (52, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (53, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (54, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (61, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (62, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (63, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (64, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (71, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (72, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (73, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (74, 0):
            return Option.SELECTABLE_DISTRACTOR
        return Option.NONE
