using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000787: Kay
/// </summary>
public class _11000787 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 1;2;3;4;5;6;9001;9002;9003;100
    }

    // Select 0:
    // $script:0831180509004348$
    // - Just tell me what you need!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (1, 0):
                // $script:0831180509004349$
                // - And today, our very special guest is... Oh! Hi, $OwnerName$! I was just practicing, hehe.
                switch (selection) {
                    // $script:0831180509004350$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509004351$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509004352$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (2, 0):
                // $script:0831180509004353$
                // - Oh, did you call me?
                switch (selection) {
                    // $script:0831180509004354$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509004355$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509004356$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (3, 0):
                // $script:0831180509004357$
                // - Do you have something to say?
                switch (selection) {
                    // $script:0831180509004358$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509004359$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509004360$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (4, 0):
                // $script:0831180509004361$
                // - And today, our very special guest is... Oh! Hi, $OwnerName$! I was just practicing, hehe.
                switch (selection) {
                    // $script:0831180509004362$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509004363$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509004364$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509004365$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (5, 0):
                // $script:0831180509004366$
                // - Oh, did you call me?
                switch (selection) {
                    // $script:0831180509004367$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509004368$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509004369$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509004370$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (6, 0):
                // $script:0831180509004371$
                // - Do you have something to say?
                switch (selection) {
                    // $script:0831180509004372$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509004373$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509004374$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509004375$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (9, 0):
                // $script:0831180509004376$
                // - You want to give me my paycheck?
                //   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
                switch (selection) {
                    // $script:0831180509004377$
                    // - Let me think about it some more.
                    case 0:
                        // TODO: goto 8040,8050,8060,9040
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509004378$
                    // - (Pay $MaidSalary$.)
                    case 1:
                        // TODO: goto 8000,8001,8010,8011,8901
                        // TODO: gotoFail 8900,8910
                        return 8900,8910;
                }
                return -1;
            case (8000, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509004379$
                // - I'm touched! You're so busy yet you still remembered to pay me! I promise to be the best servant ever!
                return -1;
            case (8001, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509004380$
                // - You take such good care of me. I can't thank you enough. I am forever indebted to you! 
                return -1;
            case (8010, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509004381$
                // - I knew you wouldn't abandon me, $OwnerName$. I promise to never, ever disappoint you!
                return -1;
            case (8011, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509004382$
                // - Ahem! There may have been a slight misunderstanding between us. As a token of my regret, I'd like you to be the first guest on my show when it opens!
                return -1;
            case (8020, 0):
                // functionID=1 
                // $script:0831180509004383$
                // - Good day, studio audience. I'd like to introduce you to our special guest for the day, $OwnerName$! Now, the million meso question, $OwnerName$... Our employment contract is expiring soon. Are you planning to extend it?
                return -1;
            case (8021, 0):
                // functionID=1 
                // $script:0831180509004384$
                // - Yes? No? Ahem, are you planning to answer?
                switch (selection) {
                    // $script:0831180509004385$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509004386$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509004387$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509004388$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (8040, 0):
                // $script:0831180509004389$
                // - Did you have something to say to me?
                switch (selection) {
                    // $script:0831180509004390$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509004391$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509004392$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509004393$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (8050, 0):
                // $script:0831180509004394$
                // - What a wonderful day, isn't it?
                switch (selection) {
                    // $script:0831180509004395$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509004396$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509004397$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509004398$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (8060, 0):
                // $script:0831180509004399$
                // - What's wrong?
                switch (selection) {
                    // $script:0831180509004400$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509004401$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509004402$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509004403$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (8900, 0):
                // $script:0831180509004404$
                // - Ah... Bwahahaha! Oh, $OwnerName$, you're hilarious! That was a joke, right? I mean, why would you say you're paying me when you don't even have the money?
                return -1;
            case (8901, 0):
                // $script:0831180509004405$
                // - Yes or no, $OwnerName$. Do you realize you've already paid me for the month? Ahem! How'd I do? Did I sound serious? A good host has to know how to ask the deep, probing questions!
                return -1;
            case (8910, 0):
                // $script:0831180509004406$
                // - $OwnerName$, enough with the jokes already. If you have no money, why do you keep saying you're paying me?
                return -1;
            case (8999, 0):
                // $script:0831180509004407$
                // - Hmm, I've never encountered situation like this before. I'm, well, I'm flustered! Excuse me while I grab a glass of water.
                return -1;
            case (9001, 0):
                // $script:0831180509004408$
                // - Someone once said that positive minds attract good luck!
                switch (selection) {
                    // $script:0831180509004409$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509004410$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509004411$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9002, 0):
                // $script:0831180509004412$
                // - $OwnerName$, did something good happen today? Hm?
                switch (selection) {
                    // $script:0831180509004413$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509004414$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509004415$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9003, 0):
                // $script:0831180509004416$
                // - Please stop doing this. You're hurting my heart... 
                switch (selection) {
                    // $script:0831180509004417$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509004418$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509004419$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9010, 0):
                // $script:0831180509004420$
                // - I could give you a list of two dozen reason why asking someone to labor without pay is wrong... Or you could just renew my contract.
                return -1;
            case (9011, 0):
                // functionID=1 
                // $script:0831180509004421$
                // - I received a call today from Helping Hands notifying me that our contract had expired. I was so busy dreaming of which guests to invite to my show that I hadn't even noticed. Were you aware, $OwnerName$?
                return -1;
            case (9020, 0):
                // functionID=1 
                // $script:0831180509004422$
                // - Ahem! It's been $MaidPassedDay$ since I stopped working for you...
                return -1;
            case (9021, 0):
                // functionID=1 
                // $script:0831180509004423$
                // - W-wait, you're not thinking about letting me go permanently, are you?
                switch (selection) {
                    // $script:0831180509004424$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509004425$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509004426$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9040, 0):
                // $script:0831180509004427$
                // - I will never give up my role as a servant or as a talk show host!  
                switch (selection) {
                    // $script:0831180509004428$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509004429$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509004430$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9030, 0):
                // $script:0831180509004431$
                // - Is this because I'm always talking about my future show? Be honest. Does it annoy you?
                return -1;
            case (9031, 0):
                // $script:0831180509004432$
                // - Excuse me?! You think I should give up my dream and return to making smoothies? No way! I didn't come this far just to give up! 
                return -1;
            case (9032, 0):
                // $script:0831180509004433$
                // - Welcome to my show, ladies and gentlemen! I have with me, $OwnerName$, brave defender of Maple World. Well, $OwnerName$? Fight any big monsters today? Discover any amazing items? What's the latest?
                return -1;
            case (10, 0):
                // functionID=1 
                // $script:0831180509004434$
                // - Believe it or not, I used to work at a juice bar.
                return -1;
            case (11, 0):
                // functionID=1 
                // $script:0831180509004435$
                // - Ask me for any drink you want.
                return -1;
            case (20, 0):
                // functionID=1 
                // $script:0831180509004436$
                // - Nice to meet you. I'm Maple World's greatest talk show host, $MaidName$! Ahem, aspiring talk show host.
                return -1;
            case (21, 0):
                // functionID=1 
                // $script:0831180509004437$
                // - By the way, was there something you needed?
                switch (selection) {
                    // $script:0831180509004438$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509004439$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509004440$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (22, 0):
                // functionID=1 
                // $script:0831180509004441$
                // - By the way, was there something you needed?
                switch (selection) {
                    // $script:0831180509004442$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509004443$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509004444$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509004445$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (30, 0):
                // $script:0831180509004446$
                // - Sure, you can tell me anything.
                switch (selection) {
                    // $script:0831180509004447$
                    // - Anything interesting happen today?
                    case 0:
                        // TODO: goto 1000,1100,2000,2100,2200,9011
                        return -1;
                    // $script:0831180509004448$
                    // - (Help him practice for his show.)
                    case 1:
                        // TODO: goto 3000,3100,4000,4100,9011
                        return -1;
                    // $script:0831180509004449$
                    // - (Ask your servant a personal question.)
                    case 2:
                        // TODO: goto 5000,5100,6000,7000,9011
                        return -1;
                    // $script:0831180509004450$
                    // - Back.
                    case 3:
                        // TODO: goto 8040,8050,8060,40,50,60,9040
                        return -1;
                }
                return -1;
            case (31, 0):
                // $script:0831180509004451$
                // - Did you have something to say to me?
                switch (selection) {
                    // $script:0831180509004452$
                    // - Anything interesting happen today?
                    case 0:
                        // TODO: goto 1000,1100,2000,2100,2200,9011
                        return -1;
                    // $script:0831180509004453$
                    // - (Help him practice for his show.)
                    case 1:
                        // TODO: goto 3000,3100,4000,4100,9011
                        return -1;
                    // $script:0831180509004454$
                    // - (Ask your servant a personal question.)
                    case 2:
                        // TODO: goto 5000,5100,6000,7000,9011
                        return -1;
                    // $script:0831180509004455$
                    // - Back.
                    case 3:
                        // TODO: goto 8040,8050,8060,40,50,60,9040
                        return -1;
                }
                return -1;
            case (32, 0):
                // $script:0831180509004456$
                // - Just thinking about my show makes my heart flutter.
                switch (selection) {
                    // $script:0831180509004457$
                    // - Anything interesting happen today?
                    case 0:
                        // TODO: goto 1000,1100,2000,2100,2200,9011
                        return -1;
                    // $script:0831180509004458$
                    // - (Help him practice for his show.)
                    case 1:
                        // TODO: goto 3000,3100,4000,4100,9011
                        return -1;
                    // $script:0831180509004459$
                    // - (Ask your servant a personal question.)
                    case 2:
                        // TODO: goto 5000,5100,6000,7000,9011
                        return -1;
                    // $script:0831180509004460$
                    // - Back.
                    case 3:
                        // TODO: goto 8040,8050,8060,40,50,60,9040
                        return -1;
                }
                return -1;
            case (40, 0):
                // $script:0831180509004461$
                // - Did you have something to say to me?
                switch (selection) {
                    // $script:0831180509004462$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509004463$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509004464$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (50, 0):
                // $script:0831180509004465$
                // - What a wonderful day, isn't it?
                switch (selection) {
                    // $script:0831180509004466$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509004467$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509004468$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (60, 0):
                // $script:0831180509004469$
                // - What's wrong?
                switch (selection) {
                    // $script:0831180509004470$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509004471$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509004472$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (1000, 0):
                // $script:0831180509004473$
                // - $OwnerName$, be honest with me about something.
                return 1000;
            case (1000, 1):
                // $script:0831180509004474$
                // - You hired me as your servant, and I've been loudly practicing my show host skills every single day.
                return 1000;
            case (1000, 2):
                // $script:0831180509004475$
                // - Does it bother you? Please be honest.
                switch (selection) {
                    // $script:0831180509004476$
                    // - Nah, it's entertaining.
                    case 0:
                        // TODO: goto 1011,1012
                        return -1;
                    // $script:0831180509004477$
                    // - I hate it so much.
                    case 1:
                        // TODO: goto 1001,1002
                        return -1;
                }
                return -1;
            case (1001, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509004478$
                // - ...I see. I don't get many jobs hosting shows, and I'm terrible at keeping house. I don't know what to do...
                return -1;
            case (1002, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509004479$
                // - Your honesty hurts, $OwnerName$. Sheesh.
                return -1;
            case (1011, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509004480$
                // - You really think so? Then my dream has a chance at coming true, right?!
                return -1;
            case (1012, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509004481$
                // - Entertaining? Me? That's the sweetest compliment anyone's ever given me in my entire life. Thank you!!
                return -1;
            case (1100, 0):
                // $script:0831180509004482$
                // - Every single day, I practice my hosting skills, but I can't help but worry sometimes.
                return 1100;
            case (1100, 1):
                // $script:0831180509004483$
                // - I really want to be a great talk show host, but I'm just not sure I'll ever get my big break.
                return 1100;
            case (1100, 2):
                // $script:0831180509004484$
                // - I'm not getting any younger, and you know they like to hire young. Should I just go back to working at the juice bar? What do you think?
                switch (selection) {
                    // $script:0831180509004485$
                    // - It's not the end of the world to just stick to what you're good at.
                    case 0:
                        // TODO: goto 1101,1102
                        return -1;
                    // $script:0831180509004486$
                    // - Never, ever give up!
                    case 1:
                        // TODO: goto 1111,1112
                        return -1;
                }
                return -1;
            case (1101, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509004487$
                // - Yeah? Maybe I'm just not cut out for bring a host. Excuse me... I'd like to be alone for a while.
                return -1;
            case (1102, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509004488$
                // - You think so? I never thought being good at something would break my heart. If only I were good at what I really, truly want to do...
                return -1;
            case (1111, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509004489$
                // - ...You're right. You're absolutely right! Shame on me for even considering giving up. It was a moment of weakness.
                return -1;
            case (1112, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509004490$
                // - Yes! That's the spirit! I won't give up on my dreams, $OwnerName$!
                return -1;
            case (2000, 0):
                // $script:0831180509004491$
                // - Oh, our next door neighbor stopped by.
                return 2000;
            case (2000, 1):
                // $script:0831180509004492$
                // - I was practicing for my show, when someone banged on the door.
                return 2000;
            case (2000, 2):
                // $script:0831180509004493$
                // - I guess he thought I was too loud. He told me to keep it down so he could sleep, but I knew fate had sent him to me.
                return 2000;
            case (2000, 3):
                // $script:0831180509004494$
                // - I needed someone to be the guest on my show. On my practice show.
                return 2000;
            case (2000, 4):
                // $script:0831180509004495$
                // - It went great! Now I have confidence that I can run my show seamlessly, no matter how wacky the guest is.
                return 2000;
            case (2000, 5):
                // $script:0831180509004496$
                // - I hope he can help again tomorrow! He looked thoroughly exhausted when he left, though...
                return -1;
            case (2100, 0):
                // $script:0831180509004497$
                // - Come to think of it, $npcName:11000012[gender:0]$ stopped by this afternoon to give me some mail.
                return 2100;
            case (2100, 1):
                // $script:0831180509004498$
                // - I was hoping it was an invitation from the palace to host some grand event, but it was from $npcName:11000171[gender:0]$. He wants me to host his son's ninth birthday party.
                return 2100;
            case (2100, 2):
                // $script:0831180509004499$
                // - That's not as exciting as a royal event, but beggars can't be choosers. And us twingos need to help each other, you know?
                return 2100;
            case (2100, 3):
                // $script:0831180509004500$
                // - I'm going to make $npcName:11000171[gender:0]$'s son's birthday the best event ever! Now, if you'll excuse me, I've got to get practicing.
                return -1;
            case (2200, 0):
                // $script:0831180509004501$
                // - I hope I get to host something amazing soon. Like... Like... Like $npcName:11000075[gender:1]$'s wedding!
                return 2200;
            case (2200, 1):
                // $script:0831180509004502$
                // - It'd be such an honor. My family would be so proud! Just the thought of it is making my pulse race!
                return 2200;
            case (2200, 2):
                // $script:0831180509004503$
                // - I mean, she's not even engaged... And she can't even hold public events right now... But it would be such a fantastic, magical, beautiful event, don't you think? Ahh, I can dream, can't I?
                return -1;
            case (3000, 0):
                // $script:0831180509004504$
                // - Every show needs a special segment that captures the hearts and imagination of the masses.
                return 3000;
            case (3000, 1):
                // $script:0831180509004505$
                // - ...Oooh, how about this? "Special: Help $npcName:11000075[gender:1]$ Find Her Man!"
                return 3000;
            case (3000, 2):
                // $script:0831180509004506$
                // - I'd invite $npcName:11000075[gender:1]$ to come on the show and then help her find the man of her dreams! Like, I could have her choose between $npcName:11000119[gender:0]$ and $npcName:11000076[gender:0]$, and then let her keep choosing between people until she found her perfect match!
                return 3000;
            case (3000, 3):
                // functionID=1 openTalkReward=True 
                // $script:0831180509004507$
                // - I can definitely make this work. I just need to get $npcName:11000075[gender:1]$ to agree to come on the show. All right, then! Off to the palace! I'm sure she can make time for me. La, la, laaaa!
                return -1;
            case (3100, 0):
                // $script:0831180509004508$
                // - I've been asked to prepare a special twingo show. Oooh, I get butterflies just thinking about it!
                return 3100;
            case (3100, 1):
                // $script:0831180509004509$
                // - There are so many possibilities! A twingo talent show, a twingo reality show, or, oooh, maybe a twingo dance contest?
                return 3100;
            case (3100, 2):
                // functionID=1 openTalkReward=True 
                // $script:0831180509004510$
                // - I can't make up my mind! $OwnerName$, what do you think?
                return -1;
            case (4000, 0):
                // $script:0831180509004511$
                // - Okay, $OwnerName$, let's practice for the world's greatest talk show!
                return 4000;
            case (4000, 1):
                // $script:0831180509004512$
                // - Hellooooo, ladies and gentlemen! It's me, your cute and super talented host, $MaidName$!!
                return 4000;
            case (4000, 2):
                // $script:0831180509004513$
                // - ...Ugh, that sounds corny. It totally sets the wrong tone!
                return -1;
            case (4100, 0):
                // $script:0831180509004514$
                // - Hello, studio audience! Welcome to The $MaidName$ Show!
                return 4100;
            case (4100, 1):
                // $script:0831180509004515$
                // - Our guest today is the one and only... $OwnerName$! Come on in, $OwnerName$.
                return 4100;
            case (4100, 2):
                // $script:0831180509004516$
                // - So, what's the latest, $OwnerName$?
                return 4100;
            case (4100, 3):
                // $script:0831180509004517$
                // - Huh? You've been busy leveling? No, no, no, $OwnerName$. What kind boring answer is that? I know this is just practice, but try to take it seriously, okay?
                return -1;
            case (5000, 0):
                // $script:0831180509004518$
                // - Practicing every day takes a toll on my vocal cords, and these babies are vital to my career.
                return 5000;
            case (5000, 1):
                // $script:0831180509004519$
                // - That's why I try not to talk too much when I'm not practicing. I mean it. Please don't talk to me unless it's necessary, okay?
                return 5000;
            case (5000, 2):
                // $script:0831180509004520$
                // - ...
                //   ...
                //   ...
                //   Are you really just going to stop talking to me now? Because I asked you to? Really?
                return -1;
            case (5100, 0):
                // $script:0831180509004521$
                // - You may have wondered why I accepted a job with Helping Hands when my dream is to be a talk show host, but you don't understand.
                return 5100;
            case (5100, 1):
                // $script:0831180509004522$
                // - Here, I get to practice my show-hosting skills around the clock, and I get paid for it! Also, strangers barge in all the time...
                return 5100;
            case (5100, 2):
                // $script:0831180509004523$
                // - And I get to pretend they're guests on my show! A great host knows how to respond to unexpected situations with poise.
                return 5100;
            case (5100, 3):
                // $script:0831180509004524$
                // - I end up interviewing them as I would if they were guests on the show. Sure, most of them try to sneak out in the middle of the interview, but I don't let them move an inch until I'm done with them.
                return -1;
            case (6000, 0):
                // $script:0831180509004525$
                // - Ahh, I wish I could host the event in $map:02000064$. I'm positive I could make it so much more exciting.
                return 6000;
            case (6000, 1):
                // $script:0831180509004526$
                // - I've offered my services to the palace several times and get the same response every time:
                return 6000;
            case (6000, 2):
                // $script:0831180509004527$
                // - "Thank you for your interest. That event does not require a host." I just don't get it!
                return 6000;
            case (6000, 3):
                // $script:0831180509004528$
                // - Think about it! If you were in the $map:61000001$ audience, wouldn't you have fun trying to guess the winner?
                return 6000;
            case (6000, 4):
                // $script:0831180509004529$
                // - But according to the palace, that's too close to gambling, which is prohibited.
                return 6000;
            case (6000, 5):
                // $script:0831180509004530$
                // - Hmph. The palace is a rather old-fashioned, if you ask me.
                return -1;
            case (7000, 0):
                // $script:0831180509004531$
                // - In my younger days, I worked at a juice bar. My joy in life was listening to the customers and making their tasty drinks.
                return 7000;
            case (7000, 1):
                // $script:0831180509004532$
                // - One day, one of the regulars came looking sad. He has broken up with his girlfriend a week ago and just couldn't get over it. I knew he needed a good laugh.
                return 7000;
            case (7000, 2):
                // $script:0831180509004533$
                // - So I went all out. I listened to him, then I told him jokes and funny stories.
                return 7000;
            case (7000, 3):
                // $script:0831180509004534$
                // - He left that night with a smile on his face, and it made me realize what I really want to do with my life.
                return 7000;
            case (7000, 4):
                // $script:0831180509004535$
                // - My dream is to become Maple World's greatest show host! I have a long way to go, but I'll get there one day.
                return -1;
            case (100, 0):
                // $script:0831180509004536$
                // - Let's give a warm welcome our first guest of the day to The $MaidName$ Show, $MyPCName$!
                switch (selection) {
                    // $script:0831180509004537$
                    // - Uh. Hi?
                    case 0:
                        // TODO: goto 101,102
                        return -1;
                    // $script:0831180509004538$
                    // - What do you mean?
                    case 1:
                        // TODO: goto 103,104
                        return -1;
                    // $script:0831180509004539$
                    // - Get me out of here. Immediately.
                    case 2:
                        // TODO: goto 105,106
                        return -1;
                }
                return -1;
            case (101, 0):
                // $script:0831180509004540$
                // - Exactly! Hi! Now, tell us alllll about your interesting life!
                return -1;
            case (102, 0):
                // $script:0831180509004541$
                // - Well, hi back! Make yourself comfy. You'll be with us for the next two hours, spilling all the juicy details of your fascinating life!
                return -1;
            case (103, 0):
                // $script:0831180509004542$
                // - Don't be shy, now. Just be yourself! Go on, say hello to our studio audience!
                return -1;
            case (104, 0):
                // $script:0831180509004543$
                // - No need to be confused, my friend. We're about to dive into our first segment of the day: "Juicy Details of $MyPCName$'s Personal Life"!
                return -1;
            case (105, 0):
                // $script:0831180509004544$
                // - Oh, no. Please! I haven't had a guest on my pretend show for three hours!
                return -1;
            case (106, 0):
                // $script:0831180509004545$
                // - Please! Even if you're busy, spare me an hour—no, thirty minutes!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (1, 0) => NpcTalkButton.SelectableDistractor,
            (2, 0) => NpcTalkButton.SelectableDistractor,
            (3, 0) => NpcTalkButton.SelectableDistractor,
            (4, 0) => NpcTalkButton.SelectableDistractor,
            (5, 0) => NpcTalkButton.SelectableDistractor,
            (6, 0) => NpcTalkButton.SelectableDistractor,
            (9, 0) => NpcTalkButton.SelectableDistractor,
            (8000, 0) => NpcTalkButton.Close,
            (8001, 0) => NpcTalkButton.Close,
            (8010, 0) => NpcTalkButton.Close,
            (8011, 0) => NpcTalkButton.Close,
            (8020, 0) => NpcTalkButton.Close,
            (8021, 0) => NpcTalkButton.SelectableDistractor,
            (8040, 0) => NpcTalkButton.SelectableDistractor,
            (8050, 0) => NpcTalkButton.SelectableDistractor,
            (8060, 0) => NpcTalkButton.SelectableDistractor,
            (8900, 0) => NpcTalkButton.Close,
            (8901, 0) => NpcTalkButton.Close,
            (8910, 0) => NpcTalkButton.Close,
            (8999, 0) => NpcTalkButton.Close,
            (9001, 0) => NpcTalkButton.SelectableDistractor,
            (9002, 0) => NpcTalkButton.SelectableDistractor,
            (9003, 0) => NpcTalkButton.SelectableDistractor,
            (9010, 0) => NpcTalkButton.Close,
            (9011, 0) => NpcTalkButton.Close,
            (9020, 0) => NpcTalkButton.Close,
            (9021, 0) => NpcTalkButton.SelectableDistractor,
            (9040, 0) => NpcTalkButton.SelectableDistractor,
            (9030, 0) => NpcTalkButton.Close,
            (9031, 0) => NpcTalkButton.Close,
            (9032, 0) => NpcTalkButton.Close,
            (10, 0) => NpcTalkButton.Close,
            (11, 0) => NpcTalkButton.Close,
            (20, 0) => NpcTalkButton.Close,
            (21, 0) => NpcTalkButton.SelectableDistractor,
            (22, 0) => NpcTalkButton.SelectableDistractor,
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (50, 0) => NpcTalkButton.SelectableDistractor,
            (60, 0) => NpcTalkButton.SelectableDistractor,
            (1000, 0) => NpcTalkButton.Next,
            (1000, 1) => NpcTalkButton.Next,
            (1000, 2) => NpcTalkButton.SelectableDistractor,
            (1001, 0) => NpcTalkButton.Close,
            (1002, 0) => NpcTalkButton.Close,
            (1011, 0) => NpcTalkButton.Close,
            (1012, 0) => NpcTalkButton.Close,
            (1100, 0) => NpcTalkButton.Next,
            (1100, 1) => NpcTalkButton.Next,
            (1100, 2) => NpcTalkButton.SelectableDistractor,
            (1101, 0) => NpcTalkButton.Close,
            (1102, 0) => NpcTalkButton.Close,
            (1111, 0) => NpcTalkButton.Close,
            (1112, 0) => NpcTalkButton.Close,
            (2000, 0) => NpcTalkButton.Next,
            (2000, 1) => NpcTalkButton.Next,
            (2000, 2) => NpcTalkButton.Next,
            (2000, 3) => NpcTalkButton.Next,
            (2000, 4) => NpcTalkButton.Next,
            (2000, 5) => NpcTalkButton.Close,
            (2100, 0) => NpcTalkButton.Next,
            (2100, 1) => NpcTalkButton.Next,
            (2100, 2) => NpcTalkButton.Next,
            (2100, 3) => NpcTalkButton.Close,
            (2200, 0) => NpcTalkButton.Next,
            (2200, 1) => NpcTalkButton.Next,
            (2200, 2) => NpcTalkButton.Close,
            (3000, 0) => NpcTalkButton.Next,
            (3000, 1) => NpcTalkButton.Next,
            (3000, 2) => NpcTalkButton.Next,
            (3000, 3) => NpcTalkButton.Close,
            (3100, 0) => NpcTalkButton.Next,
            (3100, 1) => NpcTalkButton.Next,
            (3100, 2) => NpcTalkButton.Close,
            (4000, 0) => NpcTalkButton.Next,
            (4000, 1) => NpcTalkButton.Next,
            (4000, 2) => NpcTalkButton.Close,
            (4100, 0) => NpcTalkButton.Next,
            (4100, 1) => NpcTalkButton.Next,
            (4100, 2) => NpcTalkButton.Next,
            (4100, 3) => NpcTalkButton.Close,
            (5000, 0) => NpcTalkButton.Next,
            (5000, 1) => NpcTalkButton.Next,
            (5000, 2) => NpcTalkButton.Close,
            (5100, 0) => NpcTalkButton.Next,
            (5100, 1) => NpcTalkButton.Next,
            (5100, 2) => NpcTalkButton.Next,
            (5100, 3) => NpcTalkButton.Close,
            (6000, 0) => NpcTalkButton.Next,
            (6000, 1) => NpcTalkButton.Next,
            (6000, 2) => NpcTalkButton.Next,
            (6000, 3) => NpcTalkButton.Next,
            (6000, 4) => NpcTalkButton.Next,
            (6000, 5) => NpcTalkButton.Close,
            (7000, 0) => NpcTalkButton.Next,
            (7000, 1) => NpcTalkButton.Next,
            (7000, 2) => NpcTalkButton.Next,
            (7000, 3) => NpcTalkButton.Next,
            (7000, 4) => NpcTalkButton.Close,
            (100, 0) => NpcTalkButton.SelectableDistractor,
            (101, 0) => NpcTalkButton.Close,
            (102, 0) => NpcTalkButton.Close,
            (103, 0) => NpcTalkButton.Close,
            (104, 0) => NpcTalkButton.Close,
            (105, 0) => NpcTalkButton.Close,
            (106, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
