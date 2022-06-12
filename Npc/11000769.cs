using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000769: Manu
/// </summary>
public class _11000769 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 1;2;3;4;5;6;9001;9002;9003;100
    }

    // Select 0:
    // $script:0831180509001629$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (1, 0):
                // $script:0831180509001630$
                // - Did you call me, $OwnerName$?
                switch (selection) {
                    // $script:0831180509001631$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001632$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001633$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (2, 0):
                // $script:0831180509001634$
                // - Have a great day, $OwnerName$!
                switch (selection) {
                    // $script:0831180509001635$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001636$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001637$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (3, 0):
                // $script:0831180509001638$
                // - Yes, $OwnerName$?
                switch (selection) {
                    // $script:0831180509001639$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001640$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001641$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (4, 0):
                // $script:0831180509001642$
                // - Did you call me, $OwnerName$?
                switch (selection) {
                    // $script:0831180509001643$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001644$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001645$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509001646$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (5, 0):
                // $script:0831180509001647$
                // - Have a great day, $OwnerName$!
                switch (selection) {
                    // $script:0831180509001648$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001649$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001650$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509001651$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (6, 0):
                // $script:0831180509001652$
                // - Yes, $OwnerName$?
                switch (selection) {
                    // $script:0831180509001653$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001654$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001655$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509001656$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (9, 0):
                // $script:0831180509001657$
                // - Mm? Are you going to pay me?
                //   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
                switch (selection) {
                    // $script:0831180509001658$
                    // - Never mind.
                    case 0:
                        // TODO: goto 8040,8050,8060,9040
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001659$
                    // - (Pay $MaidSalary$.)
                    case 1:
                        // TODO: goto 8000,8001,8010,8011,8901
                        // TODO: gotoFail 8900,8910
                        return -1;
                }
                return -1;
            case (8000, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001660$
                // - Oh, I'm so glad you found me useful. Thank you for extending our contract. I'm happy to stay with you for another month.
                return -1;
            case (8001, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001661$
                // - Hah hah hah, it feels great to get paid for my work work. Thank you.
                return -1;
            case (8010, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001662$
                // - Ah, this explains your cheerful mood. What's good for you is good for me, and vice versa. That's what friends are for, right? To share in each other's happiness.
                return -1;
            case (8011, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001663$
                // - Ah, I know I said everything was fine, but it really wasn't. I didn't want to tell you the truth, because I knew it was harder on you than it was on me. I'm glad everything worked out! Hah hah!
                return -1;
            case (8020, 0):
                // functionID=1 
                // $script:0831180509001664$
                // - In case you've forgotten, our contract expires soon. I know it's not easy keeping track of everything going on in your life.
                return -1;
            case (8021, 0):
                // functionID=1 
                // $script:0831180509001665$
                // - But that's what I'm here for. Hah hah.
                switch (selection) {
                    // $script:0831180509001666$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001667$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001668$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509001669$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (8040, 0):
                // $script:0831180509001670$
                // - You can tell me anything.
                switch (selection) {
                    // $script:0831180509001671$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001672$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001673$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509001674$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (8050, 0):
                // $script:0831180509001675$
                // - Sometimes, I feel lonely when I'm by myself.
                switch (selection) {
                    // $script:0831180509001676$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001677$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001678$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509001679$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (8060, 0):
                // $script:0831180509001680$
                // - Yikes... My back's killing me today... 
                switch (selection) {
                    // $script:0831180509001681$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001682$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001683$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509001684$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (8900, 0):
                // $script:0831180509001685$
                // - Oh, aren't you a bit short on funds right now? Thank you for at least trying to pay me. I'm sure you'll get some mesos soon, so don't feel too bad. Hah hah hah.
                return -1;
            case (8901, 0):
                // $script:0831180509001686$
                // - You want to pay me? But you've already paid me for the month. You're as forgetful as I am sometimes.
                return -1;
            case (8910, 0):
                // $script:0831180509001687$
                // - You've got nothing but dust in your pockets. I kind of knew this was the case. It's all right. Don't you worry about this old man... 
                return -1;
            case (8999, 0):
                // $script:0831180509001688$
                // - Hm, strange things happen all the time. Don't panic. Calm yourself and try again.
                return -1;
            case (9001, 0):
                // $script:0831180509001689$
                // - Aww... Why do you look so exhausted? 
                switch (selection) {
                    // $script:0831180509001690$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509001691$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001692$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9002, 0):
                // $script:0831180509001693$
                // - The older you get, the less food your body needs.
                switch (selection) {
                    // $script:0831180509001694$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509001695$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001696$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9003, 0):
                // $script:0831180509001697$
                // - Having nothing to do is so dull. It's been $MaidPassedDay$ since I've had a job.
                switch (selection) {
                    // $script:0831180509001698$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509001699$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001700$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9010, 0):
                // $script:0831180509001701$
                // - Ah, if we could take a moment to talk about my contract... I believe it's expired.
                return -1;
            case (9011, 0):
                // functionID=1 
                // $script:0831180509001702$
                // - Sure, but if we could take a moment to talk about my contract... I believe it's expired.
                return -1;
            case (9020, 0):
                // functionID=1 
                // $script:0831180509001703$
                // - I told you not to worry about me. Everything will work out eventually.
                return -1;
            case (9021, 0):
                // functionID=1 
                // $script:0831180509001704$
                // - The power of positive thinking, right? Hah hah. 
                switch (selection) {
                    // $script:0831180509001705$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509001706$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001707$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9040, 0):
                // $script:0831180509001708$
                // - I don't think I can go for a walk today. My knees are aching... 
                switch (selection) {
                    // $script:0831180509001709$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509001710$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001711$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9030, 0):
                // $script:0831180509001712$
                // - When the wind becomes overwhelming, mimic the reeds. Follow the wind without losing your footing. Hah hah hah, are you thinking I've finally lost my mind? I just thought you could use some encouragement.
                return -1;
            case (9031, 0):
                // $script:0831180509001713$
                // - I miss my wife. When things got tough for us, like they are for your now, Madelle helped me get through it. What I'm trying to say is, I may not be able to do much, but I'm here for you.
                return -1;
            case (9032, 0):
                // $script:0831180509001714$
                // - Everyone should experience poverty at least once. It gives you perspective. Once you've climbed a cliff, even the steepest hill is no longer intimidating.
                return -1;
            case (10, 0):
                // functionID=1 
                // $script:0831180509001715$
                // - Ask me for anything. I'll make it for you if I can.
                return -1;
            case (11, 0):
                // functionID=1 
                // $script:0831180509001716$
                // - Don't worry about it. I'm doing this to pass time.
                return -1;
            case (20, 0):
                // functionID=1 
                // $script:0831180509001717$
                // - Do you have questions for me?
                return -1;
            case (21, 0):
                // functionID=1 
                // $script:0831180509001718$
                // - Hm, it's not easy to describe oneself in just a few words. 
                switch (selection) {
                    // $script:0831180509001719$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001720$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001721$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (22, 0):
                // functionID=1 
                // $script:0831180509001722$
                // - Hm, it's not easy to describe oneself in just a few words. 
                switch (selection) {
                    // $script:0831180509001723$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001724$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001725$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509001726$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (30, 0):
                // $script:0831180509001727$
                // - I love talking to people.
                switch (selection) {
                    // $script:0831180509001728$
                    // - Anything interesting happen today?
                    case 0:
                        // TODO: goto 1000,1100,1200,1300,1400,1500,1600,2000,2100,2200,9011
                        return -1;
                    // $script:0831180509001729$
                    // - Tell me a story!
                    case 1:
                        // TODO: goto 3000,3100,4000,4100,4200,4300,9011
                        return -1;
                    // $script:0831180509001730$
                    // - (Ask your servant a personal question.)
                    case 2:
                        // TODO: goto 5000,5100,6000,7000,9011
                        return -1;
                    // $script:0831180509001731$
                    // - Back.
                    case 3:
                        // TODO: goto 8040,8050,8060,40,50,60,9040
                        return -1;
                }
                return -1;
            case (31, 0):
                // $script:0831180509001732$
                // - Oh, you want to keep this old man company?
                switch (selection) {
                    // $script:0831180509001733$
                    // - Anything interesting happen today?
                    case 0:
                        // TODO: goto 1000,1100,1200,1300,1400,1500,1600,2000,2100,2200,9011
                        return -1;
                    // $script:0831180509001734$
                    // - Tell me a story!
                    case 1:
                        // TODO: goto 3000,3100,4000,4100,4200,4300,9011
                        return -1;
                    // $script:0831180509001735$
                    // - (Ask your servant a personal question.)
                    case 2:
                        // TODO: goto 5000,5100,6000,7000,9011
                        return -1;
                    // $script:0831180509001736$
                    // - Back.
                    case 3:
                        // TODO: goto 8040,8050,8060,40,50,60,9040
                        return -1;
                }
                return -1;
            case (32, 0):
                // $script:0831180509001737$
                // - What kind of story? Is there something in particular you want to hear?
                switch (selection) {
                    // $script:0831180509001738$
                    // - Anything interesting happen today?
                    case 0:
                        // TODO: goto 1000,1100,1200,1300,1400,1500,1600,2000,2100,2200,9011
                        return -1;
                    // $script:0831180509001739$
                    // - Tell me a story!
                    case 1:
                        // TODO: goto 3000,3100,4000,4100,4200,4300,9011
                        return -1;
                    // $script:0831180509001740$
                    // - (Ask your servant a personal question.)
                    case 2:
                        // TODO: goto 5000,5100,6000,7000,9011
                        return -1;
                    // $script:0831180509001741$
                    // - Back.
                    case 3:
                        // TODO: goto 8040,8050,8060,40,50,60,9040
                        return -1;
                }
                return -1;
            case (40, 0):
                // $script:0831180509001742$
                // - You can tell me anything.
                switch (selection) {
                    // $script:0831180509001743$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001744$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001745$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (50, 0):
                // $script:0831180509001746$
                // - Sometimes, I feel lonely when I'm by myself.
                switch (selection) {
                    // $script:0831180509001747$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001748$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001749$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (60, 0):
                // $script:0831180509001750$
                // - Yikes... My back's killing me today... 
                switch (selection) {
                    // $script:0831180509001751$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001752$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001753$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (1000, 0):
                // $script:0831180509001754$
                // - Oh, I almost forgot.
                return 1000;
            case (1000, 1):
                // $script:0831180509001755$
                // - It felt so strange cooking for the first time in decades. Worse, everything was so blurry I could hardly tell the difference between sugar and salt.
                return 1000;
            case (1000, 2):
                // $script:0831180509001756$
                // - So I just used the first thing I grabbed. Turns out, it was the wrong one. But you looked hungry, so here it is!
                switch (selection) {
                    // $script:0831180509001757$
                    // - It's too salty.
                    case 0:
                        // TODO: goto 1001,1002
                        return -1;
                    // $script:0831180509001758$
                    // - It's delicious.
                    case 1:
                        // TODO: goto 1011,1012
                        return -1;
                }
                return -1;
            case (1001, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001759$
                // - Is it? Then please spit it out. This is your house and I'm your employee. You don't have to eat it if you don't want to.
                return -1;
            case (1002, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001760$
                // - Consuming too much salt makes you thirsty, which leads to drinking too much water, which leads to swelling in your face. So you should stop eating the food.
                return -1;
            case (1011, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001761$
                // - Hah hah hah, I know I'm not a good cook. Thank you for saying that.
                return -1;
            case (1012, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001762$
                // - When you're hungry, anything you eat tastes good. Hah hah hah, slow down. No one's going to fight you for that.
                return -1;
            case (1100, 0):
                // $script:0831180509001763$
                // - Guess what I have in my hand...?
                return 1100;
            case (1100, 1):
                // $script:0831180509001764$
                // - Snacks! I thought you might be hungry.
                return 1100;
            case (1100, 2):
                // $script:0831180509001765$
                // - It tastes better than it looks. I hope.
                switch (selection) {
                    // $script:0831180509001766$
                    // - Great! I was feeling a little hungry!
                    case 0:
                        // TODO: goto 1111,1112
                        return -1;
                    // $script:0831180509001767$
                    // - I'll pass. I'm, um, trying to lose weight. Yeah.
                    case 1:
                        // TODO: goto 1101,1102
                        return -1;
                }
                return -1;
            case (1101, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001768$
                // - Why? You're nothing but skin and bone. You look like you could blow away in the wind. Come on, just eat it.
                return -1;
            case (1102, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001769$
                // - Are you? Being overweight can cause diabetes, high blood pressure, hardening of the arteries, and other chronic diseases. Hm, should I be worried?
                return -1;
            case (1111, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001770$
                // - Hah hah hah, that's why I've made this! When you're my age, you get to read people more easily.
                return -1;
            case (1112, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001771$
                // - Do you get always get hungry around this time? Because I do.
                return -1;
            case (1200, 0):
                // $script:0831180509001772$
                // - I was visiting the senior center today, and someone gave me this drink. I thought you might like it.
                return 1200;
            case (1200, 1):
                // $script:0831180509001773$
                // - When you get to be my age, you already know what you like and don't want to try new things.
                switch (selection) {
                    // $script:0831180509001774$
                    // - Aw, you should try it. You might like it.
                    case 0:
                        // TODO: goto 1201,1202
                        return -1;
                    // $script:0831180509001775$
                    // - Hey, thanks!
                    case 1:
                        // TODO: goto 1211,1212
                        return -1;
                }
                return -1;
            case (1201, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001776$
                // - No, thank you. New food stopped tasting good to me some time ago. At first, it all tasted disgusting, but now it just doesn't taste like anything.
                return -1;
            case (1202, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001777$
                // - I'll be happy just to watch you drink it. Go on, take it.
                return -1;
            case (1211, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001778$
                // - The person who gave it to me said it's very nutritious. If you like it, let me know. I can ask him for more.
                return -1;
            case (1212, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001779$
                // - I'm so glad you accepted it. I would've felt awkward if you said refused.
                return -1;
            case (1300, 0):
                // $script:0831180509001780$
                // - I cooked some food my wife used to make. I never watched her cook, though.
                return 1300;
            case (1300, 1):
                // $script:0831180509001781$
                // - It tastes like its missing something, but I can't quite put my finger on it... What do you think?
                switch (selection) {
                    // $script:0831180509001782$
                    // - Hmm, not bad, but could use a sprinkle of MSG.
                    case 0:
                        // TODO: goto 1301,1302
                        return -1;
                    // $script:0831180509001783$
                    // - It's pretty delicious just the way it is.
                    case 1:
                        // TODO: goto 1311,1312
                        return -1;
                }
                return -1;
            case (1301, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001784$
                // - Hmm? MSG? I'll just use a pinch, and... Mm, mm! Yes, now it tastes perfect!
                return -1;
            case (1302, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001785$
                // - Hmmm, why don't you try tasting it again in a little bit and let me know what you think then?
                return -1;
            case (1311, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001786$
                // - I'm glad you're not a picky eater, $OwnerName$. Thank you for eating everything I cook for you.
                return -1;
            case (1312, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001787$
                // - You may think so, but I can tell something is missing. I should've asked my wife when I could... It's just another one of the many, many things I miss about her.
                return -1;
            case (1400, 0):
                // $script:0831180509001788$
                // - Tsk, you should be more careful. I found this by the front door on my way out.
                return 1400;
            case (1400, 1):
                // $script:0831180509001789$
                // - Usually, I can't see far enough to notice an item on the ground, but lucky for you, I had to adjust my shoes.
                switch (selection) {
                    // $script:0831180509001790$
                    // - Thanks for finding it.
                    case 0:
                        // TODO: goto 1411,1412
                        return -1;
                    // $script:0831180509001791$
                    // - It's not mine.
                    case 1:
                        // TODO: goto 1401,1402
                        return -1;
                }
                return -1;
            case (1401, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001792$
                // - It's not? Some stranger barged into the house the other day. Maybe he dropped it. I'd better keep it in case he comes back.
                return -1;
            case (1402, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001793$
                // - Then how did it get here? Anyway, since this is your house, the item belongs to you now, so you take it.
                return -1;
            case (1411, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001794$
                // - Happy to be of help.
                return -1;
            case (1412, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001795$
                // - You should take better care of your things.
                return -1;
            case (1500, 0):
                // $script:0831180509001796$
                // - I ran into Choi the real estate agent on my way home today. One of his clients just moved to a smaller and gave him a bunch of furniture that wouldn't fit.
                return 1500;
            case (1500, 1):
                // $script:0831180509001797$
                // - It was way too much, but Choi didn't want to throw it out, either. He asked me to take whatever I wanted, so I grabbed this. It looked like the best of the bunch. It's all yours now!
                switch (selection) {
                    // $script:0831180509001798$
                    // - I don't really need it...
                    case 0:
                        // TODO: goto 1501,1502
                        return -1;
                    // $script:0831180509001799$
                    // - Thanks!
                    case 1:
                        // TODO: goto 1511,1512
                        return -1;
                }
                return -1;
            case (1501, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001800$
                // - Hm, then what should I do with it? I don't think Choi will take it back, and I don't want to throw it away.
                return -1;
            case (1502, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001801$
                // - Hah hah hah, I guess I shouldn't have taken it! Everyone makes mistakes, and mistakes teach you valuable lessons. Those who claim never to have made a mistake are either lying to themselves or not living life to the fullest.
                return -1;
            case (1511, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001802$
                // - So I picked something good, huh? I'm glad to be of help.
                return -1;
            case (1512, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001803$
                // - Do you need anything else? Choi had a lot of other stuff, too.
                return -1;
            case (1600, 0):
                // $script:0831180509001804$
                // - Do you know what happened today? I was out walking when I ran into an overturned wagon. I helped the owner move it back into place.
                return 1600;
            case (1600, 1):
                // $script:0831180509001805$
                // - And he gave me money for helping him. Hah hah hah! Here, take it. I've got no use for so much money. Think of it as an allowance from your grandpa.
                switch (selection) {
                    // $script:0831180509001806$
                    // - Hey, thanks!
                    case 0:
                        // TODO: goto 1611,1612
                        return -1;
                    // $script:0831180509001807$
                    // - I can't take your money!
                    case 1:
                        // TODO: goto 1601,1602
                        return -1;
                }
                return -1;
            case (1601, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001808$
                // - It was easy money. Come on, I insist.
                return -1;
            case (1602, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001809$
                // - I wouldn't have offered it if I didn't care about you. The greatest happiness in life comes from knowing that you're being loved. This may not be the best way to show it, but I'm quite fond of you.
                return -1;
            case (1611, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001810$
                // - What a great day! I got to help someone, get free money, and give you an allowance! Hah!
                return -1;
            case (1612, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001811$
                // - Hah hah hah, how wonderful! Oof, I'm aching all over now. I'll probably spend more on pain medicine than I earned...
                return -1;
            case (2000, 0):
                // $script:0831180509001812$
                // - Not much. I worked around the house all day.
                return 2000;
            case (2000, 1):
                // $script:0831180509001813$
                // - A writer once said the people weren't born to work. If we were, it wouldn't make us so tired.
                return 2000;
            case (2000, 2):
                // $script:0831180509001814$
                // - I agree with him, now that I know how tiresome housework really is.
                return -1;
            case (2100, 0):
                // $script:0831180509001815$
                // - I was thinking of my wife while I cleaned today. She used to hum when she did her chores.
                return 2100;
            case (2100, 1):
                // $script:0831180509001816$
                // - So I tried that today. It actually lifted my spirits and made the work less boring.
                return -1;
            case (2200, 0):
                // $script:0831180509001817$
                // - Nothing happened to me or the house, but...
                return 2200;
            case (2200, 1):
                // $script:0831180509001818$
                // - I met Choi the real estate agent while taking a walk. He said he saw someone hanging onto a flying eagle.
                return 2200;
            case (2200, 2):
                // $script:0831180509001819$
                // - I don't know why he makes such absurd claims sometimes. It would've been more believable if he said he saw someone hanging onto a balloon. Hah hah.
                return -1;
            case (3000, 0):
                // $script:0831180509001820$
                // - While I was grocery shopping, I saw the comedian who plays the fool on that popular TV show. The kids there were copying his character and laughing at him.
                return 3000;
            case (3000, 1):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001821$
                // - A great comedy writer once said, "The toughest role in comedy is the fool, and playing it requires a genius."
                return -1;
            case (3100, 0):
                // $script:0831180509001822$
                // - I was watching a TV quiz show this morning. There were three doors. Two of them had a goat behind them, and the third had an expensive mount. The contestant didn't know which was which, of course.
                return 3100;
            case (3100, 1):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001823$
                // - So he picked a door. The host opened one of the other doors to reveal a goat. He then asked the contestant if he wanted to change his choice. What would you do if it were you?
                return -1;
            case (4000, 0):
                // $script:0831180509001824$
                // - I'm not a funny person, and I don't know any funny stories. Hah hah hah. But I know how to keep people engaged in what I'm saying, and that's to tell them what I think of them.
                return 4000;
            case (4000, 1):
                // $script:0831180509001825$
                // - I can tell you what I think of you, if you want. Oh, your ears are already perking up! Hah hah!
                return -1;
            case (4100, 0):
                // $script:0831180509001826$
                // - Once upon a time...
                //   ...
                //   ...
                return 4100;
            case (4100, 1):
                // $script:0831180509001827$
                // - Are you asleep?
                return -1;
            case (5000, 0):
                // $script:0831180509001828$
                // - You want to ask me something personal?
                return 5000;
            case (5000, 1):
                // $script:0831180509001829$
                // - We all are like the moon: each one of us has a dark side that we don't want to show others.
                return 5000;
            case (5000, 2):
                // $script:0831180509001830$
                // - If you're asking about my dark side, I'd rather not talk about it. Let's talk about yours instead. I'm all ears.
                return 5000;
            case (5000, 3):
                // $script:0831180509001831$
                // - You've been all over Victoria Island. Which part do you like the most?
                return 5000;
            case (5000, 4):
                // $script:0831180509001832$
                // - I don't care if you go anywhere else, but please don't go to $map:2000124$.
                return -1;
            case (5100, 0):
                // $script:0831180509001833$
                // - One morning I woke up to realize that all my desire for worldly wealth had vanished overnight. Everything here is fleeting.
                return 5100;
            case (5100, 1):
                // $script:0831180509001834$
                // - The realization that the years you have left are fewer than the years you've already lived does that to you.
                return 5100;
            case (5100, 2):
                // $script:0831180509001835$
                // - An old scholar once said man's purpose is to make meaningless things meaningful. I'd better live whatever life I have left to the fullest, so I can die without regrets.
                return 5100;
            case (5100, 3):
                // $script:0831180509001836$
                // - I really like this job. When my wife passed, I was so heartbroken that I didn't want to do anything for a long, long time.
                return 5100;
            case (5100, 4):
                // $script:0831180509001837$
                // - Then I realized living in the past was doing me more harm than good.
                return 5100;
            case (5100, 5):
                // $script:0831180509001838$
                // - So I decided to let the past go, enjoy the present, and wait for whatever the future brings.
                return -1;
            case (6000, 0):
                // $script:0831180509001839$
                // - I started writing a while ago. But I'm not writing a novel.
                return 6000;
            case (6000, 1):
                // $script:0831180509001840$
                // - I'm not writing something to show others. It's just for myself.
                return 6000;
            case (6000, 2):
                // $script:0831180509001841$
                // - Someone once told me that writing helps you deal with difficult emotions and find happiness again.
                return 6000;
            case (6000, 3):
                // $script:0831180509001842$
                // - So I'm writing to be happy. Please don't be too nosy about what I'm writing.
                return 6000;
            case (6000, 4):
                // $script:0831180509001843$
                // - Does my writing include things about you? Well... You'll see for yourself if I decide to show you one day.
                return -1;
            case (7000, 0):
                // $script:0831180509001844$
                // - You want to know about me and my wife? I can't think of anything special to say. Hah hah. 
                return 7000;
            case (7000, 1):
                // $script:0831180509001845$
                // - It was always just the two of us, me and Madelle. We couldn't have children... That was hard for both of us.
                return 7000;
            case (7000, 2):
                // $script:0831180509001846$
                // - In hindsight, maybe that made us even closer. It was a pain we shared together. 
                return 7000;
            case (7000, 3):
                // $script:0831180509001847$
                // - Am I sorry that I don't have children? No. But I miss the time I shared with my wife.
                return 7000;
            case (7000, 4):
                // $script:0831180509001848$
                // - Being with Madelle, I always felt warm and peaceful. We'd been together for so long that we could read each other's thoughts. But when I think about it now, I wish I had talked to her more often.
                return 7000;
            case (7000, 5):
                // $script:0831180509001849$
                // - Do you have someone you love? If not, I hope you find someone as good as my Madelle.
                return -1;
            case (100, 0):
                // $script:0831180509001850$
                // - I didn't hear the bell ring. May I ask who you are? Are you here to see the owner of the house?
                switch (selection) {
                    // $script:0831180509001851$
                    // - Yep!
                    case 0:
                        // TODO: goto 101,102
                        return -1;
                    // $script:0831180509001852$
                    // - Nope!
                    case 1:
                        // TODO: goto 103,104
                        return -1;
                    // $script:0831180509001853$
                    // - Who are you?
                    case 2:
                        // TODO: goto 105,106
                        return -1;
                }
                return -1;
            case (101, 0):
                // $script:0831180509001854$
                // - I work for him. If you'd like me to pass along a message... Actually, no. That was presumptuous of me. You probably want to speak in person.
                return -1;
            case (102, 0):
                // $script:0831180509001855$
                // - I see. Just pretend I'm not here and make yourself at home.
                return -1;
            case (103, 0):
                // $script:0831180509001856$
                // - Then what brings you here? How did you get in, anyway? Was the door open?
                return -1;
            case (104, 0):
                // $script:0831180509001857$
                // - Then what brings you here? If you're here for an open house, you've got the wrong address. This home is not for sale.
                return -1;
            case (105, 0):
                // $script:0831180509001858$
                // - Common courtesy would be introduce yourself first before asking, but I'll cut you some slack. I'm not a stickler for the rules anyway, hah hah.
                return -1;
            case (106, 0):
                // $script:0831180509001859$
                // - I am the housekeeper. Now, may I ask who you are?
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
            (1200, 0) => NpcTalkButton.Next,
            (1200, 1) => NpcTalkButton.SelectableDistractor,
            (1201, 0) => NpcTalkButton.Close,
            (1202, 0) => NpcTalkButton.Close,
            (1211, 0) => NpcTalkButton.Close,
            (1212, 0) => NpcTalkButton.Close,
            (1300, 0) => NpcTalkButton.Next,
            (1300, 1) => NpcTalkButton.SelectableDistractor,
            (1301, 0) => NpcTalkButton.Close,
            (1302, 0) => NpcTalkButton.Close,
            (1311, 0) => NpcTalkButton.Close,
            (1312, 0) => NpcTalkButton.Close,
            (1400, 0) => NpcTalkButton.Next,
            (1400, 1) => NpcTalkButton.SelectableDistractor,
            (1401, 0) => NpcTalkButton.Close,
            (1402, 0) => NpcTalkButton.Close,
            (1411, 0) => NpcTalkButton.Close,
            (1412, 0) => NpcTalkButton.Close,
            (1500, 0) => NpcTalkButton.Next,
            (1500, 1) => NpcTalkButton.SelectableDistractor,
            (1501, 0) => NpcTalkButton.Close,
            (1502, 0) => NpcTalkButton.Close,
            (1511, 0) => NpcTalkButton.Close,
            (1512, 0) => NpcTalkButton.Close,
            (1600, 0) => NpcTalkButton.Next,
            (1600, 1) => NpcTalkButton.SelectableDistractor,
            (1601, 0) => NpcTalkButton.Close,
            (1602, 0) => NpcTalkButton.Close,
            (1611, 0) => NpcTalkButton.Close,
            (1612, 0) => NpcTalkButton.Close,
            (2000, 0) => NpcTalkButton.Next,
            (2000, 1) => NpcTalkButton.Next,
            (2000, 2) => NpcTalkButton.Close,
            (2100, 0) => NpcTalkButton.Next,
            (2100, 1) => NpcTalkButton.Close,
            (2200, 0) => NpcTalkButton.Next,
            (2200, 1) => NpcTalkButton.Next,
            (2200, 2) => NpcTalkButton.Close,
            (3000, 0) => NpcTalkButton.Next,
            (3000, 1) => NpcTalkButton.Close,
            (3100, 0) => NpcTalkButton.Next,
            (3100, 1) => NpcTalkButton.Close,
            (4000, 0) => NpcTalkButton.Next,
            (4000, 1) => NpcTalkButton.Close,
            (4100, 0) => NpcTalkButton.Next,
            (4100, 1) => NpcTalkButton.Close,
            (5000, 0) => NpcTalkButton.Next,
            (5000, 1) => NpcTalkButton.Next,
            (5000, 2) => NpcTalkButton.Next,
            (5000, 3) => NpcTalkButton.Next,
            (5000, 4) => NpcTalkButton.Close,
            (5100, 0) => NpcTalkButton.Next,
            (5100, 1) => NpcTalkButton.Next,
            (5100, 2) => NpcTalkButton.Next,
            (5100, 3) => NpcTalkButton.Next,
            (5100, 4) => NpcTalkButton.Next,
            (5100, 5) => NpcTalkButton.Close,
            (6000, 0) => NpcTalkButton.Next,
            (6000, 1) => NpcTalkButton.Next,
            (6000, 2) => NpcTalkButton.Next,
            (6000, 3) => NpcTalkButton.Next,
            (6000, 4) => NpcTalkButton.Close,
            (7000, 0) => NpcTalkButton.Next,
            (7000, 1) => NpcTalkButton.Next,
            (7000, 2) => NpcTalkButton.Next,
            (7000, 3) => NpcTalkButton.Next,
            (7000, 4) => NpcTalkButton.Next,
            (7000, 5) => NpcTalkButton.Close,
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
