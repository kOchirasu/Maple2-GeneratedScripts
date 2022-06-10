using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000773: Shadow Doc
/// </summary>
public class _11000773 : NpcScript {
    internal _11000773(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 1;2;3;4;5;6;9001;9002;9003;100
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180509002563$ 
                // - Are you hurt?
                return true;
            case 1:
                // $script:0831180509002564$ 
                // - ...Did you call me?
                switch (selection) {
                    // $script:0831180509002565$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509002566$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002567$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 2:
                // $script:0831180509002568$ 
                // - Are you wounded?
                switch (selection) {
                    // $script:0831180509002569$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509002570$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002571$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 3:
                // $script:0831180509002572$ 
                // - Please stop bothering me.
                switch (selection) {
                    // $script:0831180509002573$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509002574$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002575$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 4:
                // $script:0831180509002576$ 
                // - ...Did you call me?
                switch (selection) {
                    // $script:0831180509002577$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509002578$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002579$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509002580$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 5:
                // $script:0831180509002581$ 
                // - Are you wounded?
                switch (selection) {
                    // $script:0831180509002582$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509002583$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002584$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509002585$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 6:
                // $script:0831180509002586$ 
                // - Please stop bothering me.
                switch (selection) {
                    // $script:0831180509002587$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509002588$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002589$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509002590$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 9:
                // $script:0831180509002591$ 
                // - Did you just say you want to pay me?
                //   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
                switch (selection) {
                    // $script:0831180509002592$
                    // - Let me think about it some more.
                    case 0:
                        Id = 0; // TODO: 8040,8050,8060,9040 | 8999
                        return false;
                    // $script:0831180509002593$
                    // - (Pay $MaidSalary$.)
                    case 1:
                        Id = 0; // TODO: 8000,8001,8010,8011,8901 | 8900,8910
                        return false;
                }
                return true;
            case 8000:
                // $script:0831180509002594$ functionID=1 
                // - You've made a good decision. You scratch my back, I'll scratch yours. Heh. Heh. 
                return true;
            case 8001:
                // $script:0831180509002595$ functionID=1 
                // - I like staying with you. Our relationship is mutually beneficial, you know. Heh. Heh.
                return true;
            case 8010:
                // $script:0831180509002596$ functionID=1 
                // - I won't hold a grudge against you for neglecting me. Our relationship is strictly business, and I like that we keep a professional distance from each other. 
                return true;
            case 8011:
                // $script:0831180509002597$ functionID=1 
                // - Ah, I was getting ready to go to the Land of Darkness. Now I have to unpack everything, thanks to your indecisiveness.
                return true;
            case 8020:
                // $script:0831180509002598$ functionID=1 
                // - I got only a few days left to work here in this house. Time passes really quickly. Heh. 
                return true;
            case 8021:
                // $script:0831180509002599$ functionID=1 
                // - But then, not really news, is it? 
                switch (selection) {
                    // $script:0831180509002600$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509002601$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002602$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509002603$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8040:
                // $script:0831180509002604$ 
                // - What do you want?
                switch (selection) {
                    // $script:0831180509002605$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509002606$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002607$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509002608$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8050:
                // $script:0831180509002609$ 
                // - I'm listening.
                switch (selection) {
                    // $script:0831180509002610$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509002611$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002612$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509002613$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8060:
                // $script:0831180509002614$ 
                // - Would you stop bothering me?
                switch (selection) {
                    // $script:0831180509002615$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509002616$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002617$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509002618$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8900:
                // $script:0831180509002619$ 
                // - You probably don't have enough money. Money comes and goes, you know. 
                return true;
            case 8901:
                // $script:0831180509002620$ 
                // - Tsk, tsk. Have you heard of short-term memory loss? You've already paid me this month. You should've let me operate on you when I offered.
                return true;
            case 8910:
                // $script:0831180509002621$ 
                // - Well, well. You don't have enough money. I think I told you I only treat those who can pay me. Now that you're broke, you're of no use to me. 
                return true;
            case 8999:
                // $script:0831180509002622$ 
                // - Something's wrong, and I don't know what it is. You did't think I know everything, did you? I'm a doctor, not an encyclopedia. 
                return true;
            case 9001:
                // $script:0831180509002623$ 
                // - It's been $MaidPassedDay$. Maybe it's time I move on...
                switch (selection) {
                    // $script:0831180509002624$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509002625$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002626$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9002:
                // $script:0831180509002627$ 
                // - You still look like mushroom droppings. Then again, who am I to talk?
                switch (selection) {
                    // $script:0831180509002628$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509002629$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002630$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9003:
                // $script:0831180509002631$ 
                // - First I lose my medical license, and now I'm losing my job as a housekeeper. Go figure. 
                switch (selection) {
                    // $script:0831180509002632$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509002633$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002634$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9010:
                // $script:0831180509002635$ 
                // - You've made a critical mistake, allowing my contract to expire. Now I no longer have a reason to listen to you.
                return true;
            case 9011:
                // $script:0831180509002636$ functionID=1 
                // - Did you really think you could fool me with such shallow trickery? I know our contract has expired. 
                return true;
            case 9020:
                // $script:0831180509002637$ functionID=1 
                // - First you lose your place in society, then you lose your home, and then you even lose all the people you love. Such is life.
                return true;
            case 9021:
                // $script:0831180509002638$ functionID=1 
                // - You think that's never going to happen to you? Think again. 
                switch (selection) {
                    // $script:0831180509002639$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509002640$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002641$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9040:
                // $script:0831180509002642$ 
                // - ...You're more talkative than usual today.
                switch (selection) {
                    // $script:0831180509002643$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509002644$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002645$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9030:
                // $script:0831180509002646$ 
                // - I'm a skilled medical professional and you're not taking advantage of that. What a shame! 
                return true;
            case 9031:
                // $script:0831180509002647$ 
                // - When one has no money, one cannot hire a housekeeper or receive medical treatment... or save a person one loves. 
                return true;
            case 9032:
                // $script:0831180509002648$ 
                // - Patients are the worse. Half of them want treatment and then don't pay. That's why I ask for money upfront.
                return true;
            case 10:
                // $script:0831180509002649$ functionID=1 
                // - Want a potion that will make your head spin? Literally spin?
                return true;
            case 11:
                // $script:0831180509002650$ functionID=1 
                // - Just say the word.
                return true;
            case 20:
                // $script:0831180509002651$ functionID=1 
                // - Why do you want to know about my past?
                return true;
            case 21:
                // $script:0831180509002652$ functionID=1 
                // - You look horrible.
                switch (selection) {
                    // $script:0831180509002653$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509002654$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002655$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 22:
                // $script:0831180509002656$ functionID=1 
                // - You look horrible.
                switch (selection) {
                    // $script:0831180509002657$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509002658$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002659$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509002660$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 30:
                // $script:0831180509002661$ 
                // - I have nothing to tell you.
                switch (selection) {
                    // $script:0831180509002662$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509002663$
                    // - (Ask for treatment.)
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,9011 | 
                        return false;
                    // $script:0831180509002664$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,6100,7000,9011 | 
                        return false;
                    // $script:0831180509002665$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 31:
                // $script:0831180509002666$ 
                // - This is dull, dull, dull.
                switch (selection) {
                    // $script:0831180509002667$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509002668$
                    // - (Ask for treatment.)
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,9011 | 
                        return false;
                    // $script:0831180509002669$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,6100,7000,9011 | 
                        return false;
                    // $script:0831180509002670$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 32:
                // $script:0831180509002671$ 
                // - If you have something to say, spit it out!
                switch (selection) {
                    // $script:0831180509002672$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509002673$
                    // - (Ask for treatment.)
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,9011 | 
                        return false;
                    // $script:0831180509002674$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,6100,7000,9011 | 
                        return false;
                    // $script:0831180509002675$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 40:
                // $script:0831180509002676$ 
                // - What do you want?
                switch (selection) {
                    // $script:0831180509002677$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509002678$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002679$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 50:
                // $script:0831180509002680$ 
                // - I'm listening.
                switch (selection) {
                    // $script:0831180509002681$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509002682$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002683$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 60:
                // $script:0831180509002684$ 
                // - Would you stop bothering me?
                switch (selection) {
                    // $script:0831180509002685$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509002686$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002687$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 1000:
                // $script:0831180509002688$ 
                // - The nerve! The mistreatment! Do they have any idea who they're dealing with?!
                // $script:0831180509002689$ 
                // - A former patient barged into your house today. He claimed I had made him worse! He called me a quack! A quack!! Can you imagine?
                // $script:0831180509002690$ 
                // - It was everything I could do not to throw a bottle of ketchup at him. What do you think? Am I a quack?
                switch (selection) {
                    // $script:0831180509002691$
                    // - No, but your personality could use some work.
                    case 0:
                        Id = 0; // TODO: 1011,1012 | 
                        return false;
                    // $script:0831180509002692$
                    // - Hmm, you might be a quack...
                    case 1:
                        Id = 0; // TODO: 1001,1002 | 
                        return false;
                }
                return true;
            case 1001:
                // $script:0831180509002693$ functionID=1 
                // - What?! Where's that bottle of ketchup?!
                return true;
            case 1002:
                // $script:0831180509002694$ functionID=1 
                // - That's harsh. If I'm a quack, maybe I should stop treating you for a while, see how you like it.
                return true;
            case 1011:
                // $script:0831180509002695$ functionID=1 
                // - Who cares about personality? It's about skills! I can't believe I let him talk to me like that... I'm losing my touch.
                return true;
            case 1012:
                // $script:0831180509002696$ functionID=1 
                // - You're not afraid to speak your mind, are you? Heh. Heh. Heh.
                return true;
            case 1100:
                // $script:0831180509002697$ 
                // - What do you know about the Land of Darkness?
                // $script:0831180509002698$ 
                // - A gateway has opened to that dangerous world. Not much is known, but I believe incredible treasure hides in that world...
                // $script:0831180509002699$ 
                // - And the Alliance is too frightened to go find it! They won't let anyone else go, either. Isn't that idiotic?!
                switch (selection) {
                    // $script:0831180509002700$
                    // - It's good to be cautious.
                    case 0:
                        Id = 0; // TODO: 1101,1102 | 
                        return false;
                    // $script:0831180509002701$
                    // - I completely agree with you.
                    case 1:
                        Id = 0; // TODO: 1111,1112 | 
                        return false;
                }
                return true;
            case 1101:
                // $script:0831180509002702$ functionID=1 
                // - Hmpf! You're just as cowardly as they are!
                return true;
            case 1102:
                // $script:0831180509002703$ functionID=1 
                // - Are you afraid? At least you're honest about it.
                return true;
            case 1111:
                // $script:0831180509002704$ functionID=1 
                // - Heh, heh! I knew we spoke the same language!
                return true;
            case 1112:
                // $script:0831180509002705$ functionID=1 
                // - Ah... So you're as dangerous as I am. Heh, heh!
                return true;
            case 2000:
                // $script:0831180509002706$ 
                // - Some teenager barged into the house today.
                // $script:0831180509002707$ 
                // - He was pale and his eyes were a bit crazed. He started yelling for a doctor.
                // $script:0831180509002708$ 
                // - I told him I was a doctor and that he didn't have to yell. He told me to treat him. He acted like he was going to die if I didn't.
                // $script:0831180509002709$ 
                // - But I'm the ruthless $MaidName$!
                // $script:0831180509002710$ 
                // - I told him he had to pay me first. He begged me on his hands and knees, then left when he realized he couldn't change my mind. He didn't even apologize when he left!
                // $script:0831180509002711$ 
                // - Young folks these days are so spoiled. They think they can get everything for free. I really hope he's not dead out there somewhere, though.
                return true;
            case 2100:
                // $script:0831180509002712$ 
                // - Today was a productive day. I treated so many patients. My wallet is bursting with mesos.
                // $script:0831180509002713$ 
                // - Some of them were attacked by monsters. Some fell from high places. One tripped into lava.
                // $script:0831180509002714$ 
                // - When you're hurt, you have no choice but to find the closest doctor you can, no matter how much he charges, heh heh heh heh.
                // $script:0831180509002715$ 
                // - That's why I like staying here with you. Our relationship is mutually beneficial, you know.
                return true;
            case 2200:
                // $script:0831180509002716$ 
                // - A bunch of angry militia members barged in here today. They said this was my last warning. Next time they would arrest me.
                // $script:0831180509002717$ 
                // - My crimes? Overcharging my patients and... having ketchup stains on my clothes, which supposely distresses our neighbors!
                // $script:0831180509002718$ 
                // - It's nonsense. I charge my patients what I think I'm worth, and I'm worth more than most doctors.
                // $script:0831180509002719$ 
                // - And they're making fun of my clothes now? What are they, children?
                // $script:0831180509002720$ 
                // - The idiocy of this world boggles my mind. Well! They can threaten me all they want, I'm not budging.
                return true;
            case 3000:
                // $script:0831180509002721$ 
                // - I'll treat you for free, but it's just this once. No more freebies after this.
                // $script:0831180509002722$ 
                // - Let's see... Hm... Was it here? 
                //   <font color="#909090">(He digs around, searching for something.)</font>
                // $script:0831180509002723$ 
                // - This is bad. Really bad. We need to operate right away.
                // $script:0831180509002724$ functionID=1 
                // - You have a serious, serious case of... hypochondria! Hah hah!
                return true;
            case 3100:
                // $script:0831180509002725$ 
                // - Sure, $OwnerName$, and I'll add the bill to my monthly salary.
                // $script:0831180509002726$ 
                // - I have a few questions for you. One, do you feel constantly tired, no matter how much you sleep?
                // $script:0831180509002727$ 
                // - Oh, you do? I see. Two, do you have bouts of dizziness and lack of appetite?
                // $script:0831180509002728$ 
                // - I see, I see. Finally, three, do you find yourself more forgetful these days?
                // $script:0831180509002729$ 
                // - I see. Heh. Heh. Just as I suspected.
                // $script:0831180509002730$ functionID=1 
                // - You're not sick, $OwnerName$. You're aging. Hah, hah.
                return true;
            case 4000:
                // $script:0831180509002731$ 
                // - You can pay, right? If you don't have money, don't expect me to treat you.
                // $script:0831180509002732$ 
                // - You think people's lives and health are more important than mesos...
                // $script:0831180509002733$ 
                // - I was like you once, naive and believing the best in people...
                // $script:0831180509002734$ 
                // - It doesn't matter now. The fact is, I'm not treating anyone unless I'm paid.
                return true;
            case 4100:
                // $script:0831180509002735$ 
                // - Uh oh, not good. You're a tiny bit sniffly and the slightest bit warm. You need an operation at once!
                // $script:0831180509002736$ 
                // - We don't have time to discuss details about the illness. You wouldn't know it even if I told you. The important thing now is to put you under as fast as we can!
                // $script:0831180509002737$ 
                // - Why do you keep resisting? Don't you trust me?
                // $script:0831180509002738$ 
                // - Fine, we'll do it later. That's your choice, but let me tell you, you're going to regret it... Tsk.
                return true;
            case 5000:
                // $script:0831180509002739$ 
                // - You keep looking at the stains on my shirt.
                // $script:0831180509002740$ 
                // - Don't look so queasy. It's just ketchup. 
                // $script:0831180509002741$ 
                // - I just love ketchup. Sweet and tangy, with that cool texture sliding down your throat. I have to eat some every time I get a craving, and trust me, that happens a lot.
                // $script:0831180509002742$ 
                // - $OwnerName$, you want some? Don't be shy. Open wide, and I'll squeeze some into your mouth. Come on, aaaaah.
                return true;
            case 5100:
                // $script:0831180509002743$ 
                // - My patients in the Land of Darkness generally suffer from more serious ailments than the ones from other parts of Maple World.
                // $script:0831180509002744$ 
                // - That's not surprising. They're wounded by the thralls of the Shadow Domination, after all.
                // $script:0831180509002745$ 
                // - Shadow Power is no joke. You can't resist it. Those who try, pay dearly.
                // $script:0831180509002746$ 
                // - If you must ever venture into the Land of Darkness, be extra cautious. Move in shadows. Do not draw attention to yourself.
                // $script:0831180509002747$ 
                // - Don't be like the fools who trust in their own strength, thinking they can handle what comes at them. They always end up in my office.
                return true;
            case 6000:
                // $script:0831180509002748$ 
                // - You want to know why I practice in a dangerous place like the Land of Darkness?
                // $script:0831180509002749$ 
                // - Because of rest of Maple World is filled with blockheads. I can't stand it!
                // $script:0831180509002750$ 
                // - I used to use $item:20000046$ to help my patients deal with pain. It's surprisingly effective.
                // $script:0831180509002751$ 
                // - It was an act of compassion, but the association revoked my license for using a banned drug.
                // $script:0831180509002752$ 
                // - It's just as well. I didn't like being a member of their organization anyway. Heh heh.
                return true;
            case 7000:
                // $script:0831180509002753$ 
                // - My family is gone. It's my fault. 
                // $script:0831180509002754$ 
                // - I had a daughter once. She had a laugh that would melt anyone's heart.
                // $script:0831180509002755$ 
                // - She was sick. Her illness was supposedly incurable.
                // $script:0831180509002756$ 
                // - I researched like a madman, until I learned of a mysterious herb that grows only in the Shadow World. It would have healed her.
                // $script:0831180509002757$ 
                // - But nothing from that world could be brought to this one. We're not allowed to even enter that world, let alone use items found there...
                // $script:0831180509002758$ 
                // - I lost my daughter because I was too afraid to break the law. Hah. How stupid is that?
                return true;
            case 100:
                // $script:0831180509002759$ 
                // - Yeesh, you look awful.
                switch (selection) {
                    // $script:0831180509002760$
                    // - Help... me... please!
                    case 0:
                        Id = 0; // TODO: 101,102 | 
                        return false;
                    // $script:0831180509002761$
                    // - Don't worry about me. I'm fine.
                    case 1:
                        Id = 0; // TODO: 103,104 | 
                        return false;
                    // $script:0831180509002762$
                    // - Who are you?
                    case 2:
                        Id = 0; // TODO: 105,106 | 
                        return false;
                }
                return true;
            case 101:
                // $script:0831180509002763$ 
                // - You bet. I require payment upfront.
                return true;
            case 102:
                // $script:0831180509002764$ 
                // - I recognize a hypochondriac when I see one.
                return true;
            case 103:
                // $script:0831180509002765$ 
                // - Are you sure? You look ghastly pale. Stop acting so tough and come over here. Let me take a look at you.
                return true;
            case 104:
                // $script:0831180509002766$ 
                // - Are you sure?  All right, but if you start dying, kindly leave the premises. I wouldn't want to clean that up.
                return true;
            case 105:
                // $script:0831180509002767$ 
                // - Do you live under a rock? How have you not heard of me?!
                return true;
            case 106:
                // $script:0831180509002768$ 
                // - Do you not see the ketchup stains on my gown? I'm a doctor. Hah hah hah!
                return true;
            default:
                return true;
        }
    }
}
