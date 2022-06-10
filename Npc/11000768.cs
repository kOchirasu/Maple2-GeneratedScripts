using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000768: Growlie
/// </summary>
public class _11000768 : NpcScript {
    internal _11000768(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 1;2;3;4;5;6;9001;9002;9003;100
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180509001387$ 
                // - Yeah? What do you want?
                return true;
            case 1:
                // $script:0831180509001388$ 
                // - Don't make me work too hard.
                switch (selection) {
                    // $script:0831180509001389$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001390$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001391$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 2:
                // $script:0831180509001392$ 
                // - What do you want?
                switch (selection) {
                    // $script:0831180509001393$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001394$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001395$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 3:
                // $script:0831180509001396$ 
                // - Stop nagging me!
                switch (selection) {
                    // $script:0831180509001397$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001398$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001399$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 4:
                // $script:0831180509001400$ 
                // - Don't make me work too hard.
                switch (selection) {
                    // $script:0831180509001401$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001402$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001403$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509001404$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 5:
                // $script:0831180509001405$ 
                // - What do you want?
                switch (selection) {
                    // $script:0831180509001406$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001407$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001408$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509001409$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 6:
                // $script:0831180509001410$ 
                // - Stop nagging me!
                switch (selection) {
                    // $script:0831180509001411$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001412$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001413$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509001414$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 9:
                // $script:0831180509001415$ 
                // - Huh? You want to pay me?
                //   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
                switch (selection) {
                    // $script:0831180509001416$
                    // - Let me think about it some more.
                    case 0:
                        Id = 0; // TODO: 8040,8050,8060,9040 | 8999
                        return false;
                    // $script:0831180509001417$
                    // - (Pay $MaidSalary$.)
                    case 1:
                        Id = 0; // TODO: 8000,8001,8010,8011,8901 | 8900,8910
                        return false;
                }
                return true;
            case 8000:
                // $script:0831180509001418$ functionID=1 
                // - Paying your employees on time is a good practice. Keep up the good work.
                return true;
            case 8001:
                // $script:0831180509001419$ functionID=1 
                // - Now that I've been paid, I'm going to treat myself to a feast. I love to have food delivered to the house!
                return true;
            case 8010:
                // $script:0831180509001420$ functionID=1 
                // - Remember not to get behind on paying me. Ugh, I thought I was going to starve to death. Now that I have my paycheck, I'm going to order some pizza.
                return true;
            case 8011:
                // $script:0831180509001421$ functionID=1 
                // - I was going to leave if you didn't pay me by the end of the day. You're lucky you did.
                return true;
            case 8020:
                // $script:0831180509001422$ functionID=1 
                // - $OwnerName$, you should check the calendar sometimes. Our contract expires soon. You can't always be so busy that forget.
                return true;
            case 8021:
                // $script:0831180509001423$ functionID=1 
                // - Do I really have to remind you of this?
                switch (selection) {
                    // $script:0831180509001424$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001425$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001426$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509001427$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8040:
                // $script:0831180509001428$ 
                // - Aw man, that nap hit the spot.
                switch (selection) {
                    // $script:0831180509001429$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001430$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001431$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509001432$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8050:
                // $script:0831180509001433$ 
                // - Acting friendly isn't going to get you anything.
                switch (selection) {
                    // $script:0831180509001434$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001435$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001436$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509001437$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8060:
                // $script:0831180509001438$ 
                // - Don't talk to me. I don't want to do anything right now.
                switch (selection) {
                    // $script:0831180509001439$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001440$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001441$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509001442$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8900:
                // $script:0831180509001443$ 
                // - Oh no, don't you have money to pay me? This is not acceptable. $OwnerName$, you'd better go out and earn some money.
                return true;
            case 8901:
                // $script:0831180509001444$ 
                // - You already paid me for this month. And just because I look tough doesn't mean I'm a chat. Sheesh, $OwnerName$, who do you think I am?
                return true;
            case 8910:
                // $script:0831180509001445$ 
                // - I'm in no mood for games! Just give me my money! It's been day since you were supposed to pay me. I'm so hungry, I'm getting dizzy... 
                return true;
            case 8999:
                // $script:0831180509001446$ 
                // - What? What's going on? $OwnerName$, I don't know what the problem is. You take care of it.
                return true;
            case 9001:
                // $script:0831180509001447$ 
                // - What's up? 
                switch (selection) {
                    // $script:0831180509001448$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509001449$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001450$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9002:
                // $script:0831180509001451$ 
                // - I'm too hungry to talk.
                switch (selection) {
                    // $script:0831180509001452$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509001453$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001454$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9003:
                // $script:0831180509001455$ 
                // - I told you, I'm not going to work unless you pay me.
                switch (selection) {
                    // $script:0831180509001456$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509001457$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001458$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9010:
                // $script:0831180509001459$ 
                // - Our contract expired, so I'm just going to take a nap, okay?
                return true;
            case 9011:
                // $script:0831180509001460$ functionID=1 
                // - You're trying to get out of paying me, aren't you? Our contract has expired. You can't fool me. If you want something from me, pay up.
                return true;
            case 9020:
                // $script:0831180509001461$ functionID=1 
                // - I haven't eaten for $MaidPassedDay$! My clothes are practically falling off!
                return true;
            case 9021:
                // $script:0831180509001462$ functionID=1 
                // - $OwnerName$, why are you doing this to me?
                switch (selection) {
                    // $script:0831180509001463$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509001464$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001465$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9040:
                // $script:0831180509001466$ 
                // - It's not like I'm asking for a raise... Ugh.
                switch (selection) {
                    // $script:0831180509001467$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509001468$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001469$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9030:
                // $script:0831180509001470$ 
                // - I need a meal, a real meal. Not a snack, but a full on, three course meal!
                return true;
            case 9031:
                // $script:0831180509001471$ 
                // - Are you torturing me because I grumble sometimes? But I still clean and do everything you ask. Why aren't you paying me? If you don't pay me, why, I'll... I'll... I'll go on strike! I mean it!
                return true;
            case 9032:
                // $script:0831180509001472$ 
                // - You can't take home groceries until you've paid for them first, right? Same with my services. You have to pay for them first!
                return true;
            case 10:
                // $script:0831180509001473$ functionID=1 
                // - Nobody compares to me when it comes to alchemy!
                return true;
            case 11:
                // $script:0831180509001474$ functionID=1 
                // - You just let old $MaidName$ handle your potion-making.
                return true;
            case 20:
                // $script:0831180509001475$ functionID=1 
                // - Why are you asking so many personal questions?
                return true;
            case 21:
                // $script:0831180509001476$ functionID=1 
                // - Stop asking the same questions over and over.
                switch (selection) {
                    // $script:0831180509001477$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001478$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001479$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 22:
                // $script:0831180509001480$ functionID=1 
                // - Stop asking the same questions over and over.
                switch (selection) {
                    // $script:0831180509001481$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001482$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001483$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509001484$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 30:
                // $script:0831180509001485$ 
                // - When are you going to buy me some snacks?
                switch (selection) {
                    // $script:0831180509001486$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,1200,1300,1400,1500,1600,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509001487$
                    // - (Scold.)
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,4200,4300,9011 | 
                        return false;
                    // $script:0831180509001488$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509001489$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 31:
                // $script:0831180509001490$ 
                // - Why? What? What happened?
                switch (selection) {
                    // $script:0831180509001491$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,1200,1300,1400,1500,1600,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509001492$
                    // - (Scold.)
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,4200,4300,9011 | 
                        return false;
                    // $script:0831180509001493$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509001494$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 32:
                // $script:0831180509001495$ 
                // - $OwnerName$, what's the good news?
                switch (selection) {
                    // $script:0831180509001496$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,1200,1300,1400,1500,1600,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509001497$
                    // - (Scold.)
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,4200,4300,9011 | 
                        return false;
                    // $script:0831180509001498$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509001499$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 40:
                // $script:0831180509001500$ 
                // - Aw man, that nap hit the spot.
                switch (selection) {
                    // $script:0831180509001501$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001502$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001503$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 50:
                // $script:0831180509001504$ 
                // - Acting friendly isn't going to get you anything.
                switch (selection) {
                    // $script:0831180509001505$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001506$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001507$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 60:
                // $script:0831180509001508$ 
                // - Don't talk to me. I don't want to do anything right now.
                switch (selection) {
                    // $script:0831180509001509$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001510$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001511$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 1000:
                // $script:0831180509001512$ 
                // - Hey, $OwnerName$.
                // $script:0831180509001513$ 
                // - I just had this delivered, and I don't like it. You can eat it if you want. 
                // $script:0831180509001514$ 
                // - It's a bit cold by now, though.
                switch (selection) {
                    // $script:0831180509001515$
                    // - Ugh, it's too cold!
                    case 0:
                        Id = 0; // TODO: 1001,1002 | 
                        return false;
                    // $script:0831180509001516$
                    // - It's delicious!
                    case 1:
                        Id = 0; // TODO: 1011,1012 | 
                        return false;
                }
                return true;
            case 1001:
                // $script:0831180509001517$ functionID=1 
                // - If you don't want to eat it, then don't eat it! Ingrate.
                return true;
            case 1002:
                // $script:0831180509001518$ functionID=1 
                // - Cold or hot, your belly doesn't know the difference. Just eat what I feed you.
                return true;
            case 1011:
                // $script:0831180509001519$ functionID=1 
                // - Of course, it's delicious. It's a gift from me. Next time, I'm going to eat it all myself. Don't even think of asking for a bite.
                return true;
            case 1012:
                // $script:0831180509001520$ functionID=1 
                // - It's exactly what you wanted, isn't it? Don't worry, I'll order from that restaurant again soon.
                return true;
            case 1100:
                // $script:0831180509001521$ 
                // - It's exhausting taking care of you...
                // $script:0831180509001522$ 
                // - $OwnerName$, I'd like to offer you my leftover snacks from yesterday. They're a bit stale, but you can eat them if you want.
                // $script:0831180509001523$ 
                // - If you eat even a bite, I expect you to get me more delicious snacks in return.
                switch (selection) {
                    // $script:0831180509001524$
                    // - I bought you snacks yesterday!
                    case 0:
                        Id = 0; // TODO: 1101,1102 | 
                        return false;
                    // $script:0831180509001525$
                    // - Sure.
                    case 1:
                        Id = 0; // TODO: 1111,1112 | 
                        return false;
                }
                return true;
            case 1101:
                // $script:0831180509001526$ functionID=1 
                // - That was yesterday! A new day requires new snacks! What, are you really that stingy?
                return true;
            case 1102:
                // $script:0831180509001527$ functionID=1 
                // - Are you calling me ungrateful? Forget it. I'll buy my own snacks!
                return true;
            case 1111:
                // $script:0831180509001528$ functionID=1 
                // - Bwahahaha! Just the thought of new snakes makes my mouth water!
                return true;
            case 1112:
                // $script:0831180509001529$ functionID=1 
                // - Why don't you go now, then? I want my snacks right now!
                return true;
            case 1200:
                // $script:0831180509001530$ 
                // - Whew, it's hot in here. Take this cool drink to refresh yourself.
                // $script:0831180509001531$ 
                // - Don't you think it's like an oven in here?
                switch (selection) {
                    // $script:0831180509001532$
                    // - Thanks for the drink! Just what I needed.
                    case 0:
                        Id = 0; // TODO: 1211,1212 | 
                        return false;
                    // $script:0831180509001533$
                    // - Actually, I'm freezing...
                    case 1:
                        Id = 0; // TODO: 1201,1202 | 
                        return false;
                }
                return true;
            case 1201:
                // $script:0831180509001534$ functionID=1 
                // - If you're cold, you're dehydrated. That's what I always say!
                return true;
            case 1202:
                // $script:0831180509001535$ functionID=1 
                // - Pssh, I'm sweating! How can you be cold?
                //   <font color="#909090">(He scratches at the patch of white fur on his neck.)</font>
                return true;
            case 1211:
                // $script:0831180509001536$ functionID=1 
                // - I thought it was just me, because of my fur. But it seems like you're hot, too.
                return true;
            case 1212:
                // $script:0831180509001537$ functionID=1 
                // - Am I hot because of my fur or because of the weather?
                return true;
            case 1300:
                // $script:0831180509001538$ 
                // - $npcName:11000002[gender:1]$ gave me some of food he cooked, but I don't think I like it. Taste it.
                // $script:0831180509001539$ 
                // - How does it taste? Well? Well??
                switch (selection) {
                    // $script:0831180509001540$
                    // - It's delicious!
                    case 0:
                        Id = 0; // TODO: 1311,1312 | 
                        return false;
                    // $script:0831180509001541$
                    // - Did you remember to thank $npcName:11000002[gender:1]$?
                    case 1:
                        Id = 0; // TODO: 1301,1302 | 
                        return false;
                }
                return true;
            case 1301:
                // $script:0831180509001542$ functionID=1 
                // - Why should I? $npc:11000002[gender:1]$ always gives me food.
                return true;
            case 1302:
                // $script:0831180509001543$ functionID=1 
                // - $npcName:11000002[gender:1]$ asked me the same question as she passed, but she wouldn't have dared if she knew I was older than her.
                return true;
            case 1311:
                // $script:0831180509001544$ functionID=1 
                // - I love $npcName:11000002[gender:1]$'s food! It's my favorite!
                return true;
            case 1312:
                // $script:0831180509001545$ functionID=1 
                // - ...I feel hungry all of a sudden. Come on, share with me!
                return true;
            case 1400:
                // $script:0831180509001546$ 
                // - $OwnerName$, I found this while napping inside the storage chest.
                // $script:0831180509001547$ 
                // - Is it yours?
                switch (selection) {
                    // $script:0831180509001548$
                    // - Never seen it before. Nooo idea whose it could be...
                    case 0:
                        Id = 0; // TODO: 1401,1402 | 
                        return false;
                    // $script:0831180509001549$
                    // - Yup, it's mine.
                    case 1:
                        Id = 0; // TODO: 1411,1412 | 
                        return false;
                }
                return true;
            case 1401:
                // $script:0831180509001550$ functionID=1 
                // - Then give it back! I'm going to keep it.
                return true;
            case 1402:
                // $script:0831180509001551$ functionID=1 
                // - Strange. I thought I already swept this place for valuables... Where did this come from?
                return true;
            case 1411:
                // $script:0831180509001552$ functionID=1 
                // - I would've kept it if I knew it belonged to you. Bah, I shouldn't have even asked.
                return true;
            case 1412:
                // $script:0831180509001553$ functionID=1 
                // - I found something you lost. To pay me back, give me some snacks.
                return true;
            case 1500:
                // $script:0831180509001554$ 
                // - I found this while playing in $map:2000001$. Your house is too empty. Use it to decorate a bit more.
                // $script:0831180509001555$ 
                // - Make the house more comfortable for me, all right?
                switch (selection) {
                    // $script:0831180509001556$
                    // - Sure.
                    case 0:
                        Id = 0; // TODO: 1511,1512 | 
                        return false;
                    // $script:0831180509001557$
                    // - I like the minimalist look.
                    case 1:
                        Id = 0; // TODO: 1501,1502 | 
                        return false;
                }
                return true;
            case 1501:
                // $script:0831180509001558$ functionID=1 
                // - But there aren't enough comfy places for me to lie down! Come on, just use it!
                return true;
            case 1502:
                // $script:0831180509001559$ functionID=1 
                // - Are you saying you don't want things from me? I brought it all the way home, and you don't even say thank you.
                return true;
            case 1511:
                // $script:0831180509001560$ functionID=1 
                // - I want this place to feel more homey. Decorate for me, okay?
                return true;
            case 1512:
                // $script:0831180509001561$ functionID=1 
                // - The more furniture you have, the less floor for me to mop. Fill your house up with stuff, okay?
                return true;
            case 1600:
                // $script:0831180509001562$ 
                // - I found this between the sheets of your bed.
                // $script:0831180509001563$ 
                // - Did you lose it?
                switch (selection) {
                    // $script:0831180509001564$
                    // - What were you doing on my bed?
                    case 0:
                        Id = 0; // TODO: 1601,1602 | 
                        return false;
                    // $script:0831180509001565$
                    // - Thank you.
                    case 1:
                        Id = 0; // TODO: 1611,1612 | 
                        return false;
                }
                return true;
            case 1601:
                // $script:0831180509001566$ functionID=1 
                // - Searching for this item you lost! Obviously! Not taking a nap...
                return true;
            case 1602:
                // $script:0831180509001567$ functionID=1 
                // - I got tired while cleaning, so I put my feet up for a minute. I'm entitled to breaks, you know.
                return true;
            case 1611:
                // $script:0831180509001568$ functionID=1 
                // - I was going to keep it, but I changed my mind. Lucky you.
                return true;
            case 1612:
                // $script:0831180509001569$ functionID=1 
                // - It was good I decided to take a break, wasn't it?
                return true;
            case 2000:
                // $script:0831180509001570$ 
                // - Stop trying to tell me how I do my job, and just go out there and... do whatever it is that you do!
                // $script:0831180509001571$ 
                // - The house is so dusty because you keep tracking in dirt!
                // $script:0831180509001572$ 
                // - I just don't understand why you're so dirty. Stop fooling around and take a shower!
                return true;
            case 2100:
                // $script:0831180509001573$ 
                // - One of your friends stopped by but left without giving me a name.
                // $script:0831180509001574$ 
                // - I didn't ask because... I didn't think of it, okay?
                return true;
            case 2200:
                // $script:0831180509001575$ 
                // - I don't feel like doing anything today. If you insist that I pick something to do, I choose to lie down and rest.
                // $script:0831180509001576$ 
                // - What do you mean resting isn't work? Of course it is! It involves thinking!
                // $script:0831180509001577$ 
                // - I have to think real hard about what snacks I should eat today, tomorrow, the rest of the week... That stuff is really important to me!
                return true;
            case 3000:
                // $script:0831180509001578$ 
                // - Okay, okay! I'll do it! I'll clean! Sheesh.
                // $script:0831180509001579$ functionID=1 
                // - Why do you want me to clean all the time? The house will just end up getting dirty again. Why can't I just leave it dirty?
                return true;
            case 3100:
                // $script:0831180509001580$ 
                // - You know those rough-looking guys in $map:2000001$? Yeah, I'm their leader. Stop scolding or I'll tell them to make your life difficult.
                // $script:0831180509001581$ functionID=1 
                // - What do you mean, you're not scared of my friends. They're level 10. Got that? Level 10!
                return true;
            case 4000:
                // $script:0831180509001582$ 
                // - Stop harassing me or I'll quit, I mean it!
                // $script:0831180509001583$ 
                // - If I quit, you won't have anyone to keep your house clean. It doesn't just clean itself, you know?
                return true;
            case 4100:
                // $script:0831180509001584$ 
                // - Enough is enough!
                // $script:0831180509001585$ 
                // - Argh! Why do you treat me like this? I just want to be happy and take naps. Is that too much to ask?
                // $script:0831180509001586$ 
                // - Why can't you just let me be happy?! Don't you think I deserve it?
                return true;
            case 5000:
                // $script:0831180509001587$ 
                // - I came to $map:2000001$ for $npc:11000075[gender:1]$'s event. I've always been in love with $npc:11000075[gender:1]$, ever since I was little. I even dream about her sometimes.
                // $script:0831180509001588$ 
                // - I fell in love with the $npc:11000075[gender:1]$ because of a book. She was illustrated as a character in it, and the moment I saw the picture, that was it for me.
                // $script:0831180509001589$ 
                // - I came to $map:2000001$ to see the love of my life, $npc:11000075[gender:1]$, but then the ceremony was canceled.
                // $script:0831180509001590$ 
                // - I was so desperate to see her, I sprinted toward the palace. All I wanted was a glance. Instead, $npc:11000119[gender:0]$ appeared.
                // $script:0831180509001591$ 
                // - I tried to shove past him, but he tripped me. Can you believe that? Who is he to stop me from seeing her?
                return true;
            case 5100:
                // $script:0831180509001592$ 
                // - I accepted this job because it's the best! I get to live in someone else's house, eat their food, sleep in their bed, and I even get paid! All I have to do in return is a bit of cleaning.
                // $script:0831180509001593$ 
                // - But the cleaning part isn't as easy as you'd think.
                // $script:0831180509001594$ 
                // - Dust bunnies lurk in every corner. As soon as you sweep, the dust scatters.
                // $script:0831180509001595$ 
                // - And where do you think that dust goes? Your bed! The bathroom sink! Between the cracks of the living room floor! And the it's back to square one for me.
                // $script:0831180509001596$ 
                // - Now if I just leave the dust bunnies where they are, what do you think happens? They accumulate until they grow so big, you can just pluck them away. So you see, the less you clean, the better.
                return true;
            case 6000:
                // $script:0831180509001597$ 
                // - Ever wonder why I complain so much? I wasn't always like this, you know. The world has made me what I am.
                // $script:0831180509001598$ 
                // - Everyone I've met has been mean to me. I tried to be nice to them, but all I got back was bullying and name-calling.
                // $script:0831180509001599$ 
                // - You don't have to be nice to others, $OwnerName$. They'll only hurt you, no matter how nice you are to them.
                // $script:0831180509001600$ 
                // - Don't show the world your weaknesses. You'll always regret it.
                return true;
            case 7000:
                // $script:0831180509001601$ 
                // - Have you met $npcName:22000002[gender:0]$? I used to be good friends with him.
                // $script:0831180509001602$ 
                // - He's not the sharpest, but he's stronger than anyone else I know. Let me tell you a story about him and $npcName:11000002[gender:1]$.
                // $script:0831180509001603$ 
                // - $npcName:11000002[gender:1]$ has loved cooking since she was young. She was always searching for ingredients. One day, she went to $map:2000043$ even though the grownups told her not to. She was climbing a hill, when suddenly the ground shook and a big rock came rolling straight toward her!
                // $script:0831180509001604$ 
                // - She was so scared that she fainted. $npcName:22000002[gender:0]$ saw what was happening, leapt over, and shattered the rock with a single punch! He saved $npcName:11000002[gender:1]$. That's how strong $npcName:22000002[gender:0]$ is.
                // $script:0831180509001605$ 
                // - $npcName:11000002[gender:1]$ thinks $npcName:11000055[gender:0]$'s father saved her, but I saw it all. He used to be so nice when he was young. I don't know what changed him over the years.
                // $script:0831180509001606$ 
                // - Huh? What was I doing in $map:2000043$? That's none of your business!
                return true;
            case 100:
                // $script:0831180509001607$ 
                // - <font color="#909090">(He wipes crumbs away from his mouth.)</font>
                //   Who are you? You friends with my boss?
                switch (selection) {
                    // $script:0831180509001608$
                    // - Yep!
                    case 0:
                        Id = 0; // TODO: 101,102 | 
                        return false;
                    // $script:0831180509001609$
                    // - Nope!
                    case 1:
                        Id = 0; // TODO: 103,104 | 
                        return false;
                    // $script:0831180509001610$
                    // - Who are you?
                    case 2:
                        Id = 0; // TODO: 105,106 | 
                        return false;
                }
                return true;
            case 101:
                // $script:0831180509001611$ 
                // - If you've got business with the boss, what're you talking to me for? Sheesh.
                return true;
            case 102:
                // $script:0831180509001612$ 
                // - Then sit down and stay quiet. We'll see what the boss has to say.
                return true;
            case 103:
                // $script:0831180509001613$ 
                // - They what are you doing here? Get out, before I make you get out!
                return true;
            case 104:
                // $script:0831180509001614$ 
                // - Great timing. I'm starving. Why don't you go get me something to eat?
                return true;
            case 105:
                // $script:0831180509001615$ 
                // - I'm the glue that holds this household together. Name's $MaidName$. Night to meet you.
                return true;
            case 106:
                // $script:0831180509001616$ 
                // - Why don't you tell me who you are first? Sheesh.
                return true;
            default:
                return true;
        }
    }
}
