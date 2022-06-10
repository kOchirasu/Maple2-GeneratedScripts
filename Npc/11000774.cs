using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000774: Mino
/// </summary>
public class _11000774 : NpcScript {
    internal _11000774(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 1;2;3;4;5;6;9001;9002;9003;100
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180509002784$ 
                // - Hey, what's up?
                return true;
            case 1:
                // $script:0831180509002785$ 
                // - Hey, you're back.
                switch (selection) {
                    // $script:0831180509002786$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509002787$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002788$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 2:
                // $script:0831180509002789$ 
                // - On days like this, I love to chill with friendly folks on the street. You?
                switch (selection) {
                    // $script:0831180509002790$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509002791$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002792$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 3:
                // $script:0831180509002793$ 
                // - Welcome back, $OwnerName$. Things went well, I take it?
                switch (selection) {
                    // $script:0831180509002794$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509002795$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002796$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 4:
                // $script:0831180509002797$ 
                // - Hey, you're back.
                switch (selection) {
                    // $script:0831180509002798$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509002799$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002800$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509002801$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 5:
                // $script:0831180509002802$ 
                // - On days like this, I love to chill with friendly folks on the street. You?
                switch (selection) {
                    // $script:0831180509002803$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509002804$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002805$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509002806$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 6:
                // $script:0831180509002807$ 
                // - Welcome back, $OwnerName$. Things went well, I take it?
                switch (selection) {
                    // $script:0831180509002808$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509002809$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002810$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509002811$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 9:
                // $script:0831180509002812$ 
                // - Is it time for my paycheck?
                //   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
                switch (selection) {
                    // $script:0831180509002813$
                    // - Let me think about it some more.
                    case 0:
                        Id = 0; // TODO: 8040,8050,8060,9040 | 8999
                        return false;
                    // $script:0831180509002814$
                    // - (Pay $MaidSalary$.)
                    case 1:
                        Id = 0; // TODO: 8000,8001,8010,8011,8901 | 8900,8910
                        return false;
                }
                return true;
            case 8000:
                // $script:0831180509002815$ functionID=1 
                // - Nah, I'm happy to share your burden.
                return true;
            case 8001:
                // $script:0831180509002816$ functionID=1 
                // - My muse is knocking. I need to go answer.
                return true;
            case 8010:
                // $script:0831180509002817$ functionID=1 
                // - Nah, I'm happy to share your burden.
                return true;
            case 8011:
                // $script:0831180509002818$ functionID=1 
                // - My muse is knocking. I need to go answer.
                return true;
            case 8020:
                // $script:0831180509002819$ functionID=1 
                // - Our contract is up soon, $OwnerName$. 
                return true;
            case 8021:
                // $script:0831180509002820$ functionID=1 
                // - Write it down or something, and free your mind to think about something else.
                switch (selection) {
                    // $script:0831180509002821$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509002822$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002823$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509002824$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8040:
                // $script:0831180509002825$ 
                // - Is there something you want to say?
                switch (selection) {
                    // $script:0831180509002826$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509002827$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002828$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509002829$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8050:
                // $script:0831180509002830$ 
                // - You wanna chat? Was there something you wanted to ask me?
                switch (selection) {
                    // $script:0831180509002831$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509002832$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002833$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509002834$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8060:
                // $script:0831180509002835$ 
                // - Haven't we been talking this whole time? Or is my memory playing tricks on me again...
                switch (selection) {
                    // $script:0831180509002836$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509002837$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002838$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509002839$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8900:
                // $script:0831180509002840$ 
                // - Thanks, but you don't have to try so hard. I can wait until you can really afford it. Just roll with the punches, know what I mean?
                return true;
            case 8901:
                // $script:0831180509002841$ 
                // - In your heart, can you feel it? Can you feel that you already paid me this month? It's like a poem, deep inside you.
                return true;
            case 8910:
                // $script:0831180509002842$ 
                // - Thanks, but you don't have to try so hard. I can wait until you can really afford it. Just roll with the punches, know what I mean?
                return true;
            case 8999:
                // $script:0831180509002843$ 
                // - Sure, sure, I can wait. We can always talk about something else.
                return true;
            case 9001:
                // $script:0831180509002844$ 
                // - Take responsibility, you know? Don't blame someone else.
                switch (selection) {
                    // $script:0831180509002845$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509002846$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002847$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9002:
                // $script:0831180509002848$ 
                // - Nothing in this world lasts forever.
                switch (selection) {
                    // $script:0831180509002849$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509002850$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002851$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9003:
                // $script:0831180509002852$ 
                // - Why do words float in the air after they leave my mouth?
                switch (selection) {
                    // $script:0831180509002853$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509002854$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002855$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9010:
                // $script:0831180509002856$ 
                // - My contract expired. You might think it's freeing not to have any constraints, but the best art is made in the most rigid conditions. It forces your creativity to break through. Please renew my contract.
                return true;
            case 9011:
                // $script:0831180509002857$ functionID=1 
                // - My contract expired. You might think it's freeing not to have any constraints, but the best art is made in the most rigid conditions. It forces your creativity to break through. Please renew my contract.
                return true;
            case 9020:
                // $script:0831180509002858$ functionID=1 
                // - Just $MaidPassedDay$ ago, were sharing one vision. I wonder why that changed...
                return true;
            case 9021:
                // $script:0831180509002859$ functionID=1 
                // - I wish you were more honest with me.
                switch (selection) {
                    // $script:0831180509002860$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509002861$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002862$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9040:
                // $script:0831180509002863$ 
                // - Are you really there? 
                switch (selection) {
                    // $script:0831180509002864$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509002865$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002866$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9030:
                // $script:0831180509002867$ 
                // - We grew apart $MaidPassedDay$ ago. It's nobody's fault. These things happen. But there just wasn't any closure, you know?
                return true;
            case 9031:
                // $script:0831180509002868$ 
                // - My soul can't be measured by something as materialistic as wages, but I made a pledge to Helping Hands. I can't serve without being paid. That was the price I had to pay to meet my soul mate: you. I thought we were on the same page with all that, but maybe I was wrong.
                return true;
            case 9032:
                // $script:0831180509002869$ 
                // - My muse stopped by today. I wanted to let her pour over me, but I couldn't. You get what I'm saying?
                return true;
            case 10:
                // $script:0831180509002870$ functionID=1 
                // - The muse makes my heart float and sink at the same time. I have to let both of those feeling flow over me.
                return true;
            case 11:
                // $script:0831180509002871$ functionID=1 
                // - You don't really get what I'm saying, do you?
                return true;
            case 20:
                // $script:0831180509002872$ functionID=1 
                // - Don't ask too many questions.
                return true;
            case 21:
                // $script:0831180509002873$ functionID=1 
                // - I have to look in the mirror once in a while, or else I forget what I look like.
                switch (selection) {
                    // $script:0831180509002874$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509002875$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002876$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 22:
                // $script:0831180509002877$ functionID=1 
                // - I have to look in the mirror once in a while, or else I forget what I look like.
                switch (selection) {
                    // $script:0831180509002878$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509002879$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002880$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509002881$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 30:
                // $script:0831180509002882$ 
                // - We can talk for as long as you want. I needed a break, anyway.
                switch (selection) {
                    // $script:0831180509002883$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,2000,2100,9011 | 
                        return false;
                    // $script:0831180509002884$
                    // - (Praise your servant.)
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,9011 | 
                        return false;
                    // $script:0831180509002885$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,6100,7000,9011 | 
                        return false;
                    // $script:0831180509002886$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 31:
                // $script:0831180509002887$ 
                // - Ah, good conversation is always welcome, and I always enjoy talking to you, $OwnerName$.
                switch (selection) {
                    // $script:0831180509002888$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,2000,2100,9011 | 
                        return false;
                    // $script:0831180509002889$
                    // - (Praise your servant.)
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,9011 | 
                        return false;
                    // $script:0831180509002890$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,6100,7000,9011 | 
                        return false;
                    // $script:0831180509002891$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 32:
                // $script:0831180509002892$ 
                // - The truth of the universe breathes inside every one of us.
                switch (selection) {
                    // $script:0831180509002893$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,2000,2100,9011 | 
                        return false;
                    // $script:0831180509002894$
                    // - (Praise your servant.)
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,9011 | 
                        return false;
                    // $script:0831180509002895$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,6100,7000,9011 | 
                        return false;
                    // $script:0831180509002896$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 40:
                // $script:0831180509002897$ 
                // - Is there something you want to say?
                switch (selection) {
                    // $script:0831180509002898$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509002899$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002900$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 50:
                // $script:0831180509002901$ 
                // - You wanna chat? Was there something you wanted to ask me? Or maybe... you're also drawn to the same mysterious power...
                switch (selection) {
                    // $script:0831180509002902$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509002903$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002904$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 60:
                // $script:0831180509002905$ 
                // - Haven't we been talking this whole time? Or is my memory playing tricks on me again...
                switch (selection) {
                    // $script:0831180509002906$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509002907$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002908$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 1000:
                // $script:0831180509002909$ 
                // - I've decided that today is the combination of sensitivity and specialty.
                // $script:0831180509002910$ 
                // - More intense than yesterday, and more thrilling than tomorrow. Or just possible, the opposite.
                switch (selection) {
                    // $script:0831180509002911$
                    // - (Say that you feel the same way sometimes.)
                    case 0:
                        Id = 0; // TODO: 1011,1012 | 
                        return false;
                    // $script:0831180509002912$
                    // - (Say nothing.)
                    case 1:
                        Id = 0; // TODO: 1001,1002 | 
                        return false;
                }
                return true;
            case 1001:
                // $script:0831180509002913$ functionID=1 
                // - From the look on your face... Mm, I'm not going to ask. I can feel the intensity radiating off of you.
                return true;
            case 1002:
                // $script:0831180509002914$ functionID=1 
                // - Why does it feel as if you're so far away when you're right in front of me? Every time we talk, I feel so alone.
                return true;
            case 1011:
                // $script:0831180509002915$ functionID=1 
                // - I can be honest when I'm with you. You make me feel like a child without a care in the world. It's been a long time since I felt this way...
                return true;
            case 1012:
                // $script:0831180509002916$ functionID=1 
                // - It's not easy to be who you are. For some reason, I feel better now. Will you tell me more about yourself?
                return true;
            case 1100:
                // $script:0831180509002917$ 
                // - I entrusted my soul to music a while back, in a desperate attempt to forget the anguish of life. 
                // $script:0831180509002918$ 
                // - You should try to face your inner self sometimes. Here, take this earphone and put it in your ear.
                // $script:0831180509002919$ 
                // - Now, close your eyes and get lost in the darkness. There! Our souls resonated with each other! Did you feel that?
                switch (selection) {
                    // $script:0831180509002920$
                    // - No...
                    case 0:
                        Id = 0; // TODO: 1101,1102 | 
                        return false;
                    // $script:0831180509002921$
                    // - Yes!
                    case 1:
                        Id = 0; // TODO: 1111,1112 | 
                        return false;
                }
                return true;
            case 1101:
                // $script:0831180509002922$ functionID=1 
                // - It's not your fault. It just means our relationship is not as deep as I thought it was.
                return true;
            case 1102:
                // $script:0831180509002923$ functionID=1 
                // - Heh. You did? So did I.
                return true;
            case 1111:
                // $script:0831180509002924$ functionID=1 
                // - Heh. Feels kind of strange, but I like it. Let's just stay like this for a while.
                return true;
            case 1112:
                // $script:0831180509002925$ functionID=1 
                // - <font color="#909090">(He nods his head to the beat.)</font>
                //   Yeah this is it.
                return true;
            case 2000:
                // $script:0831180509002926$ 
                // - This was such an amazing moment. Not sure if you'd agree...?
                // $script:0831180509002927$ 
                // - Today it drizzled, just a bit, but it was enough to quench my heart's thirst.
                // $script:0831180509002928$ 
                // - I haven't felt this way for a long time... Maybe I still have some warmth left in me. I feel... hopeful.
                return true;
            case 2100:
                // $script:0831180509002929$ 
                // - I saw the guy next door come home in a helicopter, and that changed my whole perception of him. Interesting, huh?
                // $script:0831180509002930$ 
                // - Sure, I'd love to ride in a helicopter someday. Maybe my tired soul can finally take a breath, hundreds of miles above the world.
                return true;
            case 2200:
                // $script:0831180509002931$ 
                // - Today, I met a girl who lives in the neighborhood. She inspired me to pick up scissors for the first time in a long time. Not many folks "get" my art style, you know?
                // $script:0831180509002932$ 
                // - I wonder if the tears I shed after that last snip were were of joy or yearning...
                // $script:0831180509002933$ 
                // - That look on your face... Mm, you still don't understand me, do you? It's cool. An appreciation of true art isn't something that can be acquired. It's something you've got to be born with.
                return true;
            case 3000:
                // $script:0831180509002934$ 
                // - How's it going? You look like you're about to burst with excitement. What's the news?
                // $script:0831180509002935$ functionID=1 
                // - Don't know why, but I've got a hunch today is going to be an exciting day for me, too.
                return true;
            case 3100:
                // $script:0831180509002936$ 
                // - Thank you for your kindness, but I don't know if I have a place for it in my heart.
                // $script:0831180509002937$ functionID=1 
                // - Don't be upset, $OwnerName$. It's not your fault. This is a problem that only I can solve.
                return true;
            case 4000:
                // $script:0831180509002938$ 
                // - I appreciate that, but you don't have to keep telling me. Sometimes words mean more when they're not spoken, you hear me?
                // $script:0831180509002939$ 
                // - I get if you don't get it. I'm a deep guy with so many layers. Don't force yourself. We'll solve this puzzle together.
                return true;
            case 4100:
                // $script:0831180509002940$ 
                // - I don't mind feeling this way. I assume this is how ordinary people feel all the time.
                // $script:0831180509002941$ 
                // - But for me... Let's just say it'll take a while to get used to this.
                return true;
            case 5000:
                // $script:0831180509002942$ 
                // - When it's sunny and there's not much to do, I go out for a walk. Not to take a break, but just to look normal, like everyone else.
                // $script:0831180509002943$ 
                // - $OwnerName$, how does taking a walk make you feel? For me, let's just say it calms the darkness inside me.
                // $script:0831180509002944$ 
                // - Don't take it personally, but... I don't want to take a walk with you. I've reserved that time to spend with me, you know? So I can't share it with anybody else.
                return true;
            case 5100:
                // $script:0831180509002945$ 
                // - Why do I use left-handed scissors with my right hand? I'm surprised you even noticed.
                // $script:0831180509002946$ 
                // - You may not understand this, but I'm not the one who chooses that. When I touch someone's hair, I get a feeling deep inside, and that feeling determines which hand I use to cut with.
                // $script:0831180509002947$ 
                // - Come to think of it, I haven't held these scissors with my left hand for a long time. Only fate knows when I'll do that again. To be honest, right now, I'm just too tired to think about it.
                return true;
            case 6000:
                // $script:0831180509002948$ 
                // - Sometimes, I just like wearing earphones, without listening to anything.
                // $script:0831180509002949$ 
                // - I do it when I want to be left alone, so I can have some time with myself.
                // $script:0831180509002950$ 
                // - You don't get it, do you, $OwnerName$? It's okay. I'm used to not being understood.
                // $script:0831180509002951$ 
                // - Of course, I have my favorites when it comes to music. I'll play some for you when I have a chance. It'll help you understand where I get my inspiration.
                return true;
            case 7000:
                // $script:0831180509002952$ 
                // - $OwnerName$, do you have any siblings? I've never told anyone but... I actually have an older brother.
                // $script:0831180509002953$ 
                // - I left home when I was pretty young. He used to send me letters, but it's been a long, long time since the last one.
                // $script:0831180509002954$ 
                // - I picked this place partly because it's bustling with activity and partly because my brother mailed his last letter from somewhere around here.
                // $script:0831180509002955$ 
                // - Recently, I met an adventurer who I think traveled with my brother for a while. I couldn't be sure, though.
                // $script:0831180509002956$ 
                // - According to him, my brother is doing fine. I don't know what happened to him, but I'm hoping to rn into here one day.
                return true;
            case 100:
                // $script:0831180509002957$ 
                // - Weren't you just here yesterday? You looking for the owner?
                switch (selection) {
                    // $script:0831180509002958$
                    // - Yep!
                    case 0:
                        Id = 0; // TODO: 101,102 | 
                        return false;
                    // $script:0831180509002959$
                    // - Nope!
                    case 1:
                        Id = 0; // TODO: 103,104 | 
                        return false;
                    // $script:0831180509002960$
                    // - Who are you?
                    case 2:
                        Id = 0; // TODO: 105,106 | 
                        return false;
                }
                return true;
            case 101:
                // $script:0831180509002961$ 
                // - Well, then, look around. See what you can find.
                return true;
            case 102:
                // $script:0831180509002962$ 
                // - Not many people come to visit. You must be really close.
                return true;
            case 103:
                // $script:0831180509002963$ 
                // - Then did you come to see me? I wanted to stay on the down low, but I know it's impossible when I'm so popular.
                return true;
            case 104:
                // $script:0831180509002964$ 
                // - If you want, you can stay for a little while. Just don't be alarmed if your energy starts to resonate with mine.
                return true;
            case 105:
                // $script:0831180509002965$ 
                // - If you want, I can tell you, but if we're connected by the red string of fate, knowing each other's name is meaningless.
                return true;
            case 106:
                // $script:0831180509002966$ 
                // - I can tell you my name. It's $MaidName$. Nothing else about me can be described in words.
                return true;
            default:
                return true;
        }
    }
}
