using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000759: Michael
/// </summary>
public class _11000759 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 1;2;3;4;5;6;9001;9002;9003;100
    }

    // Select 0:
    // $script:0831180509000705$
    // - Mm... How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (1, 0):
                // $script:0831180509000706$
                // - $OwnerName$, what is it this time?
                switch (selection) {
                    // $script:0831180509000707$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000708$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000709$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (2, 0):
                // $script:0831180509000710$
                // - Very well. I was just taking a break.
                switch (selection) {
                    // $script:0831180509000711$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000712$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000713$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (3, 0):
                // $script:0831180509000714$
                // - Oh, I didn't see you there. I was just... thinking. What can I do for you?
                switch (selection) {
                    // $script:0831180509000715$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000716$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000717$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (4, 0):
                // $script:0831180509000718$
                // - $OwnerName$, what is it this time?
                switch (selection) {
                    // $script:0831180509000719$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000720$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000721$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509000722$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (5, 0):
                // $script:0831180509000723$
                // - Very well. I was just taking a break.
                switch (selection) {
                    // $script:0831180509000724$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000725$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000726$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509000727$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (6, 0):
                // $script:0831180509000728$
                // - Oh, I didn't see you there. I was just... thinking. What can I do for you?
                switch (selection) {
                    // $script:0831180509000729$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000730$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000731$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509000732$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (9, 0):
                // $script:0831180509000733$
                // - Hm, my paycheck, huh?
                //   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
                switch (selection) {
                    // $script:0831180509000734$
                    // - Never mind.
                    case 0:
                        // TODO: goto 8040,8050,8060,9040
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000735$
                    // - (Pay $MaidSalary$.)
                    case 1:
                        // TODO: goto 8000,8001,8010,8011,8901
                        // TODO: gotoFail 8900,8910
                        return -1;
                }
                return -1;
            case (8000, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000736$
                // - You're paying me early. $OwnerName$, you like to get things done efficiently, don't you. You're my favorite kind of boss.
                //   <font color="#909090">(He chuckles softly.)</font>
                return -1;
            case (8001, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000737$
                // - Here I was, thinking our time together was about to come to an end. I guess not.
                //   <font color="#909090">(He chuckles.)</font>
                return -1;
            case (8010, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000738$
                // - I thought our contract had expired, though I suppose if you're that desperate to keep me, I can serve you for a little longer.
                //   <font color="#909090">(He chuckles.)</font>
                return -1;
            case (8011, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000739$
                // - <font color="#909090">(He chuckles.)</font>
                //   You've changed your mind? I won't say I'm happy, but I will agree to renew our contract. My own plans will be put on hold for a little longer.
                return -1;
            case (8020, 0):
                // functionID=1 
                // $script:0831180509000740$
                // - It doesn't matter to me, but our contract expires soon. I just want you to know you'll have to pay me if you want me to continue working for you.
                return -1;
            case (8021, 0):
                // functionID=1 
                // $script:0831180509000741$
                // - Our relationship is strictly business. We don't have to get emotional.
                switch (selection) {
                    // $script:0831180509000742$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000743$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000744$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509000745$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (8040, 0):
                // $script:0831180509000746$
                // - Sigh... What is it now?
                switch (selection) {
                    // $script:0831180509000747$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000748$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000749$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509000750$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (8050, 0):
                // $script:0831180509000751$
                // - Keep bothering me, and I might just tie you to a pole.
                switch (selection) {
                    // $script:0831180509000752$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000753$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000754$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509000755$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (8060, 0):
                // $script:0831180509000756$
                // - Why, aren't you mischievous, $OwnerName$!
                //   <font color="#909090">(He chuckles softly.)</font>
                switch (selection) {
                    // $script:0831180509000757$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000758$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000759$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509000760$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (8900, 0):
                // $script:0831180509000761$
                // - This is not the amount we agreed upon. I know you're too smart to attempt to pull a fast one on me, $OwnerName$...
                return -1;
            case (8901, 0):
                // $script:0831180509000762$
                // - Tsk, $OwnerName$. You've already paid me for the month. Perhaps I should've just accepted the mesos. It would have been delightful to see you in tears later. 
                //   <font color="#909090">(He chuckles softly.)</font>
                return -1;
            case (8910, 0):
                // $script:0831180509000763$
                // - I don't think so. I'm no longer your servant, unless you've changed your mind...? Even so, I doubt you have the funds to pay me right now.
                return -1;
            case (8999, 0):
                // $script:0831180509000764$
                // - What have you done? I don't understand how this happened.
                return -1;
            case (9001, 0):
                // $script:0831180509000765$
                // - What are you doing? Don't you know that our contract has expired?
                switch (selection) {
                    // $script:0831180509000766$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509000767$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000768$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9002, 0):
                // $script:0831180509000769$
                // - I have no more business with you.
                switch (selection) {
                    // $script:0831180509000770$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509000771$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000772$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9003, 0):
                // $script:0831180509000773$
                // - Hm... You're bothering me.
                switch (selection) {
                    // $script:0831180509000774$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509000775$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000776$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9010, 0):
                // $script:0831180509000777$
                // - We had a business arrangement. That does not make us friends. Our contract has expired. You can't expect me to work for you and get nothing in return.
                return -1;
            case (9011, 0):
                // functionID=1 
                // $script:0831180509000778$
                // - We had a business arrangement. That does not make us friends. Our contract has expired. Get it? Then leave me alone.
                return -1;
            case (9020, 0):
                // functionID=1 
                // $script:0831180509000779$
                // - You're a pest.
                return -1;
            case (9021, 0):
                // functionID=1 
                // $script:0831180509000780$
                // - I'd prefer not to share personal details of my life with you.
                switch (selection) {
                    // $script:0831180509000781$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509000782$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000783$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9040, 0):
                // $script:0831180509000784$
                // - You're quite thick-headed sometimes, aren't you?
                switch (selection) {
                    // $script:0831180509000785$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509000786$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000787$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9030, 0):
                // $script:0831180509000788$
                // - If you don't wish to employ me, why keep me around in your house? What are you up to?
                return -1;
            case (9031, 0):
                // $script:0831180509000789$
                // - I'm not sure what you're thinking, but our contract has expired. Or... was there something besides your house that you wanted me to take care of? If so, I don't think you can handle it.
                //   <font color="#909090">(He chuckles.)</font>
                return -1;
            case (9032, 0):
                // $script:0831180509000790$
                // - Now that our contract has expired, I'm no longer obligated to chat with you. Well, well. It's been a long time since someone has thrown me such a dirty look. 
                return -1;
            case (10, 0):
                // functionID=1 
                // $script:0831180509000791$
                // - Is there something you need?
                return -1;
            case (11, 0):
                // functionID=1 
                // $script:0831180509000792$
                // - Simple.
                return -1;
            case (20, 0):
                // functionID=1 
                // $script:0831180509000793$
                // - Knowing more about me won't change anything between us.
                return -1;
            case (21, 0):
                // functionID=1 
                // $script:0831180509000794$
                // - Please let me focus on my work.
                switch (selection) {
                    // $script:0831180509000795$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000796$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000797$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (22, 0):
                // functionID=1 
                // $script:0831180509000798$
                // - Please let me focus on my work.
                switch (selection) {
                    // $script:0831180509000799$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000800$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000801$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509000802$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (30, 0):
                // $script:0831180509000803$
                // - Tell me. I'm at your service... for now.
                switch (selection) {
                    // $script:0831180509000804$
                    // - Anything interesting happen today?
                    case 0:
                        // TODO: goto 1000,1100,2000,2100,9011
                        return -1;
                    // $script:0831180509000805$
                    // - I don't feel so good. I'm sick.
                    case 1:
                        // TODO: goto 3000,3100,4000,4100,9011
                        return -1;
                    // $script:0831180509000806$
                    // - (Ask your servant a personal question.)
                    case 2:
                        // TODO: goto 5000,5100,6000,6100,7000,9011
                        return -1;
                    // $script:0831180509000807$
                    // - Back.
                    case 3:
                        // TODO: goto 8040,8050,8060,40,50,60,9040
                        return -1;
                }
                return -1;
            case (31, 0):
                // $script:0831180509000808$
                // - I wasn't aware chit chat was part of my job description.
                switch (selection) {
                    // $script:0831180509000809$
                    // - Anything interesting happen today?
                    case 0:
                        // TODO: goto 1000,1100,2000,2100,9011
                        return -1;
                    // $script:0831180509000810$
                    // - I don't feel so good. I'm sick.
                    case 1:
                        // TODO: goto 3000,3100,4000,4100,9011
                        return -1;
                    // $script:0831180509000811$
                    // - (Ask your servant a personal question.)
                    case 2:
                        // TODO: goto 5000,5100,6000,6100,7000,9011
                        return -1;
                    // $script:0831180509000812$
                    // - Back.
                    case 3:
                        // TODO: goto 8040,8050,8060,40,50,60,9040
                        return -1;
                }
                return -1;
            case (32, 0):
                // $script:0831180509000813$
                // - Shouldn't you be talking to someone who actually cares?
                switch (selection) {
                    // $script:0831180509000814$
                    // - Anything interesting happen today?
                    case 0:
                        // TODO: goto 1000,1100,2000,2100,9011
                        return -1;
                    // $script:0831180509000815$
                    // - I don't feel so good. I'm sick.
                    case 1:
                        // TODO: goto 3000,3100,4000,4100,9011
                        return -1;
                    // $script:0831180509000816$
                    // - (Ask your servant a personal question.)
                    case 2:
                        // TODO: goto 5000,5100,6000,6100,7000,9011
                        return -1;
                    // $script:0831180509000817$
                    // - Back.
                    case 3:
                        // TODO: goto 8040,8050,8060,40,50,60,9040
                        return -1;
                }
                return -1;
            case (40, 0):
                // $script:0831180509000818$
                // - Sigh... What is it now?
                switch (selection) {
                    // $script:0831180509000819$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000820$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000821$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (50, 0):
                // $script:0831180509000822$
                // - Keep bothering me, and I might just tie you to a pole.
                switch (selection) {
                    // $script:0831180509000823$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000824$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000825$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (60, 0):
                // $script:0831180509000826$
                // - Why, aren't you mischievous, $OwnerName$!
                //   <font color="#909090">(He chuckles softly.)</font>
                switch (selection) {
                    // $script:0831180509000827$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000828$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000829$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (1000, 0):
                // $script:0831180509000830$
                // - A servant is here to take care of your house, not to be your personal slave.
                return 1000;
            case (1000, 1):
                // $script:0831180509000831$
                // - Why are you giving me that look? It's all written clearly in the contract.
                switch (selection) {
                    // $script:0831180509000832$
                    // - What did I do that was so bad?
                    case 0:
                        // TODO: goto 1001,1002
                        return -1;
                    // $script:0831180509000833$
                    // - I'm sorry. I'll stop. I promise.
                    case 1:
                        // TODO: goto 1011,1012
                        return -1;
                }
                return -1;
            case (1001, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000834$
                // - You forgot your potions when you left the house last week and made me deliver them. All the way to $map:02000216$, no less!
                return -1;
            case (1002, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000835$
                // - Don't feign ignorance. You're not that dumb. Now, I have work the requires my complete focus, so please don't speak to me.
                return -1;
            case (1011, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000836$
                // - That sheepish expression you're making right now... Surprisingly, I don't despise it.
                //   <font color="#909090">(He gives a soft chuckle.)</font>
                return -1;
            case (1012, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000837$
                // - Hmm. A surprisingly sensible response. I didn't expect that from you.
                return -1;
            case (1100, 0):
                // $script:0831180509000838$
                // - Why are you furrowing your brows at me? Do you think I'm going to steal something?
                return 1100;
            case (1100, 1):
                // $script:0831180509000839$
                // - That's something all my previous employers had in common. They always wanted to know what I was up to.
                return 1100;
            case (1100, 2):
                // $script:0831180509000840$
                // - What about you, $OwnerName$? Do you think I'm hiding something?
                switch (selection) {
                    // $script:0831180509000841$
                    // - You have to admit you give off a suspicious aura.
                    case 0:
                        // TODO: goto 1101,1102
                        return -1;
                    // $script:0831180509000842$
                    // - Nah, none of my business.
                    case 1:
                        // TODO: goto 1111,1112
                        return -1;
                }
                return -1;
            case (1101, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000843$
                // - You're no better than the rest of them. If you don't trust me, you don't need to employ me.
                return -1;
            case (1102, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000844$
                // - Heh, but you'll never unravel the truth, no matter how much you try.
                return -1;
            case (1111, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000845$
                // - You sure about that? I doubt you'd say that if you knew who I really am...
                return -1;
            case (1112, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000846$
                // - You say that, yet I see the doubt in your eyes. Speaking of which, $OwnerName$, I never knew your eyes had such sparkle. Oops, almost said something I'd regret later.
                //   <font color="#909090">(He chuckles softly.)</font>
                return -1;
            case (2000, 0):
                // $script:0831180509000847$
                // - Strangers barge into your home several times a day. It doesn't feel safe. We should install locks on the doors.
                return 2000;
            case (2000, 1):
                // $script:0831180509000848$
                // - Don't give me that look, $OwnerName$. I'm not trying to do anything unsightly behind locked doors.
                return 2000;
            case (2000, 2):
                // $script:0831180509000849$
                // - There's just... something I want to study in peace and quiet. It doesn't concern you.
                return -1;
            case (2100, 0):
                // $script:0831180509000850$
                // - We need some music to liven things up around here. What? I like listening to music, just like everyone else.
                return 2100;
            case (2100, 1):
                // $script:0831180509000851$
                // - Let's see... Judging by how you've decorated your home, it seems you have quite elegant taste, $OwnerName$. Let's play some jazz.
                return 2100;
            case (2100, 2):
                // $script:0831180509000852$
                // - That's also my favorite genre of music. Which reminds me, there's a pretty famous musician who hangs out in $map:02000076$. Maybe I should ask for an autograph.
                return -1;
            case (3000, 0):
                // $script:0831180509000853$
                // - You're sick? With what? ...You have no fever. Your heart rate is normal.
                return 3000;
            case (3000, 1):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000854$
                // - Ah, you're pretending, aren't you? All right, I'll feign ignorance just this once. Come over here and lie down.
                return -1;
            case (3100, 0):
                // $script:0831180509000855$
                // - You were bitten by a $npcName:21000023$? Come here. Let me take a look...
                return 3100;
            case (3100, 1):
                // $script:0831180509000856$
                // - Ah, this is bad. It's hard to treat rabies. I'm sorry, but there's nothing I can do that will make a difference  at this point.
                return 3100;
            case (3100, 2):
                // $script:0831180509000857$
                // - <font color="#909090">(He chuckles.)</font>
                //   Look at you, about to burst into tears.
                return 3100;
            case (3100, 3):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000858$
                // - I was joking. Now, come over here. A little bit of iodine, and you'll be as good as new.
                return -1;
            case (4000, 0):
                // $script:0831180509000859$
                // - Where does it hurt? Show me.
                return 4000;
            case (4000, 1):
                // $script:0831180509000860$
                // - ...Why would you lie about being sick? $OwnerName$, you're hopeless.
                return -1;
            case (4100, 0):
                // $script:0831180509000861$
                // - ...Again? Please stop acting like a child.
                return 4100;
            case (4100, 1):
                // $script:0831180509000862$
                // - You shouldn't make things up and make others worry about you. It's not kind.
                return 4100;
            case (4100, 2):
                // $script:0831180509000863$
                // - Am I going to have to scold you? Because if you pull this again, I will.
                return -1;
            case (5000, 0):
                // $script:0831180509000864$
                // - I don't like talking about myself. It's not a problem, because I have no friend to talk to anyway.
                return 5000;
            case (5000, 1):
                // $script:0831180509000865$
                // - At least, not any more. My only friend passed away a long time ago.
                return 5000;
            case (5000, 2):
                // $script:0831180509000866$
                // - He got into an accident... Actually, it's not of your business, really.
                return -1;
            case (5100, 0):
                // $script:0831180509000867$
                // - The story of how I learned alchemy is quite uninteresting.
                return 5100;
            case (5100, 1):
                // $script:0831180509000868$
                // - I met a grungy old beggar in $map:02000051$. He was rather fastidious and pompous for a beggar.
                return 5100;
            case (5100, 2):
                // $script:0831180509000869$
                // - But something about him seemed... powerful.
                return 5100;
            case (5100, 3):
                // $script:0831180509000870$
                // - When there's something I want, nothing can get in my way. I told him I wanted to learn how to beg, and he taught me. In the meantime, I stood at his side and learned his alchemy secrets over his shoulder.
                return 5100;
            case (5100, 4):
                // $script:0831180509000871$
                // - And look at me now. I'm as good an alchemist as he is.
                return -1;
            case (6000, 0):
                // $script:0831180509000872$
                // - Do you know what I fear the most? Death.
                return 6000;
            case (6000, 1):
                // $script:0831180509000873$
                // - Everyone fears death, and just about everyone succumbs to death eventually.
                return 6000;
            case (6000, 2):
                // $script:0831180509000874$
                // - But not me. I'm going to beat death, just like I've beaten everything else...
                return -1;
            case (7000, 0):
                // $script:0831180509000875$
                // - You've heard me mention my friend, have you not? He was the only person I could really talk to.
                return 7000;
            case (7000, 1):
                // $script:0831180509000876$
                // - He's no longer here. He may not actually be dead. Instead, he's... in another world.
                return 7000;
            case (7000, 2):
                // $script:0831180509000877$
                // - He and I ventured in the Shadow World when we were young. We got separated after a while.
                return 7000;
            case (7000, 3):
                // $script:0831180509000878$
                // - We shouldn't have been there at all, but we were dumb and reckless. When I came to, he was gone. I wouldn't had made it at all if I hadn't met those merchants...
                return 7000;
            case (7000, 4):
                // $script:0831180509000879$
                // - I may not be able to do much, but once in a while, I venture into the Shadow World to search for him. But I haven't heard a word, not even a rumor. Perhaps it's time to just let him go...
                return -1;
            case (100, 0):
                // $script:0831180509000880$
                // - Who are you? You should leave while I'm still in a pleasant mood.
                switch (selection) {
                    // $script:0831180509000881$
                    // - Yeah, okay, I'm out of here.
                    case 0:
                        // TODO: goto 101,102
                        return -1;
                    // $script:0831180509000882$
                    // - Oh, yeah? What happens when you're unpleasant?
                    case 1:
                        // TODO: goto 103,104
                        return -1;
                    // $script:0831180509000883$
                    // - What's your sign? Can I get your number?
                    case 2:
                        // TODO: goto 105,106
                        return -1;
                }
                return -1;
            case (101, 0):
                // $script:0831180509000884$
                // - Smart. The exit is that way.
                return -1;
            case (102, 0):
                // $script:0831180509000885$
                // - Good... Now, to return to my task... 
                return -1;
            case (103, 0):
                // $script:0831180509000886$
                // - <font color="#909090">(He chuckles darkly.)</font>
                //   Do you really want to find out?
                return -1;
            case (104, 0):
                // $script:0831180509000887$
                // - <font color="#909090">(He smiles.)</font>
                //   Simple. I don't let you leave.
                return -1;
            case (105, 0):
                // $script:0831180509000888$
                // - Not funny. Now get out of here.
                return -1;
            case (106, 0):
                // $script:0831180509000889$
                // - <font color="#909090">(He smirk.)</font>
                //   Sorry, $male:pal,female:lady$, you're not my type.
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
            (2100, 1) => NpcTalkButton.Next,
            (2100, 2) => NpcTalkButton.Close,
            (3000, 0) => NpcTalkButton.Next,
            (3000, 1) => NpcTalkButton.Close,
            (3100, 0) => NpcTalkButton.Next,
            (3100, 1) => NpcTalkButton.Next,
            (3100, 2) => NpcTalkButton.Next,
            (3100, 3) => NpcTalkButton.Close,
            (4000, 0) => NpcTalkButton.Next,
            (4000, 1) => NpcTalkButton.Close,
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
            (103, 0) => NpcTalkButton.Close,
            (104, 0) => NpcTalkButton.Close,
            (105, 0) => NpcTalkButton.Close,
            (106, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
