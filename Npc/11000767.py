""" 11000767: Terry """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([1, 2, 3, 4, 5, 6, 9001, 9002, 9003, 100])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180509001135$
        # - What is it?
        return None # TODO

    def __1(self, pick: int) -> int:
        # $script:0831180509001136$
        # - How was your day today?
        if pick == 0:
            # $script:0831180509001137$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001138$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001139$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __2(self, pick: int) -> int:
        # $script:0831180509001140$
        # - You're home early today.
        if pick == 0:
            # $script:0831180509001141$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001142$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001143$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __3(self, pick: int) -> int:
        # $script:0831180509001144$
        # - Hey, you're home.
        if pick == 0:
            # $script:0831180509001145$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001146$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001147$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __4(self, pick: int) -> int:
        # $script:0831180509001148$
        # - How was your day today?
        if pick == 0:
            # $script:0831180509001149$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001150$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001151$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509001152$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __5(self, pick: int) -> int:
        # $script:0831180509001153$
        # - You're home early today.
        if pick == 0:
            # $script:0831180509001154$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001155$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001156$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509001157$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __6(self, pick: int) -> int:
        # $script:0831180509001158$
        # - Hey, you're home.
        if pick == 0:
            # $script:0831180509001159$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001160$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001161$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509001162$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __9(self, pick: int) -> int:
        # $script:0831180509001163$
        # - Oh, you're giving me my paycheck.
        #   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
        if pick == 0:
            # $script:0831180509001164$
            # - Let me think about it some more.
            # TODO: goto 8040,8050,8060,9040
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001165$
            # - (Pay $MaidSalary$.)
            # TODO: goto 8000,8001,8010,8011,8901
            # TODO: gotoFail 8900,8910
            return 8900,8910
        return -1

    def __8000(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001166$
        # - Hah hah, thanks! I'm happy to work for you for this month!
        return -1

    def __8001(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001167$
        # - Has it been so long already? Thanks for asking me before I had to ask. I hate asking for money.
        return -1

    def __8010(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001168$
        # - Ah! You don't know how long I've been waiting for this! Finally, I've got some money to spend. Hah hah!
        return -1

    def __8011(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001169$
        # - Whew, I was debating whether I should cancel my savings account because I'd have nothing to put in it. Thank goodness I won't have to!
        return -1

    def __8020(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509001170$
        # - $OwnerName$, I was looking at the calender today and saw that our contract is expiring soon. Just wanted to let you know. No pressure or anything!
        return -1

    def __8021(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509001171$
        # - Then again, maybe I'm worring for nothing. Hah hah.
        if pick == 0:
            # $script:0831180509001172$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001173$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001174$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509001175$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8040(self, pick: int) -> int:
        # $script:0831180509001176$
        # - Is there anything I can do for you? 
        if pick == 0:
            # $script:0831180509001177$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001178$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001179$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509001180$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8050(self, pick: int) -> int:
        # $script:0831180509001181$
        # - I want to do something fun. Any suggestions?
        if pick == 0:
            # $script:0831180509001182$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001183$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001184$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509001185$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8060(self, pick: int) -> int:
        # $script:0831180509001186$
        # - I've got too much energy. Maybe I should work out.
        if pick == 0:
            # $script:0831180509001187$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001188$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001189$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509001190$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8900(self, pick: int) -> int:
        # $script:0831180509001191$
        # - Hey, you don't have to do this right now. If you're going through a hard time, I can wait. Don't worry about it.
        return -1

    def __8901(self, pick: int) -> int:
        # $script:0831180509001192$
        # - A paycheck, again? You already paid me for this month. Hm, maybe I should take it as a bonus... Hah hah hah!
        return -1

    def __8910(self, pick: int) -> int:
        # $script:0831180509001193$
        # - Ah, I told you it can wait. I'm all right for now. Did you forget? I've got two jobs. I'm more worried about you, to be honest.
        return -1

    def __8999(self, pick: int) -> int:
        # $script:0831180509001194$
        # - Err? What's going on? I've never been in this situation before, so I don't know what to do. Give me some time to think.
        return -1

    def __9001(self, pick: int) -> int:
        # $script:0831180509001195$
        # - I wonder what the fines are for canceling a bond before it matures... 
        if pick == 0:
            # $script:0831180509001196$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509001197$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001198$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __9002(self, pick: int) -> int:
        # $script:0831180509001199$
        # - Anything happen today, like winning a lottery or inheriting a massive fortune? 
        if pick == 0:
            # $script:0831180509001200$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509001201$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001202$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __9003(self, pick: int) -> int:
        # $script:0831180509001203$
        # - Huh? What?
        if pick == 0:
            # $script:0831180509001204$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509001205$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001206$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __9010(self, pick: int) -> int:
        # $script:0831180509001207$
        # - Aw, man, I'd love to, but my contract expired. Gotta set some boundaries or I'll go broke, ya know?
        return -1

    def __9011(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509001208$
        # - Aw, but our contract just expired.  I told you to extend it ahead of time. You forgot about it, didn't you?
        return -1

    def __9020(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509001209$
        # - The paycheck I get from $map:02000068$ barely covers my living expenses. 
        return -1

    def __9021(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509001210$
        # - $OwnerName$! How are you doing?
        if pick == 0:
            # $script:0831180509001211$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509001212$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001213$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __9040(self, pick: int) -> int:
        # $script:0831180509001214$
        # - Do you have something more to say? 
        if pick == 0:
            # $script:0831180509001215$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509001216$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001217$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __9030(self, pick: int) -> int:
        # $script:0831180509001218$
        # - I don't know what to say. I opened a CD account with Goldus Bank to save money for a ship, but at this rate, I might have to cancel it before it matures. 
        return -1

    def __9031(self, pick: int) -> int:
        # $script:0831180509001219$
        # - I thought being a butler was a stable job. I'm starting to think I was wrong. Guess nothing in life is certain... 
        return -1

    def __9032(self, pick: int) -> int:
        # $script:0831180509001220$
        # - Do you even have enough money to feed yourself? I also get money from $map:02000068$, so I'm not completely broke. At least I can feed myself. I'm worried that you can't.
        return -1

    def __10(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509001221$
        # - Oh, a drink? Sure, what kind were ya thinking?
        return -1

    def __11(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509001222$
        # - Let me know what you need!
        return -1

    def __20(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509001223$
        # - About me? Sure, what do you want to know?
        return -1

    def __21(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509001224$
        # - Ask me anything.
        if pick == 0:
            # $script:0831180509001225$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001226$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001227$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __22(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509001228$
        # - Ask me anything.
        if pick == 0:
            # $script:0831180509001229$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001230$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001231$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509001232$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __30(self, pick: int) -> int:
        # $script:0831180509001233$
        # - What do you want me to tell you? 
        if pick == 0:
            # $script:0831180509001234$
            # - Did anything interesting happen today? 
            # TODO: goto 1000,1100,1200,1300,1400,1500,1600,2000,2100,2200,9011
            self.close()
            return -1
        elif pick == 1:
            # $script:0831180509001235$
            # - Let's talk about adventures!
            # TODO: goto 3000,3100,3200,4000,4100,9011
            self.close()
            return -1
        elif pick == 2:
            # $script:0831180509001236$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000,5100,6000,7000,9011
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509001237$
            # - Back.
            # TODO: goto 8040,8050,8060,40,50,60,9040
            self.close()
            return -1
        return -1

    def __31(self, pick: int) -> int:
        # $script:0831180509001238$
        # - Sure, I can tell you whatever you wanna know.
        if pick == 0:
            # $script:0831180509001239$
            # - Did anything interesting happen today? 
            # TODO: goto 1000,1100,1200,1300,1400,1500,1600,2000,2100,2200,9011
            self.close()
            return -1
        elif pick == 1:
            # $script:0831180509001240$
            # - Let's talk about adventures!
            # TODO: goto 3000,3100,3200,4000,4100,9011
            self.close()
            return -1
        elif pick == 2:
            # $script:0831180509001241$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000,5100,6000,7000,9011
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509001242$
            # - Back.
            # TODO: goto 8040,8050,8060,40,50,60,9040
            self.close()
            return -1
        return -1

    def __32(self, pick: int) -> int:
        # $script:0831180509001243$
        # - $OwnerName$, you don't look well. Are you sure you don't need to rest?
        if pick == 0:
            # $script:0831180509001244$
            # - Did anything interesting happen today? 
            # TODO: goto 1000,1100,1200,1300,1400,1500,1600,2000,2100,2200,9011
            self.close()
            return -1
        elif pick == 1:
            # $script:0831180509001245$
            # - Let's talk about adventures!
            # TODO: goto 3000,3100,3200,4000,4100,9011
            self.close()
            return -1
        elif pick == 2:
            # $script:0831180509001246$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000,5100,6000,7000,9011
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509001247$
            # - Back.
            # TODO: goto 8040,8050,8060,40,50,60,9040
            self.close()
            return -1
        return -1

    def __40(self, pick: int) -> int:
        # $script:0831180509001248$
        # - Is there anything I can do for you? 
        if pick == 0:
            # $script:0831180509001249$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001250$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001251$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __50(self, pick: int) -> int:
        # $script:0831180509001252$
        # - I want to do something fun. Any suggestions?
        if pick == 0:
            # $script:0831180509001253$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001254$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001255$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __60(self, pick: int) -> int:
        # $script:0831180509001256$
        # - I've got too much energy. Maybe I should work out.
        if pick == 0:
            # $script:0831180509001257$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001258$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001259$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __1000(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509001260$
            # - Did you eat? Here, eat this. Wait. Why is your face so gaunt? 
            return 1000
        elif self.index == 1:
            # $script:0831180509001261$
            # - Have you lost weight? This is why you shouldn't skip meals! Here, eat this.
            if pick == 0:
                # $script:0831180509001262$
                # - You cooked this?
                # TODO: goto 1001,1002
                self.close()
                return -1
            elif pick == 1:
                # $script:0831180509001263$
                # - It's delicious!
                # TODO: goto 1011,1012
                self.close()
                return -1
            return -1
        return -1

    def __1001(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001264$
        # - Hah hah, no. Why? Do you want me to? I stay away from the kitchen. The first dish I ever made was terrible, and that scared me off. 
        return -1

    def __1002(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509001265$
            # - Oh, this? The young lady living across the way gave it to me for helping her hammer some nails. I think she lives by herself.
            return 1002
        elif self.index == 1:
            # functionID=1 openTalkReward=True 
            # $script:0831180509001266$
            # - Why are you giving me that look? I didn't ask! I just sort of got that impression.
            return -1
        return -1

    def __1011(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001267$
        # - I know, right? I like it, too! I helped our next door neighbor move some furniture, and his wife gave it to me. She's a great cook.
        return -1

    def __1012(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001268$
        # - The lady living across from us gave this to me for helping her hang some curtains, but it doesn't taste good to me. Try it. Maybe you'll like it.
        return -1

    def __1100(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509001269$
            # - You hungry, $OwnerName$? How about a snack?
            return 1100
        elif self.index == 1:
            # $script:0831180509001270$
            # - Ah, I cooked this. I had some time to kill since today was my day off. I don't know if it tastes good.
            if pick == 0:
                # $script:0831180509001271$
                # - It... doesn't taste good.
                # TODO: goto 1101,1102
                self.close()
                return -1
            elif pick == 1:
                # $script:0831180509001272$
                # - It tastes okay.
                # TODO: goto 1111,1112
                self.close()
                return -1
            return -1
        return -1

    def __1101(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001273$
        # - Oh, it doesn't? But come on, $OwnerName$. I promise it won't make you sick and I cooked it just for you. Could you just try to finish it... for me?
        return -1

    def __1102(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509001274$
            # - What? That can't be right. I followed the recipe so carefully! Give it to me. Let me taste it.
            return 1102
        elif self.index == 1:
            # functionID=1 openTalkReward=True 
            # $script:0831180509001275$
            # - <font color="#909090">(He takes a bite and spits it out immediately.)</font>
            #   Yuck!! Ugh... I'm sorry... 
            return -1
        return -1

    def __1111(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001276$
        # - Oh, really? Here, let me take a bite! Hah hah, I cooked it, but I didn't taste it. My last attempt at cooking wasn't so great. Hah hah hah... 
        return -1

    def __1112(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001277$
        # - Hah hah... I think I've gotten better at cooking. Maybe I should try to cook something else. I'll let you taste it when I do!
        return -1

    def __1200(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509001278$
            # - I don't know if I'm exhausted or have a cold. Either way, I really don't feel good. Take this. I picked it up on my way here from $map:02000068$. I brought you one because I don't want you to catch what I have.
            return 1200
        elif self.index == 1:
            # $script:0831180509001279$
            # - It's good for your health.  If you don't want to take it now, you can take it later.
            if pick == 0:
                # $script:0831180509001280$
                # - How are you feeling?
                # TODO: goto 1211,1212
                self.close()
                return -1
            elif pick == 1:
                # $script:0831180509001281$
                # - Thank you.
                # TODO: goto 1201,1202
                self.close()
                return -1
            return -1
        return -1

    def __1201(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001282$
        # - You're welcome. You should stay away from me until I get better. I don't want you to get sick because of me.
        return -1

    def __1202(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001283$
        # - Sure. You should eat well and get plenty of rest. Ugh, being sick is the worst. It always makes me miss my parents. 
        return -1

    def __1211(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001284$
        # - What, are you worried about me? Hah hah, it's no big deal. I'll be all right. I just need some rest.
        return -1

    def __1212(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001285$
        # - Aww, I'm feeling a bit achy... and cold too. But don't worry. I took some medicine. I'll feel better soon.
        return -1

    def __1300(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509001286$
            # - I picked up some food on my way here from $map:02000069$. I was so hungry when I got off my other job, I just had to eat, so I ate mine there.
            return 1300
        elif self.index == 1:
            # $script:0831180509001287$
            # - Mrs. $npc:11000453[gender:1]$ is the best cook I know. The dish I tried was so good, I had to bring you some, too! 
            if pick == 0:
                # $script:0831180509001288$
                # - Thanks.
                # TODO: goto 1311,1312
                self.close()
                return -1
            elif pick == 1:
                # $script:0831180509001289$
                # - I'm not really hungry.
                # TODO: goto 1301,1302
                self.close()
                return -1
            return -1
        return -1

    def __1301(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001290$
        # - Oh, you're not? I wouldn't have bought it if you told me... 
        return -1

    def __1302(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001291$
        # - Huh? Why not? Don't tell me you're on a diet, because you already look perfect!
        return -1

    def __1311(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001292$
        # - I know you'll love it. Come on, take a bite!
        return -1

    def __1312(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001293$
        # - Hah hah, you're welcome. Watching you eat it, I want to eat it again. Can I have a bite? 
        return -1

    def __1400(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509001294$
            # - Hah hah! Do you know what this is? It's a prize I won in an event! It pays off to be strong, ya know!
            return 1400
        elif self.index == 1:
            # $script:0831180509001295$
            # - I've participated in so many events that I know exactly what to do to win them.
            if pick == 0:
                # $script:0831180509001296$
                # - Can I have your prize?
                # TODO: goto 1401,1402
                self.close()
                return -1
            elif pick == 1:
                # $script:0831180509001297$
                # - What kind of event did you win?
                # TODO: goto 1411,1412
                self.close()
                return -1
            return -1
        return -1

    def __1401(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001298$
        # - But... it's mine. Get your own by winning your own event.
        return -1

    def __1402(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001299$
        # - Huh? No. I want to sell this and save up the money.
        return -1

    def __1411(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509001300$
            # - It's called $map:61000006$. I can give you a tip. 
            return 1411
        elif self.index == 1:
            # functionID=1 openTalkReward=True 
            # $script:0831180509001301$
            # - When you're on the path, look around carefully. You'll find moving platforms. They're the key to winning the event. I'll show them to you later.
            return -1
        return -1

    def __1412(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001302$
        # - I won in $map:61000004$! Have you tried it? For me, moving from one disconnected ladder to another was the biggest challenge.
        return -1

    def __1500(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509001303$
            # - Our upstairs neighbor moved out today. He's been a pretty good neighbor, so I helped him move his furniture.
            return 1500
        elif self.index == 1:
            # $script:0831180509001304$
            # - He left a lot of things behind. Some of it looked pretty good, so I brought this with me. What do you think? 
            if pick == 0:
                # $script:0831180509001305$
                # - Why did you bring home trash?
                # TODO: goto 1501,1502
                self.close()
                return -1
            elif pick == 1:
                # $script:0831180509001306$
                # - Nice find! Good work!
                # TODO: goto 1511,1512
                self.close()
                return -1
            return -1
        return -1

    def __1501(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001307$
        # - Trash? That's harsh. Just because he didn't want this doesn't mean it's trash.
        return -1

    def __1502(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001308$
        # - Haven't you heard? One man's trash is another man's treasure. It'd cost quite a lot to buy this new.
        return -1

    def __1511(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001309$
        # - All it needed was a bit of dusting, and it's just like new! Where do you want me to put it? 
        return -1

    def __1512(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001310$
        # - Actually, it was broken in a couple spots, but I fixed it right up, and now you can't even tell! Piece of cake.
        return -1

    def __1600(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509001311$
            # - Hey, I picked up this $item:90000001$ on my way here from $map:02000068$. You can have it. I know it's not much.
            return 1600
        elif self.index == 1:
            # $script:0831180509001312$
            # - I live here, too, you know. And I don't pay rent, so...
            if pick == 0:
                # $script:0831180509001313$
                # - Thanks.
                # TODO: goto 1611,1612
                self.close()
                return -1
            elif pick == 1:
                # $script:0831180509001314$
                # - You have any more?
                # TODO: goto 1601,1602
                self.close()
                return -1
            return -1
        return -1

    def __1601(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001315$
        # - Huh? More? That's all I got. Sorry. And hey, maybe I'll just keep all the $item:90000001$ I find from now on, if you're going to be so ungrateful. 
        return -1

    def __1602(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001316$
        # - You want more? But that's all I got today. Hey, I you bring stuff I find all the time.
        return -1

    def __1611(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001317$
        # - You're welcome. I'm sorry I don't have more to give you. I want to help but you know my situation. Every spare meso goes towards my new ship. 
        return -1

    def __1612(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001318$
        # - Ah, it's no big deal. I've got a knack for finding dropped items. I'll bring you more later.
        return -1

    def __2000(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509001319$
            # - Welcome. Nothing much happened today. How are you? If you're tired, go get some rest. I'll take care of the housework.
            return 2000
        elif self.index == 1:
            # $script:0831180509001320$
            # - Oh, I found some torn clothes while folding laundry. What did you do that shredded your clothes like that? Are you sure you're not bleeding somewhere?
            return 2000
        elif self.index == 2:
            # $script:0831180509001321$
            # - If you're hurt, don't try to hide it. Just go to the hospital. You shouldn't worry about money when you're sick. All right?
            return -1
        return -1

    def __2100(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509001322$
            # - Well, I cleaned the house and worked out as usual. I feel off if I don't work out every day. 
            return 2100
        elif self.index == 1:
            # $script:0831180509001323$
            # - Being the captain of a ship is not easy. I have to build up my strength to sail out to sea. Things will be especially tough when the waves are high.
            return 2100
        elif self.index == 2:
            # $script:0831180509001324$
            # - Speaking of which, $OwnerName$, how'd you like to work out with me? Health is the most important thing, after all!
            return -1
        return -1

    def __2200(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509001325$
            # - You want something to drink? Sure, I was just working out.
            return 2200
        elif self.index == 1:
            # $script:0831180509001326$
            # - Huh? Do I smell? Sorry. I'll take a shower after you leave.
            return 2200
        elif self.index == 2:
            # $script:0831180509001327$
            # - We're friends, but... I don't know, I don't want to make you uncomfortable.
            return -1
        return -1

    def __3000(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509001328$
            # - $OwnerName$, you know how it's been really windy out at sea not far from $map:02000062$? Well, it turns out the weather has been strange all over the world.
            return 3000
        elif self.index == 1:
            # $script:0831180509001329$
            # - I went to $map:02000069$ and met $npc:11000455[gender:0]$. He told me there was a blizzard in some temperate plains and that it poured in a desert where it hasn't rained for decades.
            return 3000
        elif self.index == 2:
            # $script:0831180509001330$
            # - Wear warm layers when you go out, so you're prepared. Me? I'm all right. I mostly stay inside, plus I'm strong because I work out every day.
            return 3000
        elif self.index == 3:
            # functionID=1 openTalkReward=True 
            # $script:0831180509001331$
            # - Anyway, sometimes when I think about what you do out there, I feel, you know, upset. You know what I mean, right?
            return -1
        return -1

    def __3100(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509001332$
            # - Have I told you about $npcName:11000444[gender:0]$? I loved "$npcName:11000444[gender:0]$'s Travels" so much I read it until the pages wore out. He's my hero!
            return 3100
        elif self.index == 1:
            # $script:0831180509001333$
            # - I just heard that he's on Victoria Island right now! He was apparently stranded by a mysterious storm. He must be getting ready to get back on his journey by now.
            return 3100
        elif self.index == 2:
            # $script:0831180509001334$
            # - Mm... I thought about asking him to let me tag along. "$npcName:11000444[gender:0]$'s Travels" changed my life, you know.
            return 3100
        elif self.index == 3:
            # functionID=1 openTalkReward=True 
            # $script:0831180509001335$
            # - But then I thought to myself, what I really want is to be the hero of "$MaidName$'s Travels." You get what I mean?
            return -1
        return -1

    def __3200(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509001336$
            # - There's a guy named $npcName:11000022[gender:0]$ in $map:02000062$. He always says he wants to go on an adventure, but I'm not sure if he means it.
            return 3200
        elif self.index == 1:
            # $script:0831180509001337$
            # - I don't think he's saving money to buy a ship like I am, either. I have a feeling he's all talk.
            return 3200
        elif self.index == 2:
            # functionID=1 openTalkReward=True 
            # $script:0831180509001338$
            # - Why am I talking about $npcName:11000022[gender:0]$, you ask? Because I need your opinion. Should I accept him into my crew?
            return -1
        return -1

    def __4000(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509001339$
            # - Sigh... I can't think about adventures right now. $OwnerName$, today...
            return 4000
        elif self.index == 1:
            # $script:0831180509001340$
            # - I had just gotten out of the shower and was wearing nothing except a towel around my waist, when someone opened the door and barged in. 
            return 4000
        elif self.index == 2:
            # $script:0831180509001341$
            # - At first, I thought it was you, but it was actually the lady from next door. Something is not right with her. I'm grateful for the food she give me sometimes, but... 
            return 4000
        elif self.index == 3:
            # $script:0831180509001342$
            # - The way she looks at me makes my hair stand on end. $OwnerName$, can we move?
            return -1
        return -1

    def __4100(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509001343$
            # - I expected this, but working two jobs is not easy. I like that I have enough money to save to buy a ship, but I'm so busy that I don't have time to actually plan the adventure. There's no end to the housework.
            return 4100
        elif self.index == 1:
            # $script:0831180509001344$
            # - I washed the comforters today. Not with a washing machine, though. I just throw them into the bathtub and press them by foot.
            return 4100
        elif self.index == 2:
            # $script:0831180509001345$
            # - It's a ton of fun, and also good exercise. $OwnerName$, you should try it with me next time.
            return -1
        return -1

    def __5000(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509001346$
            # - I was reluctant about being a male housekeeper, but it turned out I'm really good at it. I mean it.
            return 5000
        elif self.index == 1:
            # $script:0831180509001347$
            # - When you mop, you have to put a some real effort into it to get the floor sparkling clean, or else you're just spreading water around. Same with ironing. You have to press the iron hard to smooth all the wrinkles at once.
            return 5000
        elif self.index == 2:
            # $script:0831180509001348$
            # - Cooking also requires the constant kneading of flour, and kneading is tough, even for strong men. That's why tough men are better at housework.
            return -1
        return -1

    def __5100(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509001349$
            # - One day, I'm going to buy a ship and sail out to sea. Of course, I'll have a crew, too!
            return 5100
        elif self.index == 1:
            # $script:0831180509001350$
            # - I'll be Captain $MaidName$. Doesn't that roll off the tongue nicely? Hah hah hah! I can't wait to go on an adventure like $npcName:11000444[gender:0]$!
            return 5100
        elif self.index == 2:
            # $script:0831180509001351$
            # - Did you know there are many small islands around Victoria Island? Some are uninhabited, and who knows? Maybe they have treasures hidden on them!
            return 5100
        elif self.index == 3:
            # $script:0831180509001352$
            # - If I find enough treasure, I can buy a bigger ship and have a bigger crew. Then I'll be able to sail farther out to the sea and experience all the wonderful things I read in "Colombo's Travels."
            return 5100
        elif self.index == 4:
            # $script:0831180509001353$
            # - Merfolk are real, did you know that? Ooh, so are ghost ships hidden deep amidst heavy fog! And squid as tall as buildings! Those are real, too!
            return 5100
        elif self.index == 5:
            # $script:0831180509001354$
            # - When I'm out on my adventures, I might discover a new continent. Then I'd have to name it. Oh, hmm, I'd better start thinking about names... 
            return -1
        return -1

    def __6000(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509001355$
            # - I don't have a hometown. It sounds strange, but I really don't, because I was born at sea.
            return 6000
        elif self.index == 1:
            # $script:0831180509001356$
            # - My parents were international traders. They sailed to many different countries. I was born while they were sailing. That's why I don't have a hometown. 
            return 6000
        elif self.index == 2:
            # $script:0831180509001357$
            # - So I have no place to return to. I didn't feel like I belonged anywhere, until... 
            return 6000
        elif self.index == 3:
            # $script:0831180509001358$
            # - Until I came to live with you in this house. It's kind of nice having a place to call home. Just saying.
            return -1
        return -1

    def __7000(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509001359$
            # - Since birth, I'd traveled the world with my parents. A few years ago, I decided to strike out on my own. Why? Because I was an adult!
            return 7000
        elif self.index == 1:
            # $script:0831180509001360$
            # - I said goodbye and left them at the Victoria Island dock. I was itching to go on an adventure of my own, but I didn't have enough money to buy a ship. 
            return 7000
        elif self.index == 2:
            # $script:0831180509001361$
            # - Then I got to know about Helping Hands, so I took a training course. I took the guide course, and since I have experience in sailing, I was able to get a job with $map:02000068$ in $map:02000062$.
            return 7000
        elif self.index == 3:
            # $script:0831180509001362$
            # - Lately, the sea has been so rough. Not many ships are coming to $map:02000062$ and that slowed down my job considerably. That doesn't mean I get paid less, but still.
            return 7000
        elif self.index == 4:
            # $script:0831180509001363$
            # - Since I had more time than before, I decided to take on another job. I needed money. Didn't I tell you? Ships are not cheap. 
            return 7000
        elif self.index == 5:
            # $script:0831180509001364$
            # - I thought housekeeping was something I could do. Although I didn't take the housekeeping course at Helping Hands, I was a graduate, so the company helped me get a job. The result? I couldn't ask for more!
            return -1
        return -1

    def __100(self, pick: int) -> int:
        # $script:0831180509001365$
        # - Mm? Who are you? Are you here to see $OwnerName$?
        if pick == 0:
            # $script:0831180509001366$
            # - Yep!
            # TODO: goto 101,102
            self.close()
            return -1
        elif pick == 1:
            # $script:0831180509001367$
            # - Nope!
            # TODO: goto 103,104
            self.close()
            return -1
        elif pick == 2:
            # $script:0831180509001368$
            # - Who are you?
            # TODO: goto 105,106
            self.close()
            return -1
        return -1

    def __101(self, pick: int) -> int:
        # $script:0831180509001369$
        # - Then do you think maybe you're talking to the wrong person?
        return -1

    def __102(self, pick: int) -> int:
        # $script:0831180509001370$
        # - Why didn't you say so? I don't have anything to give you, but make yourself at home.
        return -1

    def __103(self, pick: int) -> int:
        # $script:0831180509001371$
        # - Well, then did you come to look around the house? There's not much to see, but knock yourself out.
        return -1

    def __104(self, pick: int) -> int:
        # $script:0831180509001372$
        # - You don't even know $OwnerName$? Wow, you must have too much time on your hands. Well, stay as long as you want.
        return -1

    def __105(self, pick: int) -> int:
        # $script:0831180509001373$
        # - Call me $MaidName$. But don't ask me any other questions.
        return -1

    def __106(self, pick: int) -> int:
        # $script:0831180509001374$
        # - I'm $MaidName$. Haven't you seen a male servant before?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (1, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (2, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (3, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (4, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (5, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (6, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (9, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (8000, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (8001, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (8010, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (8011, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (8020, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (8021, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (8040, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (8050, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (8060, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (8900, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (8901, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (8910, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (8999, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (9001, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (9002, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (9003, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (9010, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (9011, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (9020, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (9021, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (9040, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (9030, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (9031, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (9032, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (11, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (21, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (22, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (60, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (1000, 0):
            return Option.NEXT
        elif (self.state, self.index) == (1000, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (1001, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1002, 0):
            return Option.NEXT
        elif (self.state, self.index) == (1002, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (1011, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1012, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1100, 0):
            return Option.NEXT
        elif (self.state, self.index) == (1100, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (1101, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1102, 0):
            return Option.NEXT
        elif (self.state, self.index) == (1102, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (1111, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1112, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1200, 0):
            return Option.NEXT
        elif (self.state, self.index) == (1200, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (1201, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1202, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1211, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1212, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1300, 0):
            return Option.NEXT
        elif (self.state, self.index) == (1300, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (1301, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1302, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1311, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1312, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1400, 0):
            return Option.NEXT
        elif (self.state, self.index) == (1400, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (1401, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1402, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1411, 0):
            return Option.NEXT
        elif (self.state, self.index) == (1411, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (1412, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1500, 0):
            return Option.NEXT
        elif (self.state, self.index) == (1500, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (1501, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1502, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1511, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1512, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1600, 0):
            return Option.NEXT
        elif (self.state, self.index) == (1600, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (1601, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1602, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1611, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1612, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (2000, 0):
            return Option.NEXT
        elif (self.state, self.index) == (2000, 1):
            return Option.NEXT
        elif (self.state, self.index) == (2000, 2):
            return Option.CLOSE
        elif (self.state, self.index) == (2100, 0):
            return Option.NEXT
        elif (self.state, self.index) == (2100, 1):
            return Option.NEXT
        elif (self.state, self.index) == (2100, 2):
            return Option.CLOSE
        elif (self.state, self.index) == (2200, 0):
            return Option.NEXT
        elif (self.state, self.index) == (2200, 1):
            return Option.NEXT
        elif (self.state, self.index) == (2200, 2):
            return Option.CLOSE
        elif (self.state, self.index) == (3000, 0):
            return Option.NEXT
        elif (self.state, self.index) == (3000, 1):
            return Option.NEXT
        elif (self.state, self.index) == (3000, 2):
            return Option.NEXT
        elif (self.state, self.index) == (3000, 3):
            return Option.CLOSE
        elif (self.state, self.index) == (3100, 0):
            return Option.NEXT
        elif (self.state, self.index) == (3100, 1):
            return Option.NEXT
        elif (self.state, self.index) == (3100, 2):
            return Option.NEXT
        elif (self.state, self.index) == (3100, 3):
            return Option.CLOSE
        elif (self.state, self.index) == (3200, 0):
            return Option.NEXT
        elif (self.state, self.index) == (3200, 1):
            return Option.NEXT
        elif (self.state, self.index) == (3200, 2):
            return Option.CLOSE
        elif (self.state, self.index) == (4000, 0):
            return Option.NEXT
        elif (self.state, self.index) == (4000, 1):
            return Option.NEXT
        elif (self.state, self.index) == (4000, 2):
            return Option.NEXT
        elif (self.state, self.index) == (4000, 3):
            return Option.CLOSE
        elif (self.state, self.index) == (4100, 0):
            return Option.NEXT
        elif (self.state, self.index) == (4100, 1):
            return Option.NEXT
        elif (self.state, self.index) == (4100, 2):
            return Option.CLOSE
        elif (self.state, self.index) == (5000, 0):
            return Option.NEXT
        elif (self.state, self.index) == (5000, 1):
            return Option.NEXT
        elif (self.state, self.index) == (5000, 2):
            return Option.CLOSE
        elif (self.state, self.index) == (5100, 0):
            return Option.NEXT
        elif (self.state, self.index) == (5100, 1):
            return Option.NEXT
        elif (self.state, self.index) == (5100, 2):
            return Option.NEXT
        elif (self.state, self.index) == (5100, 3):
            return Option.NEXT
        elif (self.state, self.index) == (5100, 4):
            return Option.NEXT
        elif (self.state, self.index) == (5100, 5):
            return Option.CLOSE
        elif (self.state, self.index) == (6000, 0):
            return Option.NEXT
        elif (self.state, self.index) == (6000, 1):
            return Option.NEXT
        elif (self.state, self.index) == (6000, 2):
            return Option.NEXT
        elif (self.state, self.index) == (6000, 3):
            return Option.CLOSE
        elif (self.state, self.index) == (7000, 0):
            return Option.NEXT
        elif (self.state, self.index) == (7000, 1):
            return Option.NEXT
        elif (self.state, self.index) == (7000, 2):
            return Option.NEXT
        elif (self.state, self.index) == (7000, 3):
            return Option.NEXT
        elif (self.state, self.index) == (7000, 4):
            return Option.NEXT
        elif (self.state, self.index) == (7000, 5):
            return Option.CLOSE
        elif (self.state, self.index) == (100, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (101, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (102, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (103, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (104, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (105, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (106, 0):
            return Option.CLOSE
        return Option.NONE
