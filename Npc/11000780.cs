using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000780: Blake
/// </summary>
public class _11000780 : NpcScript {
    internal _11000780(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 1;2;3;4;5;6;9001;9002;9003;100
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180509003676$ 
                // - Do you have business with me?
                return true;
            case 1:
                // $script:0831180509003677$ 
                // - Did you call me?
                switch (selection) {
                    // $script:0831180509003678$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003679$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003680$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 2:
                // $script:0831180509003681$ 
                // - Have a good day!
                switch (selection) {
                    // $script:0831180509003682$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003683$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003684$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 3:
                // $script:0831180509003685$ 
                // - Mm? What are you thinking?
                switch (selection) {
                    // $script:0831180509003686$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003687$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003688$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 4:
                // $script:0831180509003689$ 
                // - Did you call me?
                switch (selection) {
                    // $script:0831180509003690$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003691$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003692$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509003693$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 5:
                // $script:0831180509003694$ 
                // - Have a good day!
                switch (selection) {
                    // $script:0831180509003695$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003696$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003697$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509003698$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 6:
                // $script:0831180509003699$ 
                // - Mm? What are you thinking?
                switch (selection) {
                    // $script:0831180509003700$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003701$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003702$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509003703$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 9:
                // $script:0831180509003704$ 
                // - You want to pay me?
                //   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
                switch (selection) {
                    // $script:0831180509003705$
                    // - Let me think about it some more.
                    case 0:
                        Id = 0; // TODO: 8040,8050,8060,9040 | 8999
                        return false;
                    // $script:0831180509003706$
                    // - (Pay $MaidSalary$.)
                    case 1:
                        Id = 0; // TODO: 8000,8001,8010,8011,8901 | 8900,8910
                        return false;
                }
                return true;
            case 8000:
                // $script:0831180509003707$ functionID=1 
                // - Time passes so quickly. Perhaps it's because I'm with you, $OwnerName$.
                //   <font color="#909090">(He smirks.)</font>
                return true;
            case 8001:
                // $script:0831180509003708$ functionID=1 
                // - You're paying me already? Hey, that makes you my favorite person today.
                return true;
            case 8010:
                // $script:0831180509003709$ functionID=1 
                // - You've been neglecting me, $OwnerName$. I don't like it. Not one bit. If it's because I haven't had time to hang out with you, well, I suppose that makes us even. Let's make up. 
                return true;
            case 8011:
                // $script:0831180509003710$ functionID=1 
                // - And here I thought you were a lost cause. Things have been tough lately, haven't they? Here, how about a pat on the back? Haha.
                return true;
            case 8020:
                // $script:0831180509003711$ functionID=1 
                // - $OwnerName$, did you know our contract expires soon? 
                return true;
            case 8021:
                // $script:0831180509003712$ functionID=1 
                // - I know you're busy, but you need to pay attention to me sometimes.
                switch (selection) {
                    // $script:0831180509003713$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003714$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003715$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509003716$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8040:
                // $script:0831180509003717$ 
                // - $OwnerName$, things have been so boring here without you.
                switch (selection) {
                    // $script:0831180509003718$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003719$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003720$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509003721$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8050:
                // $script:0831180509003722$ 
                // - Come on, loosen up a bit. Aren't we friends?
                switch (selection) {
                    // $script:0831180509003723$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003724$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003725$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509003726$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8060:
                // $script:0831180509003727$ 
                // - I'm tired. Maybe I should take a nap... 
                switch (selection) {
                    // $script:0831180509003728$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003729$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003730$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509003731$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8900:
                // $script:0831180509003732$ 
                // - Aw, $OwnerName$. This is just like when you tell your friends you'll treat them to dinner and the restaurant tells you your card's been declined. It's okay. I understand. Don't worry about me.
                return true;
            case 8901:
                // $script:0831180509003733$ 
                // - You feeling all right? You've already paid me this month. Let me feel your forehead.
                return true;
            case 8910:
                // $script:0831180509003734$ 
                // - This is really not the time to make jokes, $OwnerName$. I'm not in the mood. I'm serious!
                return true;
            case 8999:
                // $script:0831180509003735$ 
                // - Can't believe this is happening to me. Never in my life... Just, give me a minute, okay?
                return true;
            case 9001:
                // $script:0831180509003736$ 
                // - Okay. It's been $MaidPassedDay$ since I was supposed to be paid. Please tell me you have good news. 
                switch (selection) {
                    // $script:0831180509003737$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509003738$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003739$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9002:
                // $script:0831180509003740$ 
                // - Can't eat... Can't sleep... My mind just keeps spinning and spinning...
                switch (selection) {
                    // $script:0831180509003741$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509003742$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003743$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9003:
                // $script:0831180509003744$ 
                // - Before I got my big break, things were tough. Real tough. Been thinking about that a lot lately. 
                switch (selection) {
                    // $script:0831180509003745$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509003746$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003747$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9010:
                // $script:0831180509003748$ 
                // - Wait, my alarm went off, but I don't have a shoot scheduled... Oh, right. $OwnerName$, my contract expired. 
                return true;
            case 9011:
                // $script:0831180509003749$ functionID=1 
                // - Why are we talking about that when you let my contract expire. $OwnerName$, give it to my straight. You don't want me around any more?
                return true;
            case 9020:
                // $script:0831180509003750$ functionID=1 
                // - Honestly, I don't even understand what's going on any more. I'm not used to rejection. I'll be strong, though.
                return true;
            case 9021:
                // $script:0831180509003751$ functionID=1 
                // - But that doesn't mean you should stop worrying about me.
                switch (selection) {
                    // $script:0831180509003752$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509003753$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003754$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9040:
                // $script:0831180509003755$ 
                // - $OwnerName$, just tell me. Don't you want me around any more? 
                switch (selection) {
                    // $script:0831180509003756$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509003757$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003758$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9030:
                // $script:0831180509003759$ 
                // - $OwnerName$, I enjoy being around you. But I guess the feeling's not mutual.
                return true;
            case 9031:
                // $script:0831180509003760$ 
                // - I cook for for you, clean for you, make healthy smoothies for you, give you gifts I got from my fans... Wait, is that what this is about? Because I gave you gifts from my fans? 
                return true;
            case 9032:
                // $script:0831180509003761$ 
                // - $OwnerName$, maybe you should give me control of your accounts in the future. I mean, what are you doing with your money that you can't even pay me? 
                return true;
            case 10:
                // $script:0831180509003762$ functionID=1 
                // - Sure, sure. Just say the word.
                return true;
            case 11:
                // $script:0831180509003763$ functionID=1 
                // - I don't mind doing stuff for you.
                return true;
            case 20:
                // $script:0831180509003764$ functionID=1 
                // - I don't mind being stared at, but it makes me blush. Heh.
                return true;
            case 21:
                // $script:0831180509003765$ functionID=1 
                // - Don't worry about me too much.
                switch (selection) {
                    // $script:0831180509003766$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003767$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003768$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 22:
                // $script:0831180509003769$ functionID=1 
                // - Don't worry about me too much.
                switch (selection) {
                    // $script:0831180509003770$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003771$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003772$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509003773$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 30:
                // $script:0831180509003774$ 
                // - Let's hear it.
                switch (selection) {
                    // $script:0831180509003775$
                    // - Did anything interesting happen today? 
                    case 0:
                        Id = 0; // TODO: 1000,1100,1200,1300,1400,1500,1600,1700,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509003776$
                    // - (Act like you're best pals.)
                    case 1:
                        Id = 0; // TODO: 3000,3100,3200,4000,4100,4200,4300,9011 | 
                        return false;
                    // $script:0831180509003777$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509003778$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 31:
                // $script:0831180509003779$ 
                // - Sure, I love chatting.
                switch (selection) {
                    // $script:0831180509003780$
                    // - Did anything interesting happen today? 
                    case 0:
                        Id = 0; // TODO: 1000,1100,1200,1300,1400,1500,1600,1700,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509003781$
                    // - (Act like you're best pals.)
                    case 1:
                        Id = 0; // TODO: 3000,3100,3200,4000,4100,4200,4300,9011 | 
                        return false;
                    // $script:0831180509003782$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509003783$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 32:
                // $script:0831180509003784$ 
                // - All right, what do you want to talk about?
                switch (selection) {
                    // $script:0831180509003785$
                    // - Did anything interesting happen today? 
                    case 0:
                        Id = 0; // TODO: 1000,1100,1200,1300,1400,1500,1600,1700,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509003786$
                    // - (Act like you're best pals.)
                    case 1:
                        Id = 0; // TODO: 3000,3100,3200,4000,4100,4200,4300,9011 | 
                        return false;
                    // $script:0831180509003787$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509003788$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 40:
                // $script:0831180509003789$ 
                // - $OwnerName$, things have been so boring here without you.
                switch (selection) {
                    // $script:0831180509003790$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003791$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003792$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 50:
                // $script:0831180509003793$ 
                // - Come on, loosen up a bit. Aren't we friends?
                switch (selection) {
                    // $script:0831180509003794$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003795$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003796$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 60:
                // $script:0831180509003797$ 
                // - I'm tired. Maybe I should take a nap... 
                switch (selection) {
                    // $script:0831180509003798$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003799$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003800$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 1000:
                // $script:0831180509003801$ 
                // - It's been a while since I had to cook. And I've never really cooked for, you know, someone special. Feels kind of nice.
                // $script:0831180509003802$ 
                // - Instead of MSG, I put in an extra dose of awesome. Because I'm awesome, get it?
                switch (selection) {
                    // $script:0831180509003803$
                    // - I can't really tell what flavor you're going for.
                    case 0:
                        Id = 0; // TODO: 1001,1002 | 
                        return false;
                    // $script:0831180509003804$
                    // - It's delicious.
                    case 1:
                        Id = 0; // TODO: 1011,1012 | 
                        return false;
                }
                return true;
            case 1001:
                // $script:0831180509003805$ functionID=1 
                // - Yeah, everyone tells me my tastes are unique. Might take you some time to get used to it. Not bad, though, right?
                return true;
            case 1002:
                // $script:0831180509003806$ functionID=1 
                // - Heh, sorry. Like I said, I don't cook much. Next time, I'll just have something delivered.
                return true;
            case 1011:
                // $script:0831180509003807$ functionID=1 
                // - Eat up! I can always make more if you want. I mean, it might take me a while, but I don't mind.
                return true;
            case 1012:
                // $script:0831180509003808$ functionID=1 
                // - Uh, yeah? I mean, I made it, didn't I? Of course it's good. I mean, after my last performance, I'm pretty much an artist and cooking is an art, so, you know... the math works.
                return true;
            case 1100:
                // $script:0831180509003809$ 
                // - I whipped this up just to see if I enjoy cooking. Have a bite?
                // $script:0831180509003810$ 
                // - Don't give me that look. You know I can't eat it with you. I've got gigs coming up. I've got to watch my weight.
                switch (selection) {
                    // $script:0831180509003811$
                    // - But you already look great!
                    case 0:
                        Id = 0; // TODO: 1111,1112 | 
                        return false;
                    // $script:0831180509003812$
                    // - But you can just do a few extra sit-ups later!
                    case 1:
                        Id = 0; // TODO: 1101,1102 | 
                        return false;
                }
                return true;
            case 1101:
                // $script:0831180509003813$ functionID=1 
                // - Hey, my exercise regimen is a delicate balance. Besides, my trainer would kill me.
                return true;
            case 1102:
                // $script:0831180509003814$ functionID=1 
                // - I know you can't see through my clothes, but you don't get as cut as I do eating whatever you want. It takes discipline.
                return true;
            case 1111:
                // $script:0831180509003815$ functionID=1 
                // - I do, don't I? I inherited some amazing genes.
                //   <font color="#909090">(He smirks.)</font>
                return true;
            case 1112:
                // $script:0831180509003816$ functionID=1 
                // - Can't stop checking me out, can you? I get it. My good looks outshine even my singing and acting skills.
                return true;
            case 1200:
                // $script:0831180509003817$ 
                // - My company sent me this juicer...
                // $script:0831180509003818$ 
                // - It's supposed to be able to juice up anything you throw in it. I had to test it out. Here, $OwnerName$, have a taste.
                switch (selection) {
                    // $script:0831180509003819$
                    // - (Taste it.)
                    case 0:
                        Id = 0; // TODO: 1211,1212 | 
                        return false;
                    // $script:0831180509003820$
                    // - (Firmly decline.)
                    case 1:
                        Id = 0; // TODO: 1201,1202 | 
                        return false;
                }
                return true;
            case 1201:
                // $script:0831180509003821$ functionID=1 
                // - What? You're rejecting me? Somewhere, some of my fans are about to riot.
                return true;
            case 1202:
                // $script:0831180509003822$ functionID=1 
                // - C'mon, I didn't put anything bad in it. At least, smell it! C'mere...
                return true;
            case 1211:
                // $script:0831180509003823$ functionID=1 
                // - How is it? Tasty? This is such a great way to clear the fridge of old veggies.
                return true;
            case 1212:
                // $script:0831180509003824$ functionID=1 
                // - Hey, you look good when you drink. Have another sip. Yeah, that's it. Now, hold it right there. Amazing!
                return true;
            case 1300:
                // $script:0831180509003825$ 
                // - Did I tell you I was on a cooking show a while back, $OwnerName$? I thought you might like one of the dishes, so I had them send me the recipe.
                // $script:0831180509003826$ 
                // - Just think! The exquisiteness of fine cuisine from the comfort of your own home. Let me feed you a bite. And... how is it?
                switch (selection) {
                    // $script:0831180509003827$
                    // - Um, it's not my favorite...
                    case 0:
                        Id = 0; // TODO: 1301,1302 | 
                        return false;
                    // $script:0831180509003828$
                    // - It's delicious.
                    case 1:
                        Id = 0; // TODO: 1311,1312 | 
                        return false;
                }
                return true;
            case 1301:
                // $script:0831180509003829$ functionID=1 
                // - Ah, yeah. To be expected from a plebeian unaccustomed to the finer things in life. Don't worry, I'll teach you how to enjoy fine dining.
                return true;
            case 1302:
                // $script:0831180509003830$ functionID=1 
                // - Oops. Now that I think about it, I may have skipped a step or two of the recipe...
                return true;
            case 1311:
                // $script:0831180509003831$ functionID=1 
                // - Of course it is! It's a great recipe prepared by a great guy!
                return true;
            case 1312:
                // $script:0831180509003832$ functionID=1 
                // - I'm glad you enjoyed it. Maybe I should have them send me all their best and most secret recipes. Wouldn't you like to try them?
                return true;
            case 1400:
                // $script:0831180509003833$ 
                // - I got this from a fan, but I'm not quite sure of its purpose...
                // $script:0831180509003834$ 
                // - Anyway, I have no use for it. Maybe you do, $OwnerName$?
                switch (selection) {
                    // $script:0831180509003835$
                    // - Oh, no, it's too much. I can't accept that.
                    case 0:
                        Id = 0; // TODO: 1401,1402 | 
                        return false;
                    // $script:0831180509003836$
                    // - Thanks!
                    case 1:
                        Id = 0; // TODO: 1411,1412 | 
                        return false;
                }
                return true;
            case 1401:
                // $script:0831180509003837$ functionID=1 
                // - Suit yourself. I'll just keep it.
                return true;
            case 1402:
                // $script:0831180509003838$ functionID=1 
                // - Did you just reject me, $OwnerName$? Hah, that's not really something I'm used to...
                return true;
            case 1411:
                // $script:0831180509003839$ functionID=1 
                // - Do you even know what it is? Can you... explain how it works?
                return true;
            case 1412:
                // $script:0831180509003840$ functionID=1 
                // - Right-o. Just don't tell anyone. I wouldn't want to upset my fans.
                return true;
            case 1500:
                // $script:0831180509003841$ 
                // - My agent forwarded this to me. It's from the Moms Who Love $MaidName$ fan club.
                // $script:0831180509003842$ 
                // - Hey, I'm just really lovable, okay? Anyway, I don't need it. You can keep it if you want.
                switch (selection) {
                    // $script:0831180509003843$
                    // - Looks nice! Thank you!
                    case 0:
                        Id = 0; // TODO: 1511,1512 | 
                        return false;
                    // $script:0831180509003844$
                    // - Gross. This was meant for you.
                    case 1:
                        Id = 0; // TODO: 1501,1502 | 
                        return false;
                }
                return true;
            case 1501:
                // $script:0831180509003845$ functionID=1 
                // - Hey, I'm just trying to spread the love. Why is that a problem?
                return true;
            case 1502:
                // $script:0831180509003846$ functionID=1 
                // - You don't want it? But it's nice. I'll donate it to a charity auction, I guess.
                return true;
            case 1511:
                // $script:0831180509003847$ functionID=1 
                // - Great! I'm glad it's going to a good home. I love all my fans but I've already got too much stuff like that.
                return true;
            case 1512:
                // $script:0831180509003848$ functionID=1 
                // - Thanks to my fans, you're getting all kinds of free goodies for your house, $OwnerName$.
                return true;
            case 1600:
                // $script:0831180509003849$ 
                // - I was using the vacuum to practices some poses when something strange got sucked into it. My curiosity got the best of me, so I opened it up and found this.
                // $script:0831180509003850$ 
                // - You shouldn't leave stuff like this just sitting around, you know.
                switch (selection) {
                    // $script:0831180509003851$
                    // - My vacuum! Is it okay?!
                    case 0:
                        Id = 0; // TODO: 1601,1602 | 
                        return false;
                    // $script:0831180509003852$
                    // - Thank you.
                    case 1:
                        Id = 0; // TODO: 1611,1612 | 
                        return false;
                }
                return true;
            case 1601:
                // $script:0831180509003853$ functionID=1 
                // - What?! Um, I don't know?
                return true;
            case 1602:
                // $script:0831180509003854$ functionID=1 
                // - If the vacuum did break, why don't you just get a robot vacuum?
                return true;
            case 1611:
                // $script:0831180509003855$ functionID=1 
                // - Remember how I had to spot you for the food delivery guy last time? Well, maybe you should keep your mesos somewhere you can find it for next time.
                return true;
            case 1612:
                // $script:0831180509003856$ functionID=1 
                // - Keep your mesos close and your $MaidName$ closer, you know. Hahaha.
                return true;
            case 2000:
                // $script:0831180509003857$ 
                // - Hmm, anything interesting?
                // $script:0831180509003858$ 
                // - Oh, I got a commercial proposal.
                // $script:0831180509003859$ 
                // - For an anti-dandruff shampoo, I think.
                return true;
            case 2100:
                // $script:0831180509003860$ 
                // - There is nothing more special than this moment right here, right now with you, $OwnerName$.
                // $script:0831180509003861$ 
                // - Just soak it in, $OwnerName$. This moment, free from the raving masses of fans, free to do whatever I want.
                return true;
            case 2200:
                // $script:0831180509003862$ 
                // - Whew, close one. Even wearing a hat, sunglasses, and even a mask, someone recognized me.
                // $script:0831180509003863$ 
                // - He kept following me with his camera. I had to circle the neighborhood several times before I snuck away.
                // $script:0831180509003864$ 
                // - Fame is stressful. You hear me, $OwnerName$?
                return true;
            case 3000:
                // $script:0831180509003865$ 
                // - A single word of encouragement from you, $OwnerName$, gives me more strength than the support of all the rest of my fans added together.
                // $script:0831180509003866$ functionID=1 
                // - Let's not fight and be good to each other always.
                return true;
            case 3100:
                // $script:0831180509003867$ 
                // - Sometimes my heart races, and I think there's gotta be cameras hidden around the house somewhere. I just get so used to them, you know?
                // $script:0831180509003868$ functionID=1 
                // - Why am I so fearful of a hidden camera? I'll let you figure that one out.
                //   <font color="#909090">(He smirks.)</font>
                return true;
            case 3200:
                // $script:0831180509003869$ 
                // - You wanna hear my secret, how I captivate my audience?
                // $script:0831180509003870$ 
                // - I pick one girl and stare at her throughout my performance. I tell myself, "doesn't matter if I'm the handsomest guy here tonight or not, I will make that one girl mine."
                // $script:0831180509003871$ 
                // - You should see the dreamy look those girls get. Because, let's face it, I'm always the handsomest guy around.
                // $script:0831180509003872$ 
                // - Why are you giving me that look? You know it's true!
                // $script:0831180509003873$ functionID=1 
                // - I'm surprised you even care. Do you want to become a singer, $OwnerName$? Or do you just want to know about me?
                return true;
            case 4000:
                // $script:0831180509003874$ 
                // - When the going gets tough, the tough come home.
                // $script:0831180509003875$ 
                // - You know I'll always be here to welcome you home, don't you, $OwnerName$?
                return true;
            case 4100:
                // $script:0831180509003876$ 
                // - Why are you smiling? What's the good news? Then again, everyone who looks at me can't help but smile.
                // $script:0831180509003877$ 
                // - Some of them even forget to close their mouths and start to drool. Might be a cute look on you, $OwnerName$. Hahaha.
                return true;
            case 5000:
                // $script:0831180509003878$ 
                // - Don't believe the news! It's not true!
                // $script:0831180509003879$ 
                // - We only had dinner together once! And I haven't seen her since!
                // $script:0831180509003880$ 
                // - Oh. You haven't seen the news. And you don't care. Well, then.
                return true;
            case 5100:
                // $script:0831180509003881$ 
                // - A while back, I was practicing my singing when someone banged at the door. I guess I was a little too loud.
                // $script:0831180509003882$ 
                // - Still, even if it was just practice, I mean, it was me. It should've sounded amazing.
                // $script:0831180509003883$ 
                // - Maybe that's why she didn't yell. She just glanced around the house one time, then left.
                return true;
            case 6000:
                // $script:0831180509003884$ 
                // - Before I got my big break, there was this girl I liked. She wanted to be a singer, too, and we practiced together.
                // $script:0831180509003885$ 
                // - We were both broke, but we'd share what little food we had, practice all night, and wait for the first bus of the day together. But then, right before our debut...
                // $script:0831180509003886$ 
                // - She fainted in the middle of practice. They rushed her to the hospital, and we found out she was really, really sick. It was her lifelong dream to sing in front of a huge audience, but...
                // $script:0831180509003887$ 
                // - She died before her dream could come true. What was supposed to be our debut just became my solo debut...
                // $script:0831180509003888$ 
                // - Why are you giving me that suspicious look? Do you know?!
                return true;
            case 7000:
                // $script:0831180509003889$ 
                // - Fine, fine! I'll confess!!
                // $script:0831180509003890$ 
                // - I'm a fraud! A big stinkin' liar!
                // $script:0831180509003891$ 
                // - Of course you figured it out, $OwnerName$. I mean, we live together!
                // $script:0831180509003892$ 
                // - I just want you to know, I'm going to tell my fans soon, I swear. But I'll say it out loud to your first.
                // $script:0831180509003893$ 
                // - Ugh, this is tough! Okay... so... the height listed in my profile... it includes the two inches of the heel of my shoes, plus two thick layers of inner soles! Aah, please don't look at me differently now!!
                return true;
            case 100:
                // $script:0831180509003894$ 
                // - How can I help you? Oh, let me put on my mask. That's better. Now, are you here to see the owner of this house?
                switch (selection) {
                    // $script:0831180509003895$
                    // - Yep!
                    case 0:
                        Id = 0; // TODO: 101,102 | 
                        return false;
                    // $script:0831180509003896$
                    // - Nope!
                    case 1:
                        Id = 0; // TODO: 103,104 | 
                        return false;
                    // $script:0831180509003897$
                    // - Who are you?
                    case 2:
                        Id = 0; // TODO: 105,106 | 
                        return false;
                }
                return true;
            case 101:
                // $script:0831180509003898$ 
                // - Really? You're not here for... me? Are you sure? Didn't we meet once at the subway station? Or maybe it was a convenience store? You wanted my autograph, right?
                return true;
            case 102:
                // $script:0831180509003899$ 
                // - Whew! I'm so, so, so glad you didn't recognize me! Huh? What? I didn't say anything!
                return true;
            case 103:
                // $script:0831180509003900$ 
                // - Ah, so you're a fan? How did you find me? Haha, I can give you an autograph, but please, no pictures. I don't have my make-up on.
                return true;
            case 104:
                // $script:0831180509003901$ 
                // - If you're not here for that then... Wait, wait. I got it. You're from a hidden camera show, aren't you? Hah hah, good one. All right, where's the camera?
                return true;
            case 105:
                // $script:0831180509003902$ 
                // - That's a secret. It's better if you don't know. I'm sorry I sang so loudly and excellently that you couldn't help but barge in to see my beautiful face, but... well... okay, one autograph won't hurt.
                return true;
            case 106:
                // $script:0831180509003903$ 
                // - Excuse me?! You... don't know? Do you live under a rock or something? Hmph.
                return true;
            default:
                return true;
        }
    }
}
