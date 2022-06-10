using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000787: Kay
/// </summary>
public class _11000787 : NpcScript {
    internal _11000787(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 1;2;3;4;5;6;9001;9002;9003;100
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180509004348$ 
                // - Just tell me what you need!
                return true;
            case 1:
                // $script:0831180509004349$ 
                // - And today, our very special guest is... Oh! Hi, $OwnerName$! I was just practicing, hehe.
                switch (selection) {
                    // $script:0831180509004350$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004351$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004352$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 2:
                // $script:0831180509004353$ 
                // - Oh, did you call me?
                switch (selection) {
                    // $script:0831180509004354$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004355$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004356$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 3:
                // $script:0831180509004357$ 
                // - Do you have something to say?
                switch (selection) {
                    // $script:0831180509004358$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004359$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004360$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 4:
                // $script:0831180509004361$ 
                // - And today, our very special guest is... Oh! Hi, $OwnerName$! I was just practicing, hehe.
                switch (selection) {
                    // $script:0831180509004362$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004363$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004364$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509004365$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 5:
                // $script:0831180509004366$ 
                // - Oh, did you call me?
                switch (selection) {
                    // $script:0831180509004367$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004368$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004369$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509004370$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 6:
                // $script:0831180509004371$ 
                // - Do you have something to say?
                switch (selection) {
                    // $script:0831180509004372$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004373$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004374$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509004375$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 9:
                // $script:0831180509004376$ 
                // - You want to give me my paycheck?
                //   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
                switch (selection) {
                    // $script:0831180509004377$
                    // - Let me think about it some more.
                    case 0:
                        Id = 0; // TODO: 8040,8050,8060,9040 | 8999
                        return false;
                    // $script:0831180509004378$
                    // - (Pay $MaidSalary$.)
                    case 1:
                        Id = 0; // TODO: 8000,8001,8010,8011,8901 | 8900,8910
                        return false;
                }
                return true;
            case 8000:
                // $script:0831180509004379$ functionID=1 
                // - I'm touched! You're so busy yet you still remembered to pay me! I promise to be the best servant ever!
                return true;
            case 8001:
                // $script:0831180509004380$ functionID=1 
                // - You take such good care of me. I can't thank you enough. I am forever indebted to you! 
                return true;
            case 8010:
                // $script:0831180509004381$ functionID=1 
                // - I knew you wouldn't abandon me, $OwnerName$. I promise to never, ever disappoint you!
                return true;
            case 8011:
                // $script:0831180509004382$ functionID=1 
                // - Ahem! There may have been a slight misunderstanding between us. As a token of my regret, I'd like you to be the first guest on my show when it opens!
                return true;
            case 8020:
                // $script:0831180509004383$ functionID=1 
                // - Good day, studio audience. I'd like to introduce you to our special guest for the day, $OwnerName$! Now, the million meso question, $OwnerName$... Our employment contract is expiring soon. Are you planning to extend it?
                return true;
            case 8021:
                // $script:0831180509004384$ functionID=1 
                // - Yes? No? Ahem, are you planning to answer?
                switch (selection) {
                    // $script:0831180509004385$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004386$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004387$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509004388$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8040:
                // $script:0831180509004389$ 
                // - Did you have something to say to me?
                switch (selection) {
                    // $script:0831180509004390$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004391$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004392$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509004393$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8050:
                // $script:0831180509004394$ 
                // - What a wonderful day, isn't it?
                switch (selection) {
                    // $script:0831180509004395$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004396$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004397$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509004398$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8060:
                // $script:0831180509004399$ 
                // - What's wrong?
                switch (selection) {
                    // $script:0831180509004400$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004401$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004402$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509004403$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8900:
                // $script:0831180509004404$ 
                // - Ah... Bwahahaha! Oh, $OwnerName$, you're hilarious! That was a joke, right? I mean, why would you say you're paying me when you don't even have the money?
                return true;
            case 8901:
                // $script:0831180509004405$ 
                // - Yes or no, $OwnerName$. Do you realize you've already paid me for the month? Ahem! How'd I do? Did I sound serious? A good host has to know how to ask the deep, probing questions!
                return true;
            case 8910:
                // $script:0831180509004406$ 
                // - $OwnerName$, enough with the jokes already. If you have no money, why do you keep saying you're paying me?
                return true;
            case 8999:
                // $script:0831180509004407$ 
                // - Hmm, I've never encountered situation like this before. I'm, well, I'm flustered! Excuse me while I grab a glass of water.
                return true;
            case 9001:
                // $script:0831180509004408$ 
                // - Someone once said that positive minds attract good luck!
                switch (selection) {
                    // $script:0831180509004409$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509004410$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004411$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9002:
                // $script:0831180509004412$ 
                // - $OwnerName$, did something good happen today? Hm?
                switch (selection) {
                    // $script:0831180509004413$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509004414$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004415$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9003:
                // $script:0831180509004416$ 
                // - Please stop doing this. You're hurting my heart... 
                switch (selection) {
                    // $script:0831180509004417$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509004418$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004419$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9010:
                // $script:0831180509004420$ 
                // - I could give you a list of two dozen reason why asking someone to labor without pay is wrong... Or you could just renew my contract.
                return true;
            case 9011:
                // $script:0831180509004421$ functionID=1 
                // - I received a call today from Helping Hands notifying me that our contract had expired. I was so busy dreaming of which guests to invite to my show that I hadn't even noticed. Were you aware, $OwnerName$?
                return true;
            case 9020:
                // $script:0831180509004422$ functionID=1 
                // - Ahem! It's been $MaidPassedDay$ since I stopped working for you...
                return true;
            case 9021:
                // $script:0831180509004423$ functionID=1 
                // - W-wait, you're not thinking about letting me go permanently, are you?
                switch (selection) {
                    // $script:0831180509004424$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509004425$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004426$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9040:
                // $script:0831180509004427$ 
                // - I will never give up my role as a servant or as a talk show host!  
                switch (selection) {
                    // $script:0831180509004428$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509004429$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004430$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9030:
                // $script:0831180509004431$ 
                // - Is this because I'm always talking about my future show? Be honest. Does it annoy you?
                return true;
            case 9031:
                // $script:0831180509004432$ 
                // - Excuse me?! You think I should give up my dream and return to making smoothies? No way! I didn't come this far just to give up! 
                return true;
            case 9032:
                // $script:0831180509004433$ 
                // - Welcome to my show, ladies and gentlemen! I have with me, $OwnerName$, brave defender of Maple World. Well, $OwnerName$? Fight any big monsters today? Discover any amazing items? What's the latest?
                return true;
            case 10:
                // $script:0831180509004434$ functionID=1 
                // - Believe it or not, I used to work at a juice bar.
                return true;
            case 11:
                // $script:0831180509004435$ functionID=1 
                // - Ask me for any drink you want.
                return true;
            case 20:
                // $script:0831180509004436$ functionID=1 
                // - Nice to meet you. I'm Maple World's greatest talk show host, $MaidName$! Ahem, aspiring talk show host.
                return true;
            case 21:
                // $script:0831180509004437$ functionID=1 
                // - By the way, was there something you needed?
                switch (selection) {
                    // $script:0831180509004438$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004439$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004440$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 22:
                // $script:0831180509004441$ functionID=1 
                // - By the way, was there something you needed?
                switch (selection) {
                    // $script:0831180509004442$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004443$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004444$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509004445$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 30:
                // $script:0831180509004446$ 
                // - Sure, you can tell me anything.
                switch (selection) {
                    // $script:0831180509004447$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509004448$
                    // - (Help him practice for his show.)
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,9011 | 
                        return false;
                    // $script:0831180509004449$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509004450$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 31:
                // $script:0831180509004451$ 
                // - Did you have something to say to me?
                switch (selection) {
                    // $script:0831180509004452$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509004453$
                    // - (Help him practice for his show.)
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,9011 | 
                        return false;
                    // $script:0831180509004454$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509004455$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 32:
                // $script:0831180509004456$ 
                // - Just thinking about my show makes my heart flutter.
                switch (selection) {
                    // $script:0831180509004457$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509004458$
                    // - (Help him practice for his show.)
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,9011 | 
                        return false;
                    // $script:0831180509004459$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509004460$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 40:
                // $script:0831180509004461$ 
                // - Did you have something to say to me?
                switch (selection) {
                    // $script:0831180509004462$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004463$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004464$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 50:
                // $script:0831180509004465$ 
                // - What a wonderful day, isn't it?
                switch (selection) {
                    // $script:0831180509004466$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004467$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004468$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 60:
                // $script:0831180509004469$ 
                // - What's wrong?
                switch (selection) {
                    // $script:0831180509004470$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004471$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004472$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 1000:
                // $script:0831180509004473$ 
                // - $OwnerName$, be honest with me about something.
                // $script:0831180509004474$ 
                // - You hired me as your servant, and I've been loudly practicing my show host skills every single day.
                // $script:0831180509004475$ 
                // - Does it bother you? Please be honest.
                switch (selection) {
                    // $script:0831180509004476$
                    // - Nah, it's entertaining.
                    case 0:
                        Id = 0; // TODO: 1011,1012 | 
                        return false;
                    // $script:0831180509004477$
                    // - I hate it so much.
                    case 1:
                        Id = 0; // TODO: 1001,1002 | 
                        return false;
                }
                return true;
            case 1001:
                // $script:0831180509004478$ functionID=1 
                // - ...I see. I don't get many jobs hosting shows, and I'm terrible at keeping house. I don't know what to do...
                return true;
            case 1002:
                // $script:0831180509004479$ functionID=1 
                // - Your honesty hurts, $OwnerName$. Sheesh.
                return true;
            case 1011:
                // $script:0831180509004480$ functionID=1 
                // - You really think so? Then my dream has a chance at coming true, right?!
                return true;
            case 1012:
                // $script:0831180509004481$ functionID=1 
                // - Entertaining? Me? That's the sweetest compliment anyone's ever given me in my entire life. Thank you!!
                return true;
            case 1100:
                // $script:0831180509004482$ 
                // - Every single day, I practice my hosting skills, but I can't help but worry sometimes.
                // $script:0831180509004483$ 
                // - I really want to be a great talk show host, but I'm just not sure I'll ever get my big break.
                // $script:0831180509004484$ 
                // - I'm not getting any younger, and you know they like to hire young. Should I just go back to working at the juice bar? What do you think?
                switch (selection) {
                    // $script:0831180509004485$
                    // - It's not the end of the world to just stick to what you're good at.
                    case 0:
                        Id = 0; // TODO: 1101,1102 | 
                        return false;
                    // $script:0831180509004486$
                    // - Never, ever give up!
                    case 1:
                        Id = 0; // TODO: 1111,1112 | 
                        return false;
                }
                return true;
            case 1101:
                // $script:0831180509004487$ functionID=1 
                // - Yeah? Maybe I'm just not cut out for bring a host. Excuse me... I'd like to be alone for a while.
                return true;
            case 1102:
                // $script:0831180509004488$ functionID=1 
                // - You think so? I never thought being good at something would break my heart. If only I were good at what I really, truly want to do...
                return true;
            case 1111:
                // $script:0831180509004489$ functionID=1 
                // - ...You're right. You're absolutely right! Shame on me for even considering giving up. It was a moment of weakness.
                return true;
            case 1112:
                // $script:0831180509004490$ functionID=1 
                // - Yes! That's the spirit! I won't give up on my dreams, $OwnerName$!
                return true;
            case 2000:
                // $script:0831180509004491$ 
                // - Oh, our next door neighbor stopped by.
                // $script:0831180509004492$ 
                // - I was practicing for my show, when someone banged on the door.
                // $script:0831180509004493$ 
                // - I guess he thought I was too loud. He told me to keep it down so he could sleep, but I knew fate had sent him to me.
                // $script:0831180509004494$ 
                // - I needed someone to be the guest on my show. On my practice show.
                // $script:0831180509004495$ 
                // - It went great! Now I have confidence that I can run my show seamlessly, no matter how wacky the guest is.
                // $script:0831180509004496$ 
                // - I hope he can help again tomorrow! He looked thoroughly exhausted when he left, though...
                return true;
            case 2100:
                // $script:0831180509004497$ 
                // - Come to think of it, $npcName:11000012[gender:0]$ stopped by this afternoon to give me some mail.
                // $script:0831180509004498$ 
                // - I was hoping it was an invitation from the palace to host some grand event, but it was from $npcName:11000171[gender:0]$. He wants me to host his son's ninth birthday party.
                // $script:0831180509004499$ 
                // - That's not as exciting as a royal event, but beggars can't be choosers. And us twingos need to help each other, you know?
                // $script:0831180509004500$ 
                // - I'm going to make $npcName:11000171[gender:0]$'s son's birthday the best event ever! Now, if you'll excuse me, I've got to get practicing.
                return true;
            case 2200:
                // $script:0831180509004501$ 
                // - I hope I get to host something amazing soon. Like... Like... Like $npcName:11000075[gender:1]$'s wedding!
                // $script:0831180509004502$ 
                // - It'd be such an honor. My family would be so proud! Just the thought of it is making my pulse race!
                // $script:0831180509004503$ 
                // - I mean, she's not even engaged... And she can't even hold public events right now... But it would be such a fantastic, magical, beautiful event, don't you think? Ahh, I can dream, can't I?
                return true;
            case 3000:
                // $script:0831180509004504$ 
                // - Every show needs a special segment that captures the hearts and imagination of the masses.
                // $script:0831180509004505$ 
                // - ...Oooh, how about this? "Special: Help $npcName:11000075[gender:1]$ Find Her Man!"
                // $script:0831180509004506$ 
                // - I'd invite $npcName:11000075[gender:1]$ to come on the show and then help her find the man of her dreams! Like, I could have her choose between $npcName:11000119[gender:0]$ and $npcName:11000076[gender:0]$, and then let her keep choosing between people until she found her perfect match!
                // $script:0831180509004507$ functionID=1 
                // - I can definitely make this work. I just need to get $npcName:11000075[gender:1]$ to agree to come on the show. All right, then! Off to the palace! I'm sure she can make time for me. La, la, laaaa!
                return true;
            case 3100:
                // $script:0831180509004508$ 
                // - I've been asked to prepare a special twingo show. Oooh, I get butterflies just thinking about it!
                // $script:0831180509004509$ 
                // - There are so many possibilities! A twingo talent show, a twingo reality show, or, oooh, maybe a twingo dance contest?
                // $script:0831180509004510$ functionID=1 
                // - I can't make up my mind! $OwnerName$, what do you think?
                return true;
            case 4000:
                // $script:0831180509004511$ 
                // - Okay, $OwnerName$, let's practice for the world's greatest talk show!
                // $script:0831180509004512$ 
                // - Hellooooo, ladies and gentlemen! It's me, your cute and super talented host, $MaidName$!!
                // $script:0831180509004513$ 
                // - ...Ugh, that sounds corny. It totally sets the wrong tone!
                return true;
            case 4100:
                // $script:0831180509004514$ 
                // - Hello, studio audience! Welcome to The $MaidName$ Show!
                // $script:0831180509004515$ 
                // - Our guest today is the one and only... $OwnerName$! Come on in, $OwnerName$.
                // $script:0831180509004516$ 
                // - So, what's the latest, $OwnerName$?
                // $script:0831180509004517$ 
                // - Huh? You've been busy leveling? No, no, no, $OwnerName$. What kind boring answer is that? I know this is just practice, but try to take it seriously, okay?
                return true;
            case 5000:
                // $script:0831180509004518$ 
                // - Practicing every day takes a toll on my vocal cords, and these babies are vital to my career.
                // $script:0831180509004519$ 
                // - That's why I try not to talk too much when I'm not practicing. I mean it. Please don't talk to me unless it's necessary, okay?
                // $script:0831180509004520$ 
                // - ...
                //   ...
                //   ...
                //   Are you really just going to stop talking to me now? Because I asked you to? Really?
                return true;
            case 5100:
                // $script:0831180509004521$ 
                // - You may have wondered why I accepted a job with Helping Hands when my dream is to be a talk show host, but you don't understand.
                // $script:0831180509004522$ 
                // - Here, I get to practice my show-hosting skills around the clock, and I get paid for it! Also, strangers barge in all the time...
                // $script:0831180509004523$ 
                // - And I get to pretend they're guests on my show! A great host knows how to respond to unexpected situations with poise.
                // $script:0831180509004524$ 
                // - I end up interviewing them as I would if they were guests on the show. Sure, most of them try to sneak out in the middle of the interview, but I don't let them move an inch until I'm done with them.
                return true;
            case 6000:
                // $script:0831180509004525$ 
                // - Ahh, I wish I could host the event in $map:02000064$. I'm positive I could make it so much more exciting.
                // $script:0831180509004526$ 
                // - I've offered my services to the palace several times and get the same response every time:
                // $script:0831180509004527$ 
                // - "Thank you for your interest. That event does not require a host." I just don't get it!
                // $script:0831180509004528$ 
                // - Think about it! If you were in the $map:61000001$ audience, wouldn't you have fun trying to guess the winner?
                // $script:0831180509004529$ 
                // - But according to the palace, that's too close to gambling, which is prohibited.
                // $script:0831180509004530$ 
                // - Hmph. The palace is a rather old-fashioned, if you ask me.
                return true;
            case 7000:
                // $script:0831180509004531$ 
                // - In my younger days, I worked at a juice bar. My joy in life was listening to the customers and making their tasty drinks.
                // $script:0831180509004532$ 
                // - One day, one of the regulars came looking sad. He has broken up with his girlfriend a week ago and just couldn't get over it. I knew he needed a good laugh.
                // $script:0831180509004533$ 
                // - So I went all out. I listened to him, then I told him jokes and funny stories.
                // $script:0831180509004534$ 
                // - He left that night with a smile on his face, and it made me realize what I really want to do with my life.
                // $script:0831180509004535$ 
                // - My dream is to become Maple World's greatest show host! I have a long way to go, but I'll get there one day.
                return true;
            case 100:
                // $script:0831180509004536$ 
                // - Let's give a warm welcome our first guest of the day to The $MaidName$ Show, $MyPCName$!
                switch (selection) {
                    // $script:0831180509004537$
                    // - Uh. Hi?
                    case 0:
                        Id = 0; // TODO: 101,102 | 
                        return false;
                    // $script:0831180509004538$
                    // - What do you mean?
                    case 1:
                        Id = 0; // TODO: 103,104 | 
                        return false;
                    // $script:0831180509004539$
                    // - Get me out of here. Immediately.
                    case 2:
                        Id = 0; // TODO: 105,106 | 
                        return false;
                }
                return true;
            case 101:
                // $script:0831180509004540$ 
                // - Exactly! Hi! Now, tell us alllll about your interesting life!
                return true;
            case 102:
                // $script:0831180509004541$ 
                // - Well, hi back! Make yourself comfy. You'll be with us for the next two hours, spilling all the juicy details of your fascinating life!
                return true;
            case 103:
                // $script:0831180509004542$ 
                // - Don't be shy, now. Just be yourself! Go on, say hello to our studio audience!
                return true;
            case 104:
                // $script:0831180509004543$ 
                // - No need to be confused, my friend. We're about to dive into our first segment of the day: "Juicy Details of $MyPCName$'s Personal Life"!
                return true;
            case 105:
                // $script:0831180509004544$ 
                // - Oh, no. Please! I haven't had a guest on my pretend show for three hours!
                return true;
            case 106:
                // $script:0831180509004545$ 
                // - Please! Even if you're busy, spare me an hour—no, thirty minutes!
                return true;
            default:
                return true;
        }
    }
}
