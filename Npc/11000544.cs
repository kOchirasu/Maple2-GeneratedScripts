using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000544: Tim
/// </summary>
public class _11000544 : NpcScript {
    internal _11000544(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 1;2;3;4;5;6;9001;9002;9003;100
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180509000250$ 
                // - Greetings.
                return true;
            case 1:
                // $script:0831180509000251$ 
                // - Hello, $OwnerName$.
                switch (selection) {
                    // $script:0831180509000252$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509000253$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509000254$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 2:
                // $script:0831180509000255$ 
                // - Is there anything I can help you with?
                switch (selection) {
                    // $script:0831180509000256$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509000257$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509000258$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 3:
                // $script:0831180509000259$ 
                // - Just say the word, $OwnerName$.
                switch (selection) {
                    // $script:0831180509000260$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509000261$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509000262$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 4:
                // $script:0831180509000263$ 
                // - Hello, $OwnerName$.
                switch (selection) {
                    // $script:0831180509000264$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509000265$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509000266$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509000267$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 5:
                // $script:0831180509000268$ 
                // - Is there anything I can help you with?
                switch (selection) {
                    // $script:0831180509000269$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509000270$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509000271$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509000272$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 6:
                // $script:0831180509000273$ 
                // - Just say the word, $OwnerName$.
                switch (selection) {
                    // $script:0831180509000274$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509000275$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509000276$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509000277$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 9:
                // $script:0831180509000278$ 
                // - Are you giving me my paycheck?
                //   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
                switch (selection) {
                    // $script:0831180509000279$
                    // - Let me think about it some more.
                    case 0:
                        Id = 0; // TODO: 8040,8050,8060,9040 | 8999
                        return false;
                    // $script:0831180509000280$
                    // - (Pay $MaidSalary$.)
                    case 1:
                        Id = 0; // TODO: 8000,8001,8010,8011,8901 | 8900,8910
                        return false;
                }
                return true;
            case 8000:
                // $script:0831180509000281$ functionID=1 
                // - Thank you for hiring me for another month. You won't regret it.
                return true;
            case 8001:
                // $script:0831180509000282$ functionID=1 
                // - Thank you for paying me on time, $OwnerName$. My bosses at Helping Hands just can't stop talking about how wonderful you are.
                return true;
            case 8010:
                // $script:0831180509000283$ functionID=1 
                // - I thought you'd forgotten about me. You were late, but you made it before I had no choice but to leave. Now, would you like a cup of tea?
                return true;
            case 8011:
                // $script:0831180509000284$ functionID=1 
                // - Thank you for not disappointing me $OwnerName$. It is my pleasure to stay under your employment.
                return true;
            case 8020:
                // $script:0831180509000285$ functionID=1 
                // - Just so you are aware, it is almost payday.
                return true;
            case 8021:
                // $script:0831180509000286$ functionID=1 
                // - I hope you haven't forgotten about it.
                switch (selection) {
                    // $script:0831180509000287$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509000288$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509000289$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509000290$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8040:
                // $script:0831180509000291$ 
                // - Sure, $OwnerName$. I always enjoy talking to you.
                switch (selection) {
                    // $script:0831180509000292$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509000293$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509000294$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509000295$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8050:
                // $script:0831180509000296$ 
                // - Sometimes, I feel quite close to you, $OwnerName$.
                switch (selection) {
                    // $script:0831180509000297$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509000298$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509000299$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509000300$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8060:
                // $script:0831180509000301$ 
                // - Hmm? Did something happen, $OwnerName$?
                switch (selection) {
                    // $script:0831180509000302$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509000303$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509000304$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509000305$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8900:
                // $script:0831180509000306$ 
                // - If you can't afford to pay me yet, I can wait. But please understand that Helping Hands has a no pay, no work policy.
                return true;
            case 8901:
                // $script:0831180509000307$ 
                // - You've already paid me this month. You must be a little stressed out.
                return true;
            case 8910:
                // $script:0831180509000308$ 
                // - I have to follow company policy. I can't work until you pay me. I'm sorry.
                return true;
            case 8999:
                // $script:0831180509000309$ 
                // - I have an unusual migraine. Please try talking to me again later.
                return true;
            case 9001:
                // $script:0831180509000310$ 
                // - It's a violation of company policy to work without being paid on time.
                switch (selection) {
                    // $script:0831180509000311$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509000312$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509000313$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9002:
                // $script:0831180509000314$ 
                // - You are already $MaidPassedDay$ late on my paycheck.
                switch (selection) {
                    // $script:0831180509000315$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509000316$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509000317$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9003:
                // $script:0831180509000318$ 
                // - I understand that you're having financial difficulties, $OwnerName$, but I'm afraid I can't offer you any more leeway.
                switch (selection) {
                    // $script:0831180509000319$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509000320$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509000321$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9010:
                // $script:0831180509000322$ 
                // - Apologies. Company policy prohibits me from working under an expired contract.
                return true;
            case 9011:
                // $script:0831180509000323$ functionID=1 
                // - $OwnerName$, shouldn't we be talking how you're $MaidPassedDay$ overdue on my paycheck instead?
                return true;
            case 9020:
                // $script:0831180509000324$ functionID=1 
                // - I don't really have much to say.
                return true;
            case 9021:
                // $script:0831180509000325$ functionID=1 
                // - You're $MaidPassedDay$ behind on my paycheck.
                switch (selection) {
                    // $script:0831180509000326$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509000327$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509000328$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9040:
                // $script:0831180509000329$ 
                // - You're $MaidPassedDay$ behind on my paycheck.
                switch (selection) {
                    // $script:0831180509000330$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509000331$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509000332$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9030:
                // $script:0831180509000333$ 
                // - You're $MaidPassedDay$ behind on my paycheck. I know we're friends, but policy is policy.
                return true;
            case 9031:
                // $script:0831180509000334$ 
                // - You may think my mind is always on business, but you're $MaidPassedDay$ overdue on paying me, and I have bills, too...
                return true;
            case 9032:
                // $script:0831180509000335$ 
                // - I never thought you'd be like this, $OwnerName$. A contract is a promise between two parties. You seemed like someone who would keep $male:his,female:her$ word.
                return true;
            case 10:
                // $script:0831180509000336$ functionID=1 
                // - Would you like me to craft you a ring?
                return true;
            case 11:
                // $script:0831180509000337$ functionID=1 
                // - Feel free to discuss rings with me whenever you like.
                return true;
            case 20:
                // $script:0831180509000338$ functionID=1 
                // - Ah, you must wish to learn more about me.
                return true;
            case 21:
                // $script:0831180509000339$ functionID=1 
                // - But I just don't feel comfortable going into too much detail about myself...
                switch (selection) {
                    // $script:0831180509000340$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509000341$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509000342$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 22:
                // $script:0831180509000343$ functionID=1 
                // - But I just don't feel comfortable going into too much detail about myself...
                switch (selection) {
                    // $script:0831180509000344$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509000345$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509000346$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509000347$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 30:
                // $script:0831180509000348$ 
                // - You look happy today. What did you want to talk about?
                switch (selection) {
                    // $script:0831180509000349$
                    // - Did anything interesting happen?
                    case 0:
                        Id = 0; // TODO: 1000,1100,1200,1300,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509000350$
                    // - May I have a cup of tea?
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,9011 | 
                        return false;
                    // $script:0831180509000351$
                    // - Let's talk for a bit, me and you.
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509000352$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 31:
                // $script:0831180509000353$ 
                // - Oh? You have something you'd like to talk to me about?
                switch (selection) {
                    // $script:0831180509000354$
                    // - Did anything interesting happen?
                    case 0:
                        Id = 0; // TODO: 1000,1100,1200,1300,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509000355$
                    // - May I have a cup of tea?
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,9011 | 
                        return false;
                    // $script:0831180509000356$
                    // - Let's talk for a bit, me and you.
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509000357$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 32:
                // $script:0831180509000358$ 
                // - I'm not much of a talker, but as you wish.
                switch (selection) {
                    // $script:0831180509000359$
                    // - Did anything interesting happen?
                    case 0:
                        Id = 0; // TODO: 1000,1100,1200,1300,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509000360$
                    // - May I have a cup of tea?
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,9011 | 
                        return false;
                    // $script:0831180509000361$
                    // - Let's talk for a bit, me and you.
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509000362$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 40:
                // $script:0831180509000363$ 
                // - Sure, $OwnerName$. I always enjoy talking to you.
                switch (selection) {
                    // $script:0831180509000364$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509000365$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509000366$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 50:
                // $script:0831180509000367$ 
                // - Sometimes, I feel quite close to you, $OwnerName$.
                switch (selection) {
                    // $script:0831180509000368$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509000369$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509000370$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 60:
                // $script:0831180509000371$ 
                // - Hmm? Did something happen, $OwnerName$?
                switch (selection) {
                    // $script:0831180509000372$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509000373$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509000374$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 1000:
                // $script:0831180509000375$ 
                // - While nothing particularly interesting occurred today, I try to appreciate every single day that passes. Once it's gone, you can never get it back.
                // $script:0831180509000376$ 
                // - When you take time to be grateful, the world around you changes. The flowers you see, the sky above your head, even the bus that stops by the house at the same time each day, all of those become special. In the end, you realize that no two days are ever the same.
                // $script:0831180509000377$ 
                // - For example, today, right now, I'm talking to you, $OwnerName$, and that makes this moment special. Every moment we share is special.
                switch (selection) {
                    // $script:0831180509000378$
                    // - I completely agree.
                    case 0:
                        Id = 0; // TODO: 1011,1012 | 
                        return false;
                    // $script:0831180509000379$
                    // - Uh, are you feeling okay?
                    case 1:
                        Id = 0; // TODO: 1001,1002 | 
                        return false;
                }
                return true;
            case 1001:
                // $script:0831180509000380$ functionID=1 
                // - I apologize. I should be working, not spouting philosophy. If you'll excuse me...
                return true;
            case 1002:
                // $script:0831180509000381$ functionID=1 
                // - You may think it's corny, but there are many books that go into great depth about this topic. But perhaps I should keep my thoughts to myself.
                return true;
            case 1011:
                // $script:0831180509000382$ functionID=1 
                // - I knew you would, $OwnerName$. Some may think what I said is corny, but I knew you would understand.
                return true;
            case 1012:
                // $script:0831180509000383$ functionID=1 
                // - Take a deep breath. Ahhh. See? Even the air is more invigorating when you take a moment to treasure it. Thank you for chatting with me about this, $OwnerName$.
                return true;
            case 1100:
                // $script:0831180509000384$ 
                // - I was gardening today, when a grubby little dog showed up and started running around.
                // $script:0831180509000385$ 
                // - He came up to me, wagging his tail as if he wanted to play. I was elbows deep in weeds, so I wasn't sure what to do.
                switch (selection) {
                    // $script:0831180509000386$
                    // - You let a filthy dog into my garden?!
                    case 0:
                        Id = 0; // TODO: 1101,1102 | 
                        return false;
                    // $script:0831180509000387$
                    // - Awww, did you play with him? And feed him?
                    case 1:
                        Id = 0; // TODO: 1111,1112 | 
                        return false;
                }
                return true;
            case 1101:
                // $script:0831180509000388$ functionID=1 
                // - Ah, I sent him away, as gently as I could, and wiped away all his paw prints. That's all.
                return true;
            case 1102:
                // $script:0831180509000389$ 
                // - I didn't "let" him, he jumped the fence. It was no big deal. He didn't mess up your flowers or anything.
                // $script:0831180509000390$ functionID=1 
                // - He was such a cute little thing. I couldn't scold him. He was so cute, you wouldn't have been able to either, $OwnerName$.
                return true;
            case 1111:
                // $script:0831180509000391$ 
                // - I did. In fact, I probably should've asked permission before I did this, but...
                // $script:0831180509000392$ functionID=1 
                // - I also gave him a much-needed bath. He was such a cute little guy. I hope he comes back.
                return true;
            case 1112:
                // $script:0831180509000393$ 
                // - I knew you'd say that, $OwnerName$. You're just like me.
                // $script:0831180509000394$ functionID=1 
                // - I not only fed him and played with him, I also gave him a bath and brushed his fur. Then he settled down for a nice long nap at my side while I finished with the garden.
                return true;
            case 1200:
                // $script:0831180509000395$ 
                // - I had a terrible day, $OwnerName$. Are you ready to hear my horrific story?
                // $script:0831180509000396$ 
                // - I was ironing your clothes, and for some reason, I just couldn't get the seams perfect! I tried over and over and over. Seams are one of my specialties, you know.
                // $script:0831180509000397$ 
                // - I was so frustrated! I tried ironing my own clothes, starting with the one I'm wearing now.
                // $script:0831180509000398$ 
                // - And wouldn't you know, it turned out perfectly! So I went back to ironing yours, and I just couldn't do it. Ugh...
                // $script:0831180509000399$ 
                // - To conclude, none of your clothes have been ironed. What a nightmare.
                switch (selection) {
                    // $script:0831180509000400$
                    // - Hey, at least your shirt looks good.
                    case 0:
                        Id = 0; // TODO: 1211,1212 | 
                        return false;
                    // $script:0831180509000401$
                    // - Wait, so I don't have any ironed clothes to wear tomorrow?
                    case 1:
                        Id = 0; // TODO: 1201,1202 | 
                        return false;
                }
                return true;
            case 1201:
                // $script:0831180509000402$ functionID=1 
                // - That's correct. I'm so, so sorry. I feel absolutely horrible. 
                return true;
            case 1202:
                // $script:0831180509000403$ functionID=1 
                // - I have no excuse. I will stay up all through the night to attempt to get at least one outfit wrinkle-free for you to wear tomorrow.
                return true;
            case 1211:
                // $script:0831180509000404$ 
                // - I'm so sorry, I know I've completely ruined your— Excuse me? Did you just compliment me? Heh, I guess my shirt does look pretty good, doesn't it?
                // $script:0831180509000405$ functionID=1 
                // - $OwnerName$, you are an amazing person. I am honored to work for you. Let me try ironing your clothes one more time. I think I can do it this time!
                return true;
            case 1212:
                // $script:0831180509000406$ 
                // - Oh! Um. Heh. T-thank you. A servant should look presentable and sharp at all times. See this edge here? I'm normally so good at getting the seams to an extra sharp point!
                // $script:0831180509000407$ functionID=1 
                // - I feel inspired and motivated now. I will collect my ironing kit and try ironing your clothes again. Thank you for the compliment.
                return true;
            case 1300:
                // $script:0831180509000408$ 
                // - A-ah! W-what? N-nothing! Nothing happened today! N-n-nothing!
                // $script:0831180509000409$ 
                // - Ahhh, how do you always know when I'm trying to hide something, $OwnerName$?
                // $script:0831180509000410$ 
                // - Here, take a look at this paper. It says, "Your soul mate is lurking nearby. Expect an unexpected kiss at an unexpected place."
                // $script:0831180509000411$ 
                // - I got it from a fortune cookie sample at the grocery store.
                // $script:0831180509000412$ 
                // - <font color="#909090">(He takes back the paper and daintily places it in his inner pocket.)</font>
                //   I told you it was nothing.
                switch (selection) {
                    // $script:0831180509000413$
                    // - You're not taking a fortune cookie seriously, are you?
                    case 0:
                        Id = 0; // TODO: 1301,1302 | 
                        return false;
                    // $script:0831180509000414$
                    // - Hey, hey! Congratulations!
                    case 1:
                        Id = 0; // TODO: 1311,1312 | 
                        return false;
                }
                return true;
            case 1301:
                // $script:0831180509000415$ functionID=1 
                // - Who says I'm taking it seriously? You asked if anything interesting happened. I answered. Now if you'll excuse me, I have to go mend your socks.
                return true;
            case 1302:
                // $script:0831180509000416$ functionID=1 
                // - Of course not. Do you take me for an idiot? For the record, I've always carried I pack of mints on me. I didn't just start today.
                return true;
            case 1311:
                // $script:0831180509000417$ functionID=1 
                // - Wh-what? No! It's not... I'm not... Ahem. Let's not talk about this anymore.
                return true;
            case 1312:
                // $script:0831180509000418$ 
                // - You've got it all wrong, $OwnerName$. It's just a silly fortune. I'm not stupid enough to get all excited over it.
                // $script:0831180509000419$ functionID=1 
                // - Now if you'll excuse me, I believe I hear the kettle. Your tea is almost ready. Ahem.
                //   <font color="#909090">(He walks away, blushing hard.)</font>
                return true;
            case 2000:
                // $script:0831180509000420$ 
                // - Ah, today was just an ordinary day. Nothing to report, really.
                // $script:0831180509000421$ 
                // - How was your day, $OwnerName$?
                // $script:0831180509000422$ 
                // - Ah, I see. Some days pass by so peacefully. Perhaps it's days like this that make us truly happy.
                return true;
            case 2100:
                // $script:0831180509000423$ 
                // - The most notable event of the day is you talking to me, $OwnerName$. Other than that, I've just been listening to the birds chirping.
                // $script:0831180509000424$ 
                // - On days like this, I like to relax with a nice cup of tea.
                return true;
            case 3000:
                // $script:0831180509000425$ 
                // - In fact, that's just what you should do. Nothing like a sunny afternoon sipping a cup of tea. Just give me a moment to prepare it...
                // $script:0831180509000426$ functionID=1 
                // - There you go. How do you like it? It's Royal Blend with a touch of cream, perfect for an afternoon as beautiful as this one. I'll leave you to enjoy your tea in peace.
                return true;
            case 3100:
                // $script:0831180509000427$ 
                // - I recently purchases an amazing Earl Grey tea. How about I treat you to a cup, $OwnerName$? Just give me a moment, and you'll have the best tea you've ever tasted in your life.
                // $script:0831180509000428$ 
                // - Here you go. My favorite Earl Grey blend. Do you taste the bergamot flavor? Magnificent! Do you like it?
                // $script:0831180509000429$ functionID=1 
                // - I knew you would like it. The secret to brewing the perfect cup of tea is whispering for it to be delicious as you prepare it, and that's just what I did today.
                return true;
            case 4000:
                // $script:0831180509000430$ 
                // - Apologies, but I can't join you for tea at the moment. There are some items that require my immediate attention. Perhaps later.
                return true;
            case 4100:
                // $script:0831180509000431$ 
                // - Oh, would you like coffee instead of tea today? I will prepare your favorite latte, then.
                // $script:0831180509000432$ 
                // - I've carefully brewed the espresso and added fresh milk. I hope you like it. Oh, no, you don't need to save any for me. I don't drink coffee.
                return true;
            case 5000:
                // $script:0831180509000433$ 
                // - You want to know about my home? Hmm, I don't usually talk about myself. Let's see...
                // $script:0831180509000434$ 
                // - I come from a beautiful little place right by the sea, near a sharp cliff. It's cold and windy there, but the people are kind and love to sing.
                // $script:0831180509000435$ 
                // - I've been drinking tea since before I could walk.  It reminds me of home. Oh, don't worry. I'm content with my life here. I just like to reminisce sometimes.
                return true;
            case 5100:
                // $script:0831180509000436$ 
                // - You want to know my favorite hand cream? You're aware I wear gloves, aren't you? Even if I didn't, scented creams would disrupt the delicate glean of teacups and plates. It would ruin the entire tea-drinking experience.
                // $script:0831180509000437$ 
                // - When I go out out, however, I have been known to dab on a small amount of light lavender or verbena scented lotion.
                // $script:0831180509000438$ 
                // - Does that answer your question?
                return true;
            case 6000:
                // $script:0831180509000439$ 
                // - Curiosity is a powerful thing. It cultivates knowledge! It is the foundation of human civilization! Perhaps you're curious about the linen towel draped over my arm?
                // $script:0831180509000440$ 
                // - Linen towels are essential for a servant. When a spot of tea drips from a spout, the linen towel comes to the rescue. When an errant crumb falls from a cracker, the linen towel brushes it away.
                // $script:0831180509000441$ 
                // - The most important rule is to use fresh towels every hour, pristine and crisply folded. If dirtied, it is perfectly acceptable to replace the towel more often than that.
                // $script:0831180509000442$ 
                // - The linen towel has become an icon of cleanliness, professionalism, comfort, and bliss.
                return true;
            case 7000:
                // $script:0831180509000443$ 
                // - Ah, what a wonderful day. The dishes were washed to a sparkle! My heart fluttered watching the laundry fluttering in the breeze!
                // $script:0831180509000444$ 
                // - The tea I poured reminded me of someone I knew, and the water I squeezed the linen towel felt like the melody of her voice.
                // $script:0831180509000445$ 
                // - She was a childhood friend. I still remember how she held onto her wide-brimmed hat against the breeze atop that cliff, how the skirt of her white dress caressed her legs.
                // $script:0831180509000446$ 
                // - ...What am I talking about? I apologize, $OwnerName$. I've grown too comfortable around you. I never meant to share such a private memory.
                // $script:0831180509000447$ 
                // - Please forget what I just told you. I suppose even I get sentimental sometimes.
                return true;
            case 100:
                // $script:0831180509000448$ 
                // - Hello. I don't think I've seen you before. How may I help you?
                switch (selection) {
                    // $script:0831180509000449$
                    // - I'm here to see your master.
                    case 0:
                        Id = 0; // TODO: 101,102 | 
                        return false;
                    // $script:0831180509000450$
                    // - Oh, I don't need anything.
                    case 1:
                        Id = 0; // TODO: 103,104 | 
                        return false;
                    // $script:0831180509000451$
                    // - Hey, do I smell tea? It smells good!
                    case 2:
                        Id = 0; // TODO: 105,106 | 
                        return false;
                }
                return true;
            case 101:
                // $script:0831180509000452$ 
                // - Ah. Any friend of $OwnerName$ is an important guest. Please, make yourself comfortable.
                return true;
            case 102:
                // $script:0831180509000453$ 
                // - Ah, please make yourself at home. Let me know if I can help you with anything.
                return true;
            case 103:
                // $script:0831180509000454$ 
                // - Then why are you here? This property belongs to $OwnerName$. You, $male:sir,female:ma'am$, are trespassing!
                return true;
            case 104:
                // $script:0831180509000455$ 
                // - Excuse me? Then you've come into this home uninvited? I'll be watching you. One wrong move, and I'm calling the authorities.
                return true;
            case 105:
                // $script:0831180509000456$ 
                // - Why, yes! I'm brewing my favorite blend of Earl Grey. Would you like a cup?
                return true;
            case 106:
                // $script:0831180509000457$ 
                // - It does, doesn't it? Such fine tea can be recognized by scent alone. I just brewed my last scoop of English Breakfast tea. I don't know when I'll be able to get tea that fine again.
                return true;
            default:
                return true;
        }
    }
}
