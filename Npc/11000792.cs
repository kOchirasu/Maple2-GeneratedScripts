using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000792: Jorge
/// </summary>
public class _11000792 : NpcScript {
    internal _11000792(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 1;2;3;4;5;6;9001;9002;9003;100
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180509005427$ 
                // - Why'd you call me?
                return true;
            case 1:
                // $script:0831180509005428$ 
                // - You're back. What do you need?
                switch (selection) {
                    // $script:0831180509005429$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005430$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005431$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 2:
                // $script:0831180509005432$ 
                // - What can I do for you this time?
                switch (selection) {
                    // $script:0831180509005433$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005434$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005435$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 3:
                // $script:0831180509005436$ 
                // - What is it? Do you need help?
                switch (selection) {
                    // $script:0831180509005437$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005438$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005439$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 4:
                // $script:0831180509005440$ 
                // - You're back. What do you need?
                switch (selection) {
                    // $script:0831180509005441$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005442$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005443$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509005444$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 5:
                // $script:0831180509005445$ 
                // - What can I do for you this time?
                switch (selection) {
                    // $script:0831180509005446$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005447$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005448$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509005449$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 6:
                // $script:0831180509005450$ 
                // - What is it? Do you need help?
                switch (selection) {
                    // $script:0831180509005451$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005452$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005453$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509005454$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 9:
                // $script:0831180509005455$ 
                // - Are you going to pay me?
                //   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
                switch (selection) {
                    // $script:0831180509005456$
                    // - Let me think about it some more.
                    case 0:
                        Id = 0; // TODO: 8040,8050,8060,9040 | 8999
                        return false;
                    // $script:0831180509005457$
                    // - (Pay $MaidSalary$.)
                    case 1:
                        Id = 0; // TODO: 8000,8001,8010,8011,8901 | 8900,8910
                        return false;
                }
                return true;
            case 8000:
                // $script:0831180509005458$ functionID=1 
                // - Oh, you're paying me ahead of schedule. I appreciate it. Do humans label this type of behavior diligent or impatient?
                return true;
            case 8001:
                // $script:0831180509005459$ functionID=1 
                // - Most currencies are shiny, and fairies love shiny things. Maybe that's why I'm in such a good mood.
                return true;
            case 8010:
                // $script:0831180509005460$ functionID=1 
                // - A-ha, has our contract been renewed? Good timing. I had just gotten adequate rest. Thank you for hiring me again.
                return true;
            case 8011:
                // $script:0831180509005461$ functionID=1 
                // - Ah, is it time for me to play house again? Good, I was getting bored. Humans call fairies fickle, but I think humans are far worse. What do you think?
                return true;
            case 8020:
                // $script:0831180509005462$ functionID=1 
                // - Our contract will expire in a few days. Did you know that? Of course, $OwnerName$, you know your schedule better than I do, but I thought I'd give you a reminder. 
                return true;
            case 8021:
                // $script:0831180509005463$ functionID=1 
                // - By the way, I appreciate your checking my profile.
                switch (selection) {
                    // $script:0831180509005464$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005465$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005466$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509005467$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8040:
                // $script:0831180509005468$ 
                // - Was there something else you wanted?
                switch (selection) {
                    // $script:0831180509005469$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005470$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005471$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509005472$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8050:
                // $script:0831180509005473$ 
                // - What can I do for you this time?
                switch (selection) {
                    // $script:0831180509005474$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005475$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005476$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509005477$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8060:
                // $script:0831180509005478$ 
                // - Do you need help again?
                switch (selection) {
                    // $script:0831180509005479$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005480$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005481$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509005482$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8900:
                // $script:0831180509005483$ 
                // - Ahem! I may have a longer lifespan than you, but each minute of my time is just as valuable. What I mean is, $OwnerName$, if you'd checked your wallet before beginning this discussion, we could've both been doing something more productive.
                return true;
            case 8901:
                // $script:0831180509005484$ 
                // - Hmm? What day is it? If memory serves, we have at least a month left on our current contract. Would you like to go verify that information?
                return true;
            case 8910:
                // $script:0831180509005485$ 
                // - Ahem! I may have a longer lifespan than you, but each minute of my time is just as valuable. What I mean is, $OwnerName$, if you'd checked your wallet before beginning this discussion, we could've both been doing something more productive.
                return true;
            case 8999:
                // $script:0831180509005486$ 
                // - How strange! I read the Helping Hands handbook thoroughly, but there were no guidelines for situations like this. Maybe you should try again. If this problem persists, we need to document it.
                return true;
            case 9001:
                // $script:0831180509005487$ 
                // - I'll consider this time off as... a vacation?
                switch (selection) {
                    // $script:0831180509005488$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509005489$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005490$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9002:
                // $script:0831180509005491$ 
                // - Hm, what a strange point of view! Huh? Oh, I'm referring to the author of this book.
                switch (selection) {
                    // $script:0831180509005492$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509005493$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005494$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9003:
                // $script:0831180509005495$ 
                // - Hm... I can't believe this theory... Oh, sorry. Did you call me?
                switch (selection) {
                    // $script:0831180509005496$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509005497$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005498$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9010:
                // $script:0831180509005499$ 
                // - Sorry. Nope. I can't. My contract expired.
                return true;
            case 9011:
                // $script:0831180509005500$ functionID=1 
                // - Wait, we shouldn't talk about that right now. Did you know our contract expired? And I'm not only bringing that up to avoid talking to you.
                return true;
            case 9020:
                // $script:0831180509005501$ functionID=1 
                // - Huh? You and your obsession with my profile. I told you, this profile cannot capture even a 0.0000000000...0001 of who I am.
                return true;
            case 9021:
                // $script:0831180509005502$ functionID=1 
                // - Ah... Let's not talk about this anymore. I don't want to argue.
                switch (selection) {
                    // $script:0831180509005503$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509005504$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005505$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9040:
                // $script:0831180509005506$ 
                // - I'd like to focus on what I'm reading. Please don't disturb me unless it's important.
                switch (selection) {
                    // $script:0831180509005507$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509005508$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005509$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9030:
                // $script:0831180509005510$ 
                // - I've seen many humans try to change their destinies. Most drive themselves to ruin, blaming anyone but themselves on the way. No, no, I'm not calling you irresponsible, $OwnerName$.
                // $script:0831180509005511$ 
                // - I'm trying to encourage to take control of your life and choices. You have such a short, short life, but it's still full of choices.
                return true;
            case 9031:
                // $script:0831180509005512$ 
                // - Why are you asking me about the contract renewal? If you want to do it, then do it. If not, don't. You are in control of that, because you're the one with the money.
                // $script:0831180509005513$ 
                // - I remember how shocked I was when I first learned about Helping Hands. I couldn't believe someone came up with such a one-sided, unreasonable system.
                // $script:0831180509005514$ 
                // - Why am I here despite my abhorrence of the system? Foremost, because I've met a human to whom I can relate and am interested in knowing. But initially, it was purely out of curiosity.
                // $script:0831180509005515$ 
                // - Are you wondering if the human I'm referring to is you? No comment. The point is, the time I spend here is only a fraction of my lifespan, so you can do whatever you want, $OwnerName$. 
                return true;
            case 9032:
                // $script:0831180509005516$ 
                // - Fairies have this impression that humans are high maintenence. It wasn't until after I started working here—no actually, it wasn't until after our contract expired and I was forced to rest—that I realized how true that is.
                return true;
            case 10:
                // $script:0831180509005517$ functionID=1 
                // - Need a potion?
                return true;
            case 11:
                // $script:0831180509005518$ functionID=1 
                // - Just tell me what you need, and I'll do the best I can.
                return true;
            case 20:
                // $script:0831180509005519$ functionID=1 
                // - My profile won't reveal how I've lived my life...
                return true;
            case 21:
                // $script:0831180509005520$ functionID=1 
                // - Curious about my past? But that has nothing to do with my job.
                switch (selection) {
                    // $script:0831180509005521$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005522$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005523$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 22:
                // $script:0831180509005524$ functionID=1 
                // - Curious about my past? But that has nothing to do with my job.
                switch (selection) {
                    // $script:0831180509005525$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005526$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005527$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509005528$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 30:
                // $script:0831180509005529$ 
                // - You want to talk to me. Sure, what do you want to talk about?
                switch (selection) {
                    // $script:0831180509005530$
                    // - (Ask a difficult question.)
                    case 0:
                        Id = 0; // TODO: 1000,1100,2000,2100,9011 | 
                        return false;
                    // $script:0831180509005531$
                    // - (Request an old story.)
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,9011 | 
                        return false;
                    // $script:0831180509005532$
                    // - (Talk about a personal topic.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509005533$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 31:
                // $script:0831180509005534$ 
                // - I've been around a long time, $OwnerName$. Maybe my experience can help.
                switch (selection) {
                    // $script:0831180509005535$
                    // - (Ask a difficult question.)
                    case 0:
                        Id = 0; // TODO: 1000,1100,2000,2100,9011 | 
                        return false;
                    // $script:0831180509005536$
                    // - (Request an old story.)
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,9011 | 
                        return false;
                    // $script:0831180509005537$
                    // - (Talk about a personal topic.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509005538$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 32:
                // $script:0831180509005539$ 
                // - We can talk, but don't ask anything too personal.
                switch (selection) {
                    // $script:0831180509005540$
                    // - (Ask a difficult question.)
                    case 0:
                        Id = 0; // TODO: 1000,1100,2000,2100,9011 | 
                        return false;
                    // $script:0831180509005541$
                    // - (Request an old story.)
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,9011 | 
                        return false;
                    // $script:0831180509005542$
                    // - (Talk about a personal topic.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509005543$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 40:
                // $script:0831180509005544$ 
                // - Was there something else you wanted?
                switch (selection) {
                    // $script:0831180509005545$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005546$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005547$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 50:
                // $script:0831180509005548$ 
                // - What can I do for you this time?
                switch (selection) {
                    // $script:0831180509005549$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005550$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005551$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 60:
                // $script:0831180509005552$ 
                // - Do you need help again?
                switch (selection) {
                    // $script:0831180509005553$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005554$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005555$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 1000:
                // $script:0831180509005556$ 
                // - "Why do fairies live so much longer than humans," hmm? An excellent question. The secret to our longevity isn't quite what popular opinion would lead you to believe.
                // $script:0831180509005557$ 
                // - Most believe our ability to commune with nature grants us a regenerative ability that slows aging.
                // $script:0831180509005558$ 
                // - That's not quite right. The answer is actually because we are embodiments of nature herself. We live long lives the same way trees live for millennia and turtles live for centuries.
                // $script:0831180509005559$ 
                // - As for why humans can't, it's simple. You refuse to submit to nature. You've decided to change your destinies. And that's why you and I have drastically different natural lifespans.
                // $script:0831180509005560$ 
                // - Does that answer your question?
                switch (selection) {
                    // $script:0831180509005561$
                    // - That's absurd!
                    case 0:
                        Id = 0; // TODO: 1001,1002 | 
                        return false;
                    // $script:0831180509005562$
                    // - Yup!
                    case 1:
                        Id = 0; // TODO: 1011,1012 | 
                        return false;
                }
                return true;
            case 1001:
                // $script:0831180509005563$ functionID=1 
                // - Just because you don't understand it doesn't make it untrue... Now you've upset me.
                return true;
            case 1002:
                // $script:0831180509005564$ functionID=1 
                // - I didn't expect you to fully understand, but I didn't expect you to react quite like this, $OwnerName$.
                return true;
            case 1011:
                // $script:0831180509005565$ 
                // - Oh, you understood all that? Your comprehension skills are better than I estimated. I think I can come to enjoy conversing with you.
                // $script:0831180509005566$ functionID=1 
                // - If you have other questions, you may ask them, but try to space it out, okay?
                return true;
            case 1012:
                // $script:0831180509005567$ 
                // - $OwnerName$, why don't you ask yourself a question. For example, whether humans did the right thing in rejecting nature? That's rather philosophical, don't you think?
                // $script:0831180509005568$ functionID=1 
                // - Ah, look at the time! I talked for longer than I thought. Well, that's because I enjoyed our conversation.
                return true;
            case 1100:
                // $script:0831180509005569$ 
                // - Why is the sea such a pretty blue? Are you looking for the scientific answer or the poetic one? I can't speak to why you think blue is pretty, so I'll answer the scientific question instead.
                // $script:0831180509005570$ 
                // - When light hits the sea, all light waves except the one that our eye interpret as the color blue is absorbed into the water. Do you understand? Similarly, red roses only reflect the red ray, which is why they look red.
                switch (selection) {
                    // $script:0831180509005571$
                    // - Do you really believe that? Truly?
                    case 0:
                        Id = 0; // TODO: 1111,1112 | 
                        return false;
                    // $script:0831180509005572$
                    // - I disagree with you.
                    case 1:
                        Id = 0; // TODO: 1101,1102 | 
                        return false;
                }
                return true;
            case 1101:
                // $script:0831180509005573$ 
                // - Then what is your opinion, $OwnerName$? Debate begins with a difference of opinion, and they often result in enlightenment and shifts in perspective.
                // $script:0831180509005574$ functionID=1 
                // - So... you think the sea is blue because fairies painted it blue? Do you... really believe that? Well, let's not talk about it, then. I don't wish to argue.
                return true;
            case 1102:
                // $script:0831180509005575$ 
                // - Interesting. It's a pretty simple and well-known scientific fact, but you disagree. Well, what's your theory, $OwnerName$?
                // $script:0831180509005576$ functionID=1 
                // - You don't know? But how can you disagree if you don't have your own idea of what the answer is? This conversation is nonsense.
                return true;
            case 1111:
                // $script:0831180509005577$ 
                // - What I just explained is the most well-accepted theory, but explaining nature with science can be harsh on your spirit and soul. Truth be told, I have a different idea.
                // $script:0831180509005578$ 
                // - In my heart, I believe that the sea is blue because it saw that the sky was beautiful and wanted to emulate it. Or because it's a mirror to the sky's own beauty. Or maybe, the sky touched the sea once, staining it forever...
                // $script:0831180509005579$ functionID=1 
                // - I know that such theories aren't science. But still, they bring me joy. I hope you'll remember that, $OwnerName$.
                return true;
            case 1112:
                // $script:0831180509005580$ 
                // - Scientific facts are not based on belief. They're facts. Absolute. But I like that you asked that question. It shows you don't want to see the world through the lens of pure fact.
                // $script:0831180509005581$ functionID=1 
                // - That type of mental flexibility will help you grow as a person, $OwnerName$. Trust me. I have an eye for that kind of stuff.
                return true;
            case 2000:
                // $script:0831180509005582$ 
                // - You have another question? Am I your walking encyclopedia? I'm sorry, but I'm in the middle of something. Maybe next time.
                return true;
            case 2100:
                // $script:0831180509005583$ 
                // - I'm sorry, but I don't have time to answer a question right now. As you can clearly see, I'm very busy. This isn't because I don't know the answer...
                return true;
            case 3000:
                // $script:0831180509005584$ 
                // - This is a story from so long ago that even history doesn't known when it happened. It's from a time when fairies could speak to the stars, wind, and moon. I wasn't there personally. This is a tale known to all fairies who love reading.
                // $script:0831180509005585$ 
                // - It is about a male fairy, his sister, and an evil witch. 
                //   <font color="#909090">(He goes on and on, summarizing the story from a historian's perspective.)</font>
                // $script:0831180509005586$ 
                // - <font color="#909090">(He goes into a lot of boring details and even the exciting moments are dragged down by his unnecessary analyses.)</font>
                // $script:0831180509005587$ functionID=1 
                // - And thus, the brother and sister concluded their adventure. Did you enjoy the tale? You're an excellent listener. I enjoyed relaying the story to you.
                return true;
            case 3100:
                // $script:0831180509005588$ 
                // - This time, I will share something I experienced firsthand. I've seen quite a lot in my not-so-short life, and I'm sure you'd enjoy some of my extraordinary tales.
                // $script:0831180509005589$ 
                // - When I was young and curious, I traveled to many locales, even though I don't much care for traveling. This tale takes us to a remove village in the far south, whose name I can no longer remember.
                // $script:0831180509005590$ 
                // - There was a big tree in the center of the village, which the villagers consulted for important events...
                // $script:0831180509005591$ 
                // - <font color="#909090">(He goes into a lot of boring details and even the exciting moments are dragged down by his unnecessary analyses.)</font>
                // $script:0831180509005592$ 
                // - In the end, I left that village to return home, but I still wonder sometimes... what was that tree? Was it really holy?
                // $script:0831180509005593$ functionID=1 
                // - I experienced that personally, and I guarantee everything I said is 100% truth. Well, I may have exaggerated a little, but doesn't that just make it 120% truth?
                return true;
            case 4000:
                // $script:0831180509005594$ 
                // - I can't right now. I just can't. Not even for you, $OwnerName$. You understand, don't you?
                return true;
            case 4100:
                // $script:0831180509005595$ 
                // - Right now? I can't just come up with a story on the spot, $OwnerName$. Also, I'm busy.
                return true;
            case 5000:
                // $script:0831180509005596$ 
                // - I don't like talking about myself, $OwnerName$, and I prefer to keep things professional. Please understand that.
                // $script:0831180509005597$ 
                // - If we were friends, I might change my mind, but I don't feel comfortable sharing. Please don't be upset.
                return true;
            case 5100:
                // $script:0831180509005598$ 
                // - Well, let's see. My name is $MaidName$. I am fairfolk. I wear glasses. I have green hairs and eyes. I enjoy reading. But... this isn't the information you're after, is it?
                // $script:0831180509005599$ 
                // - Allow me to make this clear so that it doesn't happen again: I do not like being asked about my personal life. If you wish to talk, I enjoy discussing topics of a more academic nature.
                return true;
            case 6000:
                // $script:0831180509005600$ 
                // - $OwnerName$, why do you slather half the things you eat in ketchup? What appeals to you about that red sauce? I find it quite sour. Why do humans enjoy it so much?
                // $script:0831180509005601$ 
                // - However, I do find myself quite drawn to the taste of mayonnaise. Its ivory tone, its light scent, its creamy taste... Mmm, dip a celery stick in some mayo, and this fairfolk is in heaven!
                return true;
            case 7000:
                // $script:0831180509005602$ 
                // - $OwnerName$, last time when you asked me my age, I may have been a little harsh. I still don't wish to reveal my exact age, but I'm willing to give you some idea: I'm ridiculously old in human years but fairly young in fairfolk years.
                // $script:0831180509005603$ 
                // - We must've grown close, $OwnerName$. I find that I don't mind telling you about myself, and I even catch myself thinking of you as a friend.
                return true;
            case 100:
                // $script:0831180509005604$ 
                // - What brings you to this residence?
                switch (selection) {
                    // $script:0831180509005605$
                    // - I'm here to see your master.
                    case 0:
                        Id = 0; // TODO: 101,102 | 
                        return false;
                    // $script:0831180509005606$
                    // - I came to check out the house.
                    case 1:
                        Id = 0; // TODO: 103,104 | 
                        return false;
                    // $script:0831180509005607$
                    // - I wanted you to tell me an old tale.
                    case 2:
                        Id = 0; // TODO: 105,106 | 
                        return false;
                }
                return true;
            case 101:
                // $script:0831180509005608$ 
                // - Ah, then that makes you a friend. Hold on, I'll bring you some tea.
                return true;
            case 102:
                // $script:0831180509005609$ 
                // - Strange that I've never heard of you. Ah well, please make yourself at home.
                return true;
            case 103:
                // $script:0831180509005610$ 
                // - You can't just barge into a someone's home because you're curious about it...
                return true;
            case 104:
                // $script:0831180509005611$ 
                // - Are you here the judge the owner's taste in interior design? If so, please proceed, but please don't make too much noise.
                return true;
            case 105:
                // $script:0831180509005612$ 
                // - What do you mean by "an old tale"? Are you referring to the stories I tell the owner of this house? But you're a stranger. Why would I tell you a thing?
                return true;
            case 106:
                // $script:0831180509005613$ 
                // - Perhaps if we were friends, I would, but we've just met. Don't you think you're being a bit impolite?
                return true;
            default:
                return true;
        }
    }
}
