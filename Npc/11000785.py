""" 11000785: Marmut """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([1, 2, 3, 4, 5, 6, 9001, 9002, 9003, 100])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180509003920$
        # - Well, well...
        return None # TODO

    def __1(self, pick: int) -> int:
        # $script:0831180509003921$
        # - Hi, $OwnerName$, what can I do for you?
        if pick == 0:
            # $script:0831180509003922$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509003923$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003924$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __2(self, pick: int) -> int:
        # $script:0831180509003925$
        # - Today is quite wonderful, isn't it?
        if pick == 0:
            # $script:0831180509003926$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509003927$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003928$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __3(self, pick: int) -> int:
        # $script:0831180509003929$
        # - Hmm... This might be a problem... Maybe?
        if pick == 0:
            # $script:0831180509003930$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509003931$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003932$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __4(self, pick: int) -> int:
        # $script:0831180509003933$
        # - Hi, $OwnerName$, what can I do for you?
        if pick == 0:
            # $script:0831180509003934$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509003935$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003936$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509003937$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __5(self, pick: int) -> int:
        # $script:0831180509003938$
        # - Today is quite wonderful, isn't it?
        if pick == 0:
            # $script:0831180509003939$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509003940$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003941$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509003942$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __6(self, pick: int) -> int:
        # $script:0831180509003943$
        # - Hmm... This might be a problem... Maybe?
        if pick == 0:
            # $script:0831180509003944$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509003945$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003946$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509003947$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __9(self, pick: int) -> int:
        # $script:0831180509003948$
        # - You want to pay me?
        #   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
        if pick == 0:
            # $script:0831180509003949$
            # - Let me think about it some more.
            # TODO: goto 8040,8050,8060,9040
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509003950$
            # - (Pay $MaidSalary$.)
            # TODO: goto 8000,8001,8010,8011,8901
            # TODO: gotoFail 8900,8910
            return 8900,8910
        return -1

    def __8000(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003951$
        # - Are you sure you want to pay me already? I won't stop you if you insist, but please make sure people know I didn't request it. 
        return -1

    def __8001(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003952$
        # - I got paid! Hmm, should I ask $npcName:11000160[gender:1]$ out for lunch? What do you think? 
        return -1

    def __8010(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003953$
        # - Where did you get so much money? Well, I'm not complaining... 
        return -1

    def __8011(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003954$
        # - Er, last I checked, you didn't have enough money. You d-didn't do anything illegal to get this money, did you? Please let it be known that I never once nagged you for my paycheck, $OwnerName$.
        return -1

    def __8020(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509003955$
        # - Excuse me, $OwnerName$. Our employment contract expires in a few days. Just wanted you to know. 
        return -1

    def __8021(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509003956$
        # - Ah, well... I-I'm just saying... 
        if pick == 0:
            # $script:0831180509003957$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509003958$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003959$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509003960$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8040(self, pick: int) -> int:
        # $script:0831180509003961$
        # - Why am I so indecisive?!
        if pick == 0:
            # $script:0831180509003962$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509003963$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003964$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509003965$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8050(self, pick: int) -> int:
        # $script:0831180509003966$
        # - A housekeeper guard is a rather unusual combo, isn't it?
        if pick == 0:
            # $script:0831180509003967$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509003968$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003969$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509003970$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8060(self, pick: int) -> int:
        # $script:0831180509003971$
        # - Was there something else you needed?
        if pick == 0:
            # $script:0831180509003972$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509003973$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003974$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509003975$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8900(self, pick: int) -> int:
        # $script:0831180509003976$
        # - $OwnerName$, are you going through a hard time? This isn't enough... But before you give me a single meso, have you thought you whether you should even pay me at all?
        return -1

    def __8901(self, pick: int) -> int:
        # $script:0831180509003977$
        # - Ah... $OwnerName$... You already paid me this month. Now I'm not sure whether to accept or not...
        return -1

    def __8910(self, pick: int) -> int:
        # $script:0831180509003978$
        # - It's past my payday, but you don't seem to have the money. I'm not sure whether I should ask for my pay or not... 
        return -1

    def __8999(self, pick: int) -> int:
        # $script:0831180509003979$
        # - As the old saying goes, "don't do something unless you're absolutely certain." It seems like you weren't one hundred percent certain. Why don't you try again?
        return -1

    def __9001(self, pick: int) -> int:
        # $script:0831180509003980$
        # - Hmm... What do I do? ...Huh? Oh, nothing!
        if pick == 0:
            # $script:0831180509003981$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509003982$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003983$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __9002(self, pick: int) -> int:
        # $script:0831180509003984$
        # - Should I do something to keep myself busy? Or should I just keep loafing around? Hmm... 
        if pick == 0:
            # $script:0831180509003985$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509003986$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003987$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __9003(self, pick: int) -> int:
        # $script:0831180509003988$
        # - Should I keep doing this or not? I don't know... 
        if pick == 0:
            # $script:0831180509003989$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509003990$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003991$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __9010(self, pick: int) -> int:
        # $script:0831180509003992$
        # - How should I word this delicately? Ahem, my contract has expired. I don't work for free! Whew, I said it... 
        return -1

    def __9011(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509003993$
        # - Hmm, I need to tell $male:him,female:her$ that our contract expired but $male:he,female:she$ just won't stop talking. Is that a strategic ploy? Oh, ahem, you heard me? Well... our contract has expired.
        return -1

    def __9020(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509003994$
        # - I got some much-needed rest over the last $MaidPassedDay$, and look how refreshed I look now! 
        return -1

    def __9021(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509003995$
        # - Th-that doesn't mean I want to rest forever... 
        if pick == 0:
            # $script:0831180509003996$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509003997$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003998$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __9040(self, pick: int) -> int:
        # $script:0831180509003999$
        # - I don't know what to do... 
        if pick == 0:
            # $script:0831180509004000$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509004001$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004002$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __9030(self, pick: int) -> int:
        # $script:0831180509004003$
        # - I've been thinking, $OwnerName$. Maybe you should wait until you're rich to pay me. I don't want you to go hungry, you know?
        return -1

    def __9031(self, pick: int) -> int:
        # $script:0831180509004004$
        # - Hmm, I can't stand such a messy house, but I'm not a charity, either. I don't think it's right to work without payment. $OwnerName$, just look at those dust bunnies. Are you really okay living in such filth?
        return -1

    def __9032(self, pick: int) -> int:
        # $script:0831180509004005$
        # - $OwnerName$, if you don't pay your rent, you'll lose your house, and I'll lose my job. But if you do pay your rent... you won't have enough left to pay me. Hmmmm...
        return -1

    def __10(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004006$
        # - Who says guards can't cut gems, even if it's just a hobby?
        return -1

    def __11(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004007$
        # - Tell me whatever you like.
        return -1

    def __20(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004008$
        # - Since you asked, I can tell you, but don't complain if you find it boring.
        return -1

    def __21(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004009$
        # - How can I help you?
        if pick == 0:
            # $script:0831180509004010$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004011$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004012$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __22(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004013$
        # - How can I help you?
        if pick == 0:
            # $script:0831180509004014$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004015$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004016$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509004017$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __30(self, pick: int) -> int:
        # $script:0831180509004018$
        # - This is... troublesome...
        if pick == 0:
            # $script:0831180509004019$
            # - Anything interesting happen today?
            # TODO: goto 1000,1100,2000,2100,2200,9011
            self.close()
            return -1
        elif pick == 1:
            # $script:0831180509004020$
            # - Tell me about the Royal Guard!
            # TODO: goto 3000,3100,4000,4100,9011
            self.close()
            return -1
        elif pick == 2:
            # $script:0831180509004021$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000,5100,6000,7000,9011
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509004022$
            # - Back.
            # TODO: goto 8040,8050,8060,40,50,60,9040
            self.close()
            return -1
        return -1

    def __31(self, pick: int) -> int:
        # $script:0831180509004023$
        # - Hmm, what should I do?
        if pick == 0:
            # $script:0831180509004024$
            # - Anything interesting happen today?
            # TODO: goto 1000,1100,2000,2100,2200,9011
            self.close()
            return -1
        elif pick == 1:
            # $script:0831180509004025$
            # - Tell me about the Royal Guard!
            # TODO: goto 3000,3100,4000,4100,9011
            self.close()
            return -1
        elif pick == 2:
            # $script:0831180509004026$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000,5100,6000,7000,9011
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509004027$
            # - Back.
            # TODO: goto 8040,8050,8060,40,50,60,9040
            self.close()
            return -1
        return -1

    def __32(self, pick: int) -> int:
        # $script:0831180509004028$
        # - I don't know what to do... 
        if pick == 0:
            # $script:0831180509004029$
            # - Anything interesting happen today?
            # TODO: goto 1000,1100,2000,2100,2200,9011
            self.close()
            return -1
        elif pick == 1:
            # $script:0831180509004030$
            # - Tell me about the Royal Guard!
            # TODO: goto 3000,3100,4000,4100,9011
            self.close()
            return -1
        elif pick == 2:
            # $script:0831180509004031$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000,5100,6000,7000,9011
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509004032$
            # - Back.
            # TODO: goto 8040,8050,8060,40,50,60,9040
            self.close()
            return -1
        return -1

    def __40(self, pick: int) -> int:
        # $script:0831180509004033$
        # - Why am I so indecisive?!
        if pick == 0:
            # $script:0831180509004034$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004035$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004036$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __50(self, pick: int) -> int:
        # $script:0831180509004037$
        # - A housekeeper guard is a rather unusual combo, isn't it?
        if pick == 0:
            # $script:0831180509004038$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004039$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004040$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __60(self, pick: int) -> int:
        # $script:0831180509004041$
        # - Was there something else you needed?
        if pick == 0:
            # $script:0831180509004042$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004043$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004044$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __1000(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509004045$
            # - Come to think of it, I'm forgetting something! Or... maybe not? 
            return 1000
        elif self.index == 1:
            # $script:0831180509004046$
            # - It's time I take control of my own life! I'm taking your advice, $OwnerName$!
            return 1000
        elif self.index == 2:
            # $script:0831180509004047$
            # - I'm going to ask $npcName:11000160[gender:1]$ out to eat black noodles with me! I've been in love with her forever. I'm going to tell her how I feel! Right? Should I? I should, shouldn't I?
            if pick == 0:
                # $script:0831180509004048$
                # - Yes, you should!
                # TODO: goto 1011,1012
                self.close()
                return -1
            elif pick == 1:
                # $script:0831180509004049$
                # - Eh, the timing might not be quite right...
                # TODO: goto 1001,1002
                self.close()
                return -1
            return -1
        return -1

    def __1001(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509004050$
        # - Yeah, I think so too. Girls like her don't go for guys like me, hah hah hah...
        return -1

    def __1002(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509004051$
        # - I've waited three years, what's a few more? I can wait as long as needed!
        return -1

    def __1011(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509004052$
        # - You think so? R-r-really? I mean, I do, too! Just let me catch my b-b-breath first!
        return -1

    def __1012(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509004053$
        # - You've given me the courage I needed. Deep breaths. Deeeeeep breaths. Okay, I'm ready! I'm going to do this!
        return -1

    def __1100(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509004054$
            # - I've been doing some serious reflection.
            return 1100
        elif self.index == 1:
            # $script:0831180509004055$
            # - The other guards think I'm too indecisive. Not a day go by where $npcName:11000119[gender:0]$ doesn't scold me. 
            return 1100
        elif self.index == 2:
            # $script:0831180509004056$
            # - Maybe I'm not cut out to be a guard. $OwnerName$, what do you think?
            if pick == 0:
                # $script:0831180509004057$
                # - Yeah, maybe you should give up.
                # TODO: goto 1101,1102
                self.close()
                return -1
            elif pick == 1:
                # $script:0831180509004058$
                # - Are you really giving it your all, though?
                # TODO: goto 1111,1112
                self.close()
                return -1
            return -1
        return -1

    def __1101(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509004059$
        # - Hah hah, you think so? I knew I shouldn't have joined the Royal Guard.
        return -1

    def __1102(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509004060$
        # - Hmmm, let me just... think about it.
        return -1

    def __1111(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509004061$
        # - I feel like you just punched me in the face. Thanks for the pep talk.
        return -1

    def __1112(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509004062$
        # - You're right. I'm ashamed of myself. I've been whining without even trying my best. 
        return -1

    def __2000(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509004063$
            # - I've heard a strange noise outside for the past few hours. I hate ignoring it, but it's not like I can go out and check. 
            return 2000
        elif self.index == 1:
            # $script:0831180509004064$
            # - I can't leave the house unattended, you know? What if we get robbed? I don't want that on my head.
            return 2000
        elif self.index == 2:
            # $script:0831180509004065$
            # - If you want to go investigate the noise yourself, feel free.
            return 2000
        elif self.index == 3:
            # $script:0831180509004066$
            # - But just to be clear, I never asked you to, okay? I don't want that responsibility.
            return -1
        return -1

    def __2100(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509004067$
            # - I wasn't sure if I should tell you, but $npcName:11000119[gender:0]$ stopped by today...
            return 2100
        elif self.index == 1:
            # $script:0831180509004068$
            # - He wanted to know about the recent increase in the number of adventurers fracturing bones in $map:2000118$.
            return 2100
        elif self.index == 2:
            # $script:0831180509004069$
            # - Hey, I never asked anyone to do anything. If they volunteer to investigate the quakes and then trip and break some bones, how is that my fault?
            return 2100
        elif self.index == 3:
            # $script:0831180509004070$
            # - He said he wanted to check out the place himself and then left for $map:2000118$. Ugh, what if $npcName:11000119[gender:0]$ gets hurt too?
            return -1
        return -1

    def __2200(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509004071$
            # - I've been told, if I have time to sit around and fret about things, I should do something to change them. So today, I decided to do just that! ...I wonder if it was the right choice.
            return 2200
        elif self.index == 1:
            # $script:0831180509004072$
            # - A salesman stopped by the house today. Usually, they get annoyed by my indecisiveness and leave, but I was determined to make a purchase today!
            return 2200
        elif self.index == 2:
            # $script:0831180509004073$
            # - He said this bowl had a self-washing feature. Well... see this oil stain?
            return 2200
        elif self.index == 3:
            # $script:0831180509004074$
            # - This is why I shouldn't try new things. Ugh.
            return -1
        return -1

    def __3000(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509004075$
            # - I really admire Captain $npcName:11000119[gender:0]$. He's the reason the people of $map:2000001$ can sleep at night.
            return 3000
        elif self.index == 1:
            # $script:0831180509004076$
            # - People often compare $npcName:11000076[gender:0]$ with $npcName:11000119[gender:0]$, but I think $npcName:11000119[gender:0]$ is better.
            return 3000
        elif self.index == 2:
            # $script:0831180509004077$
            # - It's not because I've seen them fight or anything. It's the way the Empress treats them.
            return 3000
        elif self.index == 3:
            # $script:0831180509004078$
            # - $npcName:11000075[gender:1]$ always looks composed when she talks to $npcName:11000076[gender:0]$. She looks at him with unshakable trust in her eyes.
            return 3000
        elif self.index == 4:
            # $script:0831180509004079$
            # - But she's different in front of $npcName:11000119[gender:0]$. She looks disconcerted and worried. No one else makes her look like that.
            return 3000
        elif self.index == 5:
            # functionID=1 openTalkReward=True 
            # $script:0831180509004080$
            # - In other words, $npcName:11000119[gender:0]$ has the ability to disarm her. Get it, $OwnerName$?
            return -1
        return -1

    def __3100(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509004081$
            # - Hmm, if i had a worthy rival, I'd be way stronger than I am now. Like, $npcName:11000119[gender:0]$!
            return 3100
        elif self.index == 1:
            # $script:0831180509004082$
            # - Did you know there's a rivalry between $npcName:11000119[gender:0]$ and $npcName:11000076[gender:0]$? Everyone in $map:2000001$ knows.
            return 3100
        elif self.index == 2:
            # $script:0831180509004083$
            # - Guard Captain $npcName:11000119[gender:0]$ and Knight Captain $npcName:11000076[gender:0]$ have been best friends since they were kids.
            return 3100
        elif self.index == 3:
            # $script:0831180509004084$
            # - They're both really good at fighting, too. A lot of people have high expectations of them, and everyone thinks of them as rivals.
            return 3100
        elif self.index == 4:
            # $script:0831180509004085$
            # - I don't know if they'd agree, though. One second they're screaming in each others' faces, the next they're fighting enemies, side by side.
            return 3100
        elif self.index == 5:
            # functionID=1 openTalkReward=True 
            # $script:0831180509004086$
            # - Some folks say $npcName:11000169[gender:0]$ at the armory should be my rival, but he has a long way to go. Hmph.
            return -1
        return -1

    def __4000(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509004087$
            # - The Royal Guard is charged with the safely of the entire $map:2000001$ palace.
            return 4000
        elif self.index == 1:
            # $script:0831180509004088$
            # - $map:2000001$ is home to the Empress and the nobility. Not a day goes by without an incident of some sort. We have long, grueling shifts.
            return 4000
        elif self.index == 2:
            # $script:0831180509004089$
            # - Luckily, Captain $npcName:11000119[gender:0]$ has allowed us to pick up work on the side.
            return 4000
        elif self.index == 3:
            # $script:0831180509004090$
            # - The truth is, quite a number of people have filed injury claims against me, and I'm not making enough as a guard to pay them all. Just my luck, you know?
            return -1
        return -1

    def __4100(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509004091$
            # - If you're asking because you're thinking of joining the Royal Guard, I suggest you reconsider.
            return 4100
        elif self.index == 1:
            # $script:0831180509004092$
            # - $npcName:11000119[gender:0]$ is strict. It takes a tremendous amount of determination and effort to train under him.
            return 4100
        elif self.index == 2:
            # $script:0831180509004093$
            # - As for me... Well... 
            return -1
        return -1

    def __5000(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509004094$
            # - When I lived in $map:2000001$, I never imagined I'd join the Royal Guard. But three years ago, my father applied for me, without telling me.
            return 5000
        elif self.index == 1:
            # $script:0831180509004095$
            # - If he didn't, I'd still be living happily in $map:2000001$. Being a guard isn't so bad, I guess...
            return 5000
        elif self.index == 2:
            # $script:0831180509004096$
            # - All I have to do is follow the captain's commands. I don't have to worry about making decisions.
            return 5000
        elif self.index == 3:
            # $script:0831180509004097$
            # - Whenever I can't decide something, someone else comes along and decides for me. What more could I ask for?
            return -1
        return -1

    def __5100(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509004098$
            # - $npcName:11000119[gender:0]$ said we could apply for different responsibilities if we wanted to. I'm getting tired of investigating the quakes in $map:2000118$, so I considered it.
            return 5100
        elif self.index == 1:
            # $script:0831180509004099$
            # - I thought about applying for front gate duties in $map:2000001$, but then realized I didn't want to deal with tourists.
            return 5100
        elif self.index == 2:
            # $script:0831180509004100$
            # - I also didn't want to fight on the front lines in $map:2000146$ because I don't want to get hurt.
            return 5100
        elif self.index == 3:
            # $script:0831180509004101$
            # - I would love to try new things, but when I start thinking about them, I get so worried and can't make up my mind.
            return 5100
        elif self.index == 4:
            # $script:0831180509004102$
            # - Hmmm, I think I'm going to have to mull this over for a week or two.
            return -1
        return -1

    def __6000(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509004103$
            # - Have I told you about $npcName:11000160[gender:1]$? She works in front of $map:2000001$ $map:2000188$ to help travelers find their way.
            return 6000
        elif self.index == 1:
            # $script:0831180509004104$
            # - One time, I was standing in front of $map:2000188$, unable to decide what I should eat for over an hour. Did I want black noodles or spicy noodles? Suddenly $npcName:11000160[gender:1]$ showed up and handed me a bowl of black noodles.
            return 6000
        elif self.index == 2:
            # $script:0831180509004105$
            # - She solved my dilemma so easily! How could I not fall in love with her right then and there? I don't know if $npcName:11000160[gender:1]$ knows how I feel about her, though. 
            return 6000
        elif self.index == 3:
            # $script:0831180509004106$
            # - I miss $npcName:11000160[gender:1]$... I've been trying to decide for hours. Should I go to $map:2000001$ to see her?
            return -1
        return -1

    def __7000(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509004107$
            # - Should I tell her my true feelings? 
            return 7000
        elif self.index == 1:
            # $script:0831180509004108$
            # - You see, I'm not the only one with a major crush on 
            #   $npcName:11000160[gender:1]$. I think $npcName:11000169[gender:0]$ from the armory also likes her. 
            return 7000
        elif self.index == 2:
            # $script:0831180509004109$
            # - If $npcName:11000160[gender:1]$ rejects me, it'll make things so awkward. If she doesn't reject me, things would get weird between me and $npcName:11000169[gender:0]$...
            return 7000
        elif self.index == 3:
            # $script:0831180509004110$
            # - So you understand why I can't decide what to do, right?
            return -1
        return -1

    def __100(self, pick: int) -> int:
        # $script:0831180509004111$
        # - Hmm, you look like a stranger. Oops, should I not have said that?
        if pick == 0:
            # $script:0831180509004112$
            # - What do you mean?
            # TODO: goto 101,102
            self.close()
            return -1
        elif pick == 1:
            # $script:0831180509004113$
            # - I thought the house was empty. My mistake.
            # TODO: goto 103,104
            self.close()
            return -1
        elif pick == 2:
            # $script:0831180509004114$
            # - Who are you?
            # TODO: goto 105,106
            self.close()
            return -1
        return -1

    def __101(self, pick: int) -> int:
        # $script:0831180509004115$
        # - Think about it. If you are a stranger, you might be mad I said that. If you're not a stranger, I just offended the boss's guest. 
        return -1

    def __102(self, pick: int) -> int:
        # $script:0831180509004116$
        # - Ummm... Give me a moment to think how I should respond. I'm not quite sure what to say...
        return -1

    def __103(self, pick: int) -> int:
        # $script:0831180509004117$
        # - Oh, did you? Hmm, what should I do? Let you go, or arrest you for attempted burglary? Hmm...
        return -1

    def __104(self, pick: int) -> int:
        # $script:0831180509004118$
        # - Breaking and entering, huh? But what should I do? Contact the royal guard or arrest you myself? Not quite sure about the protocol here. Let me think about this... 
        return -1

    def __105(self, pick: int) -> int:
        # $script:0831180509004119$
        # - Me? Hmm, should I tell you my name? Or shouldn't I...? 
        return -1

    def __106(self, pick: int) -> int:
        # $script:0831180509004120$
        # - I'm the man in charge of keeping the house secure! Who are you?
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
            return Option.NEXT
        elif (self.state, self.index) == (1000, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (1001, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1002, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1011, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1012, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1100, 0):
            return Option.NEXT
        elif (self.state, self.index) == (1100, 1):
            return Option.NEXT
        elif (self.state, self.index) == (1100, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (1101, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1102, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1111, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1112, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (2000, 0):
            return Option.NEXT
        elif (self.state, self.index) == (2000, 1):
            return Option.NEXT
        elif (self.state, self.index) == (2000, 2):
            return Option.NEXT
        elif (self.state, self.index) == (2000, 3):
            return Option.CLOSE
        elif (self.state, self.index) == (2100, 0):
            return Option.NEXT
        elif (self.state, self.index) == (2100, 1):
            return Option.NEXT
        elif (self.state, self.index) == (2100, 2):
            return Option.NEXT
        elif (self.state, self.index) == (2100, 3):
            return Option.CLOSE
        elif (self.state, self.index) == (2200, 0):
            return Option.NEXT
        elif (self.state, self.index) == (2200, 1):
            return Option.NEXT
        elif (self.state, self.index) == (2200, 2):
            return Option.NEXT
        elif (self.state, self.index) == (2200, 3):
            return Option.CLOSE
        elif (self.state, self.index) == (3000, 0):
            return Option.NEXT
        elif (self.state, self.index) == (3000, 1):
            return Option.NEXT
        elif (self.state, self.index) == (3000, 2):
            return Option.NEXT
        elif (self.state, self.index) == (3000, 3):
            return Option.NEXT
        elif (self.state, self.index) == (3000, 4):
            return Option.NEXT
        elif (self.state, self.index) == (3000, 5):
            return Option.CLOSE
        elif (self.state, self.index) == (3100, 0):
            return Option.NEXT
        elif (self.state, self.index) == (3100, 1):
            return Option.NEXT
        elif (self.state, self.index) == (3100, 2):
            return Option.NEXT
        elif (self.state, self.index) == (3100, 3):
            return Option.NEXT
        elif (self.state, self.index) == (3100, 4):
            return Option.NEXT
        elif (self.state, self.index) == (3100, 5):
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
            return Option.NEXT
        elif (self.state, self.index) == (5000, 3):
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
