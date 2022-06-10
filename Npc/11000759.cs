using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000759: Michael
/// </summary>
public class _11000759 : NpcScript {
    internal _11000759(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 1;2;3;4;5;6;9001;9002;9003;100
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180509000705$ 
                // - Mm... How may I help you?
                return true;
            case 1:
                // $script:0831180509000706$ 
                // - $OwnerName$, what is it this time?
                switch (selection) {
                    // $script:0831180509000707$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509000708$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509000709$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 2:
                // $script:0831180509000710$ 
                // - Very well. I was just taking a break.
                switch (selection) {
                    // $script:0831180509000711$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509000712$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509000713$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 3:
                // $script:0831180509000714$ 
                // - Oh, I didn't see you there. I was just... thinking. What can I do for you?
                switch (selection) {
                    // $script:0831180509000715$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509000716$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509000717$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 4:
                // $script:0831180509000718$ 
                // - $OwnerName$, what is it this time?
                switch (selection) {
                    // $script:0831180509000719$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509000720$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509000721$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509000722$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 5:
                // $script:0831180509000723$ 
                // - Very well. I was just taking a break.
                switch (selection) {
                    // $script:0831180509000724$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509000725$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509000726$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509000727$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 6:
                // $script:0831180509000728$ 
                // - Oh, I didn't see you there. I was just... thinking. What can I do for you?
                switch (selection) {
                    // $script:0831180509000729$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509000730$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509000731$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509000732$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 9:
                // $script:0831180509000733$ 
                // - Hm, my paycheck, huh?
                //   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
                switch (selection) {
                    // $script:0831180509000734$
                    // - Never mind.
                    case 0:
                        Id = 0; // TODO: 8040,8050,8060,9040 | 8999
                        return false;
                    // $script:0831180509000735$
                    // - (Pay $MaidSalary$.)
                    case 1:
                        Id = 0; // TODO: 8000,8001,8010,8011,8901 | 8900,8910
                        return false;
                }
                return true;
            case 8000:
                // $script:0831180509000736$ functionID=1 
                // - You're paying me early. $OwnerName$, you like to get things done efficiently, don't you. You're my favorite kind of boss.
                //   <font color="#909090">(He chuckles softly.)</font>
                return true;
            case 8001:
                // $script:0831180509000737$ functionID=1 
                // - Here I was, thinking our time together was about to come to an end. I guess not.
                //   <font color="#909090">(He chuckles.)</font>
                return true;
            case 8010:
                // $script:0831180509000738$ functionID=1 
                // - I thought our contract had expired, though I suppose if you're that desperate to keep me, I can serve you for a little longer.
                //   <font color="#909090">(He chuckles.)</font>
                return true;
            case 8011:
                // $script:0831180509000739$ functionID=1 
                // - <font color="#909090">(He chuckles.)</font>
                //   You've changed your mind? I won't say I'm happy, but I will agree to renew our contract. My own plans will be put on hold for a little longer.
                return true;
            case 8020:
                // $script:0831180509000740$ functionID=1 
                // - It doesn't matter to me, but our contract expires soon. I just want you to know you'll have to pay me if you want me to continue working for you.
                return true;
            case 8021:
                // $script:0831180509000741$ functionID=1 
                // - Our relationship is strictly business. We don't have to get emotional.
                switch (selection) {
                    // $script:0831180509000742$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509000743$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509000744$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509000745$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8040:
                // $script:0831180509000746$ 
                // - Sigh... What is it now?
                switch (selection) {
                    // $script:0831180509000747$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509000748$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509000749$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509000750$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8050:
                // $script:0831180509000751$ 
                // - Keep bothering me, and I might just tie you to a pole.
                switch (selection) {
                    // $script:0831180509000752$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509000753$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509000754$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509000755$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8060:
                // $script:0831180509000756$ 
                // - Why, aren't you mischievous, $OwnerName$!
                //   <font color="#909090">(He chuckles softly.)</font>
                switch (selection) {
                    // $script:0831180509000757$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509000758$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509000759$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509000760$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8900:
                // $script:0831180509000761$ 
                // - This is not the amount we agreed upon. I know you're too smart to attempt to pull a fast one on me, $OwnerName$...
                return true;
            case 8901:
                // $script:0831180509000762$ 
                // - Tsk, $OwnerName$. You've already paid me for the month. Perhaps I should've just accepted the mesos. It would have been delightful to see you in tears later. 
                //   <font color="#909090">(He chuckles softly.)</font>
                return true;
            case 8910:
                // $script:0831180509000763$ 
                // - I don't think so. I'm no longer your servant, unless you've changed your mind...? Even so, I doubt you have the funds to pay me right now.
                return true;
            case 8999:
                // $script:0831180509000764$ 
                // - What have you done? I don't understand how this happened.
                return true;
            case 9001:
                // $script:0831180509000765$ 
                // - What are you doing? Don't you know that our contract has expired?
                switch (selection) {
                    // $script:0831180509000766$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509000767$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509000768$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9002:
                // $script:0831180509000769$ 
                // - I have no more business with you.
                switch (selection) {
                    // $script:0831180509000770$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509000771$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509000772$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9003:
                // $script:0831180509000773$ 
                // - Hm... You're bothering me.
                switch (selection) {
                    // $script:0831180509000774$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509000775$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509000776$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9010:
                // $script:0831180509000777$ 
                // - We had a business arrangement. That does not make us friends. Our contract has expired. You can't expect me to work for you and get nothing in return.
                return true;
            case 9011:
                // $script:0831180509000778$ functionID=1 
                // - We had a business arrangement. That does not make us friends. Our contract has expired. Get it? Then leave me alone.
                return true;
            case 9020:
                // $script:0831180509000779$ functionID=1 
                // - You're a pest.
                return true;
            case 9021:
                // $script:0831180509000780$ functionID=1 
                // - I'd prefer not to share personal details of my life with you.
                switch (selection) {
                    // $script:0831180509000781$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509000782$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509000783$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9040:
                // $script:0831180509000784$ 
                // - You're quite thick-headed sometimes, aren't you?
                switch (selection) {
                    // $script:0831180509000785$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509000786$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509000787$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9030:
                // $script:0831180509000788$ 
                // - If you don't wish to employ me, why keep me around in your house? What are you up to?
                return true;
            case 9031:
                // $script:0831180509000789$ 
                // - I'm not sure what you're thinking, but our contract has expired. Or... was there something besides your house that you wanted me to take care of? If so, I don't think you can handle it.
                //   <font color="#909090">(He chuckles.)</font>
                return true;
            case 9032:
                // $script:0831180509000790$ 
                // - Now that our contract has expired, I'm no longer obligated to chat with you. Well, well. It's been a long time since someone has thrown me such a dirty look. 
                return true;
            case 10:
                // $script:0831180509000791$ functionID=1 
                // - Is there something you need?
                return true;
            case 11:
                // $script:0831180509000792$ functionID=1 
                // - Simple.
                return true;
            case 20:
                // $script:0831180509000793$ functionID=1 
                // - Knowing more about me won't change anything between us.
                return true;
            case 21:
                // $script:0831180509000794$ functionID=1 
                // - Please let me focus on my work.
                switch (selection) {
                    // $script:0831180509000795$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509000796$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509000797$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 22:
                // $script:0831180509000798$ functionID=1 
                // - Please let me focus on my work.
                switch (selection) {
                    // $script:0831180509000799$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509000800$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509000801$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509000802$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 30:
                // $script:0831180509000803$ 
                // - Tell me. I'm at your service... for now.
                switch (selection) {
                    // $script:0831180509000804$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,2000,2100,9011 | 
                        return false;
                    // $script:0831180509000805$
                    // - I don't feel so good. I'm sick.
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,9011 | 
                        return false;
                    // $script:0831180509000806$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,6100,7000,9011 | 
                        return false;
                    // $script:0831180509000807$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 31:
                // $script:0831180509000808$ 
                // - I wasn't aware chit chat was part of my job description.
                switch (selection) {
                    // $script:0831180509000809$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,2000,2100,9011 | 
                        return false;
                    // $script:0831180509000810$
                    // - I don't feel so good. I'm sick.
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,9011 | 
                        return false;
                    // $script:0831180509000811$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,6100,7000,9011 | 
                        return false;
                    // $script:0831180509000812$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 32:
                // $script:0831180509000813$ 
                // - Shouldn't you be talking to someone who actually cares?
                switch (selection) {
                    // $script:0831180509000814$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,2000,2100,9011 | 
                        return false;
                    // $script:0831180509000815$
                    // - I don't feel so good. I'm sick.
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,9011 | 
                        return false;
                    // $script:0831180509000816$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,6100,7000,9011 | 
                        return false;
                    // $script:0831180509000817$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 40:
                // $script:0831180509000818$ 
                // - Sigh... What is it now?
                switch (selection) {
                    // $script:0831180509000819$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509000820$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509000821$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 50:
                // $script:0831180509000822$ 
                // - Keep bothering me, and I might just tie you to a pole.
                switch (selection) {
                    // $script:0831180509000823$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509000824$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509000825$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 60:
                // $script:0831180509000826$ 
                // - Why, aren't you mischievous, $OwnerName$!
                //   <font color="#909090">(He chuckles softly.)</font>
                switch (selection) {
                    // $script:0831180509000827$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509000828$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509000829$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 1000:
                // $script:0831180509000830$ 
                // - A servant is here to take care of your house, not to be your personal slave.
                // $script:0831180509000831$ 
                // - Why are you giving me that look? It's all written clearly in the contract.
                switch (selection) {
                    // $script:0831180509000832$
                    // - What did I do that was so bad?
                    case 0:
                        Id = 0; // TODO: 1001,1002 | 
                        return false;
                    // $script:0831180509000833$
                    // - I'm sorry. I'll stop. I promise.
                    case 1:
                        Id = 0; // TODO: 1011,1012 | 
                        return false;
                }
                return true;
            case 1001:
                // $script:0831180509000834$ functionID=1 
                // - You forgot your potions when you left the house last week and made me deliver them. All the way to $map:02000216$, no less!
                return true;
            case 1002:
                // $script:0831180509000835$ functionID=1 
                // - Don't feign ignorance. You're not that dumb. Now, I have work the requires my complete focus, so please don't speak to me.
                return true;
            case 1011:
                // $script:0831180509000836$ functionID=1 
                // - That sheepish expression you're making right now... Surprisingly, I don't despise it.
                //   <font color="#909090">(He gives a soft chuckle.)</font>
                return true;
            case 1012:
                // $script:0831180509000837$ functionID=1 
                // - Hmm. A surprisingly sensible response. I didn't expect that from you.
                return true;
            case 1100:
                // $script:0831180509000838$ 
                // - Why are you furrowing your brows at me? Do you think I'm going to steal something?
                // $script:0831180509000839$ 
                // - That's something all my previous employers had in common. They always wanted to know what I was up to.
                // $script:0831180509000840$ 
                // - What about you, $OwnerName$? Do you think I'm hiding something?
                switch (selection) {
                    // $script:0831180509000841$
                    // - You have to admit you give off a suspicious aura.
                    case 0:
                        Id = 0; // TODO: 1101,1102 | 
                        return false;
                    // $script:0831180509000842$
                    // - Nah, none of my business.
                    case 1:
                        Id = 0; // TODO: 1111,1112 | 
                        return false;
                }
                return true;
            case 1101:
                // $script:0831180509000843$ functionID=1 
                // - You're no better than the rest of them. If you don't trust me, you don't need to employ me.
                return true;
            case 1102:
                // $script:0831180509000844$ functionID=1 
                // - Heh, but you'll never unravel the truth, no matter how much you try.
                return true;
            case 1111:
                // $script:0831180509000845$ functionID=1 
                // - You sure about that? I doubt you'd say that if you knew who I really am...
                return true;
            case 1112:
                // $script:0831180509000846$ functionID=1 
                // - You say that, yet I see the doubt in your eyes. Speaking of which, $OwnerName$, I never knew your eyes had such sparkle. Oops, almost said something I'd regret later.
                //   <font color="#909090">(He chuckles softly.)</font>
                return true;
            case 2000:
                // $script:0831180509000847$ 
                // - Strangers barge into your home several times a day. It doesn't feel safe. We should install locks on the doors.
                // $script:0831180509000848$ 
                // - Don't give me that look, $OwnerName$. I'm not trying to do anything unsightly behind locked doors.
                // $script:0831180509000849$ 
                // - There's just... something I want to study in peace and quiet. It doesn't concern you.
                return true;
            case 2100:
                // $script:0831180509000850$ 
                // - We need some music to liven things up around here. What? I like listening to music, just like everyone else.
                // $script:0831180509000851$ 
                // - Let's see... Judging by how you've decorated your home, it seems you have quite elegant taste, $OwnerName$. Let's play some jazz.
                // $script:0831180509000852$ 
                // - That's also my favorite genre of music. Which reminds me, there's a pretty famous musician who hangs out in $map:02000076$. Maybe I should ask for an autograph.
                return true;
            case 3000:
                // $script:0831180509000853$ 
                // - You're sick? With what? ...You have no fever. Your heart rate is normal.
                // $script:0831180509000854$ functionID=1 
                // - Ah, you're pretending, aren't you? All right, I'll feign ignorance just this once. Come over here and lie down.
                return true;
            case 3100:
                // $script:0831180509000855$ 
                // - You were bitten by a $npcName:21000023$? Come here. Let me take a look...
                // $script:0831180509000856$ 
                // - Ah, this is bad. It's hard to treat rabies. I'm sorry, but there's nothing I can do that will make a difference  at this point.
                // $script:0831180509000857$ 
                // - <font color="#909090">(He chuckles.)</font>
                //   Look at you, about to burst into tears.
                // $script:0831180509000858$ functionID=1 
                // - I was joking. Now, come over here. A little bit of iodine, and you'll be as good as new.
                return true;
            case 4000:
                // $script:0831180509000859$ 
                // - Where does it hurt? Show me.
                // $script:0831180509000860$ 
                // - ...Why would you lie about being sick? $OwnerName$, you're hopeless.
                return true;
            case 4100:
                // $script:0831180509000861$ 
                // - ...Again? Please stop acting like a child.
                // $script:0831180509000862$ 
                // - You shouldn't make things up and make others worry about you. It's not kind.
                // $script:0831180509000863$ 
                // - Am I going to have to scold you? Because if you pull this again, I will.
                return true;
            case 5000:
                // $script:0831180509000864$ 
                // - I don't like talking about myself. It's not a problem, because I have no friend to talk to anyway.
                // $script:0831180509000865$ 
                // - At least, not any more. My only friend passed away a long time ago.
                // $script:0831180509000866$ 
                // - He got into an accident... Actually, it's not of your business, really.
                return true;
            case 5100:
                // $script:0831180509000867$ 
                // - The story of how I learned alchemy is quite uninteresting.
                // $script:0831180509000868$ 
                // - I met a grungy old beggar in $map:02000051$. He was rather fastidious and pompous for a beggar.
                // $script:0831180509000869$ 
                // - But something about him seemed... powerful.
                // $script:0831180509000870$ 
                // - When there's something I want, nothing can get in my way. I told him I wanted to learn how to beg, and he taught me. In the meantime, I stood at his side and learned his alchemy secrets over his shoulder.
                // $script:0831180509000871$ 
                // - And look at me now. I'm as good an alchemist as he is.
                return true;
            case 6000:
                // $script:0831180509000872$ 
                // - Do you know what I fear the most? Death.
                // $script:0831180509000873$ 
                // - Everyone fears death, and just about everyone succumbs to death eventually.
                // $script:0831180509000874$ 
                // - But not me. I'm going to beat death, just like I've beaten everything else...
                return true;
            case 7000:
                // $script:0831180509000875$ 
                // - You've heard me mention my friend, have you not? He was the only person I could really talk to.
                // $script:0831180509000876$ 
                // - He's no longer here. He may not actually be dead. Instead, he's... in another world.
                // $script:0831180509000877$ 
                // - He and I ventured in the Shadow World when we were young. We got separated after a while.
                // $script:0831180509000878$ 
                // - We shouldn't have been there at all, but we were dumb and reckless. When I came to, he was gone. I wouldn't had made it at all if I hadn't met those merchants...
                // $script:0831180509000879$ 
                // - I may not be able to do much, but once in a while, I venture into the Shadow World to search for him. But I haven't heard a word, not even a rumor. Perhaps it's time to just let him go...
                return true;
            case 100:
                // $script:0831180509000880$ 
                // - Who are you? You should leave while I'm still in a pleasant mood.
                switch (selection) {
                    // $script:0831180509000881$
                    // - Yeah, okay, I'm out of here.
                    case 0:
                        Id = 0; // TODO: 101,102 | 
                        return false;
                    // $script:0831180509000882$
                    // - Oh, yeah? What happens when you're unpleasant?
                    case 1:
                        Id = 0; // TODO: 103,104 | 
                        return false;
                    // $script:0831180509000883$
                    // - What's your sign? Can I get your number?
                    case 2:
                        Id = 0; // TODO: 105,106 | 
                        return false;
                }
                return true;
            case 101:
                // $script:0831180509000884$ 
                // - Smart. The exit is that way.
                return true;
            case 102:
                // $script:0831180509000885$ 
                // - Good... Now, to return to my task... 
                return true;
            case 103:
                // $script:0831180509000886$ 
                // - <font color="#909090">(He chuckles darkly.)</font>
                //   Do you really want to find out?
                return true;
            case 104:
                // $script:0831180509000887$ 
                // - <font color="#909090">(He smiles.)</font>
                //   Simple. I don't let you leave.
                return true;
            case 105:
                // $script:0831180509000888$ 
                // - Not funny. Now get out of here.
                return true;
            case 106:
                // $script:0831180509000889$ 
                // - <font color="#909090">(He smirk.)</font>
                //   Sorry, $male:pal,female:lady$, you're not my type.
                return true;
            default:
                return true;
        }
    }
}
