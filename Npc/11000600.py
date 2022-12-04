""" 11000600: Charles Kim """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([50, 60, 70, 80, 90, 100, 110, 120, 130])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002402$
        # - What can I do for you?
        return None # TODO

    def __50(self, pick: int) -> int:
        # $script:0831180407002407$
        # - You still have your $item:30000145$. Why don't you use it? You won't regret it. 
        return -1

    def __60(self, pick: int) -> int:
        # $script:0831180407002408$
        # - Welcome, $MyPCName$! How may I help you today?
        if pick == 0:
            # $script:0831180407002409$
            # - I want another $item:30000145$.
            return 61
        return -1

    def __61(self, pick: int) -> int:
        # $script:0831180407002410$
        # - $MyPCName$, you already got a free $item:30000145$ through the promotion. If you want more, then you'll have to pay 10,000 mesos each.
        if pick == 0:
            # $script:0831180407002411$
            # - Yeah, I want it.
            return 62
        elif pick == 1:
            # $script:0831180407002412$
            # - Never mind, I don't want it.
            return 63
        return -1

    def __62(self, pick: int) -> int:
        # $script:0831180407002413$
        # - Okay, just one more reminder then. If you already own a house, then you cannot buy a Maple Apartment. Makes sense, I'm sure.
        if pick == 0:
            # $script:0831180407002414$
            # - Yep.
            return 65
        elif pick == 1:
            # $script:0831180407002415$
            # - Nope.
            return 64
        return -1

    def __63(self, pick: int) -> int:
        # $script:0831180407002416$
        # - You've made the right decision. Buying a house just makes more sense financially than $item:30000145$.
        return -1

    def __64(self, pick: int) -> int:
        # $script:0831180407002417$
        # - Oh, I'm sorry. Maple World real estate regulations restrict families to only one house. You can only buy a Maple Apartment if you don't have a house. If anything changes, feel free to come back. Bye for now!
        return -1

    def __65(self, pick: int) -> int:
        # $script:0831180407002418$
        # - Good, then it's 10,000 mesos for a $item:30000145$.
        if pick == 0:
            # $script:0831180407002419$
            # - Here's the money.
            # TODO: goto 66
            # TODO: gotoFail 67
            return 67
        return -1

    def __66(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180407002420$
        # - Here's your $item:30000145$. I hope you enjoy your new home. Bye for now!
        return -1

    def __67(self, pick: int) -> int:
        # $script:0831180407002421$
        # - Ah, I'm afraid the transaction didn't go through. Please make sure you have enough money and free space in your bag for the item.
        return -1

    def __70(self, pick: int) -> int:
        # $script:0831180407002422$
        # - House prices have been dropping lately, attracting many potential buyers. It's kept me quite busy!
        return -1

    def __80(self, pick: int) -> int:
        # $script:0831180407002423$
        # - You still have your $item:30000255$. Why don't you use it? You won't regret it. 
        return -1

    def __90(self, pick: int) -> int:
        # $script:0831180407002424$
        # - Welcome, $MyPCName$! How may I help you today?
        if pick == 0:
            # $script:0831180407002425$
            # - I want another $item:30000255$.
            return 91
        return -1

    def __91(self, pick: int) -> int:
        # $script:0831180407002426$
        # - $MyPCName$, you already got a free $item:30000255$ through the promotion. If you want more, then you'll have to pay 10,000 mesos each.
        if pick == 0:
            # $script:0831180407002427$
            # - Yeah, I want it.
            return 92
        elif pick == 1:
            # $script:0831180407002428$
            # - Never mind, I don't want it.
            return 93
        return -1

    def __92(self, pick: int) -> int:
        # $script:0831180407002429$
        # - Okay, just one more reminder then. If you already own a house, then you cannot buy a Maple Apartment. Makes sense, I'm sure.
        if pick == 0:
            # $script:0831180407002430$
            # - Yep.
            return 95
        elif pick == 1:
            # $script:0831180407002431$
            # - Nope.
            return 94
        return -1

    def __93(self, pick: int) -> int:
        # $script:0831180407002432$
        # - You've made the right decision. Buying a house just makes more sense financially than $item:30000255$.
        return -1

    def __94(self, pick: int) -> int:
        # $script:0831180407002433$
        # - Oh, I'm sorry. Maple World real estate regulations restrict families to only one house. You can only buy a Maple Apartment if you don't have a house. If anything changes, feel free to come back. Bye for now!
        return -1

    def __95(self, pick: int) -> int:
        # $script:0831180407002434$
        # - Good, then it's 10,000 mesos for a $item:30000255$.
        if pick == 0:
            # $script:0831180407002435$
            # - Here's the money.
            # TODO: goto 96
            # TODO: gotoFail 97
            return 97
        return -1

    def __96(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180407002436$
        # - Here's your $item:30000255$. I hope you enjoy your new home. Bye for now!
        return -1

    def __97(self, pick: int) -> int:
        # $script:0831180407002437$
        # - Ah, I'm afraid the transaction didn't go through. Please make sure you have enough money and free space in your bag for the item.
        return -1

    def __100(self, pick: int) -> int:
        # $script:0831180407002438$
        # - You still have your $item:30000254$. Why don't you use it? You won't regret it. 
        return -1

    def __110(self, pick: int) -> int:
        # $script:0831180407002439$
        # - Welcome, $MyPCName$! How may I help you today?
        if pick == 0:
            # $script:0831180407002440$
            # - I want another $item:30000254$.
            return 111
        return -1

    def __111(self, pick: int) -> int:
        # $script:0831180407002441$
        # - $MyPCName$, you already got a free $item:30000254$ through the promotion. If you want more, then you'll have to pay 10,000 mesos each.
        if pick == 0:
            # $script:0831180407002442$
            # - Yeah, I want it.
            return 112
        elif pick == 1:
            # $script:0831180407002443$
            # - Never mind, I don't want it.
            return 113
        return -1

    def __112(self, pick: int) -> int:
        # $script:0831180407002444$
        # - Okay, just one more reminder then. If you already own a house, then you cannot buy a Maple Apartment. Makes sense, I'm sure.
        if pick == 0:
            # $script:0831180407002445$
            # - Yep.
            return 115
        elif pick == 1:
            # $script:0831180407002446$
            # - Nope.
            return 114
        return -1

    def __113(self, pick: int) -> int:
        # $script:0831180407002447$
        # - You've made the right decision. Buying a house just makes more sense financially than $item:30000254$.
        return -1

    def __114(self, pick: int) -> int:
        # $script:0831180407002448$
        # - Oh, I'm sorry. Maple World real estate regulations restrict families to only one house. You can only buy a Maple Apartment if you don't have a house. If anything changes, feel free to come back. Bye for now!
        return -1

    def __115(self, pick: int) -> int:
        # $script:0831180407002449$
        # - Good, then it's 10,000 mesos for a $item:30000254$.
        if pick == 0:
            # $script:0831180407002450$
            # - Here's the money.
            # TODO: goto 116
            # TODO: gotoFail 117
            return 117
        return -1

    def __116(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180407002451$
        # - Here's your $item:30000254$. I hope you enjoy your new home. Bye for now!
        return -1

    def __117(self, pick: int) -> int:
        # $script:0831180407002452$
        # - Ah, I'm afraid the transaction didn't go through. Please make sure you have enough money and free space in your bag for the item.
        return -1

    def __120(self, pick: int) -> int:
        # $script:0831180407002453$
        # - You still have your $item:30000253$. Why don't you use it? You won't regret it. 
        return -1

    def __130(self, pick: int) -> int:
        # $script:0831180407002454$
        # - Welcome, $MyPCName$! How may I help you today?
        if pick == 0:
            # $script:0831180407002455$
            # - I want another $item:30000253$.
            return 131
        return -1

    def __131(self, pick: int) -> int:
        # $script:0831180407002456$
        # - $MyPCName$, you already got a free $item:30000253$ through the promotion. If you want more, then you'll have to pay 10,000 mesos each.
        if pick == 0:
            # $script:0831180407002457$
            # - Yeah, I want it.
            return 132
        elif pick == 1:
            # $script:0831180407002458$
            # - Never mind, I don't want it.
            return 133
        return -1

    def __132(self, pick: int) -> int:
        # $script:0831180407002459$
        # - Okay, just one more reminder then. If you already own a house, then you cannot buy a Maple Apartment. Makes sense, I'm sure.
        if pick == 0:
            # $script:0831180407002460$
            # - Yep.
            return 135
        elif pick == 1:
            # $script:0831180407002461$
            # - Nope.
            return 134
        return -1

    def __133(self, pick: int) -> int:
        # $script:0831180407002462$
        # - You've made the right decision. Buying a house just makes more sense financially than $item:30000253$.
        return -1

    def __134(self, pick: int) -> int:
        # $script:0831180407002463$
        # - Oh, I'm sorry. Maple World real estate regulations restrict families to only one house. You can only buy a Maple Apartment if you don't have a house. If anything changes, feel free to come back. Bye for now!
        return -1

    def __135(self, pick: int) -> int:
        # $script:0831180407002464$
        # - Good, then it's 10,000 mesos for a $item:30000253$.
        if pick == 0:
            # $script:0831180407002465$
            # - Here's the money.
            # TODO: goto 136
            # TODO: gotoFail 137
            return 137
        return -1

    def __136(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180407002466$
        # - Here's your $item:30000253$. I hope you enjoy your new home. Bye for now!
        return -1

    def __137(self, pick: int) -> int:
        # $script:0831180407002467$
        # - Ah, I'm afraid the transaction didn't go through. Please make sure you have enough money and free space in your bag for the item.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (50, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (60, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (61, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (62, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (63, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (64, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (65, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (66, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (67, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (70, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (80, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (90, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (91, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (92, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (93, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (94, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (95, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (96, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (97, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (100, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (110, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (111, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (112, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (113, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (114, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (115, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (116, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (117, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (120, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (130, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (131, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (132, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (133, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (134, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (135, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (136, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (137, 0):
            return Option.CLOSE
        return Option.NONE
