using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000770: Rina
/// </summary>
public class _11000770 : NpcScript {
    internal _11000770(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 1;2;3;4;5;6;9001;9002;9003;100
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180509001875$ 
                // - Can I help you?
                return true;
            case 1:
                // $script:0831180509001876$ 
                // - Mm? What is it, dear?
                switch (selection) {
                    // $script:0831180509001877$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001878$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001879$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 2:
                // $script:0831180509001880$ 
                // - It's a wonderful day today, isn't it?
                switch (selection) {
                    // $script:0831180509001881$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001882$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001883$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 3:
                // $script:0831180509001884$ 
                // - You're just in time, $OwnerName$. I was just sitting down to eat.
                switch (selection) {
                    // $script:0831180509001885$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001886$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001887$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 4:
                // $script:0831180509001888$ 
                // - Mm? What is it, dear?
                switch (selection) {
                    // $script:0831180509001889$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001890$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001891$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509001892$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 5:
                // $script:0831180509001893$ 
                // - It's a wonderful day today, isn't it?
                switch (selection) {
                    // $script:0831180509001894$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001895$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001896$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509001897$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 6:
                // $script:0831180509001898$ 
                // - You're just in time, $OwnerName$. I was just sitting down to eat.
                switch (selection) {
                    // $script:0831180509001899$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001900$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001901$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509001902$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 9:
                // $script:0831180509001903$ 
                // - Oh, you want to pay me?
                //   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
                switch (selection) {
                    // $script:0831180509001904$
                    // - Let me think about it some more.
                    case 0:
                        Id = 0; // TODO: 8040,8050,8060,9040 | 8999
                        return false;
                    // $script:0831180509001905$
                    // - (Pay $MaidSalary$.)
                    case 1:
                        Id = 0; // TODO: 8000,8001,8010,8011,8901 | 8900,8910
                        return false;
                }
                return true;
            case 8000:
                // $script:0831180509001906$ functionID=1 
                // - Time sure flies. Thanks for hiring me again this month, dearie.
                return true;
            case 8001:
                // $script:0831180509001907$ functionID=1 
                // - Oh, how kind of you! I didn't even have to remind you! I don't like asking for money, even if I've rightfully earned it.
                return true;
            case 8010:
                // $script:0831180509001908$ functionID=1 
                // - Whew, thank you! This means I don't have to worry anymore. Why don't I cook us some nice unagi today to celebrate?
                return true;
            case 8011:
                // $script:0831180509001909$ functionID=1 
                // - So everything's worked out? Good! Now I can cut loose! How about I treat you to a feast today to celebrate?
                return true;
            case 8020:
                // $script:0831180509001910$ functionID=1 
                // - I was looking over my books today and noticed our contract is expiring soon. Have you been so busy you've forgotten, dear?
                return true;
            case 8021:
                // $script:0831180509001911$ functionID=1 
                // - You did, didn't you? I knew it! Tsk.
                switch (selection) {
                    // $script:0831180509001912$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001913$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001914$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509001915$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8040:
                // $script:0831180509001916$ 
                // - Mm? What is it, dear?
                switch (selection) {
                    // $script:0831180509001917$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001918$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001919$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509001920$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8050:
                // $script:0831180509001921$ 
                // - What a wonderful day today, isn't it?
                switch (selection) {
                    // $script:0831180509001922$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001923$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001924$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509001925$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8060:
                // $script:0831180509001926$ 
                // - I'm a little busy right now, dearie.
                switch (selection) {
                    // $script:0831180509001927$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001928$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001929$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509001930$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8900:
                // $script:0831180509001931$ 
                // - Oh, don't push yourself, dearie. Our contract doesn't expire for a while. You can pay me later, hun.
                return true;
            case 8901:
                // $script:0831180509001932$ 
                // - Oh my, you've already paid me for the month, hun. We agreed that I would be paid once a month, remember, dearie?
                return true;
            case 8910:
                // $script:0831180509001933$ 
                // - This is not the amount we agreed upon. No, no. Did you really think you could fool a woman with decades of experience under her apron?
                return true;
            case 8999:
                // $script:0831180509001934$ 
                // - How strange! Based on experience, problems like this usually go away if you just try again. Now, don't just stand there. Try again.
                return true;
            case 9001:
                // $script:0831180509001935$ 
                // - It's been $MaidPassedDay$ since I was supposed to be paid. Any good news?
                switch (selection) {
                    // $script:0831180509001936$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509001937$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001938$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9002:
                // $script:0831180509001939$ 
                // - $OwnerName$, you look like you haven't slept for days. 
                switch (selection) {
                    // $script:0831180509001940$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509001941$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001942$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9003:
                // $script:0831180509001943$ 
                // - You should take care of yourself when thing get tough. Especially while you're young.
                switch (selection) {
                    // $script:0831180509001944$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509001945$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001946$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9010:
                // $script:0831180509001947$ 
                // - Looks like my contract expired, $OwnerName$. Didn't I warn you this would happen a couple days ago? Should've done something then, dearie.
                return true;
            case 9011:
                // $script:0831180509001948$ functionID=1 
                // - Oh, $OwnerName$, our contract has expired. Have you checked the contract? You should, hun.
                return true;
            case 9020:
                // $script:0831180509001949$ functionID=1 
                // - Don't worry about me, dearie. If worse comes to worst, I can always sell my house.
                return true;
            case 9021:
                // $script:0831180509001950$ functionID=1 
                // - $OwnerName$, I know you're going through a hard time. I understand, hun.
                switch (selection) {
                    // $script:0831180509001951$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509001952$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001953$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9040:
                // $script:0831180509001954$ 
                // - Oh, $OwnerName$, sweetie! You look terrible! 
                switch (selection) {
                    // $script:0831180509001955$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509001956$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001957$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9030:
                // $script:0831180509001958$ 
                // - Oh, $OwnerName$, it's late, and you haven't eaten? There's some frozen rice in the freezer. Reheat it and eat up. I'm glad I saved it for you, hun.
                return true;
            case 9031:
                // $script:0831180509001959$ 
                // - I need to cut down my spending this month. Things are a bit tight, now that my income is so low. It's about time I went on a diet anyway.
                return true;
            case 9032:
                // $script:0831180509001960$ 
                // - Will my $npcName:11000055[gender:0]$ will ever grow up? He cried all morning for new shoes. Doesn't he know what mommy has to go through to feed him? 
                return true;
            case 10:
                // $script:0831180509001961$ functionID=1 
                // - Mm? Is there something you want to eat?
                return true;
            case 11:
                // $script:0831180509001962$ functionID=1 
                // - Let me know if you get hungry.
                return true;
            case 20:
                // $script:0831180509001963$ functionID=1 
                // - What would you possibly want to know about an old lady like me?
                return true;
            case 21:
                // $script:0831180509001964$ functionID=1 
                // - What can I do for you?
                switch (selection) {
                    // $script:0831180509001965$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001966$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001967$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 22:
                // $script:0831180509001968$ functionID=1 
                // - What can I do for you?
                switch (selection) {
                    // $script:0831180509001969$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001970$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001971$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509001972$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 30:
                // $script:0831180509001973$ 
                // - Sure, dearie, if you don't mind talking to an old lady like me.
                switch (selection) {
                    // $script:0831180509001974$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,1200,1300,1400,1500,1600,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509001975$
                    // - Let's talk about food!
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,4200,4300,9011 | 
                        return false;
                    // $script:0831180509001976$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509001977$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 31:
                // $script:0831180509001978$ 
                // - Is something bothering you?
                switch (selection) {
                    // $script:0831180509001979$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,1200,1300,1400,1500,1600,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509001980$
                    // - Let's talk about food!
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,4200,4300,9011 | 
                        return false;
                    // $script:0831180509001981$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509001982$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 32:
                // $script:0831180509001983$ 
                // - Go on, dearie, I'm listening.
                switch (selection) {
                    // $script:0831180509001984$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,1200,1300,1400,1500,1600,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509001985$
                    // - Let's talk about food!
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,4200,4300,9011 | 
                        return false;
                    // $script:0831180509001986$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509001987$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 40:
                // $script:0831180509001988$ 
                // - Mm? What is it, dear?
                switch (selection) {
                    // $script:0831180509001989$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001990$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001991$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 50:
                // $script:0831180509001992$ 
                // - What a wonderful day today, isn't it?
                switch (selection) {
                    // $script:0831180509001993$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001994$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001995$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 60:
                // $script:0831180509001996$ 
                // - I'm a little busy right now, dearie.
                switch (selection) {
                    // $script:0831180509001997$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509001998$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509001999$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 1000:
                // $script:0831180509002000$ 
                // - There's a new juice that's all the rage amongst the young folk of $map:2000001$. I tried making it today.
                // $script:0831180509002001$ 
                // - The mineral water from $map:2000089$ was difficult to procure, but besides that, it wasn't too hard to make. What do you think?
                switch (selection) {
                    // $script:0831180509002002$
                    // - Did you go to $map:2000089$ yourself?
                    case 0:
                        Id = 0; // TODO: 1001,1002 | 
                        return false;
                    // $script:0831180509002003$
                    // - Why is this juice so popular in $map:2000001$?
                    case 1:
                        Id = 0; // TODO: 1011,1012 | 
                        return false;
                }
                return true;
            case 1001:
                // $script:0831180509002004$ functionID=1 
                // - I didn't leave your house unattended, if that's what you're asking. I made $npcName:11000350[gender:0]$ help me.
                return true;
            case 1002:
                // $script:0831180509002005$ functionID=1 
                // - Do you even know where $map:2000089$ is? It's deep in a forest. Do you think an old lady like me would survive that journey?
                return true;
            case 1011:
                // $script:0831180509002006$ functionID=1 
                // - The youngsters of $map:2000001$ believe sharing this juice with people that they love will make their love last forever. How do you like it?
                return true;
            case 1012:
                // $script:0831180509002007$ 
                // - It's because of a rumor that it promotes eternal love when lovers drink it together.
                // $script:0831180509002008$ functionID=1 
                // - I don't believe it, though. I'm sure it's just a corporate scheme.
                return true;
            case 1100:
                // $script:0831180509002009$ 
                // - I made a snack with some of the leftover ingredients you had in the kitchen. My $npcName:11000055[gender:0]$  just loves sweets. I hope you like these, too, $OwnerName$.
                // $script:0831180509002010$ 
                // - You can eat it all, dearie. When you get to be my age, it all goes straight to the hips.
                switch (selection) {
                    // $script:0831180509002011$
                    // - What? You look great!
                    case 0:
                        Id = 0; // TODO: 1111,1112 | 
                        return false;
                    // $script:0831180509002012$
                    // - Thanks!
                    case 1:
                        Id = 0; // TODO: 1101,1102 | 
                        return false;
                }
                return true;
            case 1101:
                // $script:0831180509002013$ functionID=1 
                // - I can see the snack lifting your mood, hun. Sugar does that to you.
                return true;
            case 1102:
                // $script:0831180509002014$ functionID=1 
                // - I didn't think you'd scarf it down so fast. Don't blame me if you get a tummyache later!
                return true;
            case 1111:
                // $script:0831180509002015$ functionID=1 
                // - Thank you for saying that, dearie. Aren't you just the sweetest!
                return true;
            case 1112:
                // $script:0831180509002016$ functionID=1 
                // - Tsk, you're such a bad liar. Your eyes gave you away. I had quite the figure back in the day, you know... It's not much fun getting old.
                return true;
            case 1200:
                // $script:0831180509002017$ 
                // - I noticed you're having a hard time waking up in the morning. I made this to help start your day off right.
                // $script:0831180509002018$ 
                // - It's a potion with all kinds of healthy ingredients in it. Drink up. It'll wake you up right away.
                switch (selection) {
                    // $script:0831180509002019$
                    // - It's delicious!
                    case 0:
                        Id = 0; // TODO: 1201,1202 | 
                        return false;
                    // $script:0831180509002020$
                    // - Why don't you drink some, too?
                    case 1:
                        Id = 0; // TODO: 1211,1212 | 
                        return false;
                }
                return true;
            case 1201:
                // $script:0831180509002021$ functionID=1 
                // - Huh? It is? That can't be right. It's healthy, sure, but it's not supposed to taste good...
                return true;
            case 1202:
                // $script:0831180509002022$ functionID=1 
                // - Oh, you're just saying that to be nice. No health drink actually tastes good. Even I can't drink a full glass of it!
                return true;
            case 1211:
                // $script:0831180509002023$ functionID=1 
                // - Are you worried about my health, hun? Don't worry. I already had some.
                return true;
            case 1212:
                // $script:0831180509002024$ functionID=1 
                // - You have a good heart, dearie. I wish $npcName:11000055[gender:0]$ was as good as you. Then I wouldn't have to worry about him all the time. 
                return true;
            case 1300:
                // $script:0831180509002025$ 
                // - $OwnerName$, I cooked you up something special.  Nothing is more important than eating three meals a day, you know.
                // $script:0831180509002026$ 
                // - Eating well is the cornerstone to good health, after all.
                switch (selection) {
                    // $script:0831180509002027$
                    // - I'll eat it later.
                    case 0:
                        Id = 0; // TODO: 1301,1302 | 
                        return false;
                    // $script:0831180509002028$
                    // - Thanks for the food!
                    case 1:
                        Id = 0; // TODO: 1311,1312 | 
                        return false;
                }
                return true;
            case 1301:
                // $script:0831180509002029$ functionID=1 
                // - No, no. You shouldn't skip meals. Eat it right now, even if you don't want to. Trust me!
                return true;
            case 1302:
                // $script:0831180509002030$ functionID=1 
                // - Food doesn't taste good when it's cold. Try to eat at least some of it. $OwnerName$, you're as bad as $npcName:11000055[gender:0]$ sometimes...
                return true;
            case 1311:
                // $script:0831180509002031$ functionID=1 
                // - Oh, I love how you eat anything I give you. I wish $npcName:11000055[gender:0]$ ate as well as you do.
                return true;
            case 1312:
                // $script:0831180509002032$ functionID=1 
                // - I'm glad you like my food. You've gained weight since I've started working here. Perhaps it's time to cut some carbs. Hmm...
                return true;
            case 1400:
                // $script:0831180509002033$ 
                // - A salesman visited today. I told him I wasn't interested, be he insisted I take a look at his wares. I was really just only going to look, but then I thought you might like this, so I bought it for you.
                // $script:0831180509002034$ 
                // - What do you think? Do you like it?
                switch (selection) {
                    // $script:0831180509002035$
                    // - Thank you.
                    case 0:
                        Id = 0; // TODO: 1411,1412 | 
                        return false;
                    // $script:0831180509002036$
                    // - It's not good to make impulse purchases.
                    case 1:
                        Id = 0; // TODO: 1401,1402 | 
                        return false;
                }
                return true;
            case 1401:
                // $script:0831180509002037$ functionID=1 
                // - I know, but he was such a smooth talker! Maybe I just shouldn't talk to anyone I don't already know.
                return true;
            case 1402:
                // $script:0831180509002038$ functionID=1 
                // - But I got it for 50 mesos off! Ahhh, I guess you're right. But what can I do about it now?
                return true;
            case 1411:
                // $script:0831180509002039$ functionID=1 
                // - It looks good on you, $OwnerName$! And I got a great deal on it, too!
                return true;
            case 1412:
                // $script:0831180509002040$ functionID=1 
                // - I knew you'd love it, $OwnerName$. I also bought a couple of things for $npcName:11000055[gender:0]$ and $npcName:11000350[gender:0]$. Hee hee.
                return true;
            case 1500:
                // $script:0831180509002041$ 
                // - $npcName:11000350[gender:0]$ is really good with his hands. He dropped by yesterday to take a look around, then stopped by again today and brought this. He made it himself!
                // $script:0831180509002042$ 
                // - It matches your house perfectly, don't you think?
                switch (selection) {
                    // $script:0831180509002043$
                    // - Sure.
                    case 0:
                        Id = 0; // TODO: 1511,1512 | 
                        return false;
                    // $script:0831180509002044$
                    // - Wait. Who's $npcName:11000350[gender:0]$?
                    case 1:
                        Id = 0; // TODO: 1501,1502 | 
                        return false;
                }
                return true;
            case 1501:
                // $script:0831180509002045$ 
                // - Oh, didn't I tell you? $npcName:11000350[gender:0]$ is an old neighbor of mine.
                // $script:0831180509002046$ functionID=1 
                // - My son $npcName:11000055[gender:0]$ loves him. I'm sure you've seen him around $map:2000017$.
                return true;
            case 1502:
                // $script:0831180509002047$ functionID=1 
                // - I met him $npcName:11000350[gender:0]$ in $map:2000001$. We became friends because of $npcName:11000055[gender:0]$. He said he used to be a $npcName:11000350[gender:0]$, so I have no idea where he learned to make something like this!
                return true;
            case 1511:
                // $script:0831180509002048$ functionID=1 
                // - It's great, isn't it? I told you $npcName:11000350[gender:0]$ is good with his hands. Now I want to do something for him in return. Maybe he'll like my special pudding!
                return true;
            case 1512:
                // $script:0831180509002049$ functionID=1 
                // - $npcName:11000350[gender:0]$ is so kind, don't you think? Now, $OwnerName$, why don't place it somewhere right now? It'll brighten things up!
                return true;
            case 1600:
                // $script:0831180509002050$ 
                // - Today a stranger came and begged me for food. I felt sorry for him, so I gave him some leftover rice and chicken. He ate two bowls of rice! Before he left, he gave me some mesos.
                // $script:0831180509002051$ 
                // - I really didn't want to take his money, but he insisted.
                switch (selection) {
                    // $script:0831180509002052$
                    // - You shouldn't feed strangers!
                    case 0:
                        Id = 0; // TODO: 1601,1602 | 
                        return false;
                    // $script:0831180509002053$
                    // - What was he like?
                    case 1:
                        Id = 0; // TODO: 1611,1612 | 
                        return false;
                }
                return true;
            case 1601:
                // $script:0831180509002054$ functionID=1 
                // - I know I shouldn't, but I couldn't say no to such a sad-looking face. I didn't even think to ask his name.
                return true;
            case 1602:
                // $script:0831180509002055$ functionID=1 
                // - It was just leftovers! He looked familiar, somehow... Like maybe I've seen his face on a leaflet in $map:02000100$.
                return true;
            case 1611:
                // $script:0831180509002056$ functionID=1 
                // - He wore goggles around his head and a red cape on his shoulders. He seemed anxious. Couldn't stop peering around as he ate. Whatever his story is, it can't be a good one.
                return true;
            case 1612:
                // $script:0831180509002057$ 
                // - I asked him his name, but he refused to say. He was blond and had a scar on his face.
                // $script:0831180509002058$ functionID=1 
                // - He was a bit intimidating, to be honest. I could tell he was on the run. Still, I couldn't refuse him. I could tell he hadn't eaten or slept in days...
                return true;
            case 2000:
                // $script:0831180509002059$ 
                // - You came at the just the right time. I've got something to tell you.
                // $script:0831180509002060$ 
                // - I wanted to grill some eels for dinner, but I couldn't get the fire going and didn't want to use the stove. Fire-grilled eels taste best, you know. A passing mage offered to help, so I gladly accepted.
                // $script:0831180509002061$ 
                // - But then he hollered, "I'll burn you all!" and shot a giant fireball at the eels! He would've burned down the whole house, but then he shouted "I'll freeze you all!" and put out the fire with an ice bolt.
                return true;
            case 2100:
                // $script:0831180509002062$ 
                // - Nothing much happened. Oh, where did time go? I'm not even halfway done with my cooking.
                // $script:0831180509002063$ 
                // - Time goes by so quickly when I work around the house, but don't you wander off. Your food is almost ready. I made mushroom hot pot for you today to invigorate you.
                return true;
            case 2200:
                // $script:0831180509002064$ 
                // - Sure, I know something interesting. Sometimes, the food I toil so hard over disappears!
                // $script:0831180509002065$ 
                // - I don't know how it's possible. Is someone stealing it?
                // $script:0831180509002066$ 
                // - I never hear footsteps, so it has to be an animal. Maybe a stray cat or something. It's so frustrating!
                return true;
            case 3000:
                // $script:0831180509002067$ 
                // - What's my specialty, you ask? Hee hee, grilled eels, with a delicious sauce!
                // $script:0831180509002068$ 
                // - $npcName:11000119[gender:0]$ loves them so much that sometimes he stops by my house just to eat them.
                // $script:0831180509002069$ functionID=1 
                // - People always tell me I should open a grilled eel restaurant, but I want to keep cooking a hobby, not a job.
                return true;
            case 3100:
                // $script:0831180509002070$ 
                // - Hmm, a young lady has stopped by a lot recently to visit me. She wants to learn how to cook for her boyfriend. She's a cute girl with glasses... I can't remember her name.
                // $script:0831180509002071$ 
                // - Yesterday, I taught her how to cook mushroom hot pot. I showed her how to prepare the $npc:21000001$, and suddenly she paled and burst into tears.
                // $script:0831180509002072$ functionID=1 
                // - She said the $npc:21000001$ looked so pitiful that she couldn't chop them up. Ahh, she may be too soft-hearted to be a good cook.
                return true;
            case 4000:
                // $script:0831180509002073$ 
                // - To me, cooking is all about love. From deciding the menu to picking the ingredients to the actual preparation, I think about who I'm feeding and what would make them happy.
                // $script:0831180509002074$ 
                // - That's why you should try to enjoy the food that I cook for you, even if it isn't your favorite. Got it?
                return true;
            case 4100:
                // $script:0831180509002075$ 
                // - Good ingredients make good food. Speaking of which, did you know $map:2000076$ is stocked with amazing ingredients?
                // $script:0831180509002076$ 
                // - Fresh eggs, milk, pork, beef, chicken, and even fish. I lived in $map:2000076$ when I was young, and that's part of the reason I got into cooking. That's also probably why the people who live in $map:2000076$ are generally good cooks.
                return true;
            case 5000:
                // $script:0831180509002077$ 
                // - Today's pudding is especially well-made. I'll invite my son over to eat some, too. Sometimes, that kid can get more curious than this mama can handle!
                // $script:0831180509002078$ 
                // - My son's name is $npcName:11000055[gender:0]$. You might have seen him in $map:2000001$.
                // $script:0831180509002079$ 
                // - He keeps forgetting to return books to the library on time, and $npcName:11000005[gender:1]$ the librarian is not happy about it. But what can I say? My boy is just too curious for his own good!
                // $script:0831180509002080$ 
                // - I'm a little worried that all he does is read, though. Children his age need to go out and play!
                return true;
            case 5100:
                // $script:0831180509002081$ 
                // - This pudding is $npcName:11000350[gender:0]$'s favorite. Speaking of which, I wonder if he's feeding himself right... Huh? Who's $npcName:11000350[gender:0]$?
                // $script:0831180509002082$ 
                // - We met in $map:2000001$. $npcName:11000055[gender:0]$ loves him because he tells him all kinds of interesting tales about things that he's seen while traveling the world selling his wares.
                // $script:0831180509002083$ 
                // - In fact, my son loves him so much that every time he goes over to $npcName:11000350[gender:0]$'s house, he stays there until way past dinnertime.
                // $script:0831180509002084$ 
                // - $npcName:11000350[gender:0]$ has mentioned more than once that he wants to quit being a
                //   hawker and settle down somewhere. I don't know how he's doing with that. Buying a house is never easy.
                return true;
            case 6000:
                // $script:0831180509002085$ 
                // - Did you skip lunch today? You can't go on adventures if you don't take care of yourself! You know, not even $npcName:11000075[gender:1]$ gets food as delicious as this!
                // $script:0831180509002086$ 
                // - ...Huh? $npcName:11000055[gender:0]$ wants to know about his father. He grows more mature each day...
                // $script:0831180509002087$ 
                // - $OwnerName$, you look like you're curious , too. $npcName:11000055[gender:0]$'s father... He... He went on a journey to a far away place. That was... wow, it was seven years ago.
                // $script:0831180509002088$ 
                // - I haven't heard from him since. Everyone tells me I should move on, but I don't want to. I know he'll come back one day.
                // $script:0831180509002089$ 
                // - Hm, maybe I shouldn't have told you that. You look like you want to pepper me with more questions, but please understand, there are some things I'd rather not talk about.
                return true;
            case 7000:
                // $script:0831180509002090$ 
                // - What do I think of $npcName:11000350[gender:0]$? Don't be silly. Sure, $npcName:11000350[gender:0]$ is a good man, and I like that he loves my cooking.
                // $script:0831180509002091$ 
                // - $npcName:11000350[gender:0]$ reminds me of the good old days. I may be an old lady now, but I used to be quite popular amongst the gentlemen.
                // $script:0831180509002092$ 
                // - I live in $map:2000001$ now, but originally I came from $map:2000076$. Believe it or not, I used to be as pretty as $npcName:11000015[gender:1]$, and I was good at cooking even then. All the fellows used to come to $map:2000076$ just to see me.
                // $script:0831180509002093$ 
                // - There was one fellow who left a bunch of wildflowers on my doorstep every day. I thought he was a good man, but he never asked me out. Hmph, you don't draw your sword unless you intend to use it, you know!
                // $script:0831180509002094$ 
                // - Anyway, $npcName:11000350[gender:0]$ looks just like that fellow. That's why he reminds me of the old days.
                return true;
            case 100:
                // $script:0831180509002095$ 
                // - Mm? I don't think I've seen you before. What brings you to this residence?
                switch (selection) {
                    // $script:0831180509002096$
                    // - I smell something delicious.
                    case 0:
                        Id = 0; // TODO: 101,102 | 
                        return false;
                    // $script:0831180509002097$
                    // - I thought the house was empty.
                    case 1:
                        Id = 0; // TODO: 103,104 | 
                        return false;
                    // $script:0831180509002098$
                    // - Who are you?
                    case 2:
                        Id = 0; // TODO: 105,106 | 
                        return false;
                }
                return true;
            case 101:
                // $script:0831180509002099$ 
                // - You must be smelling my pudding. Mm? Are you hungry? I'm sorry, but I'm only making four servings each time: for me, $npcName:11000350[gender:0]$, $npcName:11000055[gender:0]$, and $OwnerName$.
                return true;
            case 102:
                // $script:0831180509002100$ 
                // - You're not the first to venture here while following their nose! My cooking skills are quite renowned in $map:2000001$. Today I'm making my special: grilled eels.
                return true;
            case 103:
                // $script:0831180509002101$ 
                // - Oh, don't say that. You must be tired coming all the way out here. Have a seat and put your feet up. You can help me peel the garlic if you want.
                return true;
            case 104:
                // $script:0831180509002102$ 
                // - That's what everyone who comes into the house says. Hm, I'd better do something about that. I'll to talk to $OwnerName$ and see if we can put up a doorplate.
                return true;
            case 105:
                // $script:0831180509002103$ 
                // - I help with the housework, but I'm so much more than just a servant. You know, the owner wouldn't remember to eat without my constant reminders. Speaking of which, have you had breakfast, young adventurer?
                return true;
            case 106:
                // $script:0831180509002104$ 
                // - My name is $MaidName$, and I'm help with the housework. If you're going to $map:2000001$, could you tell my son that I want him to come over for some pudding? His name is $npcName:11000055[gender:0]$.
                return true;
            default:
                return true;
        }
    }
}
