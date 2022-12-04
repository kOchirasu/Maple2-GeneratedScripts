""" 11004215: Stellar Chest """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 50])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0808172007010849$
        # - <font color="#909090">(This $npcName:11004215$ can create gem dust to help you upgrade your gemstones.)</font>
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0808172007010850$
        # - <font color="#909090">(Do you wish to create some $itemPlural:20301849$?)</font>
        if pick == 0:
            # $script:0808172007010851$
            # - (Create 1.)
            # TODO: goto 11
            # TODO: gotoFail 14
            return 14
        elif pick == 1:
            # $script:0808172007010852$
            # - (Create 10.)
            # TODO: goto 21
            # TODO: gotoFail 24
            return 24
        elif pick == 2:
            # $script:0808172007010853$
            # - (Not now.)
            return 15
        return -1

    def __11(self, pick: int) -> int:
        # $script:0808172007010854$
        # - <font color="#909090">(Consume 10 $itemPlural:30001187$ and 1 $item:30001188$ to make 1 $item:20301849$?)</font> 
        if pick == 0:
            # $script:0808172007010855$
            # - (Create 1 $item:20301849$.)
            # TODO: goto 12
            # TODO: gotoFail 13
            return 13
        return -1

    def __12(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0808172007010856$
        # - <font color="#909090">(The process has been completed. The chest awaits your next command.)</font> 
        return -1

    def __13(self, pick: int) -> int:
        # $script:0808172007010860$
        # - <font color="#909090">(Your bag is full. Return after making some space.)</font>
        return -1

    def __14(self, pick: int) -> int:
        # $script:0808172007010861$
        # - <font color="#909090">(Insufficient materials. You need 10 $itemPlural:30001187$ and 1 $item:30001188$ to begin the conversion process.)</font>
        return -1

    def __15(self, pick: int) -> int:
        # $script:0808172007010862$
        # - <font color="#909090">(The cube stands by.)</font>
        return -1

    def __21(self, pick: int) -> int:
        # $script:0808172007010857$
        # - <font color="#909090">(Consume 100 $itemPlural:30001187$ and 10 $itemPlural:30001188$ to make 10 $itemPlural:20301849$?)</font> 
        if pick == 0:
            # $script:0808172007010858$
            # - (Create 10 $itemPlural:20301849$.)
            # TODO: goto 22
            # TODO: gotoFail 13
            return 13
        return -1

    def __22(self, pick: int) -> int:
        # functionID=2 openTalkReward=True 
        # $script:0808172007010859$
        # - <font color="#909090">(The process has been completed. The chest awaits your next command.)</font> 
        return -1

    def __24(self, pick: int) -> int:
        # $script:0809135407010882$
        # - <font color="#909090">(Insufficient materials. You need 100 $itemPlural:30001187$ and 10 $itemPlural:30001188$ to begin the conversion process.)</font>
        return -1

    def __50(self, pick: int) -> int:
        # $script:0911140307011157$
        # - <font color="#909090">(After you reach level 50, you can use $itemPlural:30001187$ and $itemPlural:30001188$ on this chest to make materials for upgrading gemstones.)</font>
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (13, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (14, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (15, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (21, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (22, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (24, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.CLOSE
        return Option.NONE
