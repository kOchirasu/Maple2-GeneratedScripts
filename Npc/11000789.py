""" 11000789: Arita """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([1, 2, 3, 4, 5, 6, 9001, 9002, 9003, 100])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180509004782$
        # - Why are humans so high maintenance?
        return None # TODO

    def __1(self, pick: int) -> int:
        # $script:0831180509004783$
        # - Please! One moment, I'm talking to this zelkova.
        if pick == 0:
            # $script:0831180509004784$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004785$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004786$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __2(self, pick: int) -> int:
        # $script:0831180509004787$
        # - Isn't it a wonderful day?
        if pick == 0:
            # $script:0831180509004788$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004789$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004790$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __3(self, pick: int) -> int:
        # $script:0831180509004791$
        # - Please be careful not to tread on grass or flowers when you walk.
        if pick == 0:
            # $script:0831180509004792$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004793$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004794$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __4(self, pick: int) -> int:
        # $script:0831180509004795$
        # - Please! One moment, I'm talking to this zelkova.
        if pick == 0:
            # $script:0831180509004796$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004797$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004798$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509004799$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __5(self, pick: int) -> int:
        # $script:0831180509004800$
        # - Isn't it a wonderful day?
        if pick == 0:
            # $script:0831180509004801$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004802$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004803$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509004804$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __6(self, pick: int) -> int:
        # $script:0831180509004805$
        # - Please be careful not to tread on grass or flowers when you walk.
        if pick == 0:
            # $script:0831180509004806$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004807$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004808$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509004809$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __9(self, pick: int) -> int:
        # $script:0831180509004810$
        # - Did you just say you're going to pay me?
        #   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
        if pick == 0:
            # $script:0831180509004811$
            # - Never mind.
            # TODO: goto 8040,8050,8060,9040
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004812$
            # - (Pay $MaidSalary$.)
            # TODO: goto 8000,8001,8010,8011,8901
            # TODO: gotoFail 8900,8910
            return 8900,8910
        return -1

    def __8000(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509004813$
        # - Aha, our contract renews every time you pay me, right? That's how human contracts work? I feel like I've learned something new and fascinating about human culture, and that makes me happy!
        return -1

    def __8001(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509004814$
        # - Ah, I know. Accepting this means I accept the extension of our contract. I'm learning so much about you unusual creatures, thanks to you!
        return -1

    def __8010(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509004815$
        # - Keeping a promise made to a human is tough, but I saw it through, didn't I? I feel like I've really accomplished something great. Thanks for the experience!
        return -1

    def __8011(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509004816$
        # - Really? Hehe. I had no idea how difficult it was to be idle all day. Thank you for helping me keep my promise, $OwnerName$!
        return -1

    def __8020(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004817$
        # - $OwnerName$, did you know our employment agreement expires soon?
        return -1

    def __8021(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004818$
        # - Why are humans so high maintenance?
        if pick == 0:
            # $script:0831180509004819$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004820$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004821$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509004822$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8040(self, pick: int) -> int:
        # $script:0831180509004823$
        # - Mm? Do you have something else to tell me?
        if pick == 0:
            # $script:0831180509004824$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004825$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004826$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509004827$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8050(self, pick: int) -> int:
        # $script:0831180509004828$
        # - Please! One moment, I'm talking to this zelkova.
        if pick == 0:
            # $script:0831180509004829$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004830$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004831$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509004832$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8060(self, pick: int) -> int:
        # $script:0831180509004833$
        # - Please be careful not to tread on grass or flowers when you walk.
        if pick == 0:
            # $script:0831180509004834$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004835$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004836$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509004837$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8900(self, pick: int) -> int:
        # $script:0831180509004838$
        # - Don't be embarrassed. You can pay me whenever you have the money.
        return -1

    def __8901(self, pick: int) -> int:
        # $script:0831180509004839$
        # - Hehe, you already paid me this month, $OwnerName$!
        return -1

    def __8910(self, pick: int) -> int:
        # $script:0831180509004840$
        # - You're trying to help me keep my promise. I appreciate that so much, but it won't work if you don't have enough money. Thank you for trying.
        return -1

    def __8999(self, pick: int) -> int:
        # $script:0831180509004841$
        # - Oh, how did you do that? Neat! Show me again!
        return -1

    def __9001(self, pick: int) -> int:
        # $script:0831180509004842$
        # - There are some things I just can't do, no matter how hard I try.
        if pick == 0:
            # $script:0831180509004843$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509004844$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004845$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __9002(self, pick: int) -> int:
        # $script:0831180509004846$
        # - Is something wrong?
        if pick == 0:
            # $script:0831180509004847$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509004848$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004849$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __9003(self, pick: int) -> int:
        # $script:0831180509004850$
        # - I want to plant more flowers! You're not interested in that, are you?
        if pick == 0:
            # $script:0831180509004851$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509004852$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004853$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __9010(self, pick: int) -> int:
        # $script:0831180509004854$
        # - Huh? Wait. $OwnerName$, my contract expired...
        return -1

    def __9011(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004855$
        # - I'm so sorry to interrupt, but this is important! Our contract expired! $OwnerName$, please check the contract!
        return -1

    def __9020(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004856$
        # - It's been $MaidPassedDay$ since our contract expired. I may live a long, long life, $OwnerName$, but I want our time together to be meaningful.
        return -1

    def __9021(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004857$
        # - Time never stops, and it never waits for anyone.
        if pick == 0:
            # $script:0831180509004858$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509004859$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004860$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __9040(self, pick: int) -> int:
        # $script:0831180509004861$
        # - Mm... Okay.
        if pick == 0:
            # $script:0831180509004862$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509004863$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004864$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __9030(self, pick: int) -> int:
        # $script:0831180509004865$
        # - $OwnerName$! What happened? Won't you tell me? I know something happened... I thought we were closer than that...
        return -1

    def __9031(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509004866$
            # - Did you know fairies make contracts to use magic and spells? To us, contracts are promises we make in exchange for power. Humans, it seems, mainly use contracts for things involving time and money. When I signed on with Helping Hands, I made a promise to the company about accepting a certain wage.
            return 9031
        elif self.index == 1:
            # $script:0831180509004867$
            # - I would love to do you a favor without anything in return, but that would mean breaking my promise... I made a promise to Helping Hands in exchange for an opportunity to learn more about humans. I hope you can understand that, $OwnerName$.
            return -1
        return -1

    def __9032(self, pick: int) -> int:
        # $script:0831180509004868$
        # - $OwnerName$, you haven't talked to me lately. You didn't use to be like this. Oh, never mind. For a moment, I forgot you were human, hehe!
        return -1

    def __10(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004869$
        # - Mama taught me this! I'm good at it, hehe.
        return -1

    def __11(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004870$
        # - Sure! Anytime.
        return -1

    def __20(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004871$
        # - $OwnerName$, you're the first human I've shared so much with...
        return -1

    def __21(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004872$
        # - Isn't it a wonderful day?
        if pick == 0:
            # $script:0831180509004873$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004874$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004875$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __22(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004876$
        # - Isn't it a wonderful day?
        if pick == 0:
            # $script:0831180509004877$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004878$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004879$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509004880$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __30(self, pick: int) -> int:
        # $script:0831180509004881$
        # - Fairies are good at keeping secrets. You can tell me anything!
        if pick == 0:
            # $script:0831180509004882$
            # - Anything interesting happen today?
            # TODO: goto 1000,1100,2000,2100,2200,9011
            self.close()
            return -1
        elif pick == 1:
            # $script:0831180509004883$
            # - Tell me something about fairies.
            # TODO: goto 3000,3100,4000,4100,9011
            self.close()
            return -1
        elif pick == 2:
            # $script:0831180509004884$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000,5100,6000,7000,9011
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509004885$
            # - Back.
            # TODO: goto 8040,8050,8060,40,50,60,9040
            self.close()
            return -1
        return -1

    def __31(self, pick: int) -> int:
        # $script:0831180509004886$
        # - You look like you have something to say.
        if pick == 0:
            # $script:0831180509004887$
            # - Anything interesting happen today?
            # TODO: goto 1000,1100,2000,2100,2200,9011
            self.close()
            return -1
        elif pick == 1:
            # $script:0831180509004888$
            # - Tell me something about fairies.
            # TODO: goto 3000,3100,4000,4100,9011
            self.close()
            return -1
        elif pick == 2:
            # $script:0831180509004889$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000,5100,6000,7000,9011
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509004890$
            # - Back.
            # TODO: goto 8040,8050,8060,40,50,60,9040
            self.close()
            return -1
        return -1

    def __32(self, pick: int) -> int:
        # $script:0831180509004891$
        # - Sometimes, I wonder how things are back in $map:2000023$.
        if pick == 0:
            # $script:0831180509004892$
            # - Anything interesting happen today?
            # TODO: goto 1000,1100,2000,2100,2200,9011
            self.close()
            return -1
        elif pick == 1:
            # $script:0831180509004893$
            # - Tell me something about fairies.
            # TODO: goto 3000,3100,4000,4100,9011
            self.close()
            return -1
        elif pick == 2:
            # $script:0831180509004894$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000,5100,6000,7000,9011
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509004895$
            # - Back.
            # TODO: goto 8040,8050,8060,40,50,60,9040
            self.close()
            return -1
        return -1

    def __40(self, pick: int) -> int:
        # $script:0831180509004896$
        # - Mm? Do you have something else to tell me?
        if pick == 0:
            # $script:0831180509004897$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004898$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004899$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __50(self, pick: int) -> int:
        # $script:0831180509004900$
        # - Please! One moment, I'm talking to this zelkova.
        if pick == 0:
            # $script:0831180509004901$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004902$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004903$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __60(self, pick: int) -> int:
        # $script:0831180509004904$
        # - Please be careful not to tread on grass or flowers when you walk.
        if pick == 0:
            # $script:0831180509004905$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004906$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004907$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __1000(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509004908$
            # - I can't help it. I just don't trust humans.
            return 1000
        elif self.index == 1:
            # $script:0831180509004909$
            # - I know you're not like the others, $OwnerName$. But... we're just so different.
            return 1000
        elif self.index == 2:
            # $script:0831180509004910$
            # - I know we should all just accept one another, but I can't get used to your kind's disregard for nature or penchant for violence. Am I wrong to feel this way?
            if pick == 0:
                # $script:0831180509004911$
                # - Nah.
                # TODO: goto 1011,1012
                self.close()
                return -1
            elif pick == 1:
                # $script:0831180509004912$
                # - Yeah.
                # TODO: goto 1001,1002
                self.close()
                return -1
            return -1
        return -1

    def __1001(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509004913$
        # - No matter how hard I try, there's just some things I can't do. I don't know if a human could really understand...
        return -1

    def __1002(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509004914$
        # - I thought of all people you'd understand me. Just forget I said anything.
        return -1

    def __1011(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509004915$
        # - Thank you for understanding. All I want is for your kind to stop fighting and to live wisely!
        return -1

    def __1012(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509004916$
        # - $OwnerName$, I knew you'd understand. You're different from the rest.
        return -1

    def __1100(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509004917$
            # - $OwnerName$, I want to ask you something.
            return 1100
        elif self.index == 1:
            # $script:0831180509004918$
            # - I've mentioned a few times that fairies aren't fond of humans.
            return 1100
        elif self.index == 2:
            # $script:0831180509004919$
            # - But what's your opinion, $OwnerName$? Do you like fairies?
            if pick == 0:
                # $script:0831180509004920$
                # - Of course.
                # TODO: goto 1101,1102
                self.close()
                return -1
            elif pick == 1:
                # $script:0831180509004921$
                # - I want to learn more about your species, honestly.
                # TODO: goto 1111,1112
                self.close()
                return -1
            return -1
        return -1

    def __1101(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509004922$
        # - I've heard of humans who said the same thing, then brutally betrayed us. I'm not saying you're like that, but...
        return -1

    def __1102(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509004923$
        # - Just like that? It sounded a little insincere, if you ask me...
        return -1

    def __1111(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509004924$
        # - Ah! You and I are kindred spirits in that regard, $OwnerName$. I'm so happy we met!
        return -1

    def __1112(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509004925$
        # - Yes, I want to learn more about humans, too!
        return -1

    def __2000(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509004926$
            # - I made this pendant with a stone I found in my forest. Pretty, isn't it?
            return 2000
        elif self.index == 1:
            # $script:0831180509004927$
            # - Heh heh, surprised? My mom taught me when I was young. She's a famous craftswoman in $map:02000023$.
            return 2000
        elif self.index == 2:
            # $script:0831180509004928$
            # - But I don't think this is just some ordinary stone. It gives off a strange vibe, like... magic.
            return 2000
        elif self.index == 3:
            # $script:0831180509004929$
            # - I want to know more! I'm going to show it to $npcName:11000031[gender:0]$ tomorrow.
            return -1
        return -1

    def __2100(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509004930$
            # - Yesterday $npcName:11000034[gender:0]$ stopped by. He must have been worried that I'm staying with a human.
            return 2100
        elif self.index == 1:
            # $script:0831180509004931$
            # - He kept urging me to return to the forest, but I told him I can better relate to you than I can to other humans. And it's true. Hehe.
            return 2100
        elif self.index == 2:
            # $script:0831180509004932$
            # - $npcName:11000034[gender:0]$ would agree if he met you. If you ever have business in $map:02000023$, would you give my regards to $npcName:11000034[gender:0]$?
            return -1
        return -1

    def __2200(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509004933$
            # - I prepare food for you every day, but do you really have to eat animals and plants?
            return 2200
        elif self.index == 1:
            # $script:0831180509004934$
            # - Fairies only need one glass of honey milk in the morning and one in the afternoon. Animals and plants are my friends, and I shouldn't eat my friends, right?
            return 2200
        elif self.index == 2:
            # $script:0831180509004935$
            # - You don't need to look so guilty. I know you can't live on just milk like I can.
            return 2200
        elif self.index == 3:
            # $script:0831180509004936$
            # - "Nature makes us what we are." That's what $npcName:11000031[gender:0]$ says. Eat up!
            return -1
        return -1

    def __3000(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509004937$
            # - Humans have long coveted the ancient knowledge of the fairies. They spy on us and try to steal it when we aren't looking. 
            return 3000
        elif self.index == 1:
            # $script:0831180509004938$
            # - Those who do are usually driven to ruin by their own greed!
            return 3000
        elif self.index == 2:
            # $script:0831180509004939$
            # - With the current situation, we've had no choice but to join forces with humans, but that doesn't mean we like you. I've seen some pretty great humans but only a few of you are wise.
            return 3000
        elif self.index == 3:
            # functionID=1 openTalkReward=True 
            # $script:0831180509004940$
            # - The wise humans know their place in the grand scheme of the universe. Then again... I doubt even $npcName:11000075[gender:1]$ is completely free of selfish desires...
            return -1
        return -1

    def __3100(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509004941$
            # - Do all humans allow strangers into their homes? Today, three strangers barged in, but ran off when they saw I was here.
            return 3100
        elif self.index == 1:
            # $script:0831180509004942$
            # - They were surprised, stating that they didn't hear my footsteps. Well, that's because fairies glide instead of stomp.
            return 3100
        elif self.index == 2:
            # functionID=1 openTalkReward=True 
            # $script:0831180509004943$
            # - We don't want to hurt even a single blade of grass. Eeek! There are ants crawling all around your feet! Be careful not to step on them!!
            return -1
        return -1

    def __4000(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509004944$
            # - Have you ever wondered why I don't have wings?
            return 4000
        elif self.index == 1:
            # $script:0831180509004945$
            # - It's because there are all different types of fairies... Tree tree fairies, flower fairies, river fairies, and all sorts of others.
            return 4000
        elif self.index == 2:
            # $script:0831180509004946$
            # - Some have wings, some don't... and some just have one wing... 
            return 4000
        elif self.index == 3:
            # $script:0831180509004947$
            # - Never mind that. My point is, if you ever visit $map:02000023$, make sure you don't ask such a silly question or everyone will laugh at you.
            return -1
        return -1

    def __4100(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509004948$
            # - $npcName:11000284[gender:1]$... She's lost her shoes again. How disgraceful!
            return 4100
        elif self.index == 1:
            # $script:0831180509004949$
            # - I've told her so many times! If she truly loves her shoes, then don't wear them outside of the forest!
            return 4100
        elif self.index == 2:
            # $script:0831180509004950$
            # - Unbelievable! I hope no one helps her this time, so she learns her lesson.
            return 4100
        elif self.index == 3:
            # $script:0831180509004951$
            # - ...But that's wishful thinking. Humans can't resist helping her when she cries, and she knows that.
            return -1
        return -1

    def __5000(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509004952$
            # - Yesterday, the wind told me that trees and flowers are disappearing on the west side of Victoria Island.
            return 5000
        elif self.index == 1:
            # $script:0831180509004953$
            # - I'm guessing it must the area around $map:02000100$. I've never been there, and I'm glad! I couldn't survive even a single day in such a sad place.
            return 5000
        elif self.index == 2:
            # $script:0831180509004954$
            # - Why do humans love to dig? Why do you love tall buildings so much?
            return 5000
        elif self.index == 3:
            # $script:0831180509004955$
            # - You're building homes for yourselves but destroying ours.
            return -1
        return -1

    def __5100(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509004956$
            # - I don't hate all humans. I have great respect for $npc:11000075[gender:1]$ and for $npcName:11000039[gender:1]$.
            return 5100
        elif self.index == 1:
            # $script:0831180509004957$
            # - I have many things I can learn from $npcName:11000042[gender:1]$. I think there are only a handful of fairies who possess more ancient knowledge than he does.
            return 5100
        elif self.index == 2:
            # $script:0831180509004958$
            # - Humans and fairies are so different. I'm having a hard time getting used to you. We haven't interacted with each other for a long time. You can't expect for us to become friends overnight.
            return -1
        return -1

    def __6000(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509004959$
            # - Soon it'll be my birthday. Let's celebrate together. And don't even think to ask how many candles we'll need...
            return 6000
        elif self.index == 1:
            # $script:0831180509004960$
            # - Oh, fine, since you're my friend, I'll give you a hint.
            return 6000
        elif self.index == 2:
            # $script:0831180509004961$
            # - I just want one candle. I'm not even a hundred yet! I'm pretty young for the fairfolk.
            return 6000
        elif self.index == 3:
            # $script:0831180509004962$
            # - Fairies live a lot longer than humans, you know.
            return 6000
        elif self.index == 4:
            # $script:0831180509004963$
            # - You'd be shocked if you knew how old $npcName:11000033[gender:0]$ or $npcName:11000031[gender:0]$ are. You really just can't think of our ages in human years.
            return -1
        return -1

    def __7000(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509004964$
            # - Lately $npcName:11000032[gender:0]$ hasn't looked so good. I'm worried something happened to him.
            return 7000
        elif self.index == 1:
            # $script:0831180509004965$
            # - I tried to ask, but he wouldn't answer. $npcName:11000031[gender:0]$ seemed to know something, but he wouldn't tell me either.
            return 7000
        elif self.index == 2:
            # $script:0831180509004966$
            # - Actually $npcName:11000032[gender:0]$ was the reason I got a job with Helping Hands. He left one day all of a sudden, and it dawned on me that I didn't know much about him.
            return 7000
        elif self.index == 3:
            # $script:0831180509004967$
            # - $npcName:11000032[gender:0]$ is half-human and half-fairy. It must have been hard growing up like that, but he never showed it. I would've been nicer if I'd known he'd leave so abruptly...
            return 7000
        elif self.index == 4:
            # $script:0831180509004968$
            # - That's why I wanted to learn more about humans. I'm glad I applied for this job. Staying here with you has been so informative!
            return -1
        return -1

    def __100(self, pick: int) -> int:
        # $script:0831180509004969$
        # - Eeek! Human!! Sheesh, you scared me!
        if pick == 0:
            # $script:0831180509004970$
            # - Sorry for startling you.
            # TODO: goto 101,102
            self.close()
            return -1
        elif pick == 1:
            # $script:0831180509004971$
            # - Ha! I'm gonna step on you!
            # TODO: goto 103,104
            self.close()
            return -1
        elif pick == 2:
            # $script:0831180509004972$
            # - Who are you?
            # TODO: goto 105,106
            self.close()
            return -1
        return -1

    def __101(self, pick: int) -> int:
        # $script:0831180509004973$
        # - ...Oh. Well, that's okay.
        return -1

    def __102(self, pick: int) -> int:
        # $script:0831180509004974$
        # - I'm not used to talking to humans... It's okay, I forgive you.
        return -1

    def __103(self, pick: int) -> int:
        # $script:0831180509004975$
        # - Eeeeek!! G-go away!
        return -1

    def __104(self, pick: int) -> int:
        # $script:0831180509004976$
        # - I'm going to tell $npcName:11000031[gender:0]$! You'd better get away from me before I turn you into a frog!
        return -1

    def __105(self, pick: int) -> int:
        # $script:0831180509004977$
        # - M-me? I'm of the fairfolk... Eek, sorry! I don't think I'm ready to talk to strange humans!
        return -1

    def __106(self, pick: int) -> int:
        # $script:0831180509004978$
        # - H-hey, that doesn't matter. If you have business with <font color="#ffd200">$OwnerName$</font>, you don't need to talk to me.
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
            return Option.NEXT
        elif (self.state, self.index) == (9031, 1):
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
            return Option.CLOSE
        elif (self.state, self.index) == (3100, 0):
            return Option.NEXT
        elif (self.state, self.index) == (3100, 1):
            return Option.NEXT
        elif (self.state, self.index) == (3100, 2):
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
            return Option.NEXT
        elif (self.state, self.index) == (4100, 3):
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
            return Option.CLOSE
        elif (self.state, self.index) == (6000, 0):
            return Option.NEXT
        elif (self.state, self.index) == (6000, 1):
            return Option.NEXT
        elif (self.state, self.index) == (6000, 2):
            return Option.NEXT
        elif (self.state, self.index) == (6000, 3):
            return Option.NEXT
        elif (self.state, self.index) == (6000, 4):
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
