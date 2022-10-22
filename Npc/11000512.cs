using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000512: Momo
/// </summary>
public class _11000512 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 1;2;3;4;5;6;9001;9002;9003;100
    }

    // Select 0:
    // $script:0831180509000001$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (1, 0):
                // $script:0831180509000002$
                // - Hi, $OwnerName$, what can I do for you?
                switch (selection) {
                    // $script:0831180509000003$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509000004$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509000005$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (2, 0):
                // $script:0831180509000006$
                // - Today is quite wonderful, isn't it?
                switch (selection) {
                    // $script:0831180509000007$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509000008$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509000009$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (3, 0):
                // $script:0831180509000010$
                // - Ah, $OwnerName$! Welcome home.
                switch (selection) {
                    // $script:0831180509000011$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509000012$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509000013$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (4, 0):
                // $script:0831180509000014$
                // - I'm glad I can spend time with you, $OwnerName$.
                switch (selection) {
                    // $script:0831180509000015$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509000016$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509000017$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509000018$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (5, 0):
                // $script:0831180509000019$
                // - I know I'm not perfect, but I always do my best for you, $OwnerName$.
                switch (selection) {
                    // $script:0831180509000020$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509000021$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509000022$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509000023$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (6, 0):
                // $script:0831180509000024$
                // - $OwnerName$, welcome back! I've been waiting for you.
                switch (selection) {
                    // $script:0831180509000025$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509000026$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509000027$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509000028$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (9, 0):
                // $script:0831180509000029$
                // - Are you giving me my paycheck?
                //   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
                switch (selection) {
                    // $script:0831180509000030$
                    // - Let me think about it some more.
                    case 0:
                        // TODO: goto 8040,8050,8060,9040
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509000031$
                    // - (Pay $MaidSalary$.)
                    case 1:
                        // TODO: goto 8000,8001,8010,8011,8901
                        // TODO: gotoFail 8900,8910
                        return 8900,8910;
                }
                return -1;
            case (8000, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000032$
                // - Time flies, but maybe that's just because I'm spending it with you, $OwnerName$!
                return -1;
            case (8001, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000033$
                // - You're the best boss a person could ever ask for. Thank you, $OwnerName$!
                return -1;
            case (8010, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000034$
                // - I know things have been tough, $OwnerName$, and I've been worried, too, but thank you for deciding to keep me in your service!
                return -1;
            case (8011, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000035$
                // - I wasn't sure I'd be able to stay with you... But this means I can, right? Yay!
                return -1;
            case (8020, 0):
                // functionID=1 
                // $script:0831180509000036$
                // - Did you know that your contract with me is about to expire, $OwnerName$? You've been so busy. I completely understand.
                return -1;
            case (8021, 0):
                // functionID=1 
                // $script:0831180509000037$
                // - Reminding you about your schedule is also part of my job!
                switch (selection) {
                    // $script:0831180509000038$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509000039$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509000040$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509000041$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (8040, 0):
                // $script:0831180509000042$
                // - Oh, do you have something to tell me?
                switch (selection) {
                    // $script:0831180509000043$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509000044$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509000045$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509000046$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (8050, 0):
                // $script:0831180509000047$
                // - Is there something you wish to tell me?
                switch (selection) {
                    // $script:0831180509000048$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509000049$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509000050$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509000051$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (8060, 0):
                // $script:0831180509000052$
                // - Did you want to talk to me?
                switch (selection) {
                    // $script:0831180509000053$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509000054$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509000055$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509000056$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (8900, 0):
                // $script:0831180509000057$
                // - You don't have to pay me this much! I don't want to be a burden. Cheer up, $OwnerName$! I'll be rooting for you!
                return -1;
            case (8901, 0):
                // $script:0831180509000058$
                // - Mm, what is this? My paycheck? Oh, $OwnerName$, you already paid me for this month. I didn't know you could be so forgetful, hehe.
                return -1;
            case (8910, 0):
                // $script:0831180509000059$
                // - Oh... $OwnerName$... Are you having a hard time lately? Does... Does this mean I can't stay with you any more, $OwnerName$? 
                return -1;
            case (8999, 0):
                // $script:0831180509000060$
                // - I don't know what to do... Ah, $OwnerName$. Please give me a moment. Yikes, now where did I leave the handbook I got from Helping Hands?
                return -1;
            case (9001, 0):
                // $script:0831180509000061$
                // - I don't have money for living expenses. It's been $MaidPassedDay$ since I was supposed to be paid... 
                switch (selection) {
                    // $script:0831180509000062$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509000063$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509000064$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9002, 0):
                // $script:0831180509000065$
                // - Mm... Does this mean I can't stay with you any more, $OwnerName$? 
                switch (selection) {
                    // $script:0831180509000066$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509000067$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509000068$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9003, 0):
                // $script:0831180509000069$
                // - This difficult time will pass. It has to, right? 
                switch (selection) {
                    // $script:0831180509000070$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509000071$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509000072$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9010, 0):
                // $script:0831180509000073$
                // - Um, $OwnerName$...? This might not be the best time, but I just got a call from Helping Hands. My contract with you is up... 
                return -1;
            case (9011, 0):
                // functionID=1 
                // $script:0831180509000074$
                // - Ah, $OwnerName$, that's not important right now. I got a phone call from my coordinator at Helping Hands. She said our contract has expired.
                return -1;
            case (9020, 0):
                // functionID=1 
                // $script:0831180509000075$
                // - Don't worry about me... 
                return -1;
            case (9021, 0):
                // functionID=1 
                // $script:0831180509000076$
                // - I know this is harder for you than it is for me, $OwnerName$. 
                switch (selection) {
                    // $script:0831180509000077$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509000078$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509000079$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9040, 0):
                // $script:0831180509000080$
                // - $OwnerName$... What's going to happen to me now? 
                switch (selection) {
                    // $script:0831180509000081$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509000082$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509000083$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9030, 0):
                // $script:0831180509000084$
                // - $OwnerName$, are you having a hard time these days? Stay strong. I will, too! I'll be counting on you! We c-can get through this... Together!
                return -1;
            case (9031, 0):
                // $script:0831180509000085$
                // - $OwnerName$, don't you want me here anymore? Please don't do this! I know things have been tough, but... I'm sorry. 
                return -1;
            case (9032, 0):
                // $script:0831180509000086$
                // - $OwnerName$, I didn't mean to be a burden to you. I thought I was doing my best to be helpful. Maybe I didn't try hard enough... 
                return -1;
            case (10, 0):
                // functionID=1 
                // $script:0831180509000087$
                // - I can't say I'm a good cook, but I'm really good with beads!
                return -1;
            case (11, 0):
                // functionID=1 
                // $script:0831180509000088$
                // - If you want a necklace, just let me know!
                return -1;
            case (20, 0):
                // functionID=1 
                // $script:0831180509000089$
                // - Is there anything else you want to know about me?
                return -1;
            case (21, 0):
                // functionID=1 
                // $script:0831180509000090$
                // - Is there... Is there something you want to tell me? Oh I don't know, something... romantic, maybe?
                switch (selection) {
                    // $script:0831180509000091$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509000092$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509000093$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (22, 0):
                // functionID=1 
                // $script:0831180509000094$
                // - $OwnerName$... I want to stay with you for as long as I can.
                switch (selection) {
                    // $script:0831180509000095$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509000096$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509000097$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509000098$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (30, 0):
                // $script:0831180509000099$
                // - Oh, do you have something to tell me?
                switch (selection) {
                    // $script:0831180509000100$
                    // - Anything interesting happen today?
                    case 0:
                        // TODO: goto 1000,1100,1200,1300,1400,1500,1600,1700,2000,2100,2200,9011
                        return -1;
                    // $script:0831180509000101$
                    // - (Praise your servant.)
                    case 1:
                        // TODO: goto 3000,3100,4000,4100,4200,4300,9011
                        return -1;
                    // $script:0831180509000102$
                    // - (Ask your servant a personal question.)
                    case 2:
                        // TODO: goto 5000,5100,6000,7000,9011
                        return -1;
                    // $script:0831180509000103$
                    // - Back.
                    case 3:
                        // TODO: goto 8040,8050,8060,40,50,60,9040
                        return -1;
                }
                return -1;
            case (31, 0):
                // $script:0831180509000104$
                // - Is there something you wish to tell me?
                switch (selection) {
                    // $script:0831180509000105$
                    // - Anything interesting happen today?
                    case 0:
                        // TODO: goto 1000,1100,1200,1300,1400,1500,1600,1700,2000,2100,2200,9011
                        return -1;
                    // $script:0831180509000106$
                    // - (Praise your servant.)
                    case 1:
                        // TODO: goto 3000,3100,4000,4100,4200,4300,9011
                        return -1;
                    // $script:0831180509000107$
                    // - (Ask your servant a personal question.)
                    case 2:
                        // TODO: goto 5000,5100,6000,7000,9011
                        return -1;
                    // $script:0831180509000108$
                    // - Back.
                    case 3:
                        // TODO: goto 8040,8050,8060,40,50,60,9040
                        return -1;
                }
                return -1;
            case (32, 0):
                // $script:0831180509000109$
                // - Did you want to talk to me?
                switch (selection) {
                    // $script:0831180509000110$
                    // - Anything interesting happen today?
                    case 0:
                        // TODO: goto 1000,1100,1200,1300,1400,1500,1600,1700,2000,2100,2200,9011
                        return -1;
                    // $script:0831180509000111$
                    // - (Praise your servant.)
                    case 1:
                        // TODO: goto 3000,3100,4000,4100,4200,4300,9011
                        return -1;
                    // $script:0831180509000112$
                    // - (Ask your servant a personal question.)
                    case 2:
                        // TODO: goto 5000,5100,6000,7000,9011
                        return -1;
                    // $script:0831180509000113$
                    // - Back.
                    case 3:
                        // TODO: goto 8040,8050,8060,40,50,60,9040
                        return -1;
                }
                return -1;
            case (40, 0):
                // $script:0831180509000114$
                // - Oh, do you have something to tell me?
                switch (selection) {
                    // $script:0831180509000115$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509000116$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509000117$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (50, 0):
                // $script:0831180509000118$
                // - Is there something you wish to tell me?
                switch (selection) {
                    // $script:0831180509000119$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509000120$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509000121$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (60, 0):
                // $script:0831180509000122$
                // - Did you want to talk to me?
                switch (selection) {
                    // $script:0831180509000123$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509000124$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509000125$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (1000, 0):
                // $script:0831180509000126$
                // - Oh, yes! I've got something to tell you.
                return 1000;
            case (1000, 1):
                // $script:0831180509000127$
                // - I was in the mood to cook, so I made this for you, $OwnerName$.
                return 1000;
            case (1000, 2):
                // $script:0831180509000128$
                // - I may have accidentally used salt instead of sugar, but it tasted okay to me! How do you like it?
                switch (selection) {
                    // $script:0831180509000129$
                    // - It's delicious!
                    case 0:
                        // TODO: goto 1011,1012
                        return -1;
                    // $script:0831180509000130$
                    // - It's so salty!
                    case 1:
                        // TODO: goto 1001,1002
                        return -1;
                }
                return -1;
            case (1001, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000131$
                // - Really? I guess I'm not such a good cook after all. Don't eat any more of it. I'll eat it. As punishment. 
                return -1;
            case (1002, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000132$
                // - Huh? It is? I'm so sorry! But you didn't have to say it so rudely... Excuse me. I'd like to be alone for a moment.
                return -1;
            case (1011, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000133$
                // - I knew you'd like it! Hmm, should I make it again for you tomorrow?
                return -1;
            case (1012, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000134$
                // - Right? Hehe. I might not be good at much, but I'm great at cooking!
                return -1;
            case (1100, 0):
                // $script:0831180509000135$
                // - I almost forgot!
                return 1100;
            case (1100, 1):
                // $script:0831180509000136$
                // - I thought you might be hungry, so I bought snacks! Want to eat them with me? No, actually... I'll just watch you eat.
                return 1100;
            case (1100, 2):
                // $script:0831180509000137$
                // - I've gained a few pounds since starting this job. Probably because I'm so happy! But I should probably cut down on the snacks.
                switch (selection) {
                    // $script:0831180509000138$
                    // - What? You look great!
                    case 0:
                        // TODO: goto 1111,1112
                        return -1;
                    // $script:0831180509000139$
                    // - Yeah, you could stand to lose a few...
                    case 1:
                        // TODO: goto 1101,1102
                        return -1;
                }
                return -1;
            case (1101, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000140$
                // - Are... are you calling me fat, $OwnerName$? How rude!
                return -1;
            case (1102, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000141$
                // - Is that so... Well, I was going to tell you something important, but whoops, I forgot what it was. Too bad. 
                return -1;
            case (1111, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000142$
                // - You... you think so? You think I look great? Wow! Hehehe. Thanks!
                return -1;
            case (1112, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000143$
                // - Really? Hehe, in that case, I'll take a nibble... or two... or three... You know what, just give me that whole piece over there! Hehe!
                return -1;
            case (1200, 0):
                // $script:0831180509000144$
                // - You're so busy all the time! You need to take better care of yourself! Here, I made this nutritious drink just for you!
                return 1200;
            case (1200, 1):
                // $script:0831180509000145$
                // - It contains $npc:21000052$ claws, $npc:21000023$ droppings, $npc:21000074$, and tons of other goodies that are great for your health. Drink up!
                switch (selection) {
                    // $script:0831180509000146$
                    // - (Dump it out.)
                    case 0:
                        // TODO: goto 1201,1202
                        return -1;
                    // $script:0831180509000147$
                    // - (Drink it.)
                    case 1:
                        // TODO: goto 1211,1212
                        return -1;
                }
                return -1;
            case (1201, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000148$
                // - What?! Why?? Do you know tough it was to get those ingredients? I almost died in $map:2000174$! Aagh! 
                return -1;
            case (1202, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000149$
                // - No way... I stayed up three days straight to brew that for you, $OwnerName$... No, I can't give up. I'll make you another one! This is for the good of your health, $OwnerName$!
                return -1;
            case (1211, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000150$
                // - How do you feel? Amazing, huh? I witch I met in $map:2000006$ was right! I'll make you some more!
                return -1;
            case (1212, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000151$
                // - Huh. The witch said this would instantly make you as strong as $npc:23090005[gender:0]$! Did she lie to me? I'll make her pay!
                return -1;
            case (1300, 0):
                // $script:0831180509000152$
                // - $OwnerName$, I cooked this for you. It's a specialty from my hometown. It was my favorite when I was little! I hope you like it.
                return 1300;
            case (1300, 1):
                // $script:0831180509000153$
                // - So... what do you think? You... like it, right?
                switch (selection) {
                    // $script:0831180509000154$
                    // - Ah, it's, um, interesting.
                    case 0:
                        // TODO: goto 1301,1302
                        return -1;
                    // $script:0831180509000155$
                    // - It's delicious!
                    case 1:
                        // TODO: goto 1311,1312
                        return -1;
                }
                return -1;
            case (1301, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000156$
                // - Too rugged and low brow for you, isn't it? You don't have to eat it. I'll put in the fridge and eat it when you're not home.
                return -1;
            case (1302, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000157$
                // - Oh. Okay. Sorry, $OwnerName$. I should've made something I knew you liked, instead of something that was special only to me. 
                return -1;
            case (1311, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000158$
                // - Yay! I'm glad you like it.
                return -1;
            case (1312, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000159$
                // - Whew, I was worried for nothing. Let's eat some more... together! Heehee.
                return -1;
            case (1400, 0):
                // $script:0831180509000160$
                // - I found this while cleaning the house today. I thought I should ask you before throwing it out.
                return 1400;
            case (1400, 1):
                // $script:0831180509000161$
                // - Did you drop this hairpin? It is yours... isn't it?
                switch (selection) {
                    // $script:0831180509000162$
                    // - Yup, it's mine.
                    case 0:
                        // TODO: goto 1411,1412
                        return -1;
                    // $script:0831180509000163$
                    // - Never seen it before. Nooo idea whose it could be...
                    case 1:
                        // TODO: goto 1401,1402
                        return -1;
                }
                return -1;
            case (1401, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000164$
                // - Huh? It's not yours. But it's not mine either. Then whose is it?
                return -1;
            case (1402, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000165$
                // - How strange! You and I are the only ones who live here. If it's not yours, then... No, no... It can't be...
                return -1;
            case (1411, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000166$
                // - I knew it belonged to you, $OwnerName$! We're the only one who live here. If it's not mine, then it has to be yours! That's domestic bliss, hehe.
                return -1;
            case (1412, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000167$
                // - I'm so glad I found it for you. So helpful, right? Hehe.
                return -1;
            case (1500, 0):
                // $script:0831180509000168$
                // - I found this chair when I was grocery shopping in $map:2000001$ today! Heehee! Lucky, right? Oh, no... but what if it belongs to someone? 
                return 1500;
            case (1500, 1):
                // $script:0831180509000169$
                // - What if they're looking for it right now? What if they're worried and sad?
                switch (selection) {
                    // $script:0831180509000170$
                    // - Why are you bringing trash into my house?
                    case 0:
                        // TODO: goto 1501,1502
                        return -1;
                    // $script:0831180509000171$
                    // - I don't think anyone's sad about this chair.
                    case 1:
                        // TODO: goto 1511,1512
                        return -1;
                }
                return -1;
            case (1501, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000172$
                // - Trash? This chair is in excellent used condition! But fine. Your house, your rules. I won't do it again. I'm sorry. 
                return -1;
            case (1502, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000173$
                // - I lugged it all the way here because we need a chair! How can you call it trash? Even you have to admit it matches the decor perfectly... Hmph.
                return -1;
            case (1511, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000174$
                // - You mean someone threw away such a nice chair on purpose? You're trying to tell me in a nice way that I picked up someone else's garbage, aren't you?
                return -1;
            case (1512, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000175$
                // - Their loss, our gain! Sheesh, the people here must think money grows on trees!
                return -1;
            case (1600, 0):
                // $script:0831180509000176$
                // - The weather was so nice today! Perfect for laundry! But guess what I found in your clothes...
                return 1600;
            case (1600, 1):
                // $script:0831180509000177$
                // - Mesos! These are yours, right?
                switch (selection) {
                    // $script:0831180509000178$
                    // - Did you remember to use fabric softener?
                    case 0:
                        // TODO: goto 1601,1602
                        return -1;
                    // $script:0831180509000179$
                    // - Thank you.
                    case 1:
                        // TODO: goto 1611,1612
                        return -1;
                }
                return -1;
            case (1601, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000180$
                // - Fabric what? From where I come from, people wash their clothes in the stream and dry the under the sun. Oh, dear. Being a servant is tougher than I expected.
                return -1;
            case (1602, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000181$
                // - F-Fabric softener? Mm, just one second. Now where did I leave my Helping Hands servent guidebook?
                return -1;
            case (1611, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000182$
                // - Heehee, you're welcome, $OwnerName$! I'm forgetful, too. Once, I put my glasses in the washing machine!
                return -1;
            case (1612, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000183$
                // - I knew it! Heehee, I'd better check your clothes more thoroughly before I wash them!
                return -1;
            case (1700, 0):
                // $script:0831180509000184$
                // - La, la, la... La, la, la... 
                return 1700;
            case (1700, 1):
                // $script:0831180509000185$
                // - When you leave me alone here all day, it gets a little lonely, so I sing to cheer myself up, heehee.
                switch (selection) {
                    // $script:0831180509000186$
                    // - You should stop. You'll scare the furniture.
                    case 0:
                        // TODO: goto 1701,1702
                        return -1;
                    // $script:0831180509000187$
                    // - That's wonderful. You sounded great!
                    case 1:
                        // TODO: goto 1711,1712
                        return -1;
                }
                return -1;
            case (1701, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000188$
                // - Oh! Sorry... I'll never sing around you ever again. Sniff. 
                return -1;
            case (1702, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000189$
                // - $OwnerName$, why are you so mean? You could word it a little more nicely. "Scare the furniture." Hmph. 
                return -1;
            case (1711, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000190$
                // - You really think so? Heehee. Thanks, $OwnerName$! Maybe I'll sing for you one day. No, no. I'm much too shy.
                return -1;
            case (1712, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000191$
                // - Oh, stop. You're making me blush! Heehee.
                return -1;
            case (2000, 0):
                // $script:0831180509000192$
                // - Not a thing! Don't worry. I'll hold down the fort when you're away!
                return 2000;
            case (2000, 1):
                // $script:0831180509000193$
                // - Huh? My hair looks funny? Well, you know how an iron smooths wrinkles out of clothes? I wanted to do the same thing for my hair.
                return 2000;
            case (2000, 2):
                // $script:0831180509000194$
                // - Maybe I set the temperature too high. I'll keep trying until I get it right.
                return -1;
            case (2100, 0):
                // $script:0831180509000195$
                // - Nothing much. Oh! I almost forgot! A group of masked people barged in, asking if I was alone.
                return 2100;
            case (2100, 1):
                // $script:0831180509000196$
                // - I told them you're always by my side, because, you know, I always hold you close to my heart. Anyway, they couldn't leave fast enough. Heehee.
                return -1;
            case (2200, 0):
                // $script:0831180509000197$
                // - Not a single thing, besides the fact that you were gone for way too long, $OwnerName$.
                return 2200;
            case (2200, 1):
                // $script:0831180509000198$
                // - I'm okay. If I get bored, I can invite people over for a party or borrow your stuff and play outside.
                return 2200;
            case (2200, 2):
                // $script:0831180509000199$
                // - Hmmm, I might head to $map:2000235$ for a picnic tomorrow. I love the $item:20000093$ that's sold there! I'll bring some home for you, okay?
                return -1;
            case (3000, 0):
                // $script:0831180509000200$
                // - It's so different here than Cadimia Island, my home. So many people and things I've never seen before!
                return 3000;
            case (3000, 1):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000201$
                // - Someday I'll tell you all about Cadimia Island, heehee.
                return -1;
            case (3100, 0):
                // $script:0831180509000202$
                // - But $OwnerName$, when you're home with me, you can show your true feelings. I know you can't really be as happy as you always pretend.
                return 3100;
            case (3100, 1):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000203$
                // - I spend a lot of time thinking about how to better serve you. You've been so kind, even though I've made a lot of mistakes.
                return -1;
            case (4200, 0):
                // $script:0831180509000204$
                // - $OwnerName$, don't forget I'm here for you!
                return 4200;
            case (4200, 1):
                // $script:0831180509000205$
                // - Let me be your cheerleader today, for luck! Just don't blame me if anything bad happens, heehee.
                return -1;
            case (4300, 0):
                // $script:0831180509000206$
                // - I'm always in tip top shape, and it's thanks to you, $OwnerName$! I'll do my best for you today!
                return 4300;
            case (4300, 1):
                // $script:0831180509000207$
                // - Ever since you told me to stop putting dishes in the laundry machine, I haven't dared to use it. But can I make an exception for this sword? It's really rusty and could use a good washing!
                return -1;
            case (5000, 0):
                // $script:0831180509000208$
                // - Before I became a servant, I lived on Cadimia Island. It's pretty tiny, most people have never even heard of it.
                return 5000;
            case (5000, 1):
                // $script:0831180509000209$
                // - It was just me and gramps, living happily amongst the friendly island critters, trees, grass, and insects. I'm so far now and miss each and every one terribly.
                return 5000;
            case (5000, 2):
                // $script:0831180509000210$
                // - Mr. $npcName:11000179[gender:0]$ used to drop by the island to tell us news of the outside world. It's been years since I've seen him. I wonder how he's doing...
                return -1;
            case (5100, 0):
                // $script:0831180509000211$
                // - You want to know how I became an assistant? Well, after gramps passed away, I lived alone for a while. One day, Mr. $npcName:11000179[gender:0]$ visited.
                return 5100;
            case (5100, 1):
                // $script:0831180509000212$
                // - He said I needed to see more of the world, meet new people, and try new things.
                return 5100;
            case (5100, 2):
                // $script:0831180509000213$
                // - At first, I was terrified. I had never left the island in my life. But I thought of gramps, and that gave me courage.
                return 5100;
            case (5100, 3):
                // $script:0831180509000214$
                // - After I arrived on Victoria Island, I wasn't quite sure what to do, but I stumbled upon Helping Hands and learned how to work as an assistant. Now here I am, taking care of your home!
                return 5100;
            case (5100, 4):
                // $script:0831180509000215$
                // - Come to think of it, if it weren't for Mr. $npcName:11000179[gender:0]$, I would've never met you, $OwnerName$.
                return -1;
            case (6000, 0):
                // $script:0831180509000216$
                // - You're curious if I miss gramps? Well, sure. I mean, of course I do.
                return 6000;
            case (6000, 1):
                // $script:0831180509000217$
                // - But I'm all right. He's been gone a long time, and he'd want me to remember the good times, not mope around being sad, you know?
                return 6000;
            case (6000, 2):
                // $script:0831180509000218$
                // - Sometimes, I really miss him a lot. But life is full of hello's and goodbye's. Speaking of which, I want to create lots of great memories with you while I can, $OwnerName$!
                return -1;
            case (7000, 0):
                // $script:0831180509000219$
                // - Mm, I don't mind talking about myself, but I'd love to hear your story too, $OwnerName$.
                return 7000;
            case (7000, 1):
                // $script:0831180509000220$
                // - $OwnerName$, what kind of food do you like?...Huh? You want to know my favorite food? Mmm, I like seafood.
                return 7000;
            case (7000, 2):
                // $script:0831180509000221$
                // - $OwnerName$, what kind of animals do you like? ...Huh? You want me to answer first? I like all animals. I couldn't possibly pick a favorite.
                return 7000;
            case (7000, 3):
                // $script:0831180509000222$
                // - $OwnerName$, what's your favorite color? ...Oh, of course you want me to answer first. Hmmm, I like blue, like the ocean.
                return 7000;
            case (7000, 4):
                // $script:0831180509000223$
                // - Hmph, this was a waste of time! I wanted to learn more about you, but I ended up talking about me! Heehee, I still like talking to you, though.
                return -1;
            case (100, 0):
                // $script:0831180509000224$
                // - Hello. Are you here to visit master?
                switch (selection) {
                    // $script:0831180509000225$
                    // - Yep!
                    case 0:
                        // TODO: goto 101,102
                        return -1;
                    // $script:0831180509000226$
                    // - Nope!
                    case 1:
                        // TODO: goto 103,104
                        return -1;
                    // $script:0831180509000227$
                    // - Who are you?
                    case 2:
                        // TODO: goto 105,106
                        return -1;
                }
                return -1;
            case (101, 0):
                // $script:0831180509000228$
                // - Then you must know master well. Please have a seat.
                return -1;
            case (102, 0):
                // $script:0831180509000229$
                // - I see. Please make yourself comfortable. But to be clear, I belong to master and am nobody else's assistant. Thank you.
                return -1;
            case (103, 0):
                // $script:0831180509000230$
                // - Then why are you here? It's not nice to just barge into people's houses, you know.
                return -1;
            case (104, 0):
                // $script:0831180509000231$
                // - If you have no business here, I must ask you to leave.
                return -1;
            case (105, 0):
                // $script:0831180509000232$
                // - Shouldn't you tell me who you are first? Master would be jealous if I gave you too much attention... I hope.
                return -1;
            case (106, 0):
                // $script:0831180509000233$
                // - My name is $MaidName$, and I'm an assistant of this household. How may I help you?
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
            (1700, 0) => NpcTalkButton.Next,
            (1700, 1) => NpcTalkButton.SelectableDistractor,
            (1701, 0) => NpcTalkButton.Close,
            (1702, 0) => NpcTalkButton.Close,
            (1711, 0) => NpcTalkButton.Close,
            (1712, 0) => NpcTalkButton.Close,
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
            (4200, 0) => NpcTalkButton.Next,
            (4200, 1) => NpcTalkButton.Close,
            (4300, 0) => NpcTalkButton.Next,
            (4300, 1) => NpcTalkButton.Close,
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
            (103, 0) => NpcTalkButton.Close,
            (104, 0) => NpcTalkButton.Close,
            (105, 0) => NpcTalkButton.Close,
            (106, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
