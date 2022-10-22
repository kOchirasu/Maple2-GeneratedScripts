using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000779: Jayce
/// </summary>
public class _11000779 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 1;2;3;4;5;6;9001;9002;9003;100
    }

    // Select 0:
    // $script:0831180509003461$
    // - Hm, yes?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (1, 0):
                // $script:0831180509003462$
                // - $OwnerName$, let's go over your schedule for the day...
                switch (selection) {
                    // $script:0831180509003463$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509003464$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509003465$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (2, 0):
                // $script:0831180509003466$
                // - I know everything about you, $OwnerName$.
                switch (selection) {
                    // $script:0831180509003467$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509003468$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509003469$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (3, 0):
                // $script:0831180509003470$
                // - Don't strain yourself, now.
                switch (selection) {
                    // $script:0831180509003471$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509003472$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509003473$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (4, 0):
                // $script:0831180509003474$
                // - $OwnerName$, let's go over your schedule for the day...
                switch (selection) {
                    // $script:0831180509003475$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509003476$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509003477$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509003478$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (5, 0):
                // $script:0831180509003479$
                // - I know everything about you, $OwnerName$.
                switch (selection) {
                    // $script:0831180509003480$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509003481$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509003482$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509003483$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (6, 0):
                // $script:0831180509003484$
                // - Don't strain yourself, now.
                switch (selection) {
                    // $script:0831180509003485$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509003486$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509003487$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509003488$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (9, 0):
                // $script:0831180509003489$
                // - Would you like to pay me?
                //   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
                switch (selection) {
                    // $script:0831180509003490$
                    // - Let me think about it some more.
                    case 0:
                        // TODO: goto 8040,8050,8060,9040
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509003491$
                    // - (Pay $MaidSalary$.)
                    case 1:
                        // TODO: goto 8000,8001,8010,8011,8901
                        // TODO: gotoFail 8900,8910
                        return 8900,8910;
                }
                return -1;
            case (8000, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509003492$
                // - Absolutely. I'll extend our employment contract. You'll want to read through all the fine print yourself on this one, $OwnerName$.
                return -1;
            case (8001, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509003493$
                // - Agreed. This arrangement is mutually beneficial, so this extension was expected. Here's to a long and prosperous relationship.
                return -1;
            case (8010, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509003494$
                // - Very well. I accept your terms. I hope you weren't expecting any thanks... I'm sure I've earned this.
                return -1;
            case (8011, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509003495$
                // - Confirmed. I accept the position. We have a great working relationship, as long as you continue to maintain a professional distance.
                return -1;
            case (8020, 0):
                // functionID=1 
                // $script:0831180509003496$
                // - $OwnerName$, our contract expires soon. No need to thank me. Managing your schedule is part of my job.
                return -1;
            case (8021, 0):
                // functionID=1 
                // $script:0831180509003497$
                // - Just don't make me repeat myself.
                switch (selection) {
                    // $script:0831180509003498$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509003499$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509003500$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509003501$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (8040, 0):
                // $script:0831180509003502$
                // - Don't strain yourself, now.
                switch (selection) {
                    // $script:0831180509003503$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509003504$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509003505$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509003506$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (8050, 0):
                // $script:0831180509003507$
                // - $OwnerName$, let's go over your schedule for the day...
                switch (selection) {
                    // $script:0831180509003508$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509003509$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509003510$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509003511$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (8060, 0):
                // $script:0831180509003512$
                // - Yes?
                switch (selection) {
                    // $script:0831180509003513$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509003514$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509003515$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509003516$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (8900, 0):
                // $script:0831180509003517$
                // - Ah, I expected this. Anyone can see that you're pretty wasteful.
                return -1;
            case (8901, 0):
                // $script:0831180509003518$
                // - You're even more financially inept than I anticipated. What I mean is, you've already paid me this month.
                return -1;
            case (8910, 0):
                // $script:0831180509003519$
                // - Yes, I already knew this would happen. I keep tabs on your bank account, you know. Please don't waste my time on this again. Now, I have some documents to sort through...
                return -1;
            case (8999, 0):
                // $script:0831180509003520$
                // - This is hardly ideal. Please don't allow this to happen again.
                return -1;
            case (9001, 0):
                // $script:0831180509003521$
                // - So. What is the plan?
                switch (selection) {
                    // $script:0831180509003522$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509003523$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509003524$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9002, 0):
                // $script:0831180509003525$
                // - Time is money, and... aren't your broke? Make this quick.
                switch (selection) {
                    // $script:0831180509003526$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509003527$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509003528$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9003, 0):
                // $script:0831180509003529$
                // - Our contract has expired. What else is there to discuss?
                switch (selection) {
                    // $script:0831180509003530$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509003531$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509003532$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9010, 0):
                // $script:0831180509003533$
                // - My contract has expired, and I live and breath by contracts. I can't work until you sign a new one.
                return -1;
            case (9011, 0):
                // functionID=1 
                // $script:0831180509003534$
                // - I'm stunned. Did you realize our contract expired, even after I reminded you? So let's talk about that. How could you let this happen?
                return -1;
            case (9020, 0):
                // functionID=1 
                // $script:0831180509003535$
                // - It's been $MaidPassedDay$ since our contract expired. You don't need to give me any excuses.
                return -1;
            case (9021, 0):
                // functionID=1 
                // $script:0831180509003536$
                // - Words won't change a thing.
                switch (selection) {
                    // $script:0831180509003537$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509003538$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509003539$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9040, 0):
                // $script:0831180509003540$
                // - If you don't have anything important to say, I'd like to go. Do you mind?
                switch (selection) {
                    // $script:0831180509003541$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509003542$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509003543$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9030, 0):
                // $script:0831180509003544$
                // - I don't have time to look after you unless you rehire me, but I'm not leaving either. My desk here is set up just the way I like it. So don't mind me. Just do whatever it is you need to do.
                return -1;
            case (9031, 0):
                // $script:0831180509003545$
                // - You've been acting so strange lately, not at all like yourself. What are you up to?
                return -1;
            case (9032, 0):
                // $script:0831180509003546$
                // - You want a drink? Really? Do you realize our contract remains unsigned? Now, excuse me. I have business to take care of.
                return -1;
            case (10, 0):
                // functionID=1 
                // $script:0831180509003547$
                // - Would you like a drink?
                return -1;
            case (11, 0):
                // functionID=1 
                // $script:0831180509003548$
                // - Come on, I insist.
                return -1;
            case (20, 0):
                // functionID=1 
                // $script:0831180509003549$
                // - Please, let's not mix business with pleasure.
                return -1;
            case (21, 0):
                // functionID=1 
                // $script:0831180509003550$
                // - I know everything about you, $OwnerName$.
                switch (selection) {
                    // $script:0831180509003551$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509003552$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509003553$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (22, 0):
                // functionID=1 
                // $script:0831180509003554$
                // - I know everything about you, $OwnerName$.
                switch (selection) {
                    // $script:0831180509003555$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509003556$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509003557$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509003558$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (30, 0):
                // $script:0831180509003559$
                // - I'm rather busy, so make this quick.
                switch (selection) {
                    // $script:0831180509003560$
                    // - Anything interesting happen today?
                    case 0:
                        // TODO: goto 1000,1100,2000,2100,2200,9011
                        return -1;
                    // $script:0831180509003561$
                    // - Tell me about $map:02000216$.
                    case 1:
                        // TODO: goto 3000,3100,4000,4100,9011
                        return -1;
                    // $script:0831180509003562$
                    // - (Ask your servant a personal question.)
                    case 2:
                        // TODO: goto 5000,5100,6000,6100,7000,9011
                        return -1;
                    // $script:0831180509003563$
                    // - Back.
                    case 3:
                        // TODO: goto 8040,8050,8060,40,50,60,9040
                        return -1;
                }
                return -1;
            case (31, 0):
                // $script:0831180509003564$
                // - $OwnerName$! You look absolutely wretched.
                switch (selection) {
                    // $script:0831180509003565$
                    // - Anything interesting happen today?
                    case 0:
                        // TODO: goto 1000,1100,2000,2100,2200,9011
                        return -1;
                    // $script:0831180509003566$
                    // - Tell me about $map:02000216$.
                    case 1:
                        // TODO: goto 3000,3100,4000,4100,9011
                        return -1;
                    // $script:0831180509003567$
                    // - (Ask your servant a personal question.)
                    case 2:
                        // TODO: goto 5000,5100,6000,6100,7000,9011
                        return -1;
                    // $script:0831180509003568$
                    // - Back.
                    case 3:
                        // TODO: goto 8040,8050,8060,40,50,60,9040
                        return -1;
                }
                return -1;
            case (32, 0):
                // $script:0831180509003569$
                // - ...I have nothing to say.
                switch (selection) {
                    // $script:0831180509003570$
                    // - Anything interesting happen today?
                    case 0:
                        // TODO: goto 1000,1100,2000,2100,2200,9011
                        return -1;
                    // $script:0831180509003571$
                    // - Tell me about $map:02000216$.
                    case 1:
                        // TODO: goto 3000,3100,4000,4100,9011
                        return -1;
                    // $script:0831180509003572$
                    // - (Ask your servant a personal question.)
                    case 2:
                        // TODO: goto 5000,5100,6000,6100,7000,9011
                        return -1;
                    // $script:0831180509003573$
                    // - Back.
                    case 3:
                        // TODO: goto 8040,8050,8060,40,50,60,9040
                        return -1;
                }
                return -1;
            case (40, 0):
                // $script:0831180509003574$
                // - Don't strain yourself, now.
                switch (selection) {
                    // $script:0831180509003575$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509003576$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509003577$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (50, 0):
                // $script:0831180509003578$
                // - $OwnerName$, let's go over your schedule for the day...
                switch (selection) {
                    // $script:0831180509003579$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509003580$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509003581$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (60, 0):
                // $script:0831180509003582$
                // - Yes?
                switch (selection) {
                    // $script:0831180509003583$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509003584$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509003585$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (1000, 0):
                // $script:0831180509003586$
                // - Be straight with me for a minute.
                return 1000;
            case (1000, 1):
                // $script:0831180509003587$
                // - You know I'm not working for you because I like you...
                return 1000;
            case (1000, 2):
                // $script:0831180509003588$
                // - So... why don't you just let me go?
                switch (selection) {
                    // $script:0831180509003589$
                    // - Hey, your skills are top notch.
                    case 0:
                        // TODO: goto 1011,1012
                        return -1;
                    // $script:0831180509003590$
                    // - I'm... I'm not really sure...
                    case 1:
                        // TODO: goto 1001,1002
                        return -1;
                }
                return -1;
            case (1001, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509003591$
                // - Talking to you makes me feel like I'm losing brain cells.
                return -1;
            case (1002, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509003592$
                // - Am I really stuck with you?
                return -1;
            case (1011, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509003593$
                // - Ah, perfect. That's just the way I like it.
                return -1;
            case (1012, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509003594$
                // - I appreciate your honesty. I may have been wrong about you.
                return -1;
            case (1100, 0):
                // $script:0831180509003595$
                // - Why are you staring at me?
                return 1100;
            case (1100, 1):
                // $script:0831180509003596$
                // - I'm used to people glaring at me at the Black Market, sure, but...
                return 1100;
            case (1100, 2):
                // $script:0831180509003597$
                // - I don't enjoy being gawked at by you. Please try to stop.
                switch (selection) {
                    // $script:0831180509003598$
                    // - I can't help it...
                    case 0:
                        // TODO: goto 1101,1102
                        return -1;
                    // $script:0831180509003599$
                    // - I'm so, so sorry!
                    case 1:
                        // TODO: goto 1111,1112
                        return -1;
                }
                return -1;
            case (1101, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509003600$
                // - Perhaps there is such a thing as too much honesty, after all...
                return -1;
            case (1102, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509003601$
                // - ... Does that mean you're not going to stop?
                return -1;
            case (1111, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509003602$
                // - Oh. Well, you don't have to go that far. Now things are uncomfortable...
                return -1;
            case (1112, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509003603$
                // - So you won't do it anymore? Good. 
                return -1;
            case (2000, 0):
                // $script:0831180509003604$
                // - Nothing I couldn't handle.
                return 2000;
            case (2000, 1):
                // $script:0831180509003605$
                // - Some men in masks barged into the house, demanding I hand over everything of value.
                return 2000;
            case (2000, 2):
                // $script:0831180509003606$
                // - Hmph. They won't be back.
                return 2000;
            case (2000, 3):
                // $script:0831180509003607$
                // - Even in my pencil skirt, I was able to bruise them up pretty good. I'm a certified instructor in several forms of martial arts.
                return 2000;
            case (2000, 4):
                // $script:0831180509003608$
                // - No need to look so shocked. In my line of work, self-defense is essential. Money makes people desperate, which can lead to crazy behavior, and I have to be able to make decisions without worrying about that.
                return -1;
            case (2100, 0):
                // $script:0831180509003609$
                // - $OwnerName$, while you were out, $npcName:11000004[gender:0]$ called once and $npcName:11000096[gender:0]$ called twice.
                return 2100;
            case (2100, 1):
                // $script:0831180509003610$
                // - $npcName:11000004[gender:0]$ stated that he received new product, which he thought you might be interested in.
                return 2100;
            case (2100, 2):
                // $script:0831180509003611$
                // - $npcName:11000096[gender:0]$ called because he can't get a hold of $npcName:11000106[gender:1]$ and was wondering if you knew where she was.
                return 2100;
            case (2100, 3):
                // $script:0831180509003612$
                // - Later, he called back to ask my name. I guess that part isn't really relevant.
                return 2100;
            case (2100, 4):
                // $script:0831180509003613$
                // - Now, excuse me. I have some goods to oversee.
                return -1;
            case (2200, 0):
                // $script:0831180509003614$
                // - $OwnerName$, you look exhausted. 
                return 2200;
            case (2200, 1):
                // $script:0831180509003615$
                // - It's a good thing I just made this special juice. Drink it. It'll give you an energy boost.
                return 2200;
            case (2200, 2):
                // $script:0831180509003616$
                // - I whipped it up myself. Maybe we should name it.
                return 2200;
            case (2200, 3):
                // $script:0831180509003617$
                // - It has a whole $npcName:21000001$ in it. How about we call it... Power Mush?
                return -1;
            case (3000, 0):
                // $script:0831180509003618$
                // - Most of the objects traded at the $map:02000216$ are rare and expensive.
                return 3000;
            case (3000, 1):
                // $script:0831180509003619$
                // - Why is the $map:02000216$ such a popular place to sell? It should be obvious.
                return 3000;
            case (3000, 2):
                // $script:0831180509003620$
                // - The $map:02000216$ is the only place you can trade valuable items quickly and safely.
                return 3000;
            case (3000, 3):
                // functionID=1 openTalkReward=True 
                // $script:0831180509003621$
                // - More importantly, you can remain anonymous. We don't ask questions about where you obtained your item at the $map:02000216$. All we care about is how much it's worth.
                return -1;
            case (3100, 0):
                // $script:0831180509003622$
                // - Today was exhausting. Funny how all it takes is a little ignorance to ruin your day, isn't it? We had a new customer show up at the $map:02000216$.
                return 3100;
            case (3100, 1):
                // $script:0831180509003623$
                // - He paid an exorbitant price for a cheap item without researching what he was buying.
                return 3100;
            case (3100, 2):
                // $script:0831180509003624$
                // - After he realized it, he raised a real ruckus, screaming that he'd been scammed, we'd hear from his lawyer, yadda yadda.
                return 3100;
            case (3100, 3):
                // $script:0831180509003625$
                // - It's not our fault he made a poor purchase. Even if we wanted to help, our policy at the $map:02000216$ is to never release the personal information of our sellers.
                return 3100;
            case (3100, 4):
                // functionID=1 openTalkReward=True 
                // $script:0831180509003626$
                // - Even you aren't above that policy, $OwnerName$, so be careful what you purchase and sell at the $map:02000216$.
                return -1;
            case (4000, 0):
                // $script:0831180509003627$
                // - Are you trying to ask about Blackstar? I had no idea you were even aware of that organization.
                return 4000;
            case (4000, 1):
                // $script:0831180509003628$
                // - Does this mean you've also heard of $npcName:11000251[gender:0]$? What exactly is it that you want to know?
                return 4000;
            case (4000, 2):
                // $script:0831180509003629$
                // - $npcName:11000251[gender:0]$ is one of the $map:02000216$'s many sponsors. He was instrumental in the establishment of the market.
                return 4000;
            case (4000, 3):
                // $script:0831180509003630$
                // - Do I hear suspicion in your tone? Are you trying to ruin our business relationship?
                return -1;
            case (4100, 0):
                // $script:0831180509003631$
                // - I'm perfectly aware that not everyone has a positive opinion of our business...
                return 4100;
            case (4100, 1):
                // $script:0831180509003632$
                // - But no one can deny that the $map:02000216$ has helped revitalize the economy in the area.
                return 4100;
            case (4100, 2):
                // $script:0831180509003633$
                // - Most of the citizens of $map:02000100$, including Mayor $npcName:11000065[gender:0]$, support us. We've made ourselves vital, and now we're unstoppable. 
                return -1;
            case (5000, 0):
                // $script:0831180509003634$
                // - Ah, this is specifically covered in our contract.
                return 5000;
            case (5000, 1):
                // $script:0831180509003635$
                // - You'll see in Section IV, Article 17, that for the duration of my period in your employ, you are not to pry into my personal business.
                return 5000;
            case (5000, 2):
                // $script:0831180509003636$
                // - Now, if you're done trying to break the rules of our contract, I'd like to return to work.
                return -1;
            case (5100, 0):
                // $script:0831180509003637$
                // - Such persistence, $OwnerName$! What exactly do you want to know so terribly much?
                return 5100;
            case (5100, 1):
                // $script:0831180509003638$
                // - My work history? My childhood? My relationship with my family?
                return 5100;
            case (5100, 2):
                // $script:0831180509003639$
                // - None of that makes a bit of difference. I know who I am: one of the top traders at the $map:02000216$ and your personal secretary. Does the rest matter?
                return -1;
            case (6000, 0):
                // $script:0831180509003640$
                // - I do have a hypothetical quandary to discuss with you. I'm interested in your opinion.
                return 6000;
            case (6000, 1):
                // $script:0831180509003641$
                // - Say there was a girl who grew up in the slums of $map:02000100$. An orphan, with no memory of her parents, begging and stealing and trying to survive.
                return 6000;
            case (6000, 2):
                // $script:0831180509003642$
                // - Let's say one day she tried to steal a man's wallet and was caught.
                return 6000;
            case (6000, 3):
                // $script:0831180509003643$
                // - To her surprise, instead of throwing her in jail, the man made a joke, admired her cleverness, then took her to his home, where he gave her clean clothes, a delicious meal, and a safe place to sleep, away from the vultures at the $map:02000100$
                return 6000;
            case (6000, 4):
                // $script:0831180509003644$
                // - She was so grateful for his kindness, she became determined to pay him back in any way she could. He had changed her life.
                return 6000;
            case (6000, 5):
                // $script:0831180509003645$
                // - For the next few decades, she worked tirelessly for that man. But then, one day, she learned that was he was doing was... morally abhorrent.
                return 6000;
            case (6000, 6):
                // $script:0831180509003646$
                // - Since then, she's been torn, unsure whether to follow her moral inclinations or remain loyal to the man who had saved her from a life on the streets. What would you do, if you were her? Remember, I'm asking for a friend.
                return -1;
            case (7000, 0):
                // $script:0831180509003647$
                // - You seem awfully curious to find out why I took on secretarial duties.
                return 7000;
            case (7000, 1):
                // $script:0831180509003648$
                // - Let's just say... I'm doing it as a favor for someone who's been like a father to me since I was a child.
                return 7000;
            case (7000, 2):
                // $script:0831180509003649$
                // - I'm here to track your every move. That's all I can tell you.
                return 7000;
            case (7000, 3):
                // $script:0831180509003650$
                // - As for who this man is... Heh. I don't know, why don't you try to find out? It could be someone you know.
                return -1;
            case (100, 0):
                // $script:0831180509003651$
                // - How may I help you?
                switch (selection) {
                    // $script:0831180509003652$
                    // - I'm here to see the owner.
                    case 0:
                        // TODO: goto 101,102
                        return -1;
                    // $script:0831180509003653$
                    // - I'm here to see you.
                    case 1:
                        // TODO: goto 103,104
                        return -1;
                    // $script:0831180509003654$
                    // - Who are you?
                    case 2:
                        // TODO: goto 105,106
                        return -1;
                }
                return -1;
            case (101, 0):
                // $script:0831180509003655$
                // - Did you? Strange. I don't have you in the schedule...
                return -1;
            case (102, 0):
                // $script:0831180509003656$
                // - If that's the case, please call me to schedule an appointment first.
                return -1;
            case (103, 0):
                // $script:0831180509003657$
                // - Interesting. If you have business with me, please come see me at the $map:02000216$ instead.
                return -1;
            case (104, 0):
                // $script:0831180509003658$
                // - Do I look like I have time for games?
                return -1;
            case (105, 0):
                // $script:0831180509003659$
                // - I am $MaidName$, $OwnerName$'s personal secretary. And you are...?
                return -1;
            case (106, 0):
                // $script:0831180509003660$
                // - I am the secretary of the owner of this house. Now, care to explain why you barged in uninvited?
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
            (2000, 4) => NpcTalkButton.Close,
            (2100, 0) => NpcTalkButton.Next,
            (2100, 1) => NpcTalkButton.Next,
            (2100, 2) => NpcTalkButton.Next,
            (2100, 3) => NpcTalkButton.Next,
            (2100, 4) => NpcTalkButton.Close,
            (2200, 0) => NpcTalkButton.Next,
            (2200, 1) => NpcTalkButton.Next,
            (2200, 2) => NpcTalkButton.Next,
            (2200, 3) => NpcTalkButton.Close,
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
            (5100, 2) => NpcTalkButton.Close,
            (6000, 0) => NpcTalkButton.Next,
            (6000, 1) => NpcTalkButton.Next,
            (6000, 2) => NpcTalkButton.Next,
            (6000, 3) => NpcTalkButton.Next,
            (6000, 4) => NpcTalkButton.Next,
            (6000, 5) => NpcTalkButton.Next,
            (6000, 6) => NpcTalkButton.Close,
            (7000, 0) => NpcTalkButton.Next,
            (7000, 1) => NpcTalkButton.Next,
            (7000, 2) => NpcTalkButton.Next,
            (7000, 3) => NpcTalkButton.Close,
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
