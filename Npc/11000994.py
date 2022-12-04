""" 11000994: Lotachi """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        # TODO: Job 1
        # TODO: RandomPick 40,50,60
        return 0 # Default

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180610001119$
        # - Ahoy! 
        return None # TODO

    def __1(self, pick: int) -> int:
        # $script:0831180610001120$
        # - Civilian ships are prohibited from sailing the waters around $map:02000183$. But for the low, low price of <font color="#ffd200">4,000</font> mesos, I can smuggle you into the area. Do you want to cast off now?
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180610001124$
        # - Buddy, you need something?
        if pick == 0:
            # $script:0831180610001125$
            # - I want to go to $map:02000183$.
            return 41
        elif pick == 1:
            # $script:0831180610001126$
            # - No.
            return 42
        return -1

    def __41(self, pick: int) -> int:
        # $script:0831180610001127$
        # - $map:02000183$? Sorry, no can do. Civilian ships are prohibited from sailing in those waters.
        return -1

    def __42(self, pick: int) -> int:
        # $script:0831180610001128$
        # - Alright then. I pretty much run the harbor, so if you need anything I can help you out. For a fee, of course.
        return -1

    def __50(self, pick: int) -> int:
        # $script:0831180610001129$
        # - You want to go to $map:02000183$.
        #   The only way by ship is to pay someone to smuggle you in, and that costs at least <font color="#ffd200">4,000 mesos</font>. Bring the money, will you?
        return -1

    def __60(self, pick: int) -> int:
        # $script:1209001710001308$
        # - Ugh, my throat... it feels like my last coughing fit tore it up. Ow... were you saying something?
        if pick == 0:
            # $script:1209001710001309$
            # - I want to get on the same ship as <font color="#ffd200">Bomar</font>.
            return 61
        return -1

    def __61(self, pick: int) -> int:
        # $script:1209001710001310$
        # - All civilian ships are prohibited from sailing in that direction. Just a moment, I feel a cough coming on... no, false alarm. Okay, as I was saying, civilians are banned, but... if you really want to go, I could smuggle you in for a price—Hnrghh! Hurrgh! Ow, the cough's back... Hnrrgh! Hnrgh! Ahem! You see, I'm a master smuggler—hrrgh! Hurgh! Oh, who am I kidding? I can't sound like a smooth criminal with this cough. Look, it'll be 4,000 mesos to take you there. Please just pretend I said that with some gravitas.
        if pick == 0:
            # $script:1210013910001316$
            # - Don't worry, I'll get you what you need to wet your whistle.
            # TODO: goto 62
            # TODO: gotoFail 63
            return 63
        return -1

    def __62(self, pick: int) -> int:
        # $script:1209001710001311$
        # - How about I—Hnrgh! Hnrgh!—let you on the ship in exchange for a glass of $item:20000087$? My cough's so bad I care more about that than money. That's an option if you don't want to—Hnrrgh! Hnrgh!—go to $map:2000183$ right away.
        if pick == 0:
            # $script:1210233210001317$
            # - Can you please send me there now?
            return 64
        return -1

    def __64(self, pick: int) -> int:
        # functionID=1 
        # $script:1210233210001318$
        # - Okay. Argh, I can feel another coughing fit coming on! Leave me before you catch something!
        return -1

    def __63(self, pick: int) -> int:
        # $script:1209001710001313$
        # - Thank you... I'd like a—Hnrgh! Hnrgh!—glass of $item:20000087$, please. $npcName:11000445[gender:1]$ mixes wonderful drinks over there on the beach. Hnrghh! Huuurrgh! 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (1, 0):
            return Option.TAKE_BOAT
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (42, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (60, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (61, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (62, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (64, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (63, 0):
            return Option.CLOSE
        return Option.NONE
