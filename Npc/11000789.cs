using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000789: Arita
/// </summary>
public class _11000789 : NpcScript {
    internal _11000789(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 1;2;3;4;5;6;9001;9002;9003;100
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180509004782$ 
                // - Why are humans so high maintenance?
                return true;
            case 1:
                // $script:0831180509004783$ 
                // - Please! One moment, I'm talking to this zelkova.
                switch (selection) {
                    // $script:0831180509004784$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004785$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004786$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 2:
                // $script:0831180509004787$ 
                // - Isn't it a wonderful day?
                switch (selection) {
                    // $script:0831180509004788$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004789$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004790$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 3:
                // $script:0831180509004791$ 
                // - Please be careful not to tread on grass or flowers when you walk.
                switch (selection) {
                    // $script:0831180509004792$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004793$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004794$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 4:
                // $script:0831180509004795$ 
                // - Please! One moment, I'm talking to this zelkova.
                switch (selection) {
                    // $script:0831180509004796$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004797$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004798$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509004799$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 5:
                // $script:0831180509004800$ 
                // - Isn't it a wonderful day?
                switch (selection) {
                    // $script:0831180509004801$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004802$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004803$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509004804$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 6:
                // $script:0831180509004805$ 
                // - Please be careful not to tread on grass or flowers when you walk.
                switch (selection) {
                    // $script:0831180509004806$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004807$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004808$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509004809$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 9:
                // $script:0831180509004810$ 
                // - Did you just say you're going to pay me?
                //   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
                switch (selection) {
                    // $script:0831180509004811$
                    // - Never mind.
                    case 0:
                        Id = 0; // TODO: 8040,8050,8060,9040 | 8999
                        return false;
                    // $script:0831180509004812$
                    // - (Pay $MaidSalary$.)
                    case 1:
                        Id = 0; // TODO: 8000,8001,8010,8011,8901 | 8900,8910
                        return false;
                }
                return true;
            case 8000:
                // $script:0831180509004813$ functionID=1 
                // - Aha, our contract renews every time you pay me, right? That's how human contracts work? I feel like I've learned something new and fascinating about human culture, and that makes me happy!
                return true;
            case 8001:
                // $script:0831180509004814$ functionID=1 
                // - Ah, I know. Accepting this means I accept the extension of our contract. I'm learning so much about you unusual creatures, thanks to you!
                return true;
            case 8010:
                // $script:0831180509004815$ functionID=1 
                // - Keeping a promise made to a human is tough, but I saw it through, didn't I? I feel like I've really accomplished something great. Thanks for the experience!
                return true;
            case 8011:
                // $script:0831180509004816$ functionID=1 
                // - Really? Hehe. I had no idea how difficult it was to be idle all day. Thank you for helping me keep my promise, $OwnerName$!
                return true;
            case 8020:
                // $script:0831180509004817$ functionID=1 
                // - $OwnerName$, did you know our employment agreement expires soon?
                return true;
            case 8021:
                // $script:0831180509004818$ functionID=1 
                // - Why are humans so high maintenance?
                switch (selection) {
                    // $script:0831180509004819$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004820$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004821$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509004822$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8040:
                // $script:0831180509004823$ 
                // - Mm? Do you have something else to tell me?
                switch (selection) {
                    // $script:0831180509004824$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004825$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004826$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509004827$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8050:
                // $script:0831180509004828$ 
                // - Please! One moment, I'm talking to this zelkova.
                switch (selection) {
                    // $script:0831180509004829$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004830$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004831$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509004832$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8060:
                // $script:0831180509004833$ 
                // - Please be careful not to tread on grass or flowers when you walk.
                switch (selection) {
                    // $script:0831180509004834$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004835$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004836$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509004837$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8900:
                // $script:0831180509004838$ 
                // - Don't be embarrassed. You can pay me whenever you have the money.
                return true;
            case 8901:
                // $script:0831180509004839$ 
                // - Hehe, you already paid me this month, $OwnerName$!
                return true;
            case 8910:
                // $script:0831180509004840$ 
                // - You're trying to help me keep my promise. I appreciate that so much, but it won't work if you don't have enough money. Thank you for trying.
                return true;
            case 8999:
                // $script:0831180509004841$ 
                // - Oh, how did you do that? Neat! Show me again!
                return true;
            case 9001:
                // $script:0831180509004842$ 
                // - There are some things I just can't do, no matter how hard I try.
                switch (selection) {
                    // $script:0831180509004843$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509004844$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004845$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9002:
                // $script:0831180509004846$ 
                // - Is something wrong?
                switch (selection) {
                    // $script:0831180509004847$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509004848$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004849$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9003:
                // $script:0831180509004850$ 
                // - I want to plant more flowers! You're not interested in that, are you?
                switch (selection) {
                    // $script:0831180509004851$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509004852$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004853$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9010:
                // $script:0831180509004854$ 
                // - Huh? Wait. $OwnerName$, my contract expired...
                return true;
            case 9011:
                // $script:0831180509004855$ functionID=1 
                // - I'm so sorry to interrupt, but this is important! Our contract expired! $OwnerName$, please check the contract!
                return true;
            case 9020:
                // $script:0831180509004856$ functionID=1 
                // - It's been $MaidPassedDay$ since our contract expired. I may live a long, long life, $OwnerName$, but I want our time together to be meaningful.
                return true;
            case 9021:
                // $script:0831180509004857$ functionID=1 
                // - Time never stops, and it never waits for anyone.
                switch (selection) {
                    // $script:0831180509004858$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509004859$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004860$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9040:
                // $script:0831180509004861$ 
                // - Mm... Okay.
                switch (selection) {
                    // $script:0831180509004862$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509004863$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004864$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9030:
                // $script:0831180509004865$ 
                // - $OwnerName$! What happened? Won't you tell me? I know something happened... I thought we were closer than that...
                return true;
            case 9031:
                // $script:0831180509004866$ 
                // - Did you know fairies make contracts to use magic and spells? To us, contracts are promises we make in exchange for power. Humans, it seems, mainly use contracts for things involving time and money. When I signed on with Helping Hands, I made a promise to the company about accepting a certain wage.
                // $script:0831180509004867$ 
                // - I would love to do you a favor without anything in return, but that would mean breaking my promise... I made a promise to Helping Hands in exchange for an opportunity to learn more about humans. I hope you can understand that, $OwnerName$.
                return true;
            case 9032:
                // $script:0831180509004868$ 
                // - $OwnerName$, you haven't talked to me lately. You didn't use to be like this. Oh, never mind. For a moment, I forgot you were human, hehe!
                return true;
            case 10:
                // $script:0831180509004869$ functionID=1 
                // - Mama taught me this! I'm good at it, hehe.
                return true;
            case 11:
                // $script:0831180509004870$ functionID=1 
                // - Sure! Anytime.
                return true;
            case 20:
                // $script:0831180509004871$ functionID=1 
                // - $OwnerName$, you're the first human I've shared so much with...
                return true;
            case 21:
                // $script:0831180509004872$ functionID=1 
                // - Isn't it a wonderful day?
                switch (selection) {
                    // $script:0831180509004873$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004874$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004875$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 22:
                // $script:0831180509004876$ functionID=1 
                // - Isn't it a wonderful day?
                switch (selection) {
                    // $script:0831180509004877$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004878$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004879$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509004880$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 30:
                // $script:0831180509004881$ 
                // - Fairies are good at keeping secrets. You can tell me anything!
                switch (selection) {
                    // $script:0831180509004882$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509004883$
                    // - Tell me something about fairies.
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,9011 | 
                        return false;
                    // $script:0831180509004884$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509004885$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 31:
                // $script:0831180509004886$ 
                // - You look like you have something to say.
                switch (selection) {
                    // $script:0831180509004887$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509004888$
                    // - Tell me something about fairies.
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,9011 | 
                        return false;
                    // $script:0831180509004889$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509004890$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 32:
                // $script:0831180509004891$ 
                // - Sometimes, I wonder how things are back in $map:2000023$.
                switch (selection) {
                    // $script:0831180509004892$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509004893$
                    // - Tell me something about fairies.
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,9011 | 
                        return false;
                    // $script:0831180509004894$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509004895$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 40:
                // $script:0831180509004896$ 
                // - Mm? Do you have something else to tell me?
                switch (selection) {
                    // $script:0831180509004897$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004898$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004899$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 50:
                // $script:0831180509004900$ 
                // - Please! One moment, I'm talking to this zelkova.
                switch (selection) {
                    // $script:0831180509004901$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004902$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004903$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 60:
                // $script:0831180509004904$ 
                // - Please be careful not to tread on grass or flowers when you walk.
                switch (selection) {
                    // $script:0831180509004905$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004906$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004907$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 1000:
                // $script:0831180509004908$ 
                // - I can't help it. I just don't trust humans.
                // $script:0831180509004909$ 
                // - I know you're not like the others, $OwnerName$. But... we're just so different.
                // $script:0831180509004910$ 
                // - I know we should all just accept one another, but I can't get used to your kind's disregard for nature or penchant for violence. Am I wrong to feel this way?
                switch (selection) {
                    // $script:0831180509004911$
                    // - Nah.
                    case 0:
                        Id = 0; // TODO: 1011,1012 | 
                        return false;
                    // $script:0831180509004912$
                    // - Yeah.
                    case 1:
                        Id = 0; // TODO: 1001,1002 | 
                        return false;
                }
                return true;
            case 1001:
                // $script:0831180509004913$ functionID=1 
                // - No matter how hard I try, there's just some things I can't do. I don't know if a human could really understand...
                return true;
            case 1002:
                // $script:0831180509004914$ functionID=1 
                // - I thought of all people you'd understand me. Just forget I said anything.
                return true;
            case 1011:
                // $script:0831180509004915$ functionID=1 
                // - Thank you for understanding. All I want is for your kind to stop fighting and to live wisely!
                return true;
            case 1012:
                // $script:0831180509004916$ functionID=1 
                // - $OwnerName$, I knew you'd understand. You're different from the rest.
                return true;
            case 1100:
                // $script:0831180509004917$ 
                // - $OwnerName$, I want to ask you something.
                // $script:0831180509004918$ 
                // - I've mentioned a few times that fairies aren't fond of humans.
                // $script:0831180509004919$ 
                // - But what's your opinion, $OwnerName$? Do you like fairies?
                switch (selection) {
                    // $script:0831180509004920$
                    // - Of course.
                    case 0:
                        Id = 0; // TODO: 1101,1102 | 
                        return false;
                    // $script:0831180509004921$
                    // - I want to learn more about your species, honestly.
                    case 1:
                        Id = 0; // TODO: 1111,1112 | 
                        return false;
                }
                return true;
            case 1101:
                // $script:0831180509004922$ functionID=1 
                // - I've heard of humans who said the same thing, then brutally betrayed us. I'm not saying you're like that, but...
                return true;
            case 1102:
                // $script:0831180509004923$ functionID=1 
                // - Just like that? It sounded a little insincere, if you ask me...
                return true;
            case 1111:
                // $script:0831180509004924$ functionID=1 
                // - Ah! You and I are kindred spirits in that regard, $OwnerName$. I'm so happy we met!
                return true;
            case 1112:
                // $script:0831180509004925$ functionID=1 
                // - Yes, I want to learn more about humans, too!
                return true;
            case 2000:
                // $script:0831180509004926$ 
                // - I made this pendant with a stone I found in my forest. Pretty, isn't it?
                // $script:0831180509004927$ 
                // - Heh heh, surprised? My mom taught me when I was young. She's a famous craftswoman in $map:02000023$.
                // $script:0831180509004928$ 
                // - But I don't think this is just some ordinary stone. It gives off a strange vibe, like... magic.
                // $script:0831180509004929$ 
                // - I want to know more! I'm going to show it to $npcName:11000031[gender:0]$ tomorrow.
                return true;
            case 2100:
                // $script:0831180509004930$ 
                // - Yesterday $npcName:11000034[gender:0]$ stopped by. He must have been worried that I'm staying with a human.
                // $script:0831180509004931$ 
                // - He kept urging me to return to the forest, but I told him I can better relate to you than I can to other humans. And it's true. Hehe.
                // $script:0831180509004932$ 
                // - $npcName:11000034[gender:0]$ would agree if he met you. If you ever have business in $map:02000023$, would you give my regards to $npcName:11000034[gender:0]$?
                return true;
            case 2200:
                // $script:0831180509004933$ 
                // - I prepare food for you every day, but do you really have to eat animals and plants?
                // $script:0831180509004934$ 
                // - Fairies only need one glass of honey milk in the morning and one in the afternoon. Animals and plants are my friends, and I shouldn't eat my friends, right?
                // $script:0831180509004935$ 
                // - You don't need to look so guilty. I know you can't live on just milk like I can.
                // $script:0831180509004936$ 
                // - "Nature makes us what we are." That's what $npcName:11000031[gender:0]$ says. Eat up!
                return true;
            case 3000:
                // $script:0831180509004937$ 
                // - Humans have long coveted the ancient knowledge of the fairies. They spy on us and try to steal it when we aren't looking. 
                // $script:0831180509004938$ 
                // - Those who do are usually driven to ruin by their own greed!
                // $script:0831180509004939$ 
                // - With the current situation, we've had no choice but to join forces with humans, but that doesn't mean we like you. I've seen some pretty great humans but only a few of you are wise.
                // $script:0831180509004940$ functionID=1 
                // - The wise humans know their place in the grand scheme of the universe. Then again... I doubt even $npcName:11000075[gender:1]$ is completely free of selfish desires...
                return true;
            case 3100:
                // $script:0831180509004941$ 
                // - Do all humans allow strangers into their homes? Today, three strangers barged in, but ran off when they saw I was here.
                // $script:0831180509004942$ 
                // - They were surprised, stating that they didn't hear my footsteps. Well, that's because fairies glide instead of stomp.
                // $script:0831180509004943$ functionID=1 
                // - We don't want to hurt even a single blade of grass. Eeek! There are ants crawling all around your feet! Be careful not to step on them!!
                return true;
            case 4000:
                // $script:0831180509004944$ 
                // - Have you ever wondered why I don't have wings?
                // $script:0831180509004945$ 
                // - It's because there are all different types of fairies... Tree tree fairies, flower fairies, river fairies, and all sorts of others.
                // $script:0831180509004946$ 
                // - Some have wings, some don't... and some just have one wing... 
                // $script:0831180509004947$ 
                // - Never mind that. My point is, if you ever visit $map:02000023$, make sure you don't ask such a silly question or everyone will laugh at you.
                return true;
            case 4100:
                // $script:0831180509004948$ 
                // - $npcName:11000284[gender:1]$... She's lost her shoes again. How disgraceful!
                // $script:0831180509004949$ 
                // - I've told her so many times! If she truly loves her shoes, then don't wear them outside of the forest!
                // $script:0831180509004950$ 
                // - Unbelievable! I hope no one helps her this time, so she learns her lesson.
                // $script:0831180509004951$ 
                // - ...But that's wishful thinking. Humans can't resist helping her when she cries, and she knows that.
                return true;
            case 5000:
                // $script:0831180509004952$ 
                // - Yesterday, the wind told me that trees and flowers are disappearing on the west side of Victoria Island.
                // $script:0831180509004953$ 
                // - I'm guessing it must the area around $map:02000100$. I've never been there, and I'm glad! I couldn't survive even a single day in such a sad place.
                // $script:0831180509004954$ 
                // - Why do humans love to dig? Why do you love tall buildings so much?
                // $script:0831180509004955$ 
                // - You're building homes for yourselves but destroying ours.
                return true;
            case 5100:
                // $script:0831180509004956$ 
                // - I don't hate all humans. I have great respect for $npc:11000075[gender:1]$ and for $npcName:11000039[gender:1]$.
                // $script:0831180509004957$ 
                // - I have many things I can learn from $npcName:11000042[gender:1]$. I think there are only a handful of fairies who possess more ancient knowledge than he does.
                // $script:0831180509004958$ 
                // - Humans and fairies are so different. I'm having a hard time getting used to you. We haven't interacted with each other for a long time. You can't expect for us to become friends overnight.
                return true;
            case 6000:
                // $script:0831180509004959$ 
                // - Soon it'll be my birthday. Let's celebrate together. And don't even think to ask how many candles we'll need...
                // $script:0831180509004960$ 
                // - Oh, fine, since you're my friend, I'll give you a hint.
                // $script:0831180509004961$ 
                // - I just want one candle. I'm not even a hundred yet! I'm pretty young for the fairfolk.
                // $script:0831180509004962$ 
                // - Fairies live a lot longer than humans, you know.
                // $script:0831180509004963$ 
                // - You'd be shocked if you knew how old $npcName:11000033[gender:0]$ or $npcName:11000031[gender:0]$ are. You really just can't think of our ages in human years.
                return true;
            case 7000:
                // $script:0831180509004964$ 
                // - Lately $npcName:11000032[gender:0]$ hasn't looked so good. I'm worried something happened to him.
                // $script:0831180509004965$ 
                // - I tried to ask, but he wouldn't answer. $npcName:11000031[gender:0]$ seemed to know something, but he wouldn't tell me either.
                // $script:0831180509004966$ 
                // - Actually $npcName:11000032[gender:0]$ was the reason I got a job with Helping Hands. He left one day all of a sudden, and it dawned on me that I didn't know much about him.
                // $script:0831180509004967$ 
                // - $npcName:11000032[gender:0]$ is half-human and half-fairy. It must have been hard growing up like that, but he never showed it. I would've been nicer if I'd known he'd leave so abruptly...
                // $script:0831180509004968$ 
                // - That's why I wanted to learn more about humans. I'm glad I applied for this job. Staying here with you has been so informative!
                return true;
            case 100:
                // $script:0831180509004969$ 
                // - Eeek! Human!! Sheesh, you scared me!
                switch (selection) {
                    // $script:0831180509004970$
                    // - Sorry for startling you.
                    case 0:
                        Id = 0; // TODO: 101,102 | 
                        return false;
                    // $script:0831180509004971$
                    // - Ha! I'm gonna step on you!
                    case 1:
                        Id = 0; // TODO: 103,104 | 
                        return false;
                    // $script:0831180509004972$
                    // - Who are you?
                    case 2:
                        Id = 0; // TODO: 105,106 | 
                        return false;
                }
                return true;
            case 101:
                // $script:0831180509004973$ 
                // - ...Oh. Well, that's okay.
                return true;
            case 102:
                // $script:0831180509004974$ 
                // - I'm not used to talking to humans... It's okay, I forgive you.
                return true;
            case 103:
                // $script:0831180509004975$ 
                // - Eeeeek!! G-go away!
                return true;
            case 104:
                // $script:0831180509004976$ 
                // - I'm going to tell $npcName:11000031[gender:0]$! You'd better get away from me before I turn you into a frog!
                return true;
            case 105:
                // $script:0831180509004977$ 
                // - M-me? I'm of the fairfolk... Eek, sorry! I don't think I'm ready to talk to strange humans!
                return true;
            case 106:
                // $script:0831180509004978$ 
                // - H-hey, that doesn't matter. If you have business with <font color="#ffd200">$OwnerName$</font>, you don't need to talk to me.
                return true;
            default:
                return true;
        }
    }
}
