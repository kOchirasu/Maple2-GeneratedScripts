using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000777: Cordelia
/// </summary>
public class _11000777 : NpcScript {
    internal _11000777(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 1;2;3;4;5;6;9001;9002;9003;100
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180509002981$ 
                // - What is it, meow?
                return true;
            case 1:
                // $script:0831180509002982$ 
                // - Meow! Welcome home.
                switch (selection) {
                    // $script:0831180509002983$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509002984$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002985$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 2:
                // $script:0831180509002986$ 
                // - Did you call me, meow?
                switch (selection) {
                    // $script:0831180509002987$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509002988$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002989$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 3:
                // $script:0831180509002990$ 
                // - Meow? How long have you been standing there?
                switch (selection) {
                    // $script:0831180509002991$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509002992$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002993$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 4:
                // $script:0831180509002994$ 
                // - Meow! Welcome home.
                switch (selection) {
                    // $script:0831180509002995$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509002996$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509002997$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509002998$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 5:
                // $script:0831180509002999$ 
                // - Did you call me, meow?
                switch (selection) {
                    // $script:0831180509003000$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003001$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003002$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509003003$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 6:
                // $script:0831180509003004$ 
                // - Meow? How long have you been standing there?
                switch (selection) {
                    // $script:0831180509003005$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003006$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003007$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509003008$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 9:
                // $script:0831180509003009$ 
                // - Are you going to give me those shiny blue things?
                //   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
                switch (selection) {
                    // $script:0831180509003010$
                    // - (Refuse to pay.)
                    case 0:
                        Id = 0; // TODO: 8040,8050,8060,9040 | 8999
                        return false;
                    // $script:0831180509003011$
                    // - (Pay $MaidSalary$.)
                    case 1:
                        Id = 0; // TODO: 8000,8001,8010,8011,8901 | 8900,8910
                        return false;
                }
                return true;
            case 8000:
                // $script:0831180509003012$ functionID=1 
                // - I'll take it! So pretty, meow!
                return true;
            case 8001:
                // $script:0831180509003013$ functionID=1 
                // - $npcName:11000708$ said it's important to trust my servant, but that doesn't happen overnight. Keep paying me early, and I'll grow to trust you.
                return true;
            case 8010:
                // $script:0831180509003014$ functionID=1 
                // - I'd like to think that you were too busy saving the world from utter catastrophe to pay me on time, meow. I'm glad you eventually remembered your priorities.
                return true;
            case 8011:
                // $script:0831180509003015$ functionID=1 
                // - I was just thinking that perhaps I should fire you and search for a better servant, but it seems you've realized the error of your ways. I'll show you some grace... this time... 
                return true;
            case 8020:
                // $script:0831180509003016$ functionID=1 
                // - $OwnerName$, our contract expires soon. Do I really have to remind you of things like this, meow?
                return true;
            case 8021:
                // $script:0831180509003017$ functionID=1 
                // - You might be more work than you're worth...
                switch (selection) {
                    // $script:0831180509003018$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003019$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003020$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509003021$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8040:
                // $script:0831180509003022$ 
                // - What is it, meow?
                switch (selection) {
                    // $script:0831180509003023$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003024$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003025$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509003026$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8050:
                // $script:0831180509003027$ 
                // - $OwnerName$, what took so long? Servants shouldn't neglect their masters, meow.
                switch (selection) {
                    // $script:0831180509003028$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003029$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003030$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509003031$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8060:
                // $script:0831180509003032$ 
                // - Did you call me, meow?
                switch (selection) {
                    // $script:0831180509003033$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003034$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003035$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509003036$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8900:
                // $script:0831180509003037$ 
                // - Don't you have any more of those shiny blue things? I feel so unmotivated if I don't get some once every month or so.
                return true;
            case 8901:
                // $script:0831180509003038$ 
                // - Did you already give me your monthly tribute? You're as forgetful as $npcName:11000075[gender:1]$.
                return true;
            case 8910:
                // $script:0831180509003039$ 
                // - Don't you have any more of those shiny blue things? I feel so unmotivated if I don't get some once every month or so.
                return true;
            case 8999:
                // $script:0831180509003040$ 
                // - Meow... I'm sleepy... Let's do it later... Zzz... 
                return true;
            case 9001:
                // $script:0831180509003041$ 
                // - I must... have more... of those shiny... blue... things!
                switch (selection) {
                    // $script:0831180509003042$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509003043$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003044$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9002:
                // $script:0831180509003045$ 
                // - No longer interested in me? Hm! Bad servant! Bad!
                switch (selection) {
                    // $script:0831180509003046$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509003047$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003048$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9003:
                // $script:0831180509003049$ 
                // - Haven't you forgotten something, meow?  
                switch (selection) {
                    // $script:0831180509003050$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509003051$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003052$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9010:
                // $script:0831180509003053$ 
                // - I don't feel like it. Hey, if you give me some of those pretty blue things, I might change my mind.
                return true;
            case 9011:
                // $script:0831180509003054$ functionID=1 
                // - Mew...  I want to go back to $map:02000025$. I should've never left the castle, meow...
                return true;
            case 9020:
                // $script:0831180509003055$ functionID=1 
                // - I haven't eaten for$MaidPassedDay$! Must get more shiny blue thingies!
                return true;
            case 9021:
                // $script:0831180509003056$ functionID=1 
                // - Can't you see the circles under my eyes?
                switch (selection) {
                    // $script:0831180509003057$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509003058$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003059$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9040:
                // $script:0831180509003060$ 
                // - You really are oblivious, aren't you?
                switch (selection) {
                    // $script:0831180509003061$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509003062$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003063$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9030:
                // $script:0831180509003064$ 
                // - ...Meow...  
                //   <font color="#909090">(She peers at you for 3 seconds, and then turns around and moves away.)</font>
                return true;
            case 9031:
                // $script:0831180509003065$ 
                // - I'm going to find myself another servant, meow.
                return true;
            case 9032:
                // $script:0831180509003066$ 
                // - Meow.
                //   <font color="#909090">(She circles around you, rubs her face against your leg, and then softly walks away.)</font>
                return true;
            case 10:
                // $script:0831180509003067$ functionID=1 
                // - Want some shiny blue things, meow? Want me to go pick some up?
                return true;
            case 11:
                // $script:0831180509003068$ functionID=1 
                // - Finding shiny things is my favorite, meow.
                return true;
            case 20:
                // $script:0831180509003069$ functionID=1 
                // - Meow, are you curious about me?
                return true;
            case 21:
                // $script:0831180509003070$ functionID=1 
                // - Meow, you're no fun.
                switch (selection) {
                    // $script:0831180509003071$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003072$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003073$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 22:
                // $script:0831180509003074$ functionID=1 
                // - Meow, you're no fun.
                switch (selection) {
                    // $script:0831180509003075$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003076$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003077$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509003078$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 30:
                // $script:0831180509003079$ 
                // - Cats can't talk... Is that what you think?
                switch (selection) {
                    // $script:0831180509003080$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,1200,1300,1400,1500,1600,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509003081$
                    // - (Play with her.)
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,4200,4300,9011 | 
                        return false;
                    // $script:0831180509003082$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509003083$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 31:
                // $script:0831180509003084$ 
                // - I'm bored, meow. Play with me.
                switch (selection) {
                    // $script:0831180509003085$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,1200,1300,1400,1500,1600,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509003086$
                    // - (Play with her.)
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,4200,4300,9011 | 
                        return false;
                    // $script:0831180509003087$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509003088$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 32:
                // $script:0831180509003089$ 
                // - I'm sleepy, meow...
                switch (selection) {
                    // $script:0831180509003090$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,1200,1300,1400,1500,1600,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509003091$
                    // - (Play with her.)
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,4200,4300,9011 | 
                        return false;
                    // $script:0831180509003092$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509003093$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 40:
                // $script:0831180509003094$ 
                // - What is it, meow?
                switch (selection) {
                    // $script:0831180509003095$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003096$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003097$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 50:
                // $script:0831180509003098$ 
                // - $OwnerName$, what took so long? Servants shouldn't neglect their masters, meow.
                switch (selection) {
                    // $script:0831180509003099$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003100$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003101$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 60:
                // $script:0831180509003102$ 
                // - Did you call me, meow?
                switch (selection) {
                    // $script:0831180509003103$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003104$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003105$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 1000:
                // $script:0831180509003106$ 
                // - Take this food, meow. I went out for a stroll and picked it up next door. No one was home. It was sitting out on the kitchen counter waiting for me.
                // $script:0831180509003107$ 
                // - I started eating it but then remembered you, $OwnerName$. You should be thankful. I don't always share.
                switch (selection) {
                    // $script:0831180509003108$
                    // - You stole this food!
                    case 0:
                        Id = 0; // TODO: 1001,1002 | 
                        return false;
                    // $script:0831180509003109$
                    // - Thank you.
                    case 1:
                        Id = 0; // TODO: 1011,1012 | 
                        return false;
                }
                return true;
            case 1001:
                // $script:0831180509003110$ functionID=1 
                // - Stolen? Do you forget who I am? Everything I see is rightfully mine. The minister never understood that...
                return true;
            case 1002:
                // $script:0831180509003111$ functionID=1 
                // - If that bothers you, why are you eating it? It's a little dirty because I had to drag it all this way, but you seem content enough.
                return true;
            case 1011:
                // $script:0831180509003112$ functionID=1 
                // - You're welcome, meow. I'll bring you something tomorrow, too.
                return true;
            case 1012:
                // $script:0831180509003113$ functionID=1 
                // - Of course. I take care of my minions, when the mood strikes. Tomorrow, I'll take my walk through the palace.
                return true;
            case 1100:
                // $script:0831180509003114$ 
                // - Whoop, this reminds me...
                // $script:0831180509003115$ 
                // - We can snack together, meow. Go on, take some. Mm? You want to know where I get this?
                // $script:0831180509003116$ 
                // - When you're not home, $OwnerName$, a girl stops by to play with me and give me treats. I wasn't hungry earlier, so I saved this for you.
                switch (selection) {
                    // $script:0831180509003117$
                    // - Girl? What girl?
                    case 0:
                        Id = 0; // TODO: 1111,1112 | 
                        return false;
                    // $script:0831180509003118$
                    // - You let a stranger into the house?!
                    case 1:
                        Id = 0; // TODO: 1101,1102 | 
                        return false;
                }
                return true;
            case 1101:
                // $script:0831180509003119$ functionID=1 
                // - Are you deaf, servant? She's not a stranger, she's my friend. Now go away for a while.
                return true;
            case 1102:
                // $script:0831180509003120$ functionID=1 
                // - Well, you weren't here to screen our guest. What do I hire you for anyway, servant?
                return true;
            case 1111:
                // $script:0831180509003121$ functionID=1 
                // - I never asked her name, meow. She's from Carimia Island, where she lives with grandpa. She works around here, though. She's cute, but not as cute as me!
                return true;
            case 1112:
                // $script:0831180509003122$ 
                // - I'm not sure. I think she also lives with a servant, like I do. She seems lonely because her servant is rarely home, too.
                // $script:0831180509003123$ functionID=1 
                // - She visits me when she's lonely, meow. Between you and me, I don't think she's much of a cook...
                return true;
            case 1200:
                // $script:0831180509003124$ 
                // - You've been looking a bit ragged, so I got this for you. You don't want to know where I got it.
                // $script:0831180509003125$ 
                // - It's a health drink. It should perk you right up.
                switch (selection) {
                    // $script:0831180509003126$
                    // - No, no, you take it. I insist.
                    case 0:
                        Id = 0; // TODO: 1211,1212 | 
                        return false;
                    // $script:0831180509003127$
                    // - Where did you get it?
                    case 1:
                        Id = 0; // TODO: 1201,1202 | 
                        return false;
                }
                return true;
            case 1201:
                // $script:0831180509003128$ functionID=1 
                // - You're gonna regret asking... I nabbed it from $map:2000065$ while I was in $map:2000025$. The minister drinks it, so it's got to be good.
                return true;
            case 1202:
                // $script:0831180509003129$ functionID=1 
                // - I picked it up in $map:2000025$ $map:2000065$. Hey, my minions deserve the best.
                return true;
            case 1211:
                // $script:0831180509003130$ functionID=1 
                // - No thank you. I had a sip and did not enjoy the flavor. But it's good for your health, so you should drink every last drop.
                return true;
            case 1212:
                // $script:0831180509003131$ 
                // - I'm touched, meow. Servant, I had no idea you cared so much!
                // $script:0831180509003132$ functionID=1 
                // - But you should take it. You're the peon who pays the rent, so I need you in good health.
                return true;
            case 1300:
                // $script:0831180509003133$ 
                // - Meow. $OwnerName$, I've got something to tell you.
                // $script:0831180509003134$ 
                // - You must be hungry. Eat this, meow. I must be the only cat who worries about her minions this much.
                // $script:0831180509003135$ 
                // - Meow? Why are you looking at me like that?
                switch (selection) {
                    // $script:0831180509003136$
                    // - Did you cook this?
                    case 0:
                        Id = 0; // TODO: 1301,1302 | 
                        return false;
                    // $script:0831180509003137$
                    // - I'm just so touched!
                    case 1:
                        Id = 0; // TODO: 1311,1312 | 
                        return false;
                }
                return true;
            case 1301:
                // $script:0831180509003138$ functionID=1 
                // - Don't be silly, meow. Have you ever seen a cat cooking?
                return true;
            case 1302:
                // $script:0831180509003139$ functionID=1 
                // - I didn't cook it, meow. I picked it up next door.
                return true;
            case 1311:
                // $script:0831180509003140$ functionID=1 
                // - Aww, you're easy. I'll bring stuff more often, then.
                return true;
            case 1312:
                // $script:0831180509003141$ functionID=1 
                // - It's just leftovers. Don't read too much into it. 
                return true;
            case 1400:
                // $script:0831180509003142$ 
                // - Look at this, meow. I found it under the bed while playing with some ants.
                // $script:0831180509003143$ 
                // - Weren't you looking for this, meow?
                switch (selection) {
                    // $script:0831180509003144$
                    // - Ants?! Where?!
                    case 0:
                        Id = 0; // TODO: 1411,1412 | 
                        return false;
                    // $script:0831180509003145$
                    // - Thank you.
                    case 1:
                        Id = 0; // TODO: 1401,1402 | 
                        return false;
                }
                return true;
            case 1401:
                // $script:0831180509003146$ functionID=1 
                // - Don't make it a habit. It's your job to look after me, not the other way around.
                return true;
            case 1402:
                // $script:0831180509003147$ functionID=1 
                // - You're welcome. There are other things under the bed, but I forbid you to look.
                return true;
            case 1411:
                // $script:0831180509003148$ functionID=1 
                // - We were enjoying our time together when they suddenly stopped moving. Maybe they were sleepy after being tossed into the air and stomped on. Should I be worried about them?
                return true;
            case 1412:
                // $script:0831180509003149$ functionID=1 
                // - They went back home, meow. It's all right. Their family is so big that I see them everywhere.
                return true;
            case 1500:
                // $script:0831180509003150$ 
                // - Look at this, meow! It looks like new, doesn't it? I think we can use it!
                // $script:0831180509003151$ 
                // - Want to know where I got it? There's a girl who drops by when you're not home. She left it here as a gift, looking totally bummed out about it.
                switch (selection) {
                    // $script:0831180509003152$
                    // - I know just the spot for it!
                    case 0:
                        Id = 0; // TODO: 1501,1502 | 
                        return false;
                    // $script:0831180509003153$
                    // - Girl? What girl?
                    case 1:
                        Id = 0; // TODO: 1511,1512 | 
                        return false;
                }
                return true;
            case 1501:
                // $script:0831180509003154$ functionID=1 
                // - Where? Where? Oooh, I can't wait to see!
                return true;
            case 1502:
                // $script:0831180509003155$ functionID=1 
                // - That's right. It's ours now! Let's do what we want with it!
                return true;
            case 1511:
                // $script:0831180509003156$ 
                // - She lives with her servant, just like I do. She's pretty cute, even with her glasses. I don't know her name, though.
                // $script:0831180509003157$ functionID=1 
                // - Her servant must have been displeased she picked something up from the street. How rude!
                return true;
            case 1512:
                // $script:0831180509003158$ 
                // - She lives in the neighborhood. I only knows that she's from an island, meow.
                // $script:0831180509003159$ functionID=1 
                // - She looked upset. I think her servant yelled at her. She said the servant called the item trash! I told her she should fire her servant, but then she started crying. 
                return true;
            case 1600:
                // $script:0831180509003160$ 
                // - I was taking a stroll when I found something shiny, so I brought it home with me. I almost didn't see it because it was covered in dirt, meow.
                // $script:0831180509003161$ 
                // - It doesn't look like it's good for anything, but you can have it if you want, meow.
                switch (selection) {
                    // $script:0831180509003162$
                    // - Thanks! I'd love more if you find more!
                    case 0:
                        Id = 0; // TODO: 1611,1612 | 
                        return false;
                    // $script:0831180509003163$
                    // - More! I must have more!
                    case 1:
                        Id = 0; // TODO: 1601,1602 | 
                        return false;
                }
                return true;
            case 1601:
                // $script:0831180509003164$ functionID=1 
                // - That's all I've got. Why are your eyes gleaming like a crazy person's?
                return true;
            case 1602:
                // $script:0831180509003165$ functionID=1 
                // - I don't have any more. But if it's that great, I'm going to keep the next one I find.
                return true;
            case 1611:
                // $script:0831180509003166$ functionID=1 
                // - Meow? You like it? It's not even edible... But I can bring you more next time.
                return true;
            case 1612:
                // $script:0831180509003167$ functionID=1 
                // - $map:2000025$ is full of shiny things, meow. I'll bring more if I go there next time.
                return true;
            case 2000:
                // $script:0831180509003168$ 
                // - Nothing at all, meow. What could possibly happen in such a tiny house?
                // $script:0831180509003169$ 
                // - Unless you're interested in the cockroaches. I played with them all day.
                // $script:0831180509003170$ 
                // - But they suddenly stopped playing with me! If they didn't like me pulling off their legs, they should've said so.
                return true;
            case 2100:
                // $script:0831180509003171$ 
                // - Strange people keep barging into the house. Do you owe them money or something?
                // $script:0831180509003172$ 
                // - It's okay if you do. I've got it under control. I just look at them with large sparkly eyes, and they leave with a dreamy look on their faces.
                return true;
            case 2200:
                // $script:0831180509003173$ 
                // - Yes, I was bored! So, so bored! It's not nice to leave me alone for so long!
                // $script:0831180509003174$ 
                // - A friend visited today. $npcName:11000367$ from Barrota Harbor.
                // $script:0831180509003175$ 
                // - He brought his girlfriend, and they were all lovey dovey. Say, $OwnerName$, do you have someone you love? Why don't you introduce me sometime?
                return true;
            case 3000:
                // $script:0831180509003176$ 
                // - ...! Did you see that? Look!! A red dot! It's moving there... and there... and back there...!
                // $script:0831180509003177$ functionID=1 
                // - I'm gonna catch it! Catch it! Yes, come here, come to me, gotcha!
                return true;
            case 3100:
                // $script:0831180509003178$ 
                // - ...A feather rod? I'm going to pluck out all the feathers!
                // $script:0831180509003179$ functionID=1 
                // - Kyaah! I was so close to catching it! Servant, you're getting better at snapping your wrist! Good!
                return true;
            case 4000:
                // $script:0831180509003180$ 
                // - What are we playing today, meow? A ball? It's... flyinnnngggg! Come to meeeeee!
                // $script:0831180509003181$ 
                // - Kyaah! I got it, meow! Meow? You want me to fetch it. No! It's mine now, and I'm going to toy with it all day long!
                return true;
            case 4100:
                // $script:0831180509003182$ 
                // - What's this? What's inside? Let me in, let me in, let me in... I will get in!
                // $script:0831180509003183$ 
                // - It's a... bit snug, but it's okay. Meow, so comfy! I'm sleepy... meow... Zzz... 
                return true;
            case 5000:
                // $script:0831180509003184$ 
                // - $OwnerName$, as my servant, there are a few things you should know about me.
                // $script:0831180509003185$ 
                // - First, I like dark, tight places where I can curl up. I hate open spaces and the cold. You shouldn't disturb me when I sleep inside your sock drawer.
                // $script:0831180509003186$ 
                // - Second, I hate loud noises, such as vacuum cleaners. Those are forbidden in this house!
                // $script:0831180509003187$ 
                // - Third, I love grooming myself, meow. I love to lick my hair and nails clean, but I don't like bathing. 
                // $script:0831180509003188$ 
                // - Huh? You want to tell me a few thing about yourself too? I can already tell you'll be trouble. We've got time. You can tell me all about you later.
                return true;
            case 5100:
                // $script:0831180509003189$ 
                // - Haven't you heard it's rude to pry? But, if you insist on knowing more about me...
                // $script:0831180509003190$ 
                // - I'm from $map:2000025$. $npc:11000075[gender:1]$ loves cats. Have you ever been in the presence of her fine cat, $npc:11000708$?
                // $script:0831180509003191$ 
                // - $npc:11000075[gender:1]$ loves $npc:11000708$ like her own child. That's probably why it became a trend among the nobility to raise cats. Cats like me.
                // $script:0831180509003192$ 
                // - Life at the palace was peaceful, but $npc:11000708$ said something to me that was life-changing. She said, "$MaidName$, you should find someone who loves you as much as the Empress loves me." So I set out to do just that.
                // $script:0831180509003193$ 
                // - Oh, I'm not saying that person is you, $OwnerName$. Oh, no no. Let's not jump to conclusions.
                return true;
            case 6000:
                // $script:0831180509003194$ 
                // - $npc:11000708$ is the $npc:11000075[gender:1]$'s favorite cat. A slender body, beautiful golden hair, a shiny ribbon... And I've descended from an equally noble bloodline.
                // $script:0831180509003195$ 
                // - But $npc:11000708$'s beauty isn't what makes her so great, meow. The $npc:11000075[gender:1]$ relies on her for comfort. I don't want to imagine what Maple World would be like if $npc:11000708$ didn't exist...
                // $script:0831180509003196$ 
                // - Want to know how important $npc:11000075[gender:1]$ is to her owner? Being the Empress of Maple World is not easy, meow. $npc:11000708$ once didn't go to the bathroom for three days to stay with the Empress while she was in deep anguish.
                // $script:0831180509003197$ 
                // - I want to be as loyal as $npc:11000708$, but I can't not go to the bathroom for three days, mew. $OwnerName$, please make sure I never have to choose between you and the bathroom. 
                return true;
            case 7000:
                // $script:0831180509003198$ 
                // - When I lived in the Palace, I used to look forward to the Cat Assembly. It's a meeting among the courtiers who love cats, meow. It's hosted by the $npc:11000075[gender:1]$, and the guests of honor are us cats.
                // $script:0831180509003199$ 
                // - At the meeting, everyone from the $npc:11000075[gender:1]$ to $npc:11000601[gender:1]$ and even the guards laugh and chat regardless of station, meow. No one mentions serious subjects like the Lapentas or the Shadow World.
                // $script:0831180509003200$ 
                // - It was always fun to hear what was going on in the palace. Oh, speaking of which, I remember something $npc:11000708$ told me, meow.
                // $script:0831180509003201$ 
                // - Everyone thinks the Empress stays in the palace all the time, working, but she goes out sometimes, meow. When she does, she disguises herself and crawls through a hole in a corner of the castle wall.
                // $script:0831180509003202$ 
                // - One time, she went to her hair salon in $map:52000008$... and got caught by $npcName:11000702[gender:0]$, meow!
                // $script:0831180509003203$ 
                // - The Empress quickly used $skill:20000011$ to scale the castle wall and run away from him, meow. Who knew she was good at $skill:20000011$? I'd love to see her use it one day.
                return true;
            case 100:
                // $script:0831180509003204$ 
                // - You're a stranger, meow.  I hate strangers... 
                switch (selection) {
                    // $script:0831180509003205$
                    // - (Pat her on the head.) 
                    case 0:
                        Id = 0; // TODO: 101,102 | 
                        return false;
                    // $script:0831180509003206$
                    // - (Rub her belly.)
                    case 1:
                        Id = 0; // TODO: 103,104 | 
                        return false;
                    // $script:0831180509003207$
                    // - Here, kitty kitty kitty.
                    case 2:
                        Id = 0; // TODO: 105,106 | 
                        return false;
                }
                return true;
            case 101:
                // $script:0831180509003208$ 
                // - How dare you touch me, lowly human?!
                return true;
            case 102:
                // $script:0831180509003209$ 
                // - Everyone who visits the house wants to touch me, meow. But do they think to ask first? Noooo.
                return true;
            case 103:
                // $script:0831180509003210$ 
                // - Kyaawwoonngghh! Not there! Get away from me!!
                return true;
            case 104:
                // $script:0831180509003211$ 
                // - Rude!!!
                return true;
            case 105:
                // $script:0831180509003212$ 
                // - ...?
                return true;
            case 106:
                // $script:0831180509003213$ 
                // - ...Huh? 
                return true;
            default:
                return true;
        }
    }
}
