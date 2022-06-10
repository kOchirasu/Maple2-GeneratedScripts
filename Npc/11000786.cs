using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000786: Eka
/// </summary>
public class _11000786 : NpcScript {
    internal _11000786(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 1;2;3;4;5;6;9001;9002;9003;100
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180509004136$ 
                // - Yes, $male:sir,female:ma'am$! Anything, $male:sir,female:ma'am$! Oops, sorry! Occupational habit.
                return true;
            case 1:
                // $script:0831180509004137$ 
                // - Who's there?! Ah, it's you, $OwnerName$. Heh heh.
                switch (selection) {
                    // $script:0831180509004138$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004139$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004140$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 2:
                // $script:0831180509004141$ 
                // - The coast is clear, like always!
                switch (selection) {
                    // $script:0831180509004142$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004143$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004144$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 3:
                // $script:0831180509004145$ 
                // - I'm on duty. Please make it short.
                switch (selection) {
                    // $script:0831180509004146$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004147$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004148$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 4:
                // $script:0831180509004149$ 
                // - Who's there?! Ah, it's you, $OwnerName$. Heh heh.
                switch (selection) {
                    // $script:0831180509004150$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004151$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004152$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509004153$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 5:
                // $script:0831180509004154$ 
                // - The coast is clear, like always!
                switch (selection) {
                    // $script:0831180509004155$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004156$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004157$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509004158$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 6:
                // $script:0831180509004159$ 
                // - I'm on duty. Please make it short.
                switch (selection) {
                    // $script:0831180509004160$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004161$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004162$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509004163$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 9:
                // $script:0831180509004164$ 
                // - Are you giving me my paycheck?
                //   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
                switch (selection) {
                    // $script:0831180509004165$
                    // - Let me think about it some more.
                    case 0:
                        Id = 0; // TODO: 8040,8050,8060,9040 | 8999
                        return false;
                    // $script:0831180509004166$
                    // - (Pay $MaidSalary$.)
                    case 1:
                        Id = 0; // TODO: 8000,8001,8010,8011,8901 | 8900,8910
                        return false;
                }
                return true;
            case 8000:
                // $script:0831180509004167$ functionID=1 
                // - Whoa, you're paying me already? Thank you much! Teehee! Let's have a feast tonight!
                return true;
            case 8001:
                // $script:0831180509004168$ functionID=1 
                // - I needed this! I spent all my money on a preparing a fancy lunch box for $npcName:11000015[gender:1]$ the other day. Teehee! Thank you, $OwnerName$!
                return true;
            case 8010:
                // $script:0831180509004169$ functionID=1 
                // - Yay, you finally have money to pay me! I thought I was going to starve to death. I'm so happy everything worked out!
                return true;
            case 8011:
                // $script:0831180509004170$ functionID=1 
                // - Whoa! I was debating whether I should look for another job. It's not because of you, $OwnerName$, promise. But, a girl's gotta eat.
                return true;
            case 8020:
                // $script:0831180509004171$ functionID=1 
                // - Hmmm, our contract expires in a few days and I'm running out of money for groceries. Are you planning to pay me soon? 
                return true;
            case 8021:
                // $script:0831180509004172$ functionID=1 
                // - Hah hah! No pressure! 
                switch (selection) {
                    // $script:0831180509004173$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004174$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004175$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509004176$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8040:
                // $script:0831180509004177$ 
                // - Did you call me?
                switch (selection) {
                    // $script:0831180509004178$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004179$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004180$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509004181$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8050:
                // $script:0831180509004182$ 
                // - Just say the word.
                switch (selection) {
                    // $script:0831180509004183$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004184$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004185$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509004186$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8060:
                // $script:0831180509004187$ 
                // - Is there something else you wanted?
                switch (selection) {
                    // $script:0831180509004188$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004189$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004190$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509004191$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8900:
                // $script:0831180509004192$ 
                // - ...Err? Hah hah! N-nothing. I didn't hear or see anything! Ah... Ah hah hah... Hah hah...
                return true;
            case 8901:
                // $script:0831180509004193$ 
                // - Um, didn't you already pay me this month?
                return true;
            case 8910:
                // $script:0831180509004194$ 
                // - I see. It's not that you're intentionally not paying me, you just don't have the money. It is what it is. 
                return true;
            case 8999:
                // $script:0831180509004195$ 
                // - W-wait! Let's no panic! C-calm yourself and try again.
                return true;
            case 9001:
                // $script:0831180509004196$ 
                // - ...Huh? Did you say something?
                switch (selection) {
                    // $script:0831180509004197$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509004198$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004199$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9002:
                // $script:0831180509004200$ 
                // - What do you think $npcName:11000015[gender:1]$ would say if she finds out about this?
                switch (selection) {
                    // $script:0831180509004201$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509004202$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004203$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9003:
                // $script:0831180509004204$ 
                // - The injury I got from training isn't healing well, but I don't have the money to pay ointment for it... 
                switch (selection) {
                    // $script:0831180509004205$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509004206$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004207$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9010:
                // $script:0831180509004208$ 
                // - My contract expired. You're not really trying to make me work without pay, are you?
                return true;
            case 9011:
                // $script:0831180509004209$ functionID=1 
                // - Excuse me, $OwnerName$, but our contract expired, just like I've been warning you about for days. I can't believe you let it expire!
                return true;
            case 9020:
                // $script:0831180509004210$ functionID=1 
                // - I haven't eaten for $MaidPassedDay$. Maybe my injuries aren't healing due to lack of nutrition!  
                return true;
            case 9021:
                // $script:0831180509004211$ functionID=1 
                // - I feel so weak... 
                switch (selection) {
                    // $script:0831180509004212$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509004213$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004214$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9040:
                // $script:0831180509004215$ 
                // - I miss $npcName:11000015[gender:1]$... 
                switch (selection) {
                    // $script:0831180509004216$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509004217$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004218$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9030:
                // $script:0831180509004219$ 
                // - Now I know that being neglected is worse than being scolded. $OwnerName$, you don't want me, do you?
                return true;
            case 9031:
                // $script:0831180509004220$ 
                // - Is this because I gave your food to $npc:11000502[gender:0]$? I hope not. I didn't think you were a petty person. 
                return true;
            case 9032:
                // $script:0831180509004221$ 
                // - If I die from starvation, please bury me somewhere sunny in $map:02000076$, somewhere close to
                //   $npcName:11000015[gender:1]$. Don't let her know I suffered... What?! I'm really hungry!!
                return true;
            case 10:
                // $script:0831180509004222$ functionID=1 
                // - I love messing around with beads! I'm good at it, too.
                return true;
            case 11:
                // $script:0831180509004223$ functionID=1 
                // - I can craft stuff for you whenever.
                return true;
            case 20:
                // $script:0831180509004224$ functionID=1 
                // - Our contract includes some details about me.
                return true;
            case 21:
                // $script:0831180509004225$ functionID=1 
                // - Just say the word.
                switch (selection) {
                    // $script:0831180509004226$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004227$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004228$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 22:
                // $script:0831180509004229$ functionID=1 
                // - Just say the word.
                switch (selection) {
                    // $script:0831180509004230$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004231$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004232$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509004233$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 30:
                // $script:0831180509004234$ 
                // - Yes?
                switch (selection) {
                    // $script:0831180509004235$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509004236$
                    // - Tell me about $npcName:11000015[gender:1]$.
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,9011 | 
                        return false;
                    // $script:0831180509004237$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509004238$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 31:
                // $script:0831180509004239$ 
                // - Everyone in $map:2000076$ should be okay, right?
                switch (selection) {
                    // $script:0831180509004240$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509004241$
                    // - Tell me about $npcName:11000015[gender:1]$.
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,9011 | 
                        return false;
                    // $script:0831180509004242$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509004243$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 32:
                // $script:0831180509004244$ 
                // - I don't have time for chitchat.
                switch (selection) {
                    // $script:0831180509004245$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509004246$
                    // - Tell me about $npcName:11000015[gender:1]$.
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,9011 | 
                        return false;
                    // $script:0831180509004247$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509004248$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 40:
                // $script:0831180509004249$ 
                // - Did you call me?
                switch (selection) {
                    // $script:0831180509004250$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004251$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004252$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 50:
                // $script:0831180509004253$ 
                // - Just say the word.
                switch (selection) {
                    // $script:0831180509004254$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004255$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004256$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 60:
                // $script:0831180509004257$ 
                // - Is there something else you wanted?
                switch (selection) {
                    // $script:0831180509004258$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004259$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004260$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 1000:
                // $script:0831180509004261$ 
                // - $npcName:11000015[gender:1]$... I wonder if she's eating well...
                // $script:0831180509004262$ 
                // - $OwnerName$, I want to ask you something. I can't stop thinking about $npcName:11000015[gender:1]$. I'm worried she might think I'm bothering her.
                // $script:0831180509004263$ 
                // - A while ago, I was badly injured during an operation. $npcName:11000015[gender:1]$ was furious! I've never seen her like that. Do you think... she hates me?
                switch (selection) {
                    // $script:0831180509004264$
                    // - Yes.
                    case 0:
                        Id = 0; // TODO: 1001,1002 | 
                        return false;
                    // $script:0831180509004265$
                    // - I think it's the opposite, actually.
                    case 1:
                        Id = 0; // TODO: 1011,1012 | 
                        return false;
                }
                return true;
            case 1001:
                // $script:0831180509004266$ functionID=1 
                // - I see... $OwnerName$, you have no idea what it's like to be hated by someone you admire.
                return true;
            case 1002:
                // $script:0831180509004267$ functionID=1 
                // - Ughhhh. My world... has ended...
                return true;
            case 1011:
                // $script:0831180509004268$ functionID=1 
                // - Huh? What do you mean? You think she got angry because... she cares about me? You really think so?
                return true;
            case 1012:
                // $script:0831180509004269$ functionID=1 
                // - So you're saying $npcName:11000015[gender:1]$ was angry because she was worried about me? Ah, $npcName:11000015[gender:1]$!
                return true;
            case 1100:
                // $script:0831180509004270$ 
                // - The Green Hoods protect the order of Maple World! But...
                // $script:0831180509004271$ 
                // - A while ago, I was injured during an operation, and my father has been urging me to quit ever since.
                // $script:0831180509004272$ 
                // - I understand he loves his daughter, but I don't want to quit. I don't want disappoint my father, either... What do I do?
                switch (selection) {
                    // $script:0831180509004273$
                    // - Stay true to your convictions, for yourself and your father's sake.
                    case 0:
                        Id = 0; // TODO: 1111,1112 | 
                        return false;
                    // $script:0831180509004274$
                    // - Stop caring only about $npcName:11000015[gender:1]$. Think about your parents, too!
                    case 1:
                        Id = 0; // TODO: 1101,1102 | 
                        return false;
                }
                return true;
            case 1101:
                // $script:0831180509004275$ functionID=1 
                // - Wow, ever heard of tact? Sheesh!
                return true;
            case 1102:
                // $script:0831180509004276$ functionID=1 
                // - Wh-what?! Of course $npcName:11000015[gender:1]$ is important to me, but I'm in the Green Hoods to protect Maple World!
                return true;
            case 1111:
                // $script:0831180509004277$ functionID=1 
                // - I knew you'd say that. You're right. I can't quit!
                return true;
            case 1112:
                // $script:0831180509004278$ functionID=1 
                // - That's right! By protecting Maple World, I'm protecting my father. $OwnerName$, you have such sound logic!
                return true;
            case 2000:
                // $script:0831180509004279$ 
                // - $npcName:11000508[gender:1]$ stopped by this afternoon. She and I grew up together in $map:2000076$.
                // $script:0831180509004280$ 
                // - She said $npcName:11000015[gender:1]$ ate nothing but a piece of bread for lunch today.
                // $script:0831180509004281$ 
                // - I can't believe they're neglecting her meals like that!!
                // $script:0831180509004282$ 
                // - So I packed a three-layered lunch box with the ingredients that I was going to use for dinner tonight and sent it back with $npcName:11000508[gender:1]$. Gosh, the Green Hoods can't do anything without me! ...By the way, we'll have to skip dinner tonight.
                return true;
            case 2100:
                // $script:0831180509004283$ 
                // - Today, after finishing the housework, I patrolled the house and saw a stranger.
                // $script:0831180509004284$ 
                // - He looked suspicious, so I hid and watched... He snuck into our house! I stayed still because I wanted to catch him red-handed.
                // $script:0831180509004285$ 
                // - He went into the kitchen and poked around, looking for food. I couldn't wait any longer, so I pounced on him! And...
                // $script:0831180509004286$ 
                // - It was someone I knew: $npc:11000502[gender:0]$. He's a disgrace to his father.
                // $script:0831180509004287$ 
                // - He looked like he hadn't eaten for two days, so I had to give him food... I'm sorry I gave away your food. You can take it out of my pay if you want.
                return true;
            case 2200:
                // $script:0831180509004288$ 
                // - It's too boring to stay inside the house all day. I want to go out and exercise. $OwnerName$, want to come with me?
                // $script:0831180509004289$ 
                // - I want to join $map:61000006$, which takes place in $map:2000064$ every day, once in the morning and once in the evening.
                // $script:0831180509004290$ 
                // - It'll be fun! We'll do it together! Come on, go change into your workout gear!
                return true;
            case 3000:
                // $script:0831180509004291$ 
                // - Have you heard of $npc:11000002[gender:1]$ in $map:2000001$? Everyone in $map:2000076$ insists she was as beautiful as $npcName:11000015[gender:1]$ in her time.
                // $script:0831180509004292$ 
                // - But obviously, $npcName:11000015[gender:1]$ is way more beautiful.
                // $script:0831180509004293$ functionID=1 
                // - Ahhh... $npcName:11000015[gender:1]$... What I wouldn't give for a chance to comb her hair every day...
                return true;
            case 3100:
                // $script:0831180509004294$ 
                // - $npcName:11000015[gender:1]$ is amazing. She leads the Green Hoods with a gentle yet firm hand.
                // $script:0831180509004295$ 
                // - $npcName:11000015[gender:1]$ says it's important to protect the weak and to safeguard justice. It's the reason the Green Hoods exist. She inspires responsibility and pride in all of us.
                // $script:0831180509004296$ 
                // - As for me, I'm more interested in protecting $npcName:11000015[gender:1]$ than in protecting Maple World. 
                // $script:0831180509004297$ 
                // - I know $npcName:11000015[gender:1]$ is much stronger than I am, but I'm sure she has things that she can't tell others... I want to help her in any way I can...
                // $script:0831180509004298$ functionID=1 
                // - Uhh? What am I saying? Ah... Ah hah hah... Hah hah...
                return true;
            case 4000:
                // $script:0831180509004299$ 
                // - Huh? $npcName:11000015[gender:1]$? Hah hah! What about $npcName:11000015[gender:1]$?
                // $script:0831180509004300$ 
                // - W-wait. Did something happen to $npcName:11000015[gender:1]$? Is that it? Huh? Huh? Come on, you're killing me here. Answer me!
                // $script:0831180509004301$ 
                // - ...Oh. You don't think $npcName:11000015[gender:1]$ washed her hair today. Sheesh, what does it matter if she washed her hair or not?
                // $script:0831180509004302$ 
                // - Besides, $npcName:11000015[gender:1]$ is not a slob. She must have gotten oil on her hair while fighting. Duh!
                return true;
            case 4100:
                // $script:0831180509004303$ 
                // - Many of us joined the group because we admired $npcName:11000015[gender:1]$. T-that was my reason, obviously.
                // $script:0831180509004304$ 
                // - Charismatic, a natural leader, a heart of gold, amazing combat skills, and unparalleled beauty! $npcName:11000015[gender:1]$ is perfect in every way.
                // $script:0831180509004305$ 
                // - Hey, if you think I'm infatuated with her, fine. Think whatever you want, as long as it distracts you from crushing on her yourself.
                return true;
            case 5000:
                // $script:0831180509004306$ 
                // - A Green Hood from $map:2000076$, that's me! Born and raised in $map:2000076$, I know everyone there as well as my own family.
                // $script:0831180509004307$ 
                // - Have you met $npcName:11000508[gender:1]$ in $map:2000203$ before? She's been my best friend since we were young.
                // $script:0831180509004308$ 
                // - That girl is so strong that she can do any man's work with no problem... Hm, I guess the same goes for me too, huh? Teehee!
                return true;
            case 5100:
                // $script:0831180509004309$ 
                // - That reminds me of $npcName:11000502[gender:0]$. I hope he's not being taken advantage of by anyone, wherever he is.
                // $script:0831180509004310$ 
                // - He's some guy I've known since I young. He's a decent fellow, but a bit naive and immature. It makes him easy prey.
                // $script:0831180509004311$ 
                // - I don't know why he couldn't learn from his father... $npcName:11000502[gender:0]$ is the son of Elder $npcName:11000001[gender:0]$ in $map:2000076$.
                // $script:0831180509004312$ 
                // - Come to think of it, rumor has it that every elder for generations has had a troublemaker son. Do you think that's true?
                return true;
            case 6000:
                // $script:0831180509004313$ 
                // - I thought I was going to live ordinary life, staying in peaceful $map:2000076$ for all of my days.
                // $script:0831180509004314$ 
                // - Meeting $npcName:11000015[gender:1]$ completely changed my life. Watching a small, dainty-looking woman command a cohort of warriors touched me in a way nothing else ever has.
                // $script:0831180509004315$ 
                // - I'd never seen the world outside of $map:2000076$ or held a bow in my hand, but I decided to join her group, despite my father's objections.
                // $script:0831180509004316$ 
                // - Now that I've joined the Green Hoods, sometimes I feel sorry for $npcName:11000015[gender:1]$. She was trained to be the leader of the Green Hoods since she was born, and being responsible for so many lives has to be tough.
                // $script:0831180509004317$ 
                // - I'd love to be there when she needs someone to talk to, but I know $npcName:11000015[gender:1]$ would never show any weakness, no matter how troubled she was on the inside..
                return true;
            case 7000:
                // $script:0831180509004318$ 
                // - Ugh... I don't think the injury I got on that last operation ever properly healed. It's throbbing.
                // $script:0831180509004319$ 
                // - Do you mind putting this medicated patch on my back? I can't do it myself.
                // $script:0831180509004320$ 
                // - Whew, thanks. I bet you're curious how I got this injury...
                // $script:0831180509004321$ 
                // - I was on duty at the guard post when a group of creeps attacked. I'd never seen them before, and they used some kind of strange magic.
                // $script:0831180509004322$ 
                // - Ah, I'm still not good enough for $npcName:11000015[gender:1]$. I can't protect myself, let alone her...
                return true;
            case 100:
                // $script:0831180509004323$ 
                // - Halt! Who goes there!
                switch (selection) {
                    // $script:0831180509004324$
                    // - I know the owner.
                    case 0:
                        Id = 0; // TODO: 101,102 | 
                        return false;
                    // $script:0831180509004325$
                    // - Oops, wrong house.
                    case 1:
                        Id = 0; // TODO: 103,104 | 
                        return false;
                    // $script:0831180509004326$
                    // - Who are you?
                    case 2:
                        Id = 0; // TODO: 105,106 | 
                        return false;
                }
                return true;
            case 101:
                // $script:0831180509004327$ 
                // - You do, huh? Hm. All right, you can stay, but don't try anything stupid.
                return true;
            case 102:
                // $script:0831180509004328$ 
                // - Mm, I don't think I've seen you before. Look, if you're here for the wrong reasons, I will make you regret it.
                return true;
            case 103:
                // $script:0831180509004329$ 
                // - Ah, I see. Mistakes happen. You can be on your way now.
                return true;
            case 104:
                // $script:0831180509004330$ 
                // - Are you lost? I'm a member of the Green Hoods, so let me know if you need help.
                return true;
            case 105:
                // $script:0831180509004331$ 
                // - My name is $MaidName$. I'm a member of the Green Hoods. Now, it's your turn to identify yourself.
                return true;
            case 106:
                // $script:0831180509004332$ 
                // - My name is $MaidName$, and I keep watch over this house. How may I help you?
                return true;
            default:
                return true;
        }
    }
}
