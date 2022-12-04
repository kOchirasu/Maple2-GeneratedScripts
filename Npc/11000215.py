""" 11000215: Evan """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30, 40, 50, 60, 70, 80, 100])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000911$
        # - What seems to be the problem?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407000913$
        # - Mm? What is it? Are you having a problem posting $item:30000038$?
        if pick == 0:
            # $script:0831180407000914$
            # - Actually, I kinda lost my $item:30000038$...
            # TODO: goto 21,22
            # TODO: gotoFail 23
            return 23
        elif pick == 1:
            # $script:0831180407000915$
            # - Where am I supposed to post $item:30000038$ again?
            return 24
        return -1

    def __21(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180407000916$
        # - Oh, I see. Here's another one. Try not to lose it this time.
        return -1

    def __22(self, pick: int) -> int:
        # $script:0831180407000917$
        # - I remember giving you one, though. Why don't you check your bag one more time?
        return -1

    def __23(self, pick: int) -> int:
        # $script:0831180407000918$
        # - Your bag looks really heavy. Why don't you lighten it first?
        return -1

    def __24(self, pick: int) -> int:
        # $script:0831180407000919$
        # - There's a Dark Wind Bounty Bulletin Board in $map:02000138$. Take it there.
        return -1

    def __30(self, pick: int) -> int:
        # $script:0831180407000920$
        # - Mm? What is it? Are you having a problem posting $item:30000038$?
        if pick == 0:
            # $script:0831180407000921$
            # - Actually, I kinda lost my $item:30000038$...
            # TODO: goto 31,32
            # TODO: gotoFail 33
            return 33
        elif pick == 1:
            # $script:0831180407000922$
            # - Where am I supposed to post $item:30000038$ again?
            return 34
        return -1

    def __31(self, pick: int) -> int:
        # functionID=2 openTalkReward=True 
        # $script:0831180407000923$
        # - Oh, I see. Here's another one. Try not to lose it this time.
        return -1

    def __32(self, pick: int) -> int:
        # $script:0831180407000924$
        # - I remember giving you one, though. Why don't you check your bag one more time?
        return -1

    def __33(self, pick: int) -> int:
        # $script:0831180407000925$
        # - Your bag looks really heavy. Why don't you lighten it first?
        return -1

    def __34(self, pick: int) -> int:
        # $script:0831180407000926$
        # - There's a Dark Wind Bounty Bulletin Board in $map:02000137$. Take it there.
        return -1

    def __40(self, pick: int) -> int:
        # $script:0831180407000927$
        # - Mm? What is it? Are you having a problem posting $item:30000038$?
        if pick == 0:
            # $script:0831180407000928$
            # - Actually, I kinda lost my $item:30000038$...
            # TODO: goto 41,42
            # TODO: gotoFail 43
            return 43
        elif pick == 1:
            # $script:0831180407000929$
            # - Where am I supposed to post $item:30000038$ again?
            return 44
        return -1

    def __41(self, pick: int) -> int:
        # functionID=3 openTalkReward=True 
        # $script:0831180407000930$
        # - Oh, I see. Here's another one. Try not to lose it this time.
        return -1

    def __42(self, pick: int) -> int:
        # $script:0831180407000931$
        # - I remember giving you one, though. Why don't you check your bag one more time?
        return -1

    def __43(self, pick: int) -> int:
        # $script:0831180407000932$
        # - Your bag looks really heavy. Why don't you lighten it first?
        return -1

    def __44(self, pick: int) -> int:
        # $script:0831180407000933$
        # - There's a Dark Wind Bounty Bulletin Board in $map:02000135$. Take it there.
        return -1

    def __50(self, pick: int) -> int:
        # $script:0831180407000934$
        # - Mm? What is it? Are you having a problem posting $item:30000038$?
        if pick == 0:
            # $script:0831180407000935$
            # - Actually, I kinda lost my $item:30000038$...
            # TODO: goto 51,52
            # TODO: gotoFail 53
            return 53
        elif pick == 1:
            # $script:0831180407000936$
            # - Where am I supposed to post $item:30000038$ again?
            return 54
        return -1

    def __51(self, pick: int) -> int:
        # functionID=4 openTalkReward=True 
        # $script:0831180407000937$
        # - Oh, I see. Here's another one. Try not to lose it this time.
        return -1

    def __52(self, pick: int) -> int:
        # $script:0831180407000938$
        # - I remember giving you one, though. Why don't you check your bag one more time?
        return -1

    def __53(self, pick: int) -> int:
        # $script:0831180407000939$
        # - Your bag looks really heavy. Why don't you lighten it first?
        return -1

    def __54(self, pick: int) -> int:
        # $script:0831180407000940$
        # - There's a Dark Wind Bounty Bulletin Board in $map:02000146$. Take it there.
        return -1

    def __60(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000941$
            # - There's been a rift within Dark Wind ever since $npcName:11000044[gender:0]$ became captain. The members are split between supporting the former captain, Winn Stilton, and supporting the new captain, $npcName:11000044[gender:0]$.
            return 60
        elif self.index == 1:
            # $script:0831180407000942$
            # - I haven't decided which side I'm on, but honestly, supporting $npcName:11000044[gender:0]$ makes the most sense at this point.
            return -1
        return -1

    def __70(self, pick: int) -> int:
        # $script:0831180407000943$
        # - Captain $npcName:11000044[gender:0]$ was behind all of this! I can't believe I trusted him.
        return -1

    def __80(self, pick: int) -> int:
        # $script:1122010507007443$
        # - Checking up on me again, are you?
        if pick == 0:
            # $script:1122010507007444$
            # - Don't worry. I'm not here to interrogate you.
            return 81
        return -1

    def __81(self, pick: int) -> int:
        # $script:1122010507007445$
        # - Then why are you here, exactly?
        if pick == 0:
            # $script:1122010507007446$
            # - I'm just dropping by. I'll be back later.
            return 82
        return -1

    def __82(self, pick: int) -> int:
        # $script:1122010507007447$
        # - And will you bring the $npcName:11001912[gender:0]$ with you next time?
        if pick == 0:
            # $script:1122010507007448$
            # - No, just me. I want another look at the secret room upstairs.
            return 83
        return -1

    def __83(self, pick: int) -> int:
        # functionID=5 
        # $script:1122010507007449$
        # - The secret room? Again? That place must be something else...
        return -1

    def __100(self, pick: int) -> int:
        # $script:1129150207009373$
        # - Dark Wind gradually grows more stable, but the world is in chaos, as always.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (21, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (22, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (23, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (24, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (33, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (34, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (42, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (43, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (44, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (51, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (52, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (53, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (54, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (60, 0):
            return Option.NEXT
        elif (self.state, self.index) == (60, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (70, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (80, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (81, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (82, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (83, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (100, 0):
            return Option.CLOSE
        return Option.NONE
