using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000793: Ms. Kim
/// </summary>
public class _11000793 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 1;2;3;4;5;6;9001;9002;9003;100
    }

    // Select 0:
    // $script:0831180509005629$
    // - What's wrong?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (1, 0):
                // $script:0831180509005630$
                // - Did you call me?
                switch (selection) {
                    // $script:0831180509005631$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509005632$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509005633$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (2, 0):
                // $script:0831180509005634$
                // - Is there anything I can help you with?
                switch (selection) {
                    // $script:0831180509005635$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509005636$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509005637$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (3, 0):
                // $script:0831180509005638$
                // - Welcome back. You look terrible.
                switch (selection) {
                    // $script:0831180509005639$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509005640$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509005641$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (4, 0):
                // $script:0831180509005642$
                // - Did you call me?
                switch (selection) {
                    // $script:0831180509005643$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509005644$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509005645$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509005646$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (5, 0):
                // $script:0831180509005647$
                // - Is there anything I can help you with?
                switch (selection) {
                    // $script:0831180509005648$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509005649$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509005650$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509005651$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (6, 0):
                // $script:0831180509005652$
                // - Welcome back. You look terrible.
                switch (selection) {
                    // $script:0831180509005653$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509005654$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509005655$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509005656$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (9, 0):
                // $script:0831180509005657$
                // - Did you just say you want to pay me?
                //   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
                switch (selection) {
                    // $script:0831180509005658$
                    // - Let me think about it some more.
                    case 0:
                        // TODO: goto 8040,8050,8060,9040
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509005659$
                    // - (Pay $MaidSalary$.)
                    case 1:
                        // TODO: goto 8000,8001,8010,8011,8901
                        // TODO: gotoFail 8900,8910
                        return -1;
                }
                return -1;
            case (8000, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509005660$
                // - You're terrible at managing your assets, and yet somehow you're able to pay me early. You're a curiosity.
                return -1;
            case (8001, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509005661$
                // - Today was exhausting... until now. Suddenly I feel all my stress melting away. Once in a while, you prove that you do have some sense in your head.
                return -1;
            case (8010, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509005662$
                // - Mm...? What did you do? I thought by your financial status that you wouldn't be able to afford me for a few months. You really are a mystery. 
                return -1;
            case (8011, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509005663$
                // - I thought it was less likely you'd renew our contract, but I misjudged. I apologize. Thank you for hiring me again.
                return -1;
            case (8020, 0):
                // functionID=1 
                // $script:0831180509005664$
                // - $OwnerName$, do you realize our contract expires soon? You never know what might happen, so I suggest you take care of that before it's too late.
                return -1;
            case (8021, 0):
                // functionID=1 
                // $script:0831180509005665$
                // - Ah, $OwnerName$... You're quite a handful.
                switch (selection) {
                    // $script:0831180509005666$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509005667$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509005668$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509005669$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (8040, 0):
                // $script:0831180509005670$
                // - What's wrong?
                switch (selection) {
                    // $script:0831180509005671$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509005672$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509005673$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509005674$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (8050, 0):
                // $script:0831180509005675$
                // - What do you need?
                switch (selection) {
                    // $script:0831180509005676$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509005677$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509005678$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509005679$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (8060, 0):
                // $script:0831180509005680$
                // - Do you need something?
                switch (selection) {
                    // $script:0831180509005681$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509005682$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509005683$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509005684$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (8900, 0):
                // $script:0831180509005685$
                // - Tsk, so impulsive. Acting rashly doesn't help in situations like this. Why don't you check your bank account first?
                return -1;
            case (8901, 0):
                // $script:0831180509005686$
                // - Excuse me. You've already paid me for the month, $OwnerName$. Of course, I should've expected you to lose track.
                return -1;
            case (8910, 0):
                // $script:0831180509005687$
                // - What was that? You're not trying to act as if you already paid me, are you? Please, you can't fool me.
                return -1;
            case (8999, 0):
                // $script:0831180509005688$
                // - I suggest you calm down and try again. Panicking never helps.
                return -1;
            case (9001, 0):
                // $script:0831180509005689$
                // - I'm exhausted. I need to rest. Is there something you need?
                switch (selection) {
                    // $script:0831180509005690$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509005691$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509005692$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9002, 0):
                // $script:0831180509005693$
                // - I'm sorry, but I'd like to rest for now. Is this urgent?
                switch (selection) {
                    // $script:0831180509005694$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509005695$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509005696$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9003, 0):
                // $script:0831180509005697$
                // - Ahhh. I knew it.
                switch (selection) {
                    // $script:0831180509005698$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509005699$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509005700$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9010, 0):
                // $script:0831180509005701$
                // - My contract has expired. Didn't anyone tell you? There's no such thing as a free lunch.
                return -1;
            case (9011, 0):
                // functionID=1 
                // $script:0831180509005702$
                // - I just checked and our contract has expired. Stop pretending you're unaware. Check the contract, will you?
                return -1;
            case (9020, 0):
                // functionID=1 
                // $script:0831180509005703$
                // - It's been $MaidPassedDay$... 
                return -1;
            case (9021, 0):
                // functionID=1 
                // $script:0831180509005704$
                // - Have you even thought about our situation?
                switch (selection) {
                    // $script:0831180509005705$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509005706$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509005707$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9040, 0):
                // $script:0831180509005708$
                // - Yes, well, this is not very surprising.
                switch (selection) {
                    // $script:0831180509005709$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509005710$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509005711$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9030, 0):
                // $script:0831180509005712$
                // - Since you refuse to keep to your part of the bargain, I don't feel the need to keep to mine. That's how contracts work. You're not going to pretend you didn't know, are you?
                return -1;
            case (9031, 0):
                // $script:0831180509005713$
                // - I don't wish to mix business and personal relationships, but that doesn't change the fact that you're a friend, $OwnerName$. If you don't have the money to feed yourself, I'm happy to treat you to a meal. But don't expect me to give you money.
                return -1;
            case (9032, 0):
                // $script:0831180509005714$
                // - I expected little out of you, so this doesn't surprise me at all. I know you must feel a little bad about this, $OwnerName$, but you don't need to worry about me.
                return -1;
            case (10, 0):
                // functionID=1 
                // $script:0831180509005715$
                // - Believe or not, I'm quite good with my hands.
                return -1;
            case (11, 0):
                // functionID=1 
                // $script:0831180509005716$
                // - If you need anything, just let me know.
                return -1;
            case (20, 0):
                // functionID=1 
                // $script:0831180509005717$
                // - Wait, $OwnerName$. Are you trying to pry into my personal business? Let's keep our relationship strictly professional, thank you.
                return -1;
            case (21, 0):
                // functionID=1 
                // $script:0831180509005718$
                // - Hm, what is it?
                switch (selection) {
                    // $script:0831180509005719$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509005720$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509005721$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (22, 0):
                // functionID=1 
                // $script:0831180509005722$
                // - Hm, what is it?
                switch (selection) {
                    // $script:0831180509005723$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509005724$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509005725$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509005726$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (30, 0):
                // $script:0831180509005727$
                // - Is there something you want to tell me?
                switch (selection) {
                    // $script:0831180509005728$
                    // - Anything interesting happen today?
                    case 0:
                        // TODO: goto 1000,1100,2000,2100,2200,9011
                        return -1;
                    // $script:0831180509005729$
                    // - Teach me how to invest my money.
                    case 1:
                        // TODO: goto 3000,3100,4000,4100,9011
                        return -1;
                    // $script:0831180509005730$
                    // - (Ask your servant a personal question.)
                    case 2:
                        // TODO: goto 5000,5100,6000,7000,9011
                        return -1;
                    // $script:0831180509005731$
                    // - Back.
                    case 3:
                        // TODO: goto 8040,8050,8060,40,50,60,9040
                        return -1;
                }
                return -1;
            case (31, 0):
                // $script:0831180509005732$
                // - I'm listening.
                switch (selection) {
                    // $script:0831180509005733$
                    // - Anything interesting happen today?
                    case 0:
                        // TODO: goto 1000,1100,2000,2100,2200,9011
                        return -1;
                    // $script:0831180509005734$
                    // - Teach me how to invest my money.
                    case 1:
                        // TODO: goto 3000,3100,4000,4100,9011
                        return -1;
                    // $script:0831180509005735$
                    // - (Ask your servant a personal question.)
                    case 2:
                        // TODO: goto 5000,5100,6000,7000,9011
                        return -1;
                    // $script:0831180509005736$
                    // - Back.
                    case 3:
                        // TODO: goto 8040,8050,8060,40,50,60,9040
                        return -1;
                }
                return -1;
            case (32, 0):
                // $script:0831180509005737$
                // - Is there something you have to say?
                switch (selection) {
                    // $script:0831180509005738$
                    // - Anything interesting happen today?
                    case 0:
                        // TODO: goto 1000,1100,2000,2100,2200,9011
                        return -1;
                    // $script:0831180509005739$
                    // - Teach me how to invest my money.
                    case 1:
                        // TODO: goto 3000,3100,4000,4100,9011
                        return -1;
                    // $script:0831180509005740$
                    // - (Ask your servant a personal question.)
                    case 2:
                        // TODO: goto 5000,5100,6000,7000,9011
                        return -1;
                    // $script:0831180509005741$
                    // - Back.
                    case 3:
                        // TODO: goto 8040,8050,8060,40,50,60,9040
                        return -1;
                }
                return -1;
            case (40, 0):
                // $script:0831180509005742$
                // - What's wrong?
                switch (selection) {
                    // $script:0831180509005743$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509005744$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509005745$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (50, 0):
                // $script:0831180509005746$
                // - What do you need?
                switch (selection) {
                    // $script:0831180509005747$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509005748$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509005749$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (60, 0):
                // $script:0831180509005750$
                // - Do you need something?
                switch (selection) {
                    // $script:0831180509005751$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509005752$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509005753$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (1000, 0):
                // $script:0831180509005754$
                // - So... hm... how do I say this? 
                return 1000;
            case (1000, 1):
                // $script:0831180509005755$
                // - I thought you might be hungry, so I cooked this for you. I'm not the best chef, so... well, I hope you like it.
                return 1000;
            case (1000, 2):
                // $script:0831180509005756$
                // - I found the recipe in a cookbook. It's stir-fried chicken feet.
                switch (selection) {
                    // $script:0831180509005757$
                    // - I don't eat chicken feet. Are you kidding?
                    case 0:
                        // TODO: goto 1001,1002
                        return -1;
                    // $script:0831180509005758$
                    // - Thanks.
                    case 1:
                        // TODO: goto 1011,1012
                        return -1;
                }
                return -1;
            case (1001, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509005759$
                // - Oh, really? Hmm, maybe I should've learned more about you before embarking on this project.
                return -1;
            case (1002, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509005760$
                // - Oh. Well, everyone has some foods they don't like. Don't worry, it won't go to waste. I guess I'll eat it all.
                return -1;
            case (1011, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509005761$
                // - Thank you for eating with me. I'm glad you're enjoying it, or at least pretending too.
                return -1;
            case (1012, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509005762$
                // - I was worried you might not like it. $OwnerName$, you're kinder than I expected.
                return -1;
            case (1100, 0):
                // $script:0831180509005763$
                // - Ugh, my colleague $npc:11000600[gender:0]$ is such a pain.
                return 1100;
            case (1100, 1):
                // $script:0831180509005764$
                // - He's good at his job, but he's so forgetful. He called me three times today, thinking he was calling his mother.
                return 1100;
            case (1100, 2):
                // $script:0831180509005765$
                // - This has happened so many times that I've started to wonder if he's doing it on purpose.
                switch (selection) {
                    // $script:0831180509005766$
                    // - He likes you. Hehe.
                    case 0:
                        // TODO: goto 1111,1112
                        return -1;
                    // $script:0831180509005767$
                    // - You're overreacting.
                    case 1:
                        // TODO: goto 1101,1102
                        return -1;
                }
                return -1;
            case (1101, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509005768$
                // - Am I? Maybe you're right. I shouldn't waste my time on something so unproductive. Excuse me, I'd better get back to work.
                return -1;
            case (1102, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509005769$
                // - He's young, but so forgetful. Maybe I should tell him to go to the doctor.
                return -1;
            case (1111, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509005770$
                // - Wh-what? That's ridiculous! He's much younger than I am.
                return -1;
            case (1112, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509005771$
                // - Goodness, $OwnerName$, you should expend your brainpower on managing your investments, not coming up with silly ideas!
                return -1;
            case (2000, 0):
                // $script:0831180509005772$
                // - Nothing of importance happened, but I do want to remind you of something: even though I'm here to watch your house that doesn't mean you shouldn't stop by to check on things now and then.
                return 2000;
            case (2000, 1):
                // $script:0831180509005773$
                // - And don't say, "I trust you to handle it, $MaidName$." I mean, that's sweet, but you shouldn't put so much faith in others or they'll stomp all over you.
                return 2000;
            case (2000, 2):
                // $script:0831180509005774$
                // - But I mean, it's still nice to hear. Thank you.
                return -1;
            case (2100, 0):
                // $script:0831180509005775$
                // - I'm utterly exhausted. I have no idea how they found me...
                return 2100;
            case (2100, 1):
                // $script:0831180509005776$
                // - A group of strangers barged into the house and bombarded me with questions. "What's the hottest neighborhood right now?" "Share your best real estate tips!" That type of thing. By the time they left, I was beat.
                return 2100;
            case (2100, 2):
                // $script:0831180509005777$
                // - But I couldn't just ignore them. Haha, no way. A good real estate agent would never do anything to jeopardize her reputation.
                return -1;
            case (2200, 0):
                // $script:0831180509005778$
                // - While performing my housekeeping duties today, I decided to check on your finances: your sources of income, spending habits, value of assets, that type of thing.
                return 2200;
            case (2200, 1):
                // $script:0831180509005779$
                // - And... goodness, you're in worse shape than I imagined! You waste your money on useless stuff, and you don't get paid regularly!
                return 2200;
            case (2200, 2):
                // $script:0831180509005780$
                // - At this rate, you'll never be able to afford a house near $map:2000001$. For starters, I highly suggest your improve your skills so that you don't have to spend so much money on potions!
                return -1;
            case (3000, 0):
                // $script:0831180509005781$
                // - Knowledge is money. A good way to produce income is to sell the items you find to people who understand their true value.
                return 3000;
            case (3000, 1):
                // $script:0831180509005782$
                // - How do you find those people? I'll give you some examples. A few days ago, $npc:11000004[gender:0]$ in $map:2000001$ used megaphones to advertise his new items and that's how he reached the buyers willing to pay the most.
                return 3000;
            case (3000, 2):
                // $script:0831180509005783$
                // - Rumor has it that Dark Wind agent $npc:11000208[gender:0]$ auctioned something he found during his mission on $map:2000216$ and he made a lot of money, too.
                return 3000;
            case (3000, 3):
                // functionID=1 openTalkReward=True 
                // $script:0831180509005784$
                // - There are a lot of ways to get the most for your money. It just depends on your personal preference, $OwnerName$.
                return -1;
            case (3100, 0):
                // $script:0831180509005785$
                // - You know $npc:11000002[gender:1]$, who lives in $map:2000001$? Your question made me think of her.
                return 3100;
            case (3100, 1):
                // $script:0831180509005786$
                // - $npc:11000002[gender:1]$ had lived her whole life in $map:2000076$, but moved to where she lives now about twenty years ago. That was before the areas around $map:2000001$ were developed.
                return 3100;
            case (3100, 2):
                // $script:0831180509005787$
                // - $npc:11000002[gender:1]$'s house is worth a lot of money now. Makes sense, considering its proximity to the palace.
                return 3100;
            case (3100, 3):
                // $script:0831180509005788$
                // - But I don't think $npc:11000002[gender:1]$ wants to sell. She wants to live like she has been, raising $npc:11000055[gender:0]$.
                return 3100;
            case (3100, 4):
                // functionID=1 openTalkReward=True 
                // $script:0831180509005789$
                // - That was the home she lived in with $npc:11000055[gender:0]$'s father, so it holds sentimental value. She'd be rich if she sold, though. Just goes to show, you never can tell, can you?
                return -1;
            case (4000, 0):
                // $script:0831180509005790$
                // - I worry about you, you know. I'm glad you're showing more interest in your finances. All right, listen carefully.
                return 4000;
            case (4000, 1):
                // $script:0831180509005791$
                // - What makes a person wealthy? The possession of mesos, right?
                return 4000;
            case (4000, 2):
                // $script:0831180509005792$
                // - Mesos rarely grow on trees, so instead of wishing for good luck, think about what you can tangibly do to make more money. Understand?
                return 4000;
            case (4000, 3):
                // $script:0831180509005793$
                // - Complete every quest available to you. They pay fairly well. The people of Maple World understand that nothing is free.
                return -1;
            case (4100, 0):
                // $script:0831180509005794$
                // - Everyone wants to be rich, and honestly, the concept is simple: make more money, spend less money.
                return 4100;
            case (4100, 1):
                // $script:0831180509005795$
                // - But life gets pretty bleak if you never spend any money at all. So here's what I do: I shop when I want to, but I don't buy things I don't need.
                return 4100;
            case (4100, 2):
                // $script:0831180509005796$
                // - For example, I saw a gorgeous dress at the market, and I've been debating for two weeks whether to get it. The cool blue tone would look amazing with my complexion... I'll sleep on it for just one more night.
                return -1;
            case (5000, 0):
                // $script:0831180509005797$
                // - I know you're curious about my past, $OwnerName$, but I distinctly remember asking you to keep our relationship strictly professional.
                return 5000;
            case (5000, 1):
                // $script:0831180509005798$
                // - I'm not your friend—I'm your housekeeper. I'm happy to answer any questions related to my work, your finances, and nothing else.
                return 5000;
            case (5000, 2):
                // $script:0831180509005799$
                // - I know what you're really trying to get at is whether I'm single. We'll leave it a mystery for now.
                return -1;
            case (5100, 0):
                // $script:0831180509005800$
                // - Have you heard of $npc:11000491[gender:1]$? She's the owner of Cathy Mart, and her business has really gotten popular lately. She paid $map:2000123$ a visit the other day.
                return 5100;
            case (5100, 1):
                // $script:0831180509005801$
                // - She was looking to open a big store near $map:2000001$, which is fantastic, but oh my, what an obnoxious woman. She said she had enough money to buy all of Goldus Group and the entirety of $map:2000025$.
                return 5100;
            case (5100, 2):
                // $script:0831180509005802$
                // - I don't know what she's thinking, but having a couple of supermarkets is not the same as running a corporation as big as Goldus Group. Seriously.
                return 5100;
            case (5100, 3):
                // $script:0831180509005803$
                // - She used up my entire afternoon and then just left, whining about how there was no location good enough. I've never met such an unpleasant person in my life.
                return 5100;
            case (5100, 4):
                // $script:0831180509005804$
                // - $OwnerName$, so we're clear, I will never buy you a thing—even a potion—from Cathy Mart. Got it?
                return -1;
            case (6000, 0):
                // $script:0831180509005805$
                // - You want to know more about my colleague,$npc:11000600[gender:0]$? Well, he's a nice person. Diligent, polite.
                return 6000;
            case (6000, 1):
                // $script:0831180509005806$
                // - He has a long way to go before becoming a good agent, though. He trips when he walks and forgets to bring important documents. I constantly have to babysit him.  
                return 6000;
            case (6000, 2):
                // $script:0831180509005807$
                // - Yesterday he came over here, so I asked him what he needed. He said he thought this was his house. How such a young man can be so forgetful is beyond me.
                return -1;
            case (7000, 0):
                // $script:0831180509005808$
                // - My real name? What does it matter? You're going to call me whatever you want, anyway, haha.
                return 7000;
            case (7000, 1):
                // $script:0831180509005809$
                // - I know some people think I'm $npc:11000252[gender:0]$'s only daughter, haha.
                return 7000;
            case (7000, 2):
                // $script:0831180509005810$
                // - Let me tell you this: I owe $npc:11000252[gender:0]$ a lot. I wish he were my father, but he and I are not related.
                return 7000;
            case (7000, 3):
                // $script:0831180509005811$
                // - Please don't ask me what happened with the Chairman. I worked for him for a long time. Trust me when I tell you that not everything you hear about him is true.
                return 7000;
            case (7000, 4):
                // $script:0831180509005812$
                // - I agree he's changed, but there has to be a reason. At least, I'd like to believe that.
                return -1;
            case (100, 0):
                // $script:0831180509005813$
                // - How may I help you? Do you need a real estate agent?
                switch (selection) {
                    // $script:0831180509005814$
                    // - Yep!
                    case 0:
                        // TODO: goto 101,102
                        return -1;
                    // $script:0831180509005815$
                    // - Nope!
                    case 1:
                        // TODO: goto 103,104
                        return -1;
                    // $script:0831180509005816$
                    // - Who are you?
                    case 2:
                        return 105;
                }
                return -1;
            case (101, 0):
                // $script:0831180509005817$
                // - I'm sorry, but this is my other workplace. I can help you if you come visit me at $map:2000123$ in $map:2000001$.
                return -1;
            case (102, 0):
                // $script:0831180509005818$
                // - If it's not urgent, please talk to my assistant, $npc:11000600[gender:0]$. I'm in the middle of something very important.
                return -1;
            case (103, 0):
                // $script:0831180509005819$
                // - I see. But I've got the perfect property for you. If you let it slip between your fingers, you might regret it forever.
                return 103;
            case (103, 1):
                // $script:0831180509005820$
                // - Now, would you like to follow me to my office?
                return -1;
            case (104, 0):
                // $script:0831180509005821$
                // - Then what you are doing here? Don't tell me your here to burglarize the house. Let's be serious.
                return -1;
            case (105, 0):
                // $script:0831180509005822$
                // - My name is $MaidName$, and I'm in charge. If you don't have business here, please leave.
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
            (2000, 2) => NpcTalkButton.Close,
            (2100, 0) => NpcTalkButton.Next,
            (2100, 1) => NpcTalkButton.Next,
            (2100, 2) => NpcTalkButton.Close,
            (2200, 0) => NpcTalkButton.Next,
            (2200, 1) => NpcTalkButton.Next,
            (2200, 2) => NpcTalkButton.Close,
            (3000, 0) => NpcTalkButton.Next,
            (3000, 1) => NpcTalkButton.Next,
            (3000, 2) => NpcTalkButton.Next,
            (3000, 3) => NpcTalkButton.Close,
            (3100, 0) => NpcTalkButton.Next,
            (3100, 1) => NpcTalkButton.Next,
            (3100, 2) => NpcTalkButton.Next,
            (3100, 3) => NpcTalkButton.Next,
            (3100, 4) => NpcTalkButton.Close,
            (4000, 0) => NpcTalkButton.Next,
            (4000, 1) => NpcTalkButton.Next,
            (4000, 2) => NpcTalkButton.Next,
            (4000, 3) => NpcTalkButton.Close,
            (4100, 0) => NpcTalkButton.Next,
            (4100, 1) => NpcTalkButton.Next,
            (4100, 2) => NpcTalkButton.Close,
            (5000, 0) => NpcTalkButton.Next,
            (5000, 1) => NpcTalkButton.Next,
            (5000, 2) => NpcTalkButton.Close,
            (5100, 0) => NpcTalkButton.Next,
            (5100, 1) => NpcTalkButton.Next,
            (5100, 2) => NpcTalkButton.Next,
            (5100, 3) => NpcTalkButton.Next,
            (5100, 4) => NpcTalkButton.Close,
            (6000, 0) => NpcTalkButton.Next,
            (6000, 1) => NpcTalkButton.Next,
            (6000, 2) => NpcTalkButton.Close,
            (7000, 0) => NpcTalkButton.Next,
            (7000, 1) => NpcTalkButton.Next,
            (7000, 2) => NpcTalkButton.Next,
            (7000, 3) => NpcTalkButton.Next,
            (7000, 4) => NpcTalkButton.Close,
            (100, 0) => NpcTalkButton.SelectableDistractor,
            (101, 0) => NpcTalkButton.Close,
            (102, 0) => NpcTalkButton.Close,
            (103, 0) => NpcTalkButton.Next,
            (103, 1) => NpcTalkButton.Close,
            (104, 0) => NpcTalkButton.Close,
            (105, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
