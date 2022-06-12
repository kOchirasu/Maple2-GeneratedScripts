using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000774: Mino
/// </summary>
public class _11000774 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 1;2;3;4;5;6;9001;9002;9003;100
    }

    // Select 0:
    // $script:0831180509002784$
    // - Hey, what's up?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (1, 0):
                // $script:0831180509002785$
                // - Hey, you're back.
                switch (selection) {
                    // $script:0831180509002786$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509002787$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509002788$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (2, 0):
                // $script:0831180509002789$
                // - On days like this, I love to chill with friendly folks on the street. You?
                switch (selection) {
                    // $script:0831180509002790$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509002791$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509002792$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (3, 0):
                // $script:0831180509002793$
                // - Welcome back, $OwnerName$. Things went well, I take it?
                switch (selection) {
                    // $script:0831180509002794$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509002795$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509002796$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (4, 0):
                // $script:0831180509002797$
                // - Hey, you're back.
                switch (selection) {
                    // $script:0831180509002798$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509002799$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509002800$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509002801$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (5, 0):
                // $script:0831180509002802$
                // - On days like this, I love to chill with friendly folks on the street. You?
                switch (selection) {
                    // $script:0831180509002803$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509002804$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509002805$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509002806$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (6, 0):
                // $script:0831180509002807$
                // - Welcome back, $OwnerName$. Things went well, I take it?
                switch (selection) {
                    // $script:0831180509002808$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509002809$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509002810$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509002811$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (9, 0):
                // $script:0831180509002812$
                // - Is it time for my paycheck?
                //   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
                switch (selection) {
                    // $script:0831180509002813$
                    // - Let me think about it some more.
                    case 0:
                        // TODO: goto 8040,8050,8060,9040
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509002814$
                    // - (Pay $MaidSalary$.)
                    case 1:
                        // TODO: goto 8000,8001,8010,8011,8901
                        // TODO: gotoFail 8900,8910
                        return -1;
                }
                return -1;
            case (8000, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002815$
                // - Nah, I'm happy to share your burden.
                return -1;
            case (8001, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002816$
                // - My muse is knocking. I need to go answer.
                return -1;
            case (8010, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002817$
                // - Nah, I'm happy to share your burden.
                return -1;
            case (8011, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002818$
                // - My muse is knocking. I need to go answer.
                return -1;
            case (8020, 0):
                // functionID=1 
                // $script:0831180509002819$
                // - Our contract is up soon, $OwnerName$. 
                return -1;
            case (8021, 0):
                // functionID=1 
                // $script:0831180509002820$
                // - Write it down or something, and free your mind to think about something else.
                switch (selection) {
                    // $script:0831180509002821$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509002822$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509002823$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509002824$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (8040, 0):
                // $script:0831180509002825$
                // - Is there something you want to say?
                switch (selection) {
                    // $script:0831180509002826$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509002827$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509002828$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509002829$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (8050, 0):
                // $script:0831180509002830$
                // - You wanna chat? Was there something you wanted to ask me?
                switch (selection) {
                    // $script:0831180509002831$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509002832$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509002833$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509002834$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (8060, 0):
                // $script:0831180509002835$
                // - Haven't we been talking this whole time? Or is my memory playing tricks on me again...
                switch (selection) {
                    // $script:0831180509002836$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509002837$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509002838$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509002839$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (8900, 0):
                // $script:0831180509002840$
                // - Thanks, but you don't have to try so hard. I can wait until you can really afford it. Just roll with the punches, know what I mean?
                return -1;
            case (8901, 0):
                // $script:0831180509002841$
                // - In your heart, can you feel it? Can you feel that you already paid me this month? It's like a poem, deep inside you.
                return -1;
            case (8910, 0):
                // $script:0831180509002842$
                // - Thanks, but you don't have to try so hard. I can wait until you can really afford it. Just roll with the punches, know what I mean?
                return -1;
            case (8999, 0):
                // $script:0831180509002843$
                // - Sure, sure, I can wait. We can always talk about something else.
                return -1;
            case (9001, 0):
                // $script:0831180509002844$
                // - Take responsibility, you know? Don't blame someone else.
                switch (selection) {
                    // $script:0831180509002845$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509002846$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509002847$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9002, 0):
                // $script:0831180509002848$
                // - Nothing in this world lasts forever.
                switch (selection) {
                    // $script:0831180509002849$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509002850$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509002851$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9003, 0):
                // $script:0831180509002852$
                // - Why do words float in the air after they leave my mouth?
                switch (selection) {
                    // $script:0831180509002853$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509002854$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509002855$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9010, 0):
                // $script:0831180509002856$
                // - My contract expired. You might think it's freeing not to have any constraints, but the best art is made in the most rigid conditions. It forces your creativity to break through. Please renew my contract.
                return -1;
            case (9011, 0):
                // functionID=1 
                // $script:0831180509002857$
                // - My contract expired. You might think it's freeing not to have any constraints, but the best art is made in the most rigid conditions. It forces your creativity to break through. Please renew my contract.
                return -1;
            case (9020, 0):
                // functionID=1 
                // $script:0831180509002858$
                // - Just $MaidPassedDay$ ago, were sharing one vision. I wonder why that changed...
                return -1;
            case (9021, 0):
                // functionID=1 
                // $script:0831180509002859$
                // - I wish you were more honest with me.
                switch (selection) {
                    // $script:0831180509002860$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509002861$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509002862$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9040, 0):
                // $script:0831180509002863$
                // - Are you really there? 
                switch (selection) {
                    // $script:0831180509002864$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509002865$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509002866$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9030, 0):
                // $script:0831180509002867$
                // - We grew apart $MaidPassedDay$ ago. It's nobody's fault. These things happen. But there just wasn't any closure, you know?
                return -1;
            case (9031, 0):
                // $script:0831180509002868$
                // - My soul can't be measured by something as materialistic as wages, but I made a pledge to Helping Hands. I can't serve without being paid. That was the price I had to pay to meet my soul mate: you. I thought we were on the same page with all that, but maybe I was wrong.
                return -1;
            case (9032, 0):
                // $script:0831180509002869$
                // - My muse stopped by today. I wanted to let her pour over me, but I couldn't. You get what I'm saying?
                return -1;
            case (10, 0):
                // functionID=1 
                // $script:0831180509002870$
                // - The muse makes my heart float and sink at the same time. I have to let both of those feeling flow over me.
                return -1;
            case (11, 0):
                // functionID=1 
                // $script:0831180509002871$
                // - You don't really get what I'm saying, do you?
                return -1;
            case (20, 0):
                // functionID=1 
                // $script:0831180509002872$
                // - Don't ask too many questions.
                return -1;
            case (21, 0):
                // functionID=1 
                // $script:0831180509002873$
                // - I have to look in the mirror once in a while, or else I forget what I look like.
                switch (selection) {
                    // $script:0831180509002874$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509002875$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509002876$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (22, 0):
                // functionID=1 
                // $script:0831180509002877$
                // - I have to look in the mirror once in a while, or else I forget what I look like.
                switch (selection) {
                    // $script:0831180509002878$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509002879$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509002880$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509002881$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (30, 0):
                // $script:0831180509002882$
                // - We can talk for as long as you want. I needed a break, anyway.
                switch (selection) {
                    // $script:0831180509002883$
                    // - Anything interesting happen today?
                    case 0:
                        // TODO: goto 1000,1100,2000,2100,9011
                        return -1;
                    // $script:0831180509002884$
                    // - (Praise your servant.)
                    case 1:
                        // TODO: goto 3000,3100,4000,4100,9011
                        return -1;
                    // $script:0831180509002885$
                    // - (Ask your servant a personal question.)
                    case 2:
                        // TODO: goto 5000,5100,6000,6100,7000,9011
                        return -1;
                    // $script:0831180509002886$
                    // - Back.
                    case 3:
                        // TODO: goto 8040,8050,8060,40,50,60,9040
                        return -1;
                }
                return -1;
            case (31, 0):
                // $script:0831180509002887$
                // - Ah, good conversation is always welcome, and I always enjoy talking to you, $OwnerName$.
                switch (selection) {
                    // $script:0831180509002888$
                    // - Anything interesting happen today?
                    case 0:
                        // TODO: goto 1000,1100,2000,2100,9011
                        return -1;
                    // $script:0831180509002889$
                    // - (Praise your servant.)
                    case 1:
                        // TODO: goto 3000,3100,4000,4100,9011
                        return -1;
                    // $script:0831180509002890$
                    // - (Ask your servant a personal question.)
                    case 2:
                        // TODO: goto 5000,5100,6000,6100,7000,9011
                        return -1;
                    // $script:0831180509002891$
                    // - Back.
                    case 3:
                        // TODO: goto 8040,8050,8060,40,50,60,9040
                        return -1;
                }
                return -1;
            case (32, 0):
                // $script:0831180509002892$
                // - The truth of the universe breathes inside every one of us.
                switch (selection) {
                    // $script:0831180509002893$
                    // - Anything interesting happen today?
                    case 0:
                        // TODO: goto 1000,1100,2000,2100,9011
                        return -1;
                    // $script:0831180509002894$
                    // - (Praise your servant.)
                    case 1:
                        // TODO: goto 3000,3100,4000,4100,9011
                        return -1;
                    // $script:0831180509002895$
                    // - (Ask your servant a personal question.)
                    case 2:
                        // TODO: goto 5000,5100,6000,6100,7000,9011
                        return -1;
                    // $script:0831180509002896$
                    // - Back.
                    case 3:
                        // TODO: goto 8040,8050,8060,40,50,60,9040
                        return -1;
                }
                return -1;
            case (40, 0):
                // $script:0831180509002897$
                // - Is there something you want to say?
                switch (selection) {
                    // $script:0831180509002898$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509002899$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509002900$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (50, 0):
                // $script:0831180509002901$
                // - You wanna chat? Was there something you wanted to ask me? Or maybe... you're also drawn to the same mysterious power...
                switch (selection) {
                    // $script:0831180509002902$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509002903$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509002904$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (60, 0):
                // $script:0831180509002905$
                // - Haven't we been talking this whole time? Or is my memory playing tricks on me again...
                switch (selection) {
                    // $script:0831180509002906$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509002907$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509002908$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (1000, 0):
                // $script:0831180509002909$
                // - I've decided that today is the combination of sensitivity and specialty.
                return 1000;
            case (1000, 1):
                // $script:0831180509002910$
                // - More intense than yesterday, and more thrilling than tomorrow. Or just possible, the opposite.
                switch (selection) {
                    // $script:0831180509002911$
                    // - (Say that you feel the same way sometimes.)
                    case 0:
                        // TODO: goto 1011,1012
                        return -1;
                    // $script:0831180509002912$
                    // - (Say nothing.)
                    case 1:
                        // TODO: goto 1001,1002
                        return -1;
                }
                return -1;
            case (1001, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002913$
                // - From the look on your face... Mm, I'm not going to ask. I can feel the intensity radiating off of you.
                return -1;
            case (1002, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002914$
                // - Why does it feel as if you're so far away when you're right in front of me? Every time we talk, I feel so alone.
                return -1;
            case (1011, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002915$
                // - I can be honest when I'm with you. You make me feel like a child without a care in the world. It's been a long time since I felt this way...
                return -1;
            case (1012, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002916$
                // - It's not easy to be who you are. For some reason, I feel better now. Will you tell me more about yourself?
                return -1;
            case (1100, 0):
                // $script:0831180509002917$
                // - I entrusted my soul to music a while back, in a desperate attempt to forget the anguish of life. 
                return 1100;
            case (1100, 1):
                // $script:0831180509002918$
                // - You should try to face your inner self sometimes. Here, take this earphone and put it in your ear.
                return 1100;
            case (1100, 2):
                // $script:0831180509002919$
                // - Now, close your eyes and get lost in the darkness. There! Our souls resonated with each other! Did you feel that?
                switch (selection) {
                    // $script:0831180509002920$
                    // - No...
                    case 0:
                        // TODO: goto 1101,1102
                        return -1;
                    // $script:0831180509002921$
                    // - Yes!
                    case 1:
                        // TODO: goto 1111,1112
                        return -1;
                }
                return -1;
            case (1101, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002922$
                // - It's not your fault. It just means our relationship is not as deep as I thought it was.
                return -1;
            case (1102, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002923$
                // - Heh. You did? So did I.
                return -1;
            case (1111, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002924$
                // - Heh. Feels kind of strange, but I like it. Let's just stay like this for a while.
                return -1;
            case (1112, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002925$
                // - <font color="#909090">(He nods his head to the beat.)</font>
                //   Yeah this is it.
                return -1;
            case (2000, 0):
                // $script:0831180509002926$
                // - This was such an amazing moment. Not sure if you'd agree...?
                return 2000;
            case (2000, 1):
                // $script:0831180509002927$
                // - Today it drizzled, just a bit, but it was enough to quench my heart's thirst.
                return 2000;
            case (2000, 2):
                // $script:0831180509002928$
                // - I haven't felt this way for a long time... Maybe I still have some warmth left in me. I feel... hopeful.
                return -1;
            case (2100, 0):
                // $script:0831180509002929$
                // - I saw the guy next door come home in a helicopter, and that changed my whole perception of him. Interesting, huh?
                return 2100;
            case (2100, 1):
                // $script:0831180509002930$
                // - Sure, I'd love to ride in a helicopter someday. Maybe my tired soul can finally take a breath, hundreds of miles above the world.
                return -1;
            case (2200, 0):
                // $script:0831180509002931$
                // - Today, I met a girl who lives in the neighborhood. She inspired me to pick up scissors for the first time in a long time. Not many folks "get" my art style, you know?
                return 2200;
            case (2200, 1):
                // $script:0831180509002932$
                // - I wonder if the tears I shed after that last snip were were of joy or yearning...
                return 2200;
            case (2200, 2):
                // $script:0831180509002933$
                // - That look on your face... Mm, you still don't understand me, do you? It's cool. An appreciation of true art isn't something that can be acquired. It's something you've got to be born with.
                return -1;
            case (3000, 0):
                // $script:0831180509002934$
                // - How's it going? You look like you're about to burst with excitement. What's the news?
                return 3000;
            case (3000, 1):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002935$
                // - Don't know why, but I've got a hunch today is going to be an exciting day for me, too.
                return -1;
            case (3100, 0):
                // $script:0831180509002936$
                // - Thank you for your kindness, but I don't know if I have a place for it in my heart.
                return 3100;
            case (3100, 1):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002937$
                // - Don't be upset, $OwnerName$. It's not your fault. This is a problem that only I can solve.
                return -1;
            case (4000, 0):
                // $script:0831180509002938$
                // - I appreciate that, but you don't have to keep telling me. Sometimes words mean more when they're not spoken, you hear me?
                return 4000;
            case (4000, 1):
                // $script:0831180509002939$
                // - I get if you don't get it. I'm a deep guy with so many layers. Don't force yourself. We'll solve this puzzle together.
                return -1;
            case (4100, 0):
                // $script:0831180509002940$
                // - I don't mind feeling this way. I assume this is how ordinary people feel all the time.
                return 4100;
            case (4100, 1):
                // $script:0831180509002941$
                // - But for me... Let's just say it'll take a while to get used to this.
                return -1;
            case (5000, 0):
                // $script:0831180509002942$
                // - When it's sunny and there's not much to do, I go out for a walk. Not to take a break, but just to look normal, like everyone else.
                return 5000;
            case (5000, 1):
                // $script:0831180509002943$
                // - $OwnerName$, how does taking a walk make you feel? For me, let's just say it calms the darkness inside me.
                return 5000;
            case (5000, 2):
                // $script:0831180509002944$
                // - Don't take it personally, but... I don't want to take a walk with you. I've reserved that time to spend with me, you know? So I can't share it with anybody else.
                return -1;
            case (5100, 0):
                // $script:0831180509002945$
                // - Why do I use left-handed scissors with my right hand? I'm surprised you even noticed.
                return 5100;
            case (5100, 1):
                // $script:0831180509002946$
                // - You may not understand this, but I'm not the one who chooses that. When I touch someone's hair, I get a feeling deep inside, and that feeling determines which hand I use to cut with.
                return 5100;
            case (5100, 2):
                // $script:0831180509002947$
                // - Come to think of it, I haven't held these scissors with my left hand for a long time. Only fate knows when I'll do that again. To be honest, right now, I'm just too tired to think about it.
                return -1;
            case (6000, 0):
                // $script:0831180509002948$
                // - Sometimes, I just like wearing earphones, without listening to anything.
                return 6000;
            case (6000, 1):
                // $script:0831180509002949$
                // - I do it when I want to be left alone, so I can have some time with myself.
                return 6000;
            case (6000, 2):
                // $script:0831180509002950$
                // - You don't get it, do you, $OwnerName$? It's okay. I'm used to not being understood.
                return 6000;
            case (6000, 3):
                // $script:0831180509002951$
                // - Of course, I have my favorites when it comes to music. I'll play some for you when I have a chance. It'll help you understand where I get my inspiration.
                return -1;
            case (7000, 0):
                // $script:0831180509002952$
                // - $OwnerName$, do you have any siblings? I've never told anyone but... I actually have an older brother.
                return 7000;
            case (7000, 1):
                // $script:0831180509002953$
                // - I left home when I was pretty young. He used to send me letters, but it's been a long, long time since the last one.
                return 7000;
            case (7000, 2):
                // $script:0831180509002954$
                // - I picked this place partly because it's bustling with activity and partly because my brother mailed his last letter from somewhere around here.
                return 7000;
            case (7000, 3):
                // $script:0831180509002955$
                // - Recently, I met an adventurer who I think traveled with my brother for a while. I couldn't be sure, though.
                return 7000;
            case (7000, 4):
                // $script:0831180509002956$
                // - According to him, my brother is doing fine. I don't know what happened to him, but I'm hoping to rn into here one day.
                return -1;
            case (100, 0):
                // $script:0831180509002957$
                // - Weren't you just here yesterday? You looking for the owner?
                switch (selection) {
                    // $script:0831180509002958$
                    // - Yep!
                    case 0:
                        // TODO: goto 101,102
                        return -1;
                    // $script:0831180509002959$
                    // - Nope!
                    case 1:
                        // TODO: goto 103,104
                        return -1;
                    // $script:0831180509002960$
                    // - Who are you?
                    case 2:
                        // TODO: goto 105,106
                        return -1;
                }
                return -1;
            case (101, 0):
                // $script:0831180509002961$
                // - Well, then, look around. See what you can find.
                return -1;
            case (102, 0):
                // $script:0831180509002962$
                // - Not many people come to visit. You must be really close.
                return -1;
            case (103, 0):
                // $script:0831180509002963$
                // - Then did you come to see me? I wanted to stay on the down low, but I know it's impossible when I'm so popular.
                return -1;
            case (104, 0):
                // $script:0831180509002964$
                // - If you want, you can stay for a little while. Just don't be alarmed if your energy starts to resonate with mine.
                return -1;
            case (105, 0):
                // $script:0831180509002965$
                // - If you want, I can tell you, but if we're connected by the red string of fate, knowing each other's name is meaningless.
                return -1;
            case (106, 0):
                // $script:0831180509002966$
                // - I can tell you my name. It's $MaidName$. Nothing else about me can be described in words.
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
            (1000, 1) => NpcTalkButton.SelectableDistractor,
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
            (5000, 2) => NpcTalkButton.Close,
            (5100, 0) => NpcTalkButton.Next,
            (5100, 1) => NpcTalkButton.Next,
            (5100, 2) => NpcTalkButton.Close,
            (6000, 0) => NpcTalkButton.Next,
            (6000, 1) => NpcTalkButton.Next,
            (6000, 2) => NpcTalkButton.Next,
            (6000, 3) => NpcTalkButton.Close,
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
