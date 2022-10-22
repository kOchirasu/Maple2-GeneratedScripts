using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000770: Rina
/// </summary>
public class _11000770 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 1;2;3;4;5;6;9001;9002;9003;100
    }

    // Select 0:
    // $script:0831180509001875$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (1, 0):
                // $script:0831180509001876$
                // - Mm? What is it, dear?
                switch (selection) {
                    // $script:0831180509001877$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509001878$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509001879$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (2, 0):
                // $script:0831180509001880$
                // - It's a wonderful day today, isn't it?
                switch (selection) {
                    // $script:0831180509001881$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509001882$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509001883$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (3, 0):
                // $script:0831180509001884$
                // - You're just in time, $OwnerName$. I was just sitting down to eat.
                switch (selection) {
                    // $script:0831180509001885$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509001886$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509001887$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (4, 0):
                // $script:0831180509001888$
                // - Mm? What is it, dear?
                switch (selection) {
                    // $script:0831180509001889$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509001890$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509001891$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509001892$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (5, 0):
                // $script:0831180509001893$
                // - It's a wonderful day today, isn't it?
                switch (selection) {
                    // $script:0831180509001894$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509001895$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509001896$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509001897$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (6, 0):
                // $script:0831180509001898$
                // - You're just in time, $OwnerName$. I was just sitting down to eat.
                switch (selection) {
                    // $script:0831180509001899$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509001900$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509001901$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509001902$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (9, 0):
                // $script:0831180509001903$
                // - Oh, you want to pay me?
                //   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
                switch (selection) {
                    // $script:0831180509001904$
                    // - Let me think about it some more.
                    case 0:
                        // TODO: goto 8040,8050,8060,9040
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509001905$
                    // - (Pay $MaidSalary$.)
                    case 1:
                        // TODO: goto 8000,8001,8010,8011,8901
                        // TODO: gotoFail 8900,8910
                        return 8900,8910;
                }
                return -1;
            case (8000, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001906$
                // - Time sure flies. Thanks for hiring me again this month, dearie.
                return -1;
            case (8001, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001907$
                // - Oh, how kind of you! I didn't even have to remind you! I don't like asking for money, even if I've rightfully earned it.
                return -1;
            case (8010, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001908$
                // - Whew, thank you! This means I don't have to worry anymore. Why don't I cook us some nice unagi today to celebrate?
                return -1;
            case (8011, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001909$
                // - So everything's worked out? Good! Now I can cut loose! How about I treat you to a feast today to celebrate?
                return -1;
            case (8020, 0):
                // functionID=1 
                // $script:0831180509001910$
                // - I was looking over my books today and noticed our contract is expiring soon. Have you been so busy you've forgotten, dear?
                return -1;
            case (8021, 0):
                // functionID=1 
                // $script:0831180509001911$
                // - You did, didn't you? I knew it! Tsk.
                switch (selection) {
                    // $script:0831180509001912$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509001913$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509001914$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509001915$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (8040, 0):
                // $script:0831180509001916$
                // - Mm? What is it, dear?
                switch (selection) {
                    // $script:0831180509001917$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509001918$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509001919$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509001920$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (8050, 0):
                // $script:0831180509001921$
                // - What a wonderful day today, isn't it?
                switch (selection) {
                    // $script:0831180509001922$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509001923$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509001924$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509001925$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (8060, 0):
                // $script:0831180509001926$
                // - I'm a little busy right now, dearie.
                switch (selection) {
                    // $script:0831180509001927$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509001928$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509001929$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509001930$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (8900, 0):
                // $script:0831180509001931$
                // - Oh, don't push yourself, dearie. Our contract doesn't expire for a while. You can pay me later, hun.
                return -1;
            case (8901, 0):
                // $script:0831180509001932$
                // - Oh my, you've already paid me for the month, hun. We agreed that I would be paid once a month, remember, dearie?
                return -1;
            case (8910, 0):
                // $script:0831180509001933$
                // - This is not the amount we agreed upon. No, no. Did you really think you could fool a woman with decades of experience under her apron?
                return -1;
            case (8999, 0):
                // $script:0831180509001934$
                // - How strange! Based on experience, problems like this usually go away if you just try again. Now, don't just stand there. Try again.
                return -1;
            case (9001, 0):
                // $script:0831180509001935$
                // - It's been $MaidPassedDay$ since I was supposed to be paid. Any good news?
                switch (selection) {
                    // $script:0831180509001936$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509001937$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509001938$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9002, 0):
                // $script:0831180509001939$
                // - $OwnerName$, you look like you haven't slept for days. 
                switch (selection) {
                    // $script:0831180509001940$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509001941$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509001942$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9003, 0):
                // $script:0831180509001943$
                // - You should take care of yourself when thing get tough. Especially while you're young.
                switch (selection) {
                    // $script:0831180509001944$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509001945$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509001946$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9010, 0):
                // $script:0831180509001947$
                // - Looks like my contract expired, $OwnerName$. Didn't I warn you this would happen a couple days ago? Should've done something then, dearie.
                return -1;
            case (9011, 0):
                // functionID=1 
                // $script:0831180509001948$
                // - Oh, $OwnerName$, our contract has expired. Have you checked the contract? You should, hun.
                return -1;
            case (9020, 0):
                // functionID=1 
                // $script:0831180509001949$
                // - Don't worry about me, dearie. If worse comes to worst, I can always sell my house.
                return -1;
            case (9021, 0):
                // functionID=1 
                // $script:0831180509001950$
                // - $OwnerName$, I know you're going through a hard time. I understand, hun.
                switch (selection) {
                    // $script:0831180509001951$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509001952$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509001953$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9040, 0):
                // $script:0831180509001954$
                // - Oh, $OwnerName$, sweetie! You look terrible! 
                switch (selection) {
                    // $script:0831180509001955$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509001956$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509001957$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9030, 0):
                // $script:0831180509001958$
                // - Oh, $OwnerName$, it's late, and you haven't eaten? There's some frozen rice in the freezer. Reheat it and eat up. I'm glad I saved it for you, hun.
                return -1;
            case (9031, 0):
                // $script:0831180509001959$
                // - I need to cut down my spending this month. Things are a bit tight, now that my income is so low. It's about time I went on a diet anyway.
                return -1;
            case (9032, 0):
                // $script:0831180509001960$
                // - Will my $npcName:11000055[gender:0]$ will ever grow up? He cried all morning for new shoes. Doesn't he know what mommy has to go through to feed him? 
                return -1;
            case (10, 0):
                // functionID=1 
                // $script:0831180509001961$
                // - Mm? Is there something you want to eat?
                return -1;
            case (11, 0):
                // functionID=1 
                // $script:0831180509001962$
                // - Let me know if you get hungry.
                return -1;
            case (20, 0):
                // functionID=1 
                // $script:0831180509001963$
                // - What would you possibly want to know about an old lady like me?
                return -1;
            case (21, 0):
                // functionID=1 
                // $script:0831180509001964$
                // - What can I do for you?
                switch (selection) {
                    // $script:0831180509001965$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509001966$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509001967$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (22, 0):
                // functionID=1 
                // $script:0831180509001968$
                // - What can I do for you?
                switch (selection) {
                    // $script:0831180509001969$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509001970$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509001971$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509001972$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (30, 0):
                // $script:0831180509001973$
                // - Sure, dearie, if you don't mind talking to an old lady like me.
                switch (selection) {
                    // $script:0831180509001974$
                    // - Anything interesting happen today?
                    case 0:
                        // TODO: goto 1000,1100,1200,1300,1400,1500,1600,2000,2100,2200,9011
                        return -1;
                    // $script:0831180509001975$
                    // - Let's talk about food!
                    case 1:
                        // TODO: goto 3000,3100,4000,4100,4200,4300,9011
                        return -1;
                    // $script:0831180509001976$
                    // - (Ask your servant a personal question.)
                    case 2:
                        // TODO: goto 5000,5100,6000,7000,9011
                        return -1;
                    // $script:0831180509001977$
                    // - Back.
                    case 3:
                        // TODO: goto 8040,8050,8060,40,50,60,9040
                        return -1;
                }
                return -1;
            case (31, 0):
                // $script:0831180509001978$
                // - Is something bothering you?
                switch (selection) {
                    // $script:0831180509001979$
                    // - Anything interesting happen today?
                    case 0:
                        // TODO: goto 1000,1100,1200,1300,1400,1500,1600,2000,2100,2200,9011
                        return -1;
                    // $script:0831180509001980$
                    // - Let's talk about food!
                    case 1:
                        // TODO: goto 3000,3100,4000,4100,4200,4300,9011
                        return -1;
                    // $script:0831180509001981$
                    // - (Ask your servant a personal question.)
                    case 2:
                        // TODO: goto 5000,5100,6000,7000,9011
                        return -1;
                    // $script:0831180509001982$
                    // - Back.
                    case 3:
                        // TODO: goto 8040,8050,8060,40,50,60,9040
                        return -1;
                }
                return -1;
            case (32, 0):
                // $script:0831180509001983$
                // - Go on, dearie, I'm listening.
                switch (selection) {
                    // $script:0831180509001984$
                    // - Anything interesting happen today?
                    case 0:
                        // TODO: goto 1000,1100,1200,1300,1400,1500,1600,2000,2100,2200,9011
                        return -1;
                    // $script:0831180509001985$
                    // - Let's talk about food!
                    case 1:
                        // TODO: goto 3000,3100,4000,4100,4200,4300,9011
                        return -1;
                    // $script:0831180509001986$
                    // - (Ask your servant a personal question.)
                    case 2:
                        // TODO: goto 5000,5100,6000,7000,9011
                        return -1;
                    // $script:0831180509001987$
                    // - Back.
                    case 3:
                        // TODO: goto 8040,8050,8060,40,50,60,9040
                        return -1;
                }
                return -1;
            case (40, 0):
                // $script:0831180509001988$
                // - Mm? What is it, dear?
                switch (selection) {
                    // $script:0831180509001989$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509001990$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509001991$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (50, 0):
                // $script:0831180509001992$
                // - What a wonderful day today, isn't it?
                switch (selection) {
                    // $script:0831180509001993$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509001994$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509001995$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (60, 0):
                // $script:0831180509001996$
                // - I'm a little busy right now, dearie.
                switch (selection) {
                    // $script:0831180509001997$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509001998$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509001999$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (1000, 0):
                // $script:0831180509002000$
                // - There's a new juice that's all the rage amongst the young folk of $map:2000001$. I tried making it today.
                return 1000;
            case (1000, 1):
                // $script:0831180509002001$
                // - The mineral water from $map:2000089$ was difficult to procure, but besides that, it wasn't too hard to make. What do you think?
                switch (selection) {
                    // $script:0831180509002002$
                    // - Did you go to $map:2000089$ yourself?
                    case 0:
                        // TODO: goto 1001,1002
                        return -1;
                    // $script:0831180509002003$
                    // - Why is this juice so popular in $map:2000001$?
                    case 1:
                        // TODO: goto 1011,1012
                        return -1;
                }
                return -1;
            case (1001, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002004$
                // - I didn't leave your house unattended, if that's what you're asking. I made $npcName:11000350[gender:0]$ help me.
                return -1;
            case (1002, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002005$
                // - Do you even know where $map:2000089$ is? It's deep in a forest. Do you think an old lady like me would survive that journey?
                return -1;
            case (1011, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002006$
                // - The youngsters of $map:2000001$ believe sharing this juice with people that they love will make their love last forever. How do you like it?
                return -1;
            case (1012, 0):
                // $script:0831180509002007$
                // - It's because of a rumor that it promotes eternal love when lovers drink it together.
                return 1012;
            case (1012, 1):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002008$
                // - I don't believe it, though. I'm sure it's just a corporate scheme.
                return -1;
            case (1100, 0):
                // $script:0831180509002009$
                // - I made a snack with some of the leftover ingredients you had in the kitchen. My $npcName:11000055[gender:0]$  just loves sweets. I hope you like these, too, $OwnerName$.
                return 1100;
            case (1100, 1):
                // $script:0831180509002010$
                // - You can eat it all, dearie. When you get to be my age, it all goes straight to the hips.
                switch (selection) {
                    // $script:0831180509002011$
                    // - What? You look great!
                    case 0:
                        // TODO: goto 1111,1112
                        return -1;
                    // $script:0831180509002012$
                    // - Thanks!
                    case 1:
                        // TODO: goto 1101,1102
                        return -1;
                }
                return -1;
            case (1101, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002013$
                // - I can see the snack lifting your mood, hun. Sugar does that to you.
                return -1;
            case (1102, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002014$
                // - I didn't think you'd scarf it down so fast. Don't blame me if you get a tummyache later!
                return -1;
            case (1111, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002015$
                // - Thank you for saying that, dearie. Aren't you just the sweetest!
                return -1;
            case (1112, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002016$
                // - Tsk, you're such a bad liar. Your eyes gave you away. I had quite the figure back in the day, you know... It's not much fun getting old.
                return -1;
            case (1200, 0):
                // $script:0831180509002017$
                // - I noticed you're having a hard time waking up in the morning. I made this to help start your day off right.
                return 1200;
            case (1200, 1):
                // $script:0831180509002018$
                // - It's a potion with all kinds of healthy ingredients in it. Drink up. It'll wake you up right away.
                switch (selection) {
                    // $script:0831180509002019$
                    // - It's delicious!
                    case 0:
                        // TODO: goto 1201,1202
                        return -1;
                    // $script:0831180509002020$
                    // - Why don't you drink some, too?
                    case 1:
                        // TODO: goto 1211,1212
                        return -1;
                }
                return -1;
            case (1201, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002021$
                // - Huh? It is? That can't be right. It's healthy, sure, but it's not supposed to taste good...
                return -1;
            case (1202, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002022$
                // - Oh, you're just saying that to be nice. No health drink actually tastes good. Even I can't drink a full glass of it!
                return -1;
            case (1211, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002023$
                // - Are you worried about my health, hun? Don't worry. I already had some.
                return -1;
            case (1212, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002024$
                // - You have a good heart, dearie. I wish $npcName:11000055[gender:0]$ was as good as you. Then I wouldn't have to worry about him all the time. 
                return -1;
            case (1300, 0):
                // $script:0831180509002025$
                // - $OwnerName$, I cooked you up something special.  Nothing is more important than eating three meals a day, you know.
                return 1300;
            case (1300, 1):
                // $script:0831180509002026$
                // - Eating well is the cornerstone to good health, after all.
                switch (selection) {
                    // $script:0831180509002027$
                    // - I'll eat it later.
                    case 0:
                        // TODO: goto 1301,1302
                        return -1;
                    // $script:0831180509002028$
                    // - Thanks for the food!
                    case 1:
                        // TODO: goto 1311,1312
                        return -1;
                }
                return -1;
            case (1301, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002029$
                // - No, no. You shouldn't skip meals. Eat it right now, even if you don't want to. Trust me!
                return -1;
            case (1302, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002030$
                // - Food doesn't taste good when it's cold. Try to eat at least some of it. $OwnerName$, you're as bad as $npcName:11000055[gender:0]$ sometimes...
                return -1;
            case (1311, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002031$
                // - Oh, I love how you eat anything I give you. I wish $npcName:11000055[gender:0]$ ate as well as you do.
                return -1;
            case (1312, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002032$
                // - I'm glad you like my food. You've gained weight since I've started working here. Perhaps it's time to cut some carbs. Hmm...
                return -1;
            case (1400, 0):
                // $script:0831180509002033$
                // - A salesman visited today. I told him I wasn't interested, be he insisted I take a look at his wares. I was really just only going to look, but then I thought you might like this, so I bought it for you.
                return 1400;
            case (1400, 1):
                // $script:0831180509002034$
                // - What do you think? Do you like it?
                switch (selection) {
                    // $script:0831180509002035$
                    // - Thank you.
                    case 0:
                        // TODO: goto 1411,1412
                        return -1;
                    // $script:0831180509002036$
                    // - It's not good to make impulse purchases.
                    case 1:
                        // TODO: goto 1401,1402
                        return -1;
                }
                return -1;
            case (1401, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002037$
                // - I know, but he was such a smooth talker! Maybe I just shouldn't talk to anyone I don't already know.
                return -1;
            case (1402, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002038$
                // - But I got it for 50 mesos off! Ahhh, I guess you're right. But what can I do about it now?
                return -1;
            case (1411, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002039$
                // - It looks good on you, $OwnerName$! And I got a great deal on it, too!
                return -1;
            case (1412, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002040$
                // - I knew you'd love it, $OwnerName$. I also bought a couple of things for $npcName:11000055[gender:0]$ and $npcName:11000350[gender:0]$. Hee hee.
                return -1;
            case (1500, 0):
                // $script:0831180509002041$
                // - $npcName:11000350[gender:0]$ is really good with his hands. He dropped by yesterday to take a look around, then stopped by again today and brought this. He made it himself!
                return 1500;
            case (1500, 1):
                // $script:0831180509002042$
                // - It matches your house perfectly, don't you think?
                switch (selection) {
                    // $script:0831180509002043$
                    // - Sure.
                    case 0:
                        // TODO: goto 1511,1512
                        return -1;
                    // $script:0831180509002044$
                    // - Wait. Who's $npcName:11000350[gender:0]$?
                    case 1:
                        // TODO: goto 1501,1502
                        return -1;
                }
                return -1;
            case (1501, 0):
                // $script:0831180509002045$
                // - Oh, didn't I tell you? $npcName:11000350[gender:0]$ is an old neighbor of mine.
                return 1501;
            case (1501, 1):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002046$
                // - My son $npcName:11000055[gender:0]$ loves him. I'm sure you've seen him around $map:2000017$.
                return -1;
            case (1502, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002047$
                // - I met him $npcName:11000350[gender:0]$ in $map:2000001$. We became friends because of $npcName:11000055[gender:0]$. He said he used to be a $npcName:11000350[gender:0]$, so I have no idea where he learned to make something like this!
                return -1;
            case (1511, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002048$
                // - It's great, isn't it? I told you $npcName:11000350[gender:0]$ is good with his hands. Now I want to do something for him in return. Maybe he'll like my special pudding!
                return -1;
            case (1512, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002049$
                // - $npcName:11000350[gender:0]$ is so kind, don't you think? Now, $OwnerName$, why don't place it somewhere right now? It'll brighten things up!
                return -1;
            case (1600, 0):
                // $script:0831180509002050$
                // - Today a stranger came and begged me for food. I felt sorry for him, so I gave him some leftover rice and chicken. He ate two bowls of rice! Before he left, he gave me some mesos.
                return 1600;
            case (1600, 1):
                // $script:0831180509002051$
                // - I really didn't want to take his money, but he insisted.
                switch (selection) {
                    // $script:0831180509002052$
                    // - You shouldn't feed strangers!
                    case 0:
                        // TODO: goto 1601,1602
                        return -1;
                    // $script:0831180509002053$
                    // - What was he like?
                    case 1:
                        // TODO: goto 1611,1612
                        return -1;
                }
                return -1;
            case (1601, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002054$
                // - I know I shouldn't, but I couldn't say no to such a sad-looking face. I didn't even think to ask his name.
                return -1;
            case (1602, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002055$
                // - It was just leftovers! He looked familiar, somehow... Like maybe I've seen his face on a leaflet in $map:02000100$.
                return -1;
            case (1611, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002056$
                // - He wore goggles around his head and a red cape on his shoulders. He seemed anxious. Couldn't stop peering around as he ate. Whatever his story is, it can't be a good one.
                return -1;
            case (1612, 0):
                // $script:0831180509002057$
                // - I asked him his name, but he refused to say. He was blond and had a scar on his face.
                return 1612;
            case (1612, 1):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002058$
                // - He was a bit intimidating, to be honest. I could tell he was on the run. Still, I couldn't refuse him. I could tell he hadn't eaten or slept in days...
                return -1;
            case (2000, 0):
                // $script:0831180509002059$
                // - You came at the just the right time. I've got something to tell you.
                return 2000;
            case (2000, 1):
                // $script:0831180509002060$
                // - I wanted to grill some eels for dinner, but I couldn't get the fire going and didn't want to use the stove. Fire-grilled eels taste best, you know. A passing mage offered to help, so I gladly accepted.
                return 2000;
            case (2000, 2):
                // $script:0831180509002061$
                // - But then he hollered, "I'll burn you all!" and shot a giant fireball at the eels! He would've burned down the whole house, but then he shouted "I'll freeze you all!" and put out the fire with an ice bolt.
                return -1;
            case (2100, 0):
                // $script:0831180509002062$
                // - Nothing much happened. Oh, where did time go? I'm not even halfway done with my cooking.
                return 2100;
            case (2100, 1):
                // $script:0831180509002063$
                // - Time goes by so quickly when I work around the house, but don't you wander off. Your food is almost ready. I made mushroom hot pot for you today to invigorate you.
                return -1;
            case (2200, 0):
                // $script:0831180509002064$
                // - Sure, I know something interesting. Sometimes, the food I toil so hard over disappears!
                return 2200;
            case (2200, 1):
                // $script:0831180509002065$
                // - I don't know how it's possible. Is someone stealing it?
                return 2200;
            case (2200, 2):
                // $script:0831180509002066$
                // - I never hear footsteps, so it has to be an animal. Maybe a stray cat or something. It's so frustrating!
                return -1;
            case (3000, 0):
                // $script:0831180509002067$
                // - What's my specialty, you ask? Hee hee, grilled eels, with a delicious sauce!
                return 3000;
            case (3000, 1):
                // $script:0831180509002068$
                // - $npcName:11000119[gender:0]$ loves them so much that sometimes he stops by my house just to eat them.
                return 3000;
            case (3000, 2):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002069$
                // - People always tell me I should open a grilled eel restaurant, but I want to keep cooking a hobby, not a job.
                return -1;
            case (3100, 0):
                // $script:0831180509002070$
                // - Hmm, a young lady has stopped by a lot recently to visit me. She wants to learn how to cook for her boyfriend. She's a cute girl with glasses... I can't remember her name.
                return 3100;
            case (3100, 1):
                // $script:0831180509002071$
                // - Yesterday, I taught her how to cook mushroom hot pot. I showed her how to prepare the $npc:21000001$, and suddenly she paled and burst into tears.
                return 3100;
            case (3100, 2):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002072$
                // - She said the $npc:21000001$ looked so pitiful that she couldn't chop them up. Ahh, she may be too soft-hearted to be a good cook.
                return -1;
            case (4000, 0):
                // $script:0831180509002073$
                // - To me, cooking is all about love. From deciding the menu to picking the ingredients to the actual preparation, I think about who I'm feeding and what would make them happy.
                return 4000;
            case (4000, 1):
                // $script:0831180509002074$
                // - That's why you should try to enjoy the food that I cook for you, even if it isn't your favorite. Got it?
                return -1;
            case (4100, 0):
                // $script:0831180509002075$
                // - Good ingredients make good food. Speaking of which, did you know $map:2000076$ is stocked with amazing ingredients?
                return 4100;
            case (4100, 1):
                // $script:0831180509002076$
                // - Fresh eggs, milk, pork, beef, chicken, and even fish. I lived in $map:2000076$ when I was young, and that's part of the reason I got into cooking. That's also probably why the people who live in $map:2000076$ are generally good cooks.
                return -1;
            case (5000, 0):
                // $script:0831180509002077$
                // - Today's pudding is especially well-made. I'll invite my son over to eat some, too. Sometimes, that kid can get more curious than this mama can handle!
                return 5000;
            case (5000, 1):
                // $script:0831180509002078$
                // - My son's name is $npcName:11000055[gender:0]$. You might have seen him in $map:2000001$.
                return 5000;
            case (5000, 2):
                // $script:0831180509002079$
                // - He keeps forgetting to return books to the library on time, and $npcName:11000005[gender:1]$ the librarian is not happy about it. But what can I say? My boy is just too curious for his own good!
                return 5000;
            case (5000, 3):
                // $script:0831180509002080$
                // - I'm a little worried that all he does is read, though. Children his age need to go out and play!
                return -1;
            case (5100, 0):
                // $script:0831180509002081$
                // - This pudding is $npcName:11000350[gender:0]$'s favorite. Speaking of which, I wonder if he's feeding himself right... Huh? Who's $npcName:11000350[gender:0]$?
                return 5100;
            case (5100, 1):
                // $script:0831180509002082$
                // - We met in $map:2000001$. $npcName:11000055[gender:0]$ loves him because he tells him all kinds of interesting tales about things that he's seen while traveling the world selling his wares.
                return 5100;
            case (5100, 2):
                // $script:0831180509002083$
                // - In fact, my son loves him so much that every time he goes over to $npcName:11000350[gender:0]$'s house, he stays there until way past dinnertime.
                return 5100;
            case (5100, 3):
                // $script:0831180509002084$
                // - $npcName:11000350[gender:0]$ has mentioned more than once that he wants to quit being a
                //   hawker and settle down somewhere. I don't know how he's doing with that. Buying a house is never easy.
                return -1;
            case (6000, 0):
                // $script:0831180509002085$
                // - Did you skip lunch today? You can't go on adventures if you don't take care of yourself! You know, not even $npcName:11000075[gender:1]$ gets food as delicious as this!
                return 6000;
            case (6000, 1):
                // $script:0831180509002086$
                // - ...Huh? $npcName:11000055[gender:0]$ wants to know about his father. He grows more mature each day...
                return 6000;
            case (6000, 2):
                // $script:0831180509002087$
                // - $OwnerName$, you look like you're curious , too. $npcName:11000055[gender:0]$'s father... He... He went on a journey to a far away place. That was... wow, it was seven years ago.
                return 6000;
            case (6000, 3):
                // $script:0831180509002088$
                // - I haven't heard from him since. Everyone tells me I should move on, but I don't want to. I know he'll come back one day.
                return 6000;
            case (6000, 4):
                // $script:0831180509002089$
                // - Hm, maybe I shouldn't have told you that. You look like you want to pepper me with more questions, but please understand, there are some things I'd rather not talk about.
                return -1;
            case (7000, 0):
                // $script:0831180509002090$
                // - What do I think of $npcName:11000350[gender:0]$? Don't be silly. Sure, $npcName:11000350[gender:0]$ is a good man, and I like that he loves my cooking.
                return 7000;
            case (7000, 1):
                // $script:0831180509002091$
                // - $npcName:11000350[gender:0]$ reminds me of the good old days. I may be an old lady now, but I used to be quite popular amongst the gentlemen.
                return 7000;
            case (7000, 2):
                // $script:0831180509002092$
                // - I live in $map:2000001$ now, but originally I came from $map:2000076$. Believe it or not, I used to be as pretty as $npcName:11000015[gender:1]$, and I was good at cooking even then. All the fellows used to come to $map:2000076$ just to see me.
                return 7000;
            case (7000, 3):
                // $script:0831180509002093$
                // - There was one fellow who left a bunch of wildflowers on my doorstep every day. I thought he was a good man, but he never asked me out. Hmph, you don't draw your sword unless you intend to use it, you know!
                return 7000;
            case (7000, 4):
                // $script:0831180509002094$
                // - Anyway, $npcName:11000350[gender:0]$ looks just like that fellow. That's why he reminds me of the old days.
                return -1;
            case (100, 0):
                // $script:0831180509002095$
                // - Mm? I don't think I've seen you before. What brings you to this residence?
                switch (selection) {
                    // $script:0831180509002096$
                    // - I smell something delicious.
                    case 0:
                        // TODO: goto 101,102
                        return -1;
                    // $script:0831180509002097$
                    // - I thought the house was empty.
                    case 1:
                        // TODO: goto 103,104
                        return -1;
                    // $script:0831180509002098$
                    // - Who are you?
                    case 2:
                        // TODO: goto 105,106
                        return -1;
                }
                return -1;
            case (101, 0):
                // $script:0831180509002099$
                // - You must be smelling my pudding. Mm? Are you hungry? I'm sorry, but I'm only making four servings each time: for me, $npcName:11000350[gender:0]$, $npcName:11000055[gender:0]$, and $OwnerName$.
                return -1;
            case (102, 0):
                // $script:0831180509002100$
                // - You're not the first to venture here while following their nose! My cooking skills are quite renowned in $map:2000001$. Today I'm making my special: grilled eels.
                return -1;
            case (103, 0):
                // $script:0831180509002101$
                // - Oh, don't say that. You must be tired coming all the way out here. Have a seat and put your feet up. You can help me peel the garlic if you want.
                return -1;
            case (104, 0):
                // $script:0831180509002102$
                // - That's what everyone who comes into the house says. Hm, I'd better do something about that. I'll to talk to $OwnerName$ and see if we can put up a doorplate.
                return -1;
            case (105, 0):
                // $script:0831180509002103$
                // - I help with the housework, but I'm so much more than just a servant. You know, the owner wouldn't remember to eat without my constant reminders. Speaking of which, have you had breakfast, young adventurer?
                return -1;
            case (106, 0):
                // $script:0831180509002104$
                // - My name is $MaidName$, and I'm help with the housework. If you're going to $map:2000001$, could you tell my son that I want him to come over for some pudding? His name is $npcName:11000055[gender:0]$.
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
            (1012, 0) => NpcTalkButton.Next,
            (1012, 1) => NpcTalkButton.Close,
            (1100, 0) => NpcTalkButton.Next,
            (1100, 1) => NpcTalkButton.SelectableDistractor,
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
            (1501, 0) => NpcTalkButton.Next,
            (1501, 1) => NpcTalkButton.Close,
            (1502, 0) => NpcTalkButton.Close,
            (1511, 0) => NpcTalkButton.Close,
            (1512, 0) => NpcTalkButton.Close,
            (1600, 0) => NpcTalkButton.Next,
            (1600, 1) => NpcTalkButton.SelectableDistractor,
            (1601, 0) => NpcTalkButton.Close,
            (1602, 0) => NpcTalkButton.Close,
            (1611, 0) => NpcTalkButton.Close,
            (1612, 0) => NpcTalkButton.Next,
            (1612, 1) => NpcTalkButton.Close,
            (2000, 0) => NpcTalkButton.Next,
            (2000, 1) => NpcTalkButton.Next,
            (2000, 2) => NpcTalkButton.Close,
            (2100, 0) => NpcTalkButton.Next,
            (2100, 1) => NpcTalkButton.Close,
            (2200, 0) => NpcTalkButton.Next,
            (2200, 1) => NpcTalkButton.Next,
            (2200, 2) => NpcTalkButton.Close,
            (3000, 0) => NpcTalkButton.Next,
            (3000, 1) => NpcTalkButton.Next,
            (3000, 2) => NpcTalkButton.Close,
            (3100, 0) => NpcTalkButton.Next,
            (3100, 1) => NpcTalkButton.Next,
            (3100, 2) => NpcTalkButton.Close,
            (4000, 0) => NpcTalkButton.Next,
            (4000, 1) => NpcTalkButton.Close,
            (4100, 0) => NpcTalkButton.Next,
            (4100, 1) => NpcTalkButton.Close,
            (5000, 0) => NpcTalkButton.Next,
            (5000, 1) => NpcTalkButton.Next,
            (5000, 2) => NpcTalkButton.Next,
            (5000, 3) => NpcTalkButton.Close,
            (5100, 0) => NpcTalkButton.Next,
            (5100, 1) => NpcTalkButton.Next,
            (5100, 2) => NpcTalkButton.Next,
            (5100, 3) => NpcTalkButton.Close,
            (6000, 0) => NpcTalkButton.Next,
            (6000, 1) => NpcTalkButton.Next,
            (6000, 2) => NpcTalkButton.Next,
            (6000, 3) => NpcTalkButton.Next,
            (6000, 4) => NpcTalkButton.Close,
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
