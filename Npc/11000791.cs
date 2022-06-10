using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000791: Solvay
/// </summary>
public class _11000791 : NpcScript {
    internal _11000791(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 1;2;3;4;5;6;9001;9002;9003;100
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180509005211$ 
                // - Now, where should I go today?
                return true;
            case 1:
                // $script:0831180509005212$ 
                // - It's a beautiful day, isn't it?
                switch (selection) {
                    // $script:0831180509005213$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005214$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005215$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 2:
                // $script:0831180509005216$ 
                // - Ah... $OwnerName$.
                switch (selection) {
                    // $script:0831180509005217$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005218$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005219$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 3:
                // $script:0831180509005220$ 
                // - Welcome! ...Ah. I thought you were a customer. Hah hah.
                switch (selection) {
                    // $script:0831180509005221$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005222$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005223$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 4:
                // $script:0831180509005224$ 
                // - It's a beautiful day, isn't it?
                switch (selection) {
                    // $script:0831180509005225$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005226$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005227$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509005228$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 5:
                // $script:0831180509005229$ 
                // - Ah... $OwnerName$.
                switch (selection) {
                    // $script:0831180509005230$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005231$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005232$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509005233$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 6:
                // $script:0831180509005234$ 
                // - Welcome! ...Ah. I thought you were a customer. Hah hah.
                switch (selection) {
                    // $script:0831180509005235$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005236$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005237$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509005238$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 9:
                // $script:0831180509005239$ 
                // - Huh? Do you want to give me my paycheck?
                //   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
                switch (selection) {
                    // $script:0831180509005240$
                    // - Let me think about it some more.
                    case 0:
                        Id = 0; // TODO: 8040,8050,8060,9040 | 8999
                        return false;
                    // $script:0831180509005241$
                    // - (Pay $MaidSalary$.)
                    case 1:
                        Id = 0; // TODO: 8000,8001,8010,8011,8901 | 8900,8910
                        return false;
                }
                return true;
            case 8000:
                // $script:0831180509005242$ functionID=1 
                // - My wallet has felt heavier lately because you always pay me early. Thanks for hiring me for another month! Hah hah!
                return true;
            case 8001:
                // $script:0831180509005243$ functionID=1 
                // - Haha, thanks, $OwnerName$. I'm grateful to have a kind, competent boss like you.
                return true;
            case 8010:
                // $script:0831180509005244$ functionID=1 
                // - Haha, I told you: money comes and money goes. Thank you. I'll try to minimize the number of customers who come to the house, but I mean, it can't be helped sometimes.
                return true;
            case 8011:
                // $script:0831180509005245$ functionID=1 
                // - What? How'd you get so much money so quickly? $OwnerName$, this is serious. You gotta tell me how! Please!
                return true;
            case 8020:
                // $script:0831180509005246$ functionID=1 
                // - $OwnerName$, is everything all right? Our contract expires soon and you haven't mentioned it, so I was just wondering.
                return true;
            case 8021:
                // $script:0831180509005247$ functionID=1 
                // - But if you're not worried, I won't worry either.
                switch (selection) {
                    // $script:0831180509005248$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005249$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005250$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509005251$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8040:
                // $script:0831180509005252$ 
                // - Just say the word.
                switch (selection) {
                    // $script:0831180509005253$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005254$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005255$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509005256$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8050:
                // $script:0831180509005257$ 
                // - Do you have business with me?
                switch (selection) {
                    // $script:0831180509005258$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005259$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005260$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509005261$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8060:
                // $script:0831180509005262$ 
                // - Ah, I didn't know you were standing there.
                switch (selection) {
                    // $script:0831180509005263$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005264$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005265$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509005266$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8900:
                // $script:0831180509005267$ 
                // - Ah, my contract doesn't expire for some time. You don't have to stretch yourself thin. Besides, if you pay me in multiple paychecks, I have to record each one in my ledger. I'd rather just do it once, if it's all the same to you.
                return true;
            case 8901:
                // $script:0831180509005268$ 
                // - Haha, $OwnerName$, you've already paid me for the month. I'm ethical, see? You can trust me.
                return true;
            case 8910:
                // $script:0831180509005269$ 
                // - From experience, I can tell you: when money's tight, you have to cut down on spending. It's okay if you can't pay me right now. We can renew our contract at a later date. I've got my own business, so I'll be fine without this job.
                return true;
            case 8999:
                // $script:0831180509005270$ 
                // - Hm, this must be a bug. I may not look it, but I know a thing or two about programming. If you can replicate the problem, it's definitely a bug. Let's see if you can replicate it.
                return true;
            case 9001:
                // $script:0831180509005271$ 
                // - $OwnerName$, what's really going on?
                switch (selection) {
                    // $script:0831180509005272$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509005273$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005274$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9002:
                // $script:0831180509005275$ 
                // - Mm... Is this because I keep inviting customers over?
                switch (selection) {
                    // $script:0831180509005276$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509005277$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005278$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9003:
                // $script:0831180509005279$ 
                // - This is not because I'm too talkative or too boring, is it?
                switch (selection) {
                    // $script:0831180509005280$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509005281$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005282$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9010:
                // $script:0831180509005283$ 
                // - I'm sorry, $OwnerName$, but I can't. Our contract expired, and business is business, you know?
                return true;
            case 9011:
                // $script:0831180509005284$ functionID=1 
                // - Is that really important right now, $OwnerName$? Our contract expired, and I don't mix business with pleasure.
                return true;
            case 9020:
                // $script:0831180509005285$ functionID=1 
                // - It's been $MaidPassedDay$ since I've stopped working as your servant. I'm doing just fine, to be honest.
                return true;
            case 9021:
                // $script:0831180509005286$ functionID=1 
                // - You don't have to worry about me.
                switch (selection) {
                    // $script:0831180509005287$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509005288$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005289$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9040:
                // $script:0831180509005290$ 
                // - Hm... I'd better behave for a while... 
                switch (selection) {
                    // $script:0831180509005291$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509005292$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005293$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9030:
                // $script:0831180509005294$ 
                // - I will attempt to stop inviting customers into your home. That's the reason you won't renew our contract, isn't it? Or is there something else?
                return true;
            case 9031:
                // $script:0831180509005295$ 
                // - Hm, this unexpected financial blow is affecting my business. I'll have to think of a solution. Don't worry about me. This isn't the first time I've had a hiccup with money.
                return true;
            case 9032:
                // $script:0831180509005296$ 
                // - I have my own business, so I still have a means to live, even if I'm not paid for this side job. But $OwnerName$, you don't have a side job. Are you all right?
                return true;
            case 10:
                // $script:0831180509005297$ functionID=1 
                // - I've learned this little trick while working as a hawker.
                return true;
            case 11:
                // $script:0831180509005298$ functionID=1 
                // - Let me know if I can help you.
                return true;
            case 20:
                // $script:0831180509005299$ functionID=1 
                // - I'm just an ordinary hawker. That's all.
                return true;
            case 21:
                // $script:0831180509005300$ functionID=1 
                // - Hm... Business is slow today... Ah, nothing. Hah hah!
                switch (selection) {
                    // $script:0831180509005301$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005302$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005303$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 22:
                // $script:0831180509005304$ functionID=1 
                // - Hm... Business is slow today... Ah, nothing. Hah hah!
                switch (selection) {
                    // $script:0831180509005305$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005306$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005307$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509005308$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 30:
                // $script:0831180509005309$ 
                // - Taking care of this house sometimes make me want my own property.
                switch (selection) {
                    // $script:0831180509005310$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509005311$
                    // - (Gossip.)
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,9011 | 
                        return false;
                    // $script:0831180509005312$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509005313$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 31:
                // $script:0831180509005314$ 
                // - I wonder everything's going at the Barrota Trading Company...
                switch (selection) {
                    // $script:0831180509005315$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509005316$
                    // - (Gossip.)
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,9011 | 
                        return false;
                    // $script:0831180509005317$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509005318$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 32:
                // $script:0831180509005319$ 
                // - I need my business to be successful, you know.
                switch (selection) {
                    // $script:0831180509005320$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509005321$
                    // - (Gossip.)
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,9011 | 
                        return false;
                    // $script:0831180509005322$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509005323$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 40:
                // $script:0831180509005324$ 
                // - Just say the word.
                switch (selection) {
                    // $script:0831180509005325$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005326$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005327$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 50:
                // $script:0831180509005328$ 
                // - Do you have business with me?
                switch (selection) {
                    // $script:0831180509005329$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005330$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005331$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 60:
                // $script:0831180509005332$ 
                // - Ah, I didn't know you were standing there.
                switch (selection) {
                    // $script:0831180509005333$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005334$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005335$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 1000:
                // $script:0831180509005336$ 
                // - I want to ask you a serious question. It's about what just happened to $npcName:11000526[gender:0]$.
                // $script:0831180509005337$ 
                // - I think Dark Wind is suspicious of members of the Barrota Trading Company.
                // $script:0831180509005338$ 
                // - So... $OwnerName$, what do you think of Dark Wind?
                switch (selection) {
                    // $script:0831180509005339$
                    // - Dark Wind is essential for keeping the peace in $map:2000100$.
                    case 0:
                        Id = 0; // TODO: 1001,1002 | 
                        return false;
                    // $script:0831180509005340$
                    // - That whole organization is rather shady...
                    case 1:
                        Id = 0; // TODO: 1011,1012 | 
                        return false;
                }
                return true;
            case 1001:
                // $script:0831180509005341$ functionID=1 
                // - Hm... You think so? I guess our opinions differ. I suppose that's only human nature.
                return true;
            case 1002:
                // $script:0831180509005342$ functionID=1 
                // - Does that mean you think it's okay for them to treat me the way they do? The injustice!
                return true;
            case 1011:
                // $script:0831180509005343$ functionID=1 
                // - I knew I couldn't be the only one who thought so! There's definitely something strange going on.
                return true;
            case 1012:
                // $script:0831180509005344$ functionID=1 
                // - Right?! But that organization is already so entrenched in $map:2000100$... Anyway, thank you. Now I'm even more confident in my opinion.
                return true;
            case 1100:
                // $script:0831180509005345$ 
                // - Lately, I've been thinking maybe I gossip too much.
                // $script:0831180509005346$ 
                // - But hearing all sorts of rumors comes with my job. And it's not like I can just forget what I hear.
                // $script:0831180509005347$ 
                // - Should I stop telling others what I hear? What are your thoughts on this?
                switch (selection) {
                    // $script:0831180509005348$
                    // - You should be careful about what you say.
                    case 0:
                        Id = 0; // TODO: 1111,1112 | 
                        return false;
                    // $script:0831180509005349$
                    // - I don't care either way.
                    case 1:
                        Id = 0; // TODO: 1101,1102 | 
                        return false;
                }
                return true;
            case 1101:
                // $script:0831180509005350$ functionID=1 
                // - You don't? But I don't want something bad to happen to me, so I'm thinking maybe I should stop.
                return true;
            case 1102:
                // $script:0831180509005351$ functionID=1 
                // - You don't care. So that means you don't care if I tell others about you, right, $OwnerName$? I see what you do when you think I'm not looking...
                return true;
            case 1111:
                // $script:0831180509005352$ functionID=1 
                // - I should, right? Thank you for being honest with me. I'll be more careful from now on.
                return true;
            case 1112:
                // $script:0831180509005353$ functionID=1 
                // - But you like listening to me gossip, don't you, $OwnerName$? Still, I'm glad I asked.
                return true;
            case 2000:
                // $script:0831180509005354$ 
                // - Ahhh... Things haven't been so hot with the Barrota Trading Company.
                // $script:0831180509005355$ 
                // - We're Maple World's largest and most reputable group of traders! How did it come to this...? 
                // $script:0831180509005356$ 
                // - I don't know how they knew where to find me, but a Dark Wind agent stopped by the house a while ago.
                // $script:0831180509005357$ 
                // - I swear to you, I've never done anything unethical as a hawker. Not once! Maybe a bit of gossip, but nothing even close to illegal.
                // $script:0831180509005358$ 
                // - He may be a Dark Wind agent, but that doesn't give him the right to treat me the way he did, accusing me of all sorts of horrible things, asking me all sorts of mean questions. I feel violated!
                return true;
            case 2100:
                // $script:0831180509005359$ 
                // - While taking care of your home, I've located many items that you don't use.
                // $script:0831180509005360$ 
                // - For example, this exercise equipment. Only used once or twice, am I correct?
                // $script:0831180509005361$ 
                // - $OwnerName$, with your permission, I'd like to sell these items. You get the benefit of less clutter, and I get the benefit of a cut of the profits. Win-win, all around, wouldn't you say?
                return true;
            case 2200:
                // $script:0831180509005362$ 
                // - I hung a banner over the door today, and a lot of people stopped by the house to shop.
                // $script:0831180509005363$ 
                // - I had no idea having a physical shop could be so convenient!
                // $script:0831180509005364$ 
                // - Ah, o-of course, $OwnerName$, this is your house, but I get bored sitting around, waiting for you.
                // $script:0831180509005365$ 
                // - So I was thinking... You don't mind if I do my business in your house from time to time, do you?
                return true;
            case 3000:
                // $script:0831180509005366$ 
                // - Okay, so you know $npc:11000074[gender:0]$ in $map:02000001$? He's a trusted subject of $npcName:11000075[gender:1]$.
                // $script:0831180509005367$ 
                // - He has a daughter, $npcName:11000058[gender:1]$. She lives in her father's mansion in $map:02000119$.
                // $script:0831180509005368$ 
                // - But rumor has it that the minister had another daughter...
                // $script:0831180509005369$ 
                // - No, not a lovechild. Sheesh, what are you talking about? $npcName:11000058[gender:1]$ had a twin sister, and she disappeared all of a sudden.
                // $script:0831180509005370$ functionID=1 
                // - It happened a long time ago, so no one knows if her sister is alive or dead. Tragic, isn't it?
                return true;
            case 3100:
                // $script:0831180509005371$ 
                // - This is kind insane, but $npcName:11000252[gender:0]$ in $map:02000100$ has a big secret.
                // $script:0831180509005372$ 
                // - Who? Really? You've never heard of Goldus Group?
                // $script:0831180509005373$ 
                // - Goldus Group partakes in all sorts of businesses—real estate, banking, pharmaceutical, to name a few.
                // $script:0831180509005374$ 
                // - And its chairman is—hm, I don't know if I should tell you this. 
                // $script:0831180509005375$ 
                // - Its chairman is... He's actually...
                // $script:0831180509005376$ functionID=1 
                // - Ugh, no, I can't. If this gets out, the Barrota Trading Company can get in huge trouble.
                return true;
            case 4000:
                // $script:0831180509005377$ 
                // - Hawkers travel everywhere in Maple World. Some of us have even recently dared to enter the Shadow World.
                // $script:0831180509005378$ 
                // - Rumor has it that a hawker named $npcName:11000609[gender:0]$ returned from that shadowy realm, looking like he'd seen a ghost.
                // $script:0831180509005379$ 
                // - He was lucky. Blackstar protects merchants. I'd be surprised if a normal person made it back from that world.
                // $script:0831180509005380$ 
                // - $OwnerName$, don't you dare even think of going there. Stop it. Stop. I know you're already thinking about it...
                return true;
            case 4100:
                // $script:0831180509005381$ 
                // - They say Maple World is in shambles because of the actions of one young, harmless-looking man named... Um... What was his name? 
                // $script:0831180509005382$ 
                // - Whatever. Dark Wind is searching everywhere for him.
                // $script:0831180509005383$ 
                // - I saw his wanted poster in $map:02000100$. He has blond hair, red eyes, and a scar on his face.
                // $script:0831180509005384$ 
                // - $OwnerName$, if you see anyone looking like him, you should report him to Dark Wind. That way you can collect the bounty and share it with me.
                return true;
            case 5000:
                // $script:0831180509005385$ 
                // - I have my reasons for being a hawker. Money is one of them, sure. I mean, we all need money, right?
                // $script:0831180509005386$ 
                // - But that's not the only reason. It might be hard for residents of big cities like $map:02000001$ to imagine, but some folks really do live far, far away from civilization.
                // $script:0831180509005387$ 
                // - And those people need me to get things for them. They count the days until my next visit and watch me approach with excitement in their eyes.
                // $script:0831180509005388$ 
                // - It's not easy traveling over rough terrain, weighed down with a backpack of cargo...
                // $script:0831180509005389$ 
                // - But I truly love it. Selling valued items, delivering news... I get so caught up in all of it that I lose track of time.
                return true;
            case 5100:
                // $script:0831180509005390$ 
                // - The Barrota Trading Company is Maple World's hawker union. We've got hundreds of members, hawking all over the world.
                // $script:0831180509005391$ 
                // - We don't just sell items. People also rely on us to deliver the latest news.
                // $script:0831180509005392$ 
                // - Think of it this way: If this world were a body, we'd be the blood vessels spreading life throughout it! Haha!
                // $script:0831180509005393$ 
                // - Well, we're in a tight spot right now, but it's got to be some sort of misunderstanding. I couldn't imagine Maple World without hawkers.
                return true;
            case 6000:
                // $script:0831180509005394$ 
                // - $OwnerName$, you may not remember this...
                // $script:0831180509005395$ 
                // - Long ago, we first met in $map:63000001$. You were looking for a trip to get to $map:02000062$  for the Empress's event, remember?
                // $script:0831180509005396$ 
                // - It's okay if you don't remember. I've got a good enough memory for the both of us. In fact, the whole trading company knows about my superb memory.
                // $script:0831180509005397$ 
                // - Back then, I was so excited about the Empress's little shindig... Who would've thought we'd end up living in the same house? The future is full of secrets, isn't it?
                return true;
            case 7000:
                // $script:0831180509005398$ 
                // - I've never really given serious thought to settling down. What can I say? I just love being a hawker.
                // $script:0831180509005399$ 
                // - Now, $npcName:11000170[gender:0]$, on the other hand, he found himself a lady while selling his wares. Says he's ready to settle down. He just has to work up the courage to talk to the girl.
                // $script:0831180509005400$ 
                // - It's made me think. I don't know, maybe someday I want to settle down, too... Have a family, all that...
                // $script:0831180509005401$ 
                // - But not yet. First, I want to hustle and build up an amazing reputation as a hawker!
                return true;
            case 100:
                // $script:0831180509005402$ 
                // - Welcome! Is there something you're looking for?
                switch (selection) {
                    // $script:0831180509005403$
                    // - Show me your wares.
                    case 0:
                        Id = 0; // TODO: 101,102 | 
                        return false;
                    // $script:0831180509005404$
                    // - I really don't care.
                    case 1:
                        Id = 0; // TODO: 103,104 | 
                        return false;
                    // $script:0831180509005405$
                    // - I thought this was a house, not a store.
                    case 2:
                        Id = 0; // TODO: 105,106 | 
                        return false;
                }
                return true;
            case 101:
                // $script:0831180509005406$ 
                // - Oh. Right. Nobody actually says that. I don't actually have my wares on me right now, you see... Heh... Heh...
                return true;
            case 102:
                // $script:0831180509005407$ 
                // - I would love too, but all my items are completely sold out for the day? Where do you live? I'll carry all my goods to you later this week for your own personal shopping experience.
                return true;
            case 103:
                // $script:0831180509005408$ 
                // - Oh, come on, doesn't cost anything to take a look!
                return true;
            case 104:
                // $script:0831180509005409$ 
                // - Hm... Then why are you here?
                return true;
            case 105:
                // $script:0831180509005410$ 
                // - Oh, too bad... You see, I'm offering a 90% discount for anyone who visits here to see me. You sure you're not here for me?
                return true;
            case 106:
                // $script:0831180509005411$ 
                // - Yeah? Then why didn't you knock before barging in?
                return true;
            default:
                return true;
        }
    }
}
