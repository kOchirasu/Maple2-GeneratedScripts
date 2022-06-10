using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000769: Manu
/// </summary>
public class _11000769 : NpcScript {
    internal _11000769(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 1;2;3;4;5;6;9001;9002;9003;100
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180509001629$ 
                // - How may I help you? 
                return true;
            case 1:
                // $script:0831180509001630$ 
                // - Did you call me, $OwnerName$? 
                switch (selection) {
                    // $script:0831180509001631$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001632$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001633$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 2:
                // $script:0831180509001634$ 
                // - Have a great day, $OwnerName$! 
                switch (selection) {
                    // $script:0831180509001635$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001636$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001637$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 3:
                // $script:0831180509001638$ 
                // - Yes, $OwnerName$? 
                switch (selection) {
                    // $script:0831180509001639$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001640$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001641$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 4:
                // $script:0831180509001642$ 
                // - Did you call me, $OwnerName$? 
                switch (selection) {
                    // $script:0831180509001643$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001644$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001645$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509001646$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 5:
                // $script:0831180509001647$ 
                // - Have a great day, $OwnerName$! 
                switch (selection) {
                    // $script:0831180509001648$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001649$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001650$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509001651$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 6:
                // $script:0831180509001652$ 
                // - Yes, $OwnerName$? 
                switch (selection) {
                    // $script:0831180509001653$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001654$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001655$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509001656$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 9:
                // $script:0831180509001657$ 
                // - Mm? Are you going to pay me?
<b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b> 
                switch (selection) {
                    // $script:0831180509001658$
                    // - Never mind.
                    case 0:
                        Id = 0; // TODO: 8040,8050,8060,9040 | 8999
                        return false;
                    // $script:0831180509001659$
                    // - (Pay $MaidSalary$.)
                    case 1:
                        Id = 0; // TODO: 8000,8001,8010,8011,8901 | 8900,8910
                        return false;
                }
                return true;
            case 8000:
                // $script:0831180509001660$ functionID=1 
                // - Oh, I'm so glad you found me useful. Thank you for extending our contract. I'm happy to stay with you for another month. 
                return true;
            case 8001:
                // $script:0831180509001661$ functionID=1 
                // - Hah hah hah, it feels great to get paid for my work work. Thank you. 
                return true;
            case 8010:
                // $script:0831180509001662$ functionID=1 
                // - Ah, this explains your cheerful mood. What's good for you is good for me, and vice versa. That's what friends are for, right? To share in each other's happiness. 
                return true;
            case 8011:
                // $script:0831180509001663$ functionID=1 
                // - Ah, I know I said everything was fine, but it really wasn't. I didn't want to tell you the truth, because I knew it was harder on you than it was on me. I'm glad everything worked out! Hah hah! 
                return true;
            case 8020:
                // $script:0831180509001664$ functionID=1 
                // - In case you've forgotten, our contract expires soon. I know it's not easy keeping track of everything going on in your life. 
                return true;
            case 8021:
                // $script:0831180509001665$ functionID=1 
                // - But that's what I'm here for. Hah hah. 
                switch (selection) {
                    // $script:0831180509001666$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001667$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001668$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509001669$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8040:
                // $script:0831180509001670$ 
                // - You can tell me anything. 
                switch (selection) {
                    // $script:0831180509001671$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001672$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001673$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509001674$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8050:
                // $script:0831180509001675$ 
                // - Sometimes, I feel lonely when I'm by myself. 
                switch (selection) {
                    // $script:0831180509001676$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001677$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001678$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509001679$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8060:
                // $script:0831180509001680$ 
                // - Yikes... My back's killing me today...  
                switch (selection) {
                    // $script:0831180509001681$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001682$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001683$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509001684$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8900:
                // $script:0831180509001685$ 
                // - Oh, aren't you a bit short on funds right now? Thank you for at least trying to pay me. I'm sure you'll get some mesos soon, so don't feel too bad. Hah hah hah. 
                return true;
            case 8901:
                // $script:0831180509001686$ 
                // - You want to pay me? But you've already paid me for the month. You're as forgetful as I am sometimes. 
                return true;
            case 8910:
                // $script:0831180509001687$ 
                // - You've got nothing but dust in your pockets. I kind of knew this was the case. It's all right. Don't you worry about this old man...  
                return true;
            case 8999:
                // $script:0831180509001688$ 
                // - Hm, strange things happen all the time. Don't panic. Calm yourself and try again. 
                return true;
            case 9001:
                // $script:0831180509001689$ 
                // - Aww... Why do you look so exhausted?  
                switch (selection) {
                    // $script:0831180509001690$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509001691$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001692$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9002:
                // $script:0831180509001693$ 
                // - The older you get, the less food your body needs. 
                switch (selection) {
                    // $script:0831180509001694$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509001695$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001696$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9003:
                // $script:0831180509001697$ 
                // - Having nothing to do is so dull. It's been $MaidPassedDay$ since I've had a job. 
                switch (selection) {
                    // $script:0831180509001698$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509001699$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001700$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9010:
                // $script:0831180509001701$ 
                // - Ah, if we could take a moment to talk about my contract... I believe it's expired. 
                return true;
            case 9011:
                // $script:0831180509001702$ functionID=1 
                // - Sure, but if we could take a moment to talk about my contract... I believe it's expired. 
                return true;
            case 9020:
                // $script:0831180509001703$ functionID=1 
                // - I told you not to worry about me. Everything will work out eventually. 
                return true;
            case 9021:
                // $script:0831180509001704$ functionID=1 
                // - The power of positive thinking, right? Hah hah.  
                switch (selection) {
                    // $script:0831180509001705$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509001706$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001707$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9040:
                // $script:0831180509001708$ 
                // - I don't think I can go for a walk today. My knees are aching...  
                switch (selection) {
                    // $script:0831180509001709$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509001710$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001711$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9030:
                // $script:0831180509001712$ 
                // - When the wind becomes overwhelming, mimic the reeds. Follow the wind without losing your footing. Hah hah hah, are you thinking I've finally lost my mind? I just thought you could use some encouragement. 
                return true;
            case 9031:
                // $script:0831180509001713$ 
                // - I miss my wife. When things got tough for us, like they are for your now, Madelle helped me get through it. What I'm trying to say is, I may not be able to do much, but I'm here for you. 
                return true;
            case 9032:
                // $script:0831180509001714$ 
                // - Everyone should experience poverty at least once. It gives you perspective. Once you've climbed a cliff, even the steepest hill is no longer intimidating. 
                return true;
            case 10:
                // $script:0831180509001715$ functionID=1 
                // - Ask me for anything. I'll make it for you if I can. 
                return true;
            case 11:
                // $script:0831180509001716$ functionID=1 
                // - Don't worry about it. I'm doing this to pass time. 
                return true;
            case 20:
                // $script:0831180509001717$ functionID=1 
                // - Do you have questions for me? 
                return true;
            case 21:
                // $script:0831180509001718$ functionID=1 
                // - Hm, it's not easy to describe oneself in just a few words.  
                switch (selection) {
                    // $script:0831180509001719$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001720$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001721$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 22:
                // $script:0831180509001722$ functionID=1 
                // - Hm, it's not easy to describe oneself in just a few words.  
                switch (selection) {
                    // $script:0831180509001723$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001724$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001725$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509001726$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 30:
                // $script:0831180509001727$ 
                // - I love talking to people. 
                switch (selection) {
                    // $script:0831180509001728$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,1200,1300,1400,1500,1600,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509001729$
                    // - Tell me a story!
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,4200,4300,9011 | 
                        return false;
                    // $script:0831180509001730$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509001731$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 31:
                // $script:0831180509001732$ 
                // - Oh, you want to keep this old man company? 
                switch (selection) {
                    // $script:0831180509001733$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,1200,1300,1400,1500,1600,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509001734$
                    // - Tell me a story!
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,4200,4300,9011 | 
                        return false;
                    // $script:0831180509001735$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509001736$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 32:
                // $script:0831180509001737$ 
                // - What kind of story? Is there something in particular you want to hear? 
                switch (selection) {
                    // $script:0831180509001738$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,1200,1300,1400,1500,1600,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509001739$
                    // - Tell me a story!
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,4200,4300,9011 | 
                        return false;
                    // $script:0831180509001740$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509001741$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 40:
                // $script:0831180509001742$ 
                // - You can tell me anything. 
                switch (selection) {
                    // $script:0831180509001743$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001744$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001745$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 50:
                // $script:0831180509001746$ 
                // - Sometimes, I feel lonely when I'm by myself. 
                switch (selection) {
                    // $script:0831180509001747$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001748$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001749$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 60:
                // $script:0831180509001750$ 
                // - Yikes... My back's killing me today...  
                switch (selection) {
                    // $script:0831180509001751$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001752$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001753$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 1000:
                // $script:0831180509001754$ 
                // - Oh, I almost forgot. 
                // $script:0831180509001755$ 
                // - It felt so strange cooking for the first time in decades. Worse, everything was so blurry I could hardly tell the difference between sugar and salt. 
                // $script:0831180509001756$ 
                // - So I just used the first thing I grabbed. Turns out, it was the wrong one. But you looked hungry, so here it is! 
                switch (selection) {
                    // $script:0831180509001757$
                    // - It's too salty.
                    case 0:
                        Id = 0; // TODO: 1001,1002 | 
                        return false;
                    // $script:0831180509001758$
                    // - It's delicious.
                    case 1:
                        Id = 0; // TODO: 1011,1012 | 
                        return false;
                }
                return true;
            case 1001:
                // $script:0831180509001759$ functionID=1 
                // - Is it? Then please spit it out. This is your house and I'm your employee. You don't have to eat it if you don't want to. 
                return true;
            case 1002:
                // $script:0831180509001760$ functionID=1 
                // - Consuming too much salt makes you thirsty, which leads to drinking too much water, which leads to swelling in your face. So you should stop eating the food. 
                return true;
            case 1011:
                // $script:0831180509001761$ functionID=1 
                // - Hah hah hah, I know I'm not a good cook. Thank you for saying that. 
                return true;
            case 1012:
                // $script:0831180509001762$ functionID=1 
                // - When you're hungry, anything you eat tastes good. Hah hah hah, slow down. No one's going to fight you for that. 
                return true;
            case 1100:
                // $script:0831180509001763$ 
                // - Guess what I have in my hand...? 
                // $script:0831180509001764$ 
                // - Snacks! I thought you might be hungry. 
                // $script:0831180509001765$ 
                // - It tastes better than it looks. I hope. 
                switch (selection) {
                    // $script:0831180509001766$
                    // - Great! I was feeling a little hungry!
                    case 0:
                        Id = 0; // TODO: 1111,1112 | 
                        return false;
                    // $script:0831180509001767$
                    // - I'll pass. I'm, um, trying to lose weight. Yeah.
                    case 1:
                        Id = 0; // TODO: 1101,1102 | 
                        return false;
                }
                return true;
            case 1101:
                // $script:0831180509001768$ functionID=1 
                // - Why? You're nothing but skin and bone. You look like you could blow away in the wind. Come on, just eat it. 
                return true;
            case 1102:
                // $script:0831180509001769$ functionID=1 
                // - Are you? Being overweight can cause diabetes, high blood pressure, hardening of the arteries, and other chronic diseases. Hm, should I be worried? 
                return true;
            case 1111:
                // $script:0831180509001770$ functionID=1 
                // - Hah hah hah, that's why I've made this! When you're my age, you get to read people more easily. 
                return true;
            case 1112:
                // $script:0831180509001771$ functionID=1 
                // - Do you get always get hungry around this time? Because I do. 
                return true;
            case 1200:
                // $script:0831180509001772$ 
                // - I was visiting the senior center today, and someone gave me this drink. I thought you might like it. 
                // $script:0831180509001773$ 
                // - When you get to be my age, you already know what you like and don't want to try new things. 
                switch (selection) {
                    // $script:0831180509001774$
                    // - Aw, you should try it. You might like it.
                    case 0:
                        Id = 0; // TODO: 1201,1202 | 
                        return false;
                    // $script:0831180509001775$
                    // - Hey, thanks!
                    case 1:
                        Id = 0; // TODO: 1211,1212 | 
                        return false;
                }
                return true;
            case 1201:
                // $script:0831180509001776$ functionID=1 
                // - No, thank you. New food stopped tasting good to me some time ago. At first, it all tasted disgusting, but now it just doesn't taste like anything. 
                return true;
            case 1202:
                // $script:0831180509001777$ functionID=1 
                // - I'll be happy just to watch you drink it. Go on, take it. 
                return true;
            case 1211:
                // $script:0831180509001778$ functionID=1 
                // - The person who gave it to me said it's very nutritious. If you like it, let me know. I can ask him for more. 
                return true;
            case 1212:
                // $script:0831180509001779$ functionID=1 
                // - I'm so glad you accepted it. I would've felt awkward if you said refused. 
                return true;
            case 1300:
                // $script:0831180509001780$ 
                // - I cooked some food my wife used to make. I never watched her cook, though. 
                // $script:0831180509001781$ 
                // - It tastes like its missing something, but I can't quite put my finger on it... What do you think? 
                switch (selection) {
                    // $script:0831180509001782$
                    // - Hmm, not bad, but could use a sprinkle of MSG.
                    case 0:
                        Id = 0; // TODO: 1301,1302 | 
                        return false;
                    // $script:0831180509001783$
                    // - It's pretty delicious just the way it is.
                    case 1:
                        Id = 0; // TODO: 1311,1312 | 
                        return false;
                }
                return true;
            case 1301:
                // $script:0831180509001784$ functionID=1 
                // - Hmm? MSG? I'll just use a pinch, and... Mm, mm! Yes, now it tastes perfect! 
                return true;
            case 1302:
                // $script:0831180509001785$ functionID=1 
                // - Hmmm, why don't you try tasting it again in a little bit and let me know what you think then? 
                return true;
            case 1311:
                // $script:0831180509001786$ functionID=1 
                // - I'm glad you're not a picky eater, $OwnerName$. Thank you for eating everything I cook for you. 
                return true;
            case 1312:
                // $script:0831180509001787$ functionID=1 
                // - You may think so, but I can tell something is missing. I should've asked my wife when I could... It's just another one of the many, many things I miss about her. 
                return true;
            case 1400:
                // $script:0831180509001788$ 
                // - Tsk, you should be more careful. I found this by the front door on my way out. 
                // $script:0831180509001789$ 
                // - Usually, I can't see far enough to notice an item on the ground, but lucky for you, I had to adjust my shoes. 
                switch (selection) {
                    // $script:0831180509001790$
                    // - Thanks for finding it.
                    case 0:
                        Id = 0; // TODO: 1411,1412 | 
                        return false;
                    // $script:0831180509001791$
                    // - It's not mine.
                    case 1:
                        Id = 0; // TODO: 1401,1402 | 
                        return false;
                }
                return true;
            case 1401:
                // $script:0831180509001792$ functionID=1 
                // - It's not? Some stranger barged into the house the other day. Maybe he dropped it. I'd better keep it in case he comes back. 
                return true;
            case 1402:
                // $script:0831180509001793$ functionID=1 
                // - Then how did it get here? Anyway, since this is your house, the item belongs to you now, so you take it. 
                return true;
            case 1411:
                // $script:0831180509001794$ functionID=1 
                // - Happy to be of help. 
                return true;
            case 1412:
                // $script:0831180509001795$ functionID=1 
                // - You should take better care of your things. 
                return true;
            case 1500:
                // $script:0831180509001796$ 
                // - I ran into Choi the real estate agent on my way home today. One of his clients just moved to a smaller and gave him a bunch of furniture that wouldn't fit. 
                // $script:0831180509001797$ 
                // - It was way too much, but Choi didn't want to throw it out, either. He asked me to take whatever I wanted, so I grabbed this. It looked like the best of the bunch. It's all yours now! 
                switch (selection) {
                    // $script:0831180509001798$
                    // - I don't really need it...
                    case 0:
                        Id = 0; // TODO: 1501,1502 | 
                        return false;
                    // $script:0831180509001799$
                    // - Thanks!
                    case 1:
                        Id = 0; // TODO: 1511,1512 | 
                        return false;
                }
                return true;
            case 1501:
                // $script:0831180509001800$ functionID=1 
                // - Hm, then what should I do with it? I don't think Choi will take it back, and I don't want to throw it away. 
                return true;
            case 1502:
                // $script:0831180509001801$ functionID=1 
                // - Hah hah hah, I guess I shouldn't have taken it! Everyone makes mistakes, and mistakes teach you valuable lessons. Those who claim never to have made a mistake are either lying to themselves or not living life to the fullest. 
                return true;
            case 1511:
                // $script:0831180509001802$ functionID=1 
                // - So I picked something good, huh? I'm glad to be of help. 
                return true;
            case 1512:
                // $script:0831180509001803$ functionID=1 
                // - Do you need anything else? Choi had a lot of other stuff, too. 
                return true;
            case 1600:
                // $script:0831180509001804$ 
                // - Do you know what happened today? I was out walking when I ran into an overturned wagon. I helped the owner move it back into place. 
                // $script:0831180509001805$ 
                // - And he gave me money for helping him. Hah hah hah! Here, take it. I've got no use for so much money. Think of it as an allowance from your grandpa. 
                switch (selection) {
                    // $script:0831180509001806$
                    // - Hey, thanks!
                    case 0:
                        Id = 0; // TODO: 1611,1612 | 
                        return false;
                    // $script:0831180509001807$
                    // - I can't take your money!
                    case 1:
                        Id = 0; // TODO: 1601,1602 | 
                        return false;
                }
                return true;
            case 1601:
                // $script:0831180509001808$ functionID=1 
                // - It was easy money. Come on, I insist. 
                return true;
            case 1602:
                // $script:0831180509001809$ functionID=1 
                // - I wouldn't have offered it if I didn't care about you. The greatest happiness in life comes from knowing that you're being loved. This may not be the best way to show it, but I'm quite fond of you. 
                return true;
            case 1611:
                // $script:0831180509001810$ functionID=1 
                // - What a great day! I got to help someone, get free money, and give you an allowance! Hah! 
                return true;
            case 1612:
                // $script:0831180509001811$ functionID=1 
                // - Hah hah hah, how wonderful! Oof, I'm aching all over now. I'll probably spend more on pain medicine than I earned... 
                return true;
            case 2000:
                // $script:0831180509001812$ 
                // - Not much. I worked around the house all day. 
                // $script:0831180509001813$ 
                // - A writer once said the people weren't born to work. If we were, it wouldn't make us so tired. 
                // $script:0831180509001814$ 
                // - I agree with him, now that I know how tiresome housework really is. 
                return true;
            case 2100:
                // $script:0831180509001815$ 
                // - I was thinking of my wife while I cleaned today. She used to hum when she did her chores. 
                // $script:0831180509001816$ 
                // - So I tried that today. It actually lifted my spirits and made the work less boring. 
                return true;
            case 2200:
                // $script:0831180509001817$ 
                // - Nothing happened to me or the house, but... 
                // $script:0831180509001818$ 
                // - I met Choi the real estate agent while taking a walk. He said he saw someone hanging onto a flying eagle. 
                // $script:0831180509001819$ 
                // - I don't know why he makes such absurd claims sometimes. It would've been more believable if he said he saw someone hanging onto a balloon. Hah hah. 
                return true;
            case 3000:
                // $script:0831180509001820$ 
                // - While I was grocery shopping, I saw the comedian who plays the fool on that popular TV show. The kids there were copying his character and laughing at him. 
                // $script:0831180509001821$ functionID=1 
                // - A great comedy writer once said, "The toughest role in comedy is the fool, and playing it requires a genius." 
                return true;
            case 3100:
                // $script:0831180509001822$ 
                // - I was watching a TV quiz show this morning. There were three doors. Two of them had a goat behind them, and the third had an expensive mount. The contestant didn't know which was which, of course. 
                // $script:0831180509001823$ functionID=1 
                // - So he picked a door. The host opened one of the other doors to reveal a goat. He then asked the contestant if he wanted to change his choice. What would you do if it were you? 
                return true;
            case 4000:
                // $script:0831180509001824$ 
                // - I'm not a funny person, and I don't know any funny stories. Hah hah hah. But I know how to keep people engaged in what I'm saying, and that's to tell them what I think of them. 
                // $script:0831180509001825$ 
                // - I can tell you what I think of you, if you want. Oh, your ears are already perking up! Hah hah! 
                return true;
            case 4100:
                // $script:0831180509001826$ 
                // - Once upon a time...
...
... 
                // $script:0831180509001827$ 
                // - Are you asleep? 
                return true;
            case 5000:
                // $script:0831180509001828$ 
                // - You want to ask me something personal? 
                // $script:0831180509001829$ 
                // - We all are like the moon: each one of us has a dark side that we don't want to show others. 
                // $script:0831180509001830$ 
                // - If you're asking about my dark side, I'd rather not talk about it. Let's talk about yours instead. I'm all ears. 
                // $script:0831180509001831$ 
                // - You've been all over Victoria Island. Which part do you like the most? 
                // $script:0831180509001832$ 
                // - I don't care if you go anywhere else, but please don't go to $map:2000124$. 
                return true;
            case 5100:
                // $script:0831180509001833$ 
                // - One morning I woke up to realize that all my desire for worldly wealth had vanished overnight. Everything here is fleeting. 
                // $script:0831180509001834$ 
                // - The realization that the years you have left are fewer than the years you've already lived does that to you. 
                // $script:0831180509001835$ 
                // - An old scholar once said man's purpose is to make meaningless things meaningful. I'd better live whatever life I have left to the fullest, so I can die without regrets. 
                // $script:0831180509001836$ 
                // - I really like this job. When my wife passed, I was so heartbroken that I didn't want to do anything for a long, long time. 
                // $script:0831180509001837$ 
                // - Then I realized living in the past was doing me more harm than good. 
                // $script:0831180509001838$ 
                // - So I decided to let the past go, enjoy the present, and wait for whatever the future brings. 
                return true;
            case 6000:
                // $script:0831180509001839$ 
                // - I started writing a while ago. But I'm not writing a novel. 
                // $script:0831180509001840$ 
                // - I'm not writing something to show others. It's just for myself. 
                // $script:0831180509001841$ 
                // - Someone once told me that writing helps you deal with difficult emotions and find happiness again. 
                // $script:0831180509001842$ 
                // - So I'm writing to be happy. Please don't be too nosy about what I'm writing. 
                // $script:0831180509001843$ 
                // - Does my writing include things about you? Well... You'll see for yourself if I decide to show you one day. 
                return true;
            case 7000:
                // $script:0831180509001844$ 
                // - You want to know about me and my wife? I can't think of anything special to say. Hah hah.  
                // $script:0831180509001845$ 
                // - It was always just the two of us, me and Madelle. We couldn't have children... That was hard for both of us. 
                // $script:0831180509001846$ 
                // - In hindsight, maybe that made us even closer. It was a pain we shared together.  
                // $script:0831180509001847$ 
                // - Am I sorry that I don't have children? No. But I miss the time I shared with my wife. 
                // $script:0831180509001848$ 
                // - Being with Madelle, I always felt warm and peaceful. We'd been together for so long that we could read each other's thoughts. But when I think about it now, I wish I had talked to her more often. 
                // $script:0831180509001849$ 
                // - Do you have someone you love? If not, I hope you find someone as good as my Madelle. 
                return true;
            case 100:
                // $script:0831180509001850$ 
                // - I didn't hear the bell ring. May I ask who you are? Are you here to see the owner of the house? 
                switch (selection) {
                    // $script:0831180509001851$
                    // - Yep!
                    case 0:
                        Id = 0; // TODO: 101,102 | 
                        return false;
                    // $script:0831180509001852$
                    // - Nope!
                    case 1:
                        Id = 0; // TODO: 103,104 | 
                        return false;
                    // $script:0831180509001853$
                    // - Who are you?
                    case 2:
                        Id = 0; // TODO: 105,106 | 
                        return false;
                }
                return true;
            case 101:
                // $script:0831180509001854$ 
                // - I work for him. If you'd like me to pass along a message... Actually, no. That was presumptuous of me. You probably want to speak in person. 
                return true;
            case 102:
                // $script:0831180509001855$ 
                // - I see. Just pretend I'm not here and make yourself at home. 
                return true;
            case 103:
                // $script:0831180509001856$ 
                // - Then what brings you here? How did you get in, anyway? Was the door open? 
                return true;
            case 104:
                // $script:0831180509001857$ 
                // - Then what brings you here? If you're here for an open house, you've got the wrong address. This home is not for sale. 
                return true;
            case 105:
                // $script:0831180509001858$ 
                // - Common courtesy would be introduce yourself first before asking, but I'll cut you some slack. I'm not a stickler for the rules anyway, hah hah. 
                return true;
            case 106:
                // $script:0831180509001859$ 
                // - I am the housekeeper. Now, may I ask who you are? 
                return true;
            default:
                return true;
        }
    }
}
