""" 11001265: Eupheria """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40, 60, 70])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1203182807004707$
        # - Have you come to see me?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1206005307004760$
        # - Though I deeply wish to pursue $npcName:11001231[gender:0]$, for now I will follow $npcName:11001246[gender:0]$'s advice and bide my time.
        if pick == 0:
            # $script:1206005307004761$
            # - What advice is that?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:1206005307004762$
        # - He said I'd need another ten years' training to have a hope of defeating $npcName:11001231[gender:0]$. I can't put into words how much that stings, but deep down, I know he's right.
        return -1

    def __40(self, pick: int) -> int:
        # $script:1216035207005142$
        # - Can I help you with something, $MyPCName$?
        if pick == 0:
            # $script:1216035207005143$
            # - I'm looking for something.
            return 41
        elif pick == 1:
            # $script:1216035207005144$
            # - No.
            return 100
        return -1

    def __41(self, pick: int) -> int:
        # $script:1216035207005145$
        # - If you've come to me, then you must have a problem that only I can assist you with. Speak.
        if pick == 0:
            # $script:1216035207005146$
            # - Do you have a spare $item:40000022$?
            return 50
        return -1

    def __50(self, pick: int) -> int:
        # $script:1216035207005147$
        # - You're here for the $item:40000022$? Please wait a moment.
        if pick == 0:
            # $script:1216035207005148$
            # - (Wait several moments.)
            return 51
        return -1

    def __51(self, pick: int) -> int:
        # $script:1216035207005149$
        # - Is this what you're looking for? It's what was written in that copy of the Wisdom of the Baaz you showed me.
        if pick == 0:
            # $script:1216035207005150$
            # - That's right.
            return 52
        return -1

    def __52(self, pick: int) -> int:
        # $script:1216035207005151$
        # - I know we wouldn't have found it without you, but please... don't lose this again. It contains valuable information regarding our legacy as Runeblades!
        if pick == 0:
            # $script:1216035207005152$
            # - Sure.
            # TODO: goto 53
            # TODO: gotoFail 90
            return 90
        return -1

    def __53(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:1216035207005153$
        # - Here, take it. You're lucky I transcribed an extra copy.
        return -1

    def __60(self, pick: int) -> int:
        # $script:1216035207005154$
        # - Can I help you with something, $MyPCName$?
        if pick == 0:
            # $script:1216035207005155$
            # - I'm looking for something.
            return 61
        elif pick == 1:
            # $script:1216035207005156$
            # - No.
            return 100
        return -1

    def __61(self, pick: int) -> int:
        # $script:1216035207005157$
        # - If you've come to me, then you must have a problem that only I can assist you with. Speak.
        if pick == 0:
            # $script:1216035207005158$
            # - Do you have a spare $item:40000024$?
            return 62
        elif pick == 1:
            # $script:1216113507005178$
            # - Do you have a spare $item:40000022$?
            return 50
        return -1

    def __62(self, pick: int) -> int:
        # $script:1216035207005159$
        # - You're here for the $item:40000024$? Please wait a moment.
        if pick == 0:
            # $script:1216035207005160$
            # - (Wait several moments.)
            # TODO: goto 63
            # TODO: gotoFail 69
            return 69
        return -1

    def __63(self, pick: int) -> int:
        # $script:1216035207005161$
        # - Is this what you're looking for? It's what was written in that copy of the Wisdom of the Baaz you showed me.
        if pick == 0:
            # $script:1216035207005162$
            # - That's right.
            return 64
        return -1

    def __64(self, pick: int) -> int:
        # $script:1216035207005163$
        # - I know we wouldn't have found it without you, but please... don't lose this again. It contains valuable information regarding our legacy as Runeblades!
        if pick == 0:
            # $script:1216035207005164$
            # - Sure.
            # TODO: goto 65
            # TODO: gotoFail 90
            return 90
        return -1

    def __65(self, pick: int) -> int:
        # functionID=2 openTalkReward=True 
        # $script:1216035207005165$
        # - Here, take it. You're lucky I transcribed an extra copy.
        return -1

    def __69(self, pick: int) -> int:
        # $script:1216035207005166$
        # - According to the documents we've restored, it's likely that the writings in this $item:40000024$ originated from the second volume of the Wisdom of the Baaz. If you want to complete it, you need that volume.
        return -1

    def __70(self, pick: int) -> int:
        # $script:1216040007005167$
        # - Can I help you with something, $MyPCName$?
        if pick == 0:
            # $script:1216040007005168$
            # - I'm looking for something.
            return 71
        elif pick == 1:
            # $script:1216040007005169$
            # - No.
            return 100
        return -1

    def __71(self, pick: int) -> int:
        # $script:1216040007005170$
        # - If you've come to me, then you must have a problem that only I can assist you with. Speak.
        if pick == 0:
            # $script:1216040007005171$
            # - Do you have a spare $item:40000023$?
            return 72
        elif pick == 1:
            # $script:1216113507005179$
            # - Do you have a spare $item:40000024$?
            return 62
        elif pick == 2:
            # $script:1216113507005180$
            # - Do you have a spare $item:40000022$?
            return 50
        return -1

    def __72(self, pick: int) -> int:
        # $script:1216031507005132$
        # - You're here for the $item:40000023$? Please wait a moment.
        if pick == 0:
            # $script:1216031507005133$
            # - (Wait several moments.)
            # TODO: goto 73
            # TODO: gotoFail 79
            return 79
        return -1

    def __73(self, pick: int) -> int:
        # $script:1216031507005134$
        # - Is this what you're looking for? It's what was written in that copy of the Wisdom of the Baaz you showed me.
        if pick == 0:
            # $script:1216031507005135$
            # - That's right.
            return 74
        return -1

    def __74(self, pick: int) -> int:
        # $script:1216031507005136$
        # - I know we wouldn't have found it without you, but please... don't lose this again. It contains valuable information regarding our legacy as Runeblades!
        if pick == 0:
            # $script:1216031507005137$
            # - Sure.
            # TODO: goto 75
            # TODO: gotoFail 90
            return 90
        return -1

    def __75(self, pick: int) -> int:
        # functionID=3 openTalkReward=True 
        # $script:1216031507005138$
        # - Here, take it. You're lucky I transcribed an extra copy.
        return -1

    def __79(self, pick: int) -> int:
        # $script:1216031507005139$
        # - According to the documents we've restored, it's likely that the writings in this $item:40000023$ originated from the third volume of the Wisdom of the Baaz. If you want to complete it, you need that volume.
        return -1

    def __90(self, pick: int) -> int:
        # $script:1216031507005140$
        # - I do not believe you have room in your bag for this. Why not clear some space?
        return -1

    def __100(self, pick: int) -> int:
        # $script:1216031507005141$
        # - Hmm? Well, come back when you need my help.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (51, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (52, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (53, 0):
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
        elif (self.state, self.index) == (69, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (70, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (71, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (72, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (73, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (74, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (75, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (79, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (90, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (100, 0):
            return Option.CLOSE
        return Option.NONE
