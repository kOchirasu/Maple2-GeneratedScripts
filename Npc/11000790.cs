using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000790: Squattush
/// </summary>
public class _11000790 : NpcScript {
    internal _11000790(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 1;2;3;4;5;6;9001;9002;9003;100
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180509004994$ 
                // - Hmph! What in blazes is it?
                return true;
            case 1:
                // $script:0831180509004995$ 
                // - Why do you keep summoning me? Don't you know I'm old?
                switch (selection) {
                    // $script:0831180509004996$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004997$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004998$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 2:
                // $script:0831180509004999$ 
                // - Hmph! Why do you keep bothering me?
                switch (selection) {
                    // $script:0831180509005000$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005001$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005002$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 3:
                // $script:0831180509005003$ 
                // - All right, all right. What do ya wanna to talk about?
                switch (selection) {
                    // $script:0831180509005004$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005005$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005006$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 4:
                // $script:0831180509005007$ 
                // - Why do you keep summoning me? Don't you know I'm old?
                switch (selection) {
                    // $script:0831180509005008$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005009$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005010$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509005011$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 5:
                // $script:0831180509005012$ 
                // - Hmph! Why do you keep bothering me?
                switch (selection) {
                    // $script:0831180509005013$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005014$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005015$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509005016$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 6:
                // $script:0831180509005017$ 
                // - All right, all right. What do ya wanna to talk about?
                switch (selection) {
                    // $script:0831180509005018$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005019$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005020$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509005021$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 9:
                // $script:0831180509005022$ 
                // - Did you just say you're going to pay me?
                //   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
                switch (selection) {
                    // $script:0831180509005023$
                    // - Let me think about it some more.
                    case 0:
                        Id = 0; // TODO: 8040,8050,8060,9040 | 8999
                        return false;
                    // $script:0831180509005024$
                    // - (Pay $MaidSalary$.)
                    case 1:
                        Id = 0; // TODO: 8000,8001,8010,8011,8901 | 8900,8910
                        return false;
                }
                return true;
            case 8000:
                // $script:0831180509005025$ functionID=1 
                // - Ooh, has it been that long already? Thanks for hiring me again. Hah hah.
                return true;
            case 8001:
                // $script:0831180509005026$ functionID=1 
                // - Ah, you're paying me early. Great! My, my, you're glowing today! 
                return true;
            case 8010:
                // $script:0831180509005027$ functionID=1 
                // - Hah, you're never home. Been working the old grind, eh? Good, good. I'm proud of ya.
                return true;
            case 8011:
                // $script:0831180509005028$ functionID=1 
                // - Aw, you've disappointed me for so long, but you've made it up to me now. I feel like I can fly! I'll let your slight slide, hah hah.
                return true;
            case 8020:
                // $script:0831180509005029$ functionID=1 
                // - $OwnerName$, you know what day it is? You'd better check your calendar. Our contract expires soon. You'll take care of it, right? 
                return true;
            case 8021:
                // $script:0831180509005030$ functionID=1 
                // - I don't have to worry, do I?
                switch (selection) {
                    // $script:0831180509005031$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005032$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005033$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509005034$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8040:
                // $script:0831180509005035$ 
                // - Why do you keep summoning me? Don't you know I'm old?
                switch (selection) {
                    // $script:0831180509005036$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005037$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005038$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509005039$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8050:
                // $script:0831180509005040$ 
                // - Hmph! Why do you keep bothering me?
                switch (selection) {
                    // $script:0831180509005041$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005042$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005043$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509005044$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8060:
                // $script:0831180509005045$ 
                // - All right, all right. What do ya wanna to talk about?
                switch (selection) {
                    // $script:0831180509005046$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005047$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005048$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509005049$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8900:
                // $script:0831180509005050$ 
                // - If you don't have the money, maybe I should teach you how to beg on the streets. Your pride won't keep you from starving, right?
                return true;
            case 8901:
                // $script:0831180509005051$ 
                // - Tsk. So young, but you're more senile than I am! You've already paid me for the month! 
                return true;
            case 8910:
                // $script:0831180509005052$ 
                // - Hmph, how dare you tease me! Pretending to pay someone when you have no intention of actually paying is worth than giving someone something and then taking it away! You little rascal!
                return true;
            case 8999:
                // $script:0831180509005053$ 
                // - Huh? Th-this... Well, this... Ahem! If you don't know what's going on, just keep quiet.
                return true;
            case 9001:
                // $script:0831180509005054$ 
                // - Tsk, tsk. Young people these days have no patience.
                switch (selection) {
                    // $script:0831180509005055$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509005056$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005057$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9002:
                // $script:0831180509005058$ 
                // - You don't want me anymore. Is that it?
                switch (selection) {
                    // $script:0831180509005059$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509005060$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005061$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9003:
                // $script:0831180509005062$ 
                // - Ugh... My bones hurt... 
                switch (selection) {
                    // $script:0831180509005063$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509005064$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005065$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9010:
                // $script:0831180509005066$ 
                // - Hey, our contract expired. You're still gonna feed me, right?
                return true;
            case 9011:
                // $script:0831180509005067$ functionID=1 
                // - Hmph, what are you doing? Our contract expired. Stop changing the subject, and check the contract.
                return true;
            case 9020:
                // $script:0831180509005068$ functionID=1 
                // - It's been $MaidPassedDay$... Any good news?
                return true;
            case 9021:
                // $script:0831180509005069$ functionID=1 
                // - Will I ever stop worrying about money? 
                switch (selection) {
                    // $script:0831180509005070$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509005071$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005072$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9040:
                // $script:0831180509005073$ 
                // - I got this job because I didn't want to beg anymore... Ugh... 
                switch (selection) {
                    // $script:0831180509005074$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509005075$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005076$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9030:
                // $script:0831180509005077$ 
                // - I didn't ask you to pay my medical bills or give me an allowance. All I asked was that you feed me three times a day, and you failed at even that! How can you sleep at night, knowing this frail old man is starving?
                return true;
            case 9031:
                // $script:0831180509005078$ 
                // - My vision is getting weaker, my hearing isn't any better, and I feel fainter by the day. I don't have many days left, you know. How would you feel if all of a sudden, whoosh, I'm gone? You should be nice to me while you still can. 
                return true;
            case 9032:
                // $script:0831180509005079$ 
                // - Maybe it's time I quit and go back to where I truly belong: the streets of $map:02000051$.
                return true;
            case 10:
                // $script:0831180509005080$ functionID=1 
                // - Mm? Do you have something to ask me?
                return true;
            case 11:
                // $script:0831180509005081$ functionID=1 
                // - Sure. I earn my keep.
                return true;
            case 20:
                // $script:0831180509005082$ functionID=1 
                // - What do you want to know about a lonely old man?
                return true;
            case 21:
                // $script:0831180509005083$ functionID=1 
                // - Ugh... I hate being old...
                switch (selection) {
                    // $script:0831180509005084$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005085$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005086$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 22:
                // $script:0831180509005087$ functionID=1 
                // - Ugh... I hate being old...
                switch (selection) {
                    // $script:0831180509005088$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005089$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005090$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509005091$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 30:
                // $script:0831180509005092$ 
                // - If you have something to say, then say it.
                switch (selection) {
                    // $script:0831180509005093$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509005094$
                    // - Tell me my fortune!
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,9011 | 
                        return false;
                    // $script:0831180509005095$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509005096$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 31:
                // $script:0831180509005097$ 
                // - What? You want me to tell your fortune?
                switch (selection) {
                    // $script:0831180509005098$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509005099$
                    // - Tell me my fortune!
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,9011 | 
                        return false;
                    // $script:0831180509005100$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509005101$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 32:
                // $script:0831180509005102$ 
                // - I can hear you just fine. Tell me.
                switch (selection) {
                    // $script:0831180509005103$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509005104$
                    // - Tell me my fortune!
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,9011 | 
                        return false;
                    // $script:0831180509005105$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509005106$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 40:
                // $script:0831180509005107$ 
                // - Why do you keep summoning me? Don't you know I'm old?
                switch (selection) {
                    // $script:0831180509005108$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005109$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005110$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 50:
                // $script:0831180509005111$ 
                // - Hmph! Why do you keep bothering me?
                switch (selection) {
                    // $script:0831180509005112$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005113$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005114$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 60:
                // $script:0831180509005115$ 
                // - All right, all right. What do ya wanna to talk about?
                switch (selection) {
                    // $script:0831180509005116$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005117$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005118$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 1000:
                // $script:0831180509005119$ 
                // - I want to ask you something.
                // $script:0831180509005120$ 
                // - You may think I'm a crazy old coot, but I'm not doing this because I like it.
                // $script:0831180509005121$ 
                // - Am I bothering you? Be honest. I won't get mad.
                switch (selection) {
                    // $script:0831180509005122$
                    // - Honestly... yes.
                    case 0:
                        Id = 0; // TODO: 1001,1002 | 
                        return false;
                    // $script:0831180509005123$
                    // - I know you have your reasons.
                    case 1:
                        Id = 0; // TODO: 1011,1012 | 
                        return false;
                }
                return true;
            case 1001:
                // $script:0831180509005124$ functionID=1 
                // - What? Y-y-y-you rascal! Haven't you heard you're supposed to talk to your elders with respect?! What is this world coming to?
                return true;
            case 1002:
                // $script:0831180509005125$ functionID=1 
                // - What?! You think you'll be young and healthy forever, little punk?
                return true;
            case 1011:
                // $script:0831180509005126$ functionID=1 
                // - You're not as stupid as I thought. Hah hah.
                return true;
            case 1012:
                // $script:0831180509005127$ functionID=1 
                // - Hah hah, you shouldn't say that, knuclehead. Hah hah.
                return true;
            case 1100:
                // $script:0831180509005128$ 
                // - Are you sure you don't want to learn how to beg?
                // $script:0831180509005129$ 
                // - I don't make as much as I used to. I've become too famous.
                // $script:0831180509005130$ 
                // - You have the makings of a good beggar. So how about it? Want to beg with me on the streets of $map:2000051$?
                switch (selection) {
                    // $script:0831180509005131$
                    // - No.
                    case 0:
                        Id = 0; // TODO: 1111,1112 | 
                        return false;
                    // $script:0831180509005132$
                    // - Yes.
                    case 1:
                        Id = 0; // TODO: 1101,1102 | 
                        return false;
                }
                return true;
            case 1101:
                // $script:0831180509005133$ functionID=1 
                // - I didn't think you'd say yes. Are you sure? You're young, but already a lost cause. Tsk.
                return true;
            case 1102:
                // $script:0831180509005134$ functionID=1 
                // - You little...! That was a test, and you failed miserably!
                return true;
            case 1111:
                // $script:0831180509005135$ functionID=1 
                // - No other job is as stable as begging, but I guess you're too young to stoop so low. All right, just don't say I didn't ask.
                return true;
            case 1112:
                // $script:0831180509005136$ functionID=1 
                // - Starve for three days, and you'll be willing to do anything. When it happens, we'll see.
                return true;
            case 2000:
                // $script:0831180509005137$ 
                // - You little rascal! Do you treat your own grandfather this way?
                // $script:0831180509005138$ 
                // - How could you leave me alone in the house for so long? Do you know how bored I've been?
                // $script:0831180509005139$ 
                // - I've been a beggar for all my life, but that doesn't mean you can treat me like this! I'm going to tell the neighbors!
                // $script:0831180509005140$ 
                // - You're sorry? Sorry doesn't cut it. Although... if you give me some mesos, I might forgive you. But until then, forget it!
                return true;
            case 2100:
                // $script:0831180509005141$ 
                // - Nah, nothing happened today. But hey, what do you think of these clothes? They look like they were made for me, don't they?
                // $script:0831180509005142$ 
                // - I got them from that wardrobe over there, hah hah.
                // $script:0831180509005143$ 
                // - You have such nice clothes, and you never wear them, so I thought someone ought to enjoy them.
                // $script:0831180509005144$ 
                // - Huh? I'm wearing a dress? You rascal! You're only saying that because you don't want me to wear your clothes.
                // $script:0831180509005145$ 
                // - You're more cunning than I am. You'll go far in life.
                return true;
            case 2200:
                // $script:0831180509005146$ 
                // - Aaaack, my arms! Ugh, my legs! Oooouch, my shoulders, my back, my knees.  It's going to rain today.
                // $script:0831180509005147$ 
                // - I don't care how sunny it looks right now. Trust me. It's going to pour soon.
                // $script:0831180509005148$ 
                // - I'm soooo achy. My whole body hurts. I wish I had something to soothe my muscles. Hint, hint, hint...
                return true;
            case 3000:
                // $script:0831180509005149$ 
                // - Heh heh, if you want to see your fortune, you'd better have some money.
                // $script:0831180509005150$ 
                // - Eeeeeh! Aaaaaah! Mushroom god, swine god, slime god, hear me! Daaaaance!
                // $script:0831180509005151$ 
                // - Oooh, I see it! I see it! $OwnerName$'s future!
                // $script:0831180509005152$ 
                // - Your future holds incredible luck! You will succeed in every enchanting attempt, find amazing items in dungeons, and pick up ten billion mesos that other people dropped on the ground!!
                // $script:0831180509005153$ functionID=1 
                // - Hey, if it turns out not to be true, don't blame me. I'm only relaying the vision the gods gave me, and sometimes, it's a little hazy...
                return true;
            case 3100:
                // $script:0831180509005154$ 
                // - Heh heh, if you want to see your fortune, you'd better have some money.
                // $script:0831180509005155$ 
                // - Eeeeeh! Aaaaaah! Mushroom god, swine god, slime god, hear me! Daaaaance!
                // $script:0831180509005156$ 
                // - Oooh, I see it! I see it! $OwnerName$'s future!
                // $script:0831180509005157$ 
                // - ...You will discover truth hidden in darkness... And protect the red maple leaf from the clutch of shadow...
                // $script:0831180509005158$ functionID=1 
                // - ...You will save the last life of the cursed tribe... Umm... Hah hah, this isn't like my other fortunes. I must have eaten something funny when taking out the garbage last night.
                return true;
            case 4000:
                // $script:0831180509005159$ 
                // - Heh heh, if you want to see your fortune, you'd better have some money.
                // $script:0831180509005160$ 
                // - Eeeeeh! Aaaaaah! Mushroom god, swine god, slime god, hear me! Daaaaance!
                // $script:0831180509005161$ 
                // - Oooh, I see it! I see it! $OwnerName$'s future!
                // $script:0831180509005162$ 
                // - Wow, your luck is so bad today that if you were to fall backwards and hit the back of your head, you'd also break your nose somehow.
                // $script:0831180509005163$ 
                // - Tsk. On days like this, you shouldn't leave the house. Come on. Let's go watch TV together. I'll keep you safe.
                return true;
            case 4100:
                // $script:0831180509005164$ 
                // - Heh heh, if you want to see your fortune, you'd better have some money.
                // $script:0831180509005165$ 
                // - Eeeeeh! Aaaaaah! Mushroom god, swine god, slime god, hear me! Daaaaance!
                // $script:0831180509005166$ 
                // - Oooh, I see it! I see it! $OwnerName$'s future!
                // $script:0831180509005167$ 
                // - The aura of romance floats in the west.
                //   If you're single, you won't be for much longer.
                //   If you're attached, your love will soon be tested.
                // $script:0831180509005168$ 
                // - Hah hah, well, good for you, $OwnerName$. Just don't overlook those who are dressed in brown. Heh heh.
                return true;
            case 5000:
                // $script:0831180509005169$ 
                // - Why are you harassing me? You're just like the rest, looking down on me because I'm a beggar.
                // $script:0831180509005170$ 
                // - I may beg for money in $map:02000051$, but I was a charming warrior in my day.
                // $script:0831180509005171$ 
                // - You don't believe me? You little rascal, I'm telling the truth! Even $npcName:11000075[gender:1]$ swooned over me.
                return true;
            case 5100:
                // $script:0831180509005172$ 
                // - This is why I hate getting old. People just start to think you're going senile. But without my generation, you wouldn't exist, you knucklehead.
                // $script:0831180509005173$ 
                // - Mm? What's this? A coupon I can use at $map:02000107$. Wow, is this really for me?
                // $script:0831180509005174$ 
                // - I knew you were good, deep down inside! How'd you know I wanted to look nice?
                // $script:0831180509005175$ 
                // - I would look so different right now if only... Ah... Never mind, just talking to myself. Hah hah.
                // $script:0831180509005176$ 
                // - Anyway, thank you for your kindness. Mushroom god, swine god, pour your blessings upon $OwnerName$.
                return true;
            case 6000:
                // $script:0831180509005177$ 
                // - Hey, you know where I can find some ancient tomes? I need to check something.
                // $script:0831180509005178$ 
                // - And don't you dare suggest $map:02000031$. I've already been there. Not only was the librarian completely unreasonable...
                // $script:0831180509005179$ 
                // - But I've already looked through every single book there. They didn't have the one I wanted.
                // $script:0831180509005180$ 
                // - I heard there's a magic library inside a forest... Heard of it? They just might have something that'll help me lift this curse... 
                // $script:0831180509005181$ 
                // - What? Nothing. I just needed to check something. But if you don't know where it is, just forget the whole thing.
                return true;
            case 7000:
                // $script:0831180509005182$ 
                // - Grrr, that hag... One day, I'll make her... Aah! How long have you been standing there?
                // $script:0831180509005183$ 
                // - Hmph, why are you so interested in other people's business? Nothing is going on!
                // $script:0831180509005184$ 
                // - If you've got so much time on your hands, you should get out there and hunt some monsters. Hunt a lot, so you can feed me!
                // $script:0831180509005185$ 
                // - Or how'd you like to go to $map:02000051$ and beg with me? No, don't put on your boots. I was only kidding! Tsk.
                return true;
            case 100:
                // $script:0831180509005186$ 
                // - Alms for the poor. Alms for the ugly. Take pity on an old man...
                switch (selection) {
                    // $script:0831180509005187$
                    // - (Give him money.)
                    case 0:
                        Id = 0; // TODO: 101,102 | 
                        return false;
                    // $script:0831180509005188$
                    // - (Refuse.)
                    case 1:
                        Id = 0; // TODO: 103,104 | 
                        return false;
                    // $script:0831180509005189$
                    // - (Pretend you don't see him.)
                    case 2:
                        Id = 0; // TODO: 105,106 | 
                        return false;
                }
                return true;
            case 101:
                // $script:0831180509005190$ 
                // - Such kindness! Thank you! Gods bless you! You are an angel from heaven!
                return true;
            case 102:
                // $script:0831180509005191$ 
                // - Thank you, thank you! I'm taking this straight to spend at the $map:02000138$.
                return true;
            case 103:
                // $script:0831180509005192$ 
                // - You heartless, no-good... So cold! I hope you get eliminated in the first round of $map:61000001$!
                return true;
            case 104:
                // $script:0831180509005193$ 
                // - Y-y-y-you little...! Get out of my sight!
                return true;
            case 105:
                // $script:0831180509005194$ 
                // - So rude! Beggars are people, too!!
                return true;
            case 106:
                // $script:0831180509005195$ 
                // - Tsk. What is this world coming to? Pathetic.
                return true;
            default:
                return true;
        }
    }
}
