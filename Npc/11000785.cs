using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000785: Marmut
/// </summary>
public class _11000785 : NpcScript {
    internal _11000785(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 1;2;3;4;5;6;9001;9002;9003;100
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180509003920$ 
                // - Well, well...
                return true;
            case 1:
                // $script:0831180509003921$ 
                // - Hi, $OwnerName$, what can I do for you?
                switch (selection) {
                    // $script:0831180509003922$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003923$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003924$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 2:
                // $script:0831180509003925$ 
                // - Today is quite wonderful, isn't it?
                switch (selection) {
                    // $script:0831180509003926$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003927$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003928$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 3:
                // $script:0831180509003929$ 
                // - Hmm... This might be a problem... Maybe?
                switch (selection) {
                    // $script:0831180509003930$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003931$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003932$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 4:
                // $script:0831180509003933$ 
                // - Hi, $OwnerName$, what can I do for you?
                switch (selection) {
                    // $script:0831180509003934$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003935$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003936$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509003937$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 5:
                // $script:0831180509003938$ 
                // - Today is quite wonderful, isn't it?
                switch (selection) {
                    // $script:0831180509003939$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003940$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003941$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509003942$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 6:
                // $script:0831180509003943$ 
                // - Hmm... This might be a problem... Maybe?
                switch (selection) {
                    // $script:0831180509003944$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003945$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003946$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509003947$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 9:
                // $script:0831180509003948$ 
                // - You want to pay me?
                //   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
                switch (selection) {
                    // $script:0831180509003949$
                    // - Let me think about it some more.
                    case 0:
                        Id = 0; // TODO: 8040,8050,8060,9040 | 8999
                        return false;
                    // $script:0831180509003950$
                    // - (Pay $MaidSalary$.)
                    case 1:
                        Id = 0; // TODO: 8000,8001,8010,8011,8901 | 8900,8910
                        return false;
                }
                return true;
            case 8000:
                // $script:0831180509003951$ functionID=1 
                // - Are you sure you want to pay me already? I won't stop you if you insist, but please make sure people know I didn't request it. 
                return true;
            case 8001:
                // $script:0831180509003952$ functionID=1 
                // - I got paid! Hmm, should I ask $npcName:11000160[gender:1]$ out for lunch? What do you think? 
                return true;
            case 8010:
                // $script:0831180509003953$ functionID=1 
                // - Where did you get so much money? Well, I'm not complaining... 
                return true;
            case 8011:
                // $script:0831180509003954$ functionID=1 
                // - Er, last I checked, you didn't have enough money. You d-didn't do anything illegal to get this money, did you? Please let it be known that I never once nagged you for my paycheck, $OwnerName$.
                return true;
            case 8020:
                // $script:0831180509003955$ functionID=1 
                // - Excuse me, $OwnerName$. Our employment contract expires in a few days. Just wanted you to know. 
                return true;
            case 8021:
                // $script:0831180509003956$ functionID=1 
                // - Ah, well... I-I'm just saying... 
                switch (selection) {
                    // $script:0831180509003957$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003958$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003959$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509003960$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8040:
                // $script:0831180509003961$ 
                // - Why am I so indecisive?!
                switch (selection) {
                    // $script:0831180509003962$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003963$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003964$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509003965$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8050:
                // $script:0831180509003966$ 
                // - A housekeeper guard is a rather unusual combo, isn't it?
                switch (selection) {
                    // $script:0831180509003967$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003968$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003969$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509003970$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8060:
                // $script:0831180509003971$ 
                // - Was there something else you needed?
                switch (selection) {
                    // $script:0831180509003972$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003973$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003974$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509003975$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8900:
                // $script:0831180509003976$ 
                // - $OwnerName$, are you going through a hard time? This isn't enough... But before you give me a single meso, have you thought you whether you should even pay me at all?
                return true;
            case 8901:
                // $script:0831180509003977$ 
                // - Ah... $OwnerName$... You already paid me this month. Now I'm not sure whether to accept or not...
                return true;
            case 8910:
                // $script:0831180509003978$ 
                // - It's past my payday, but you don't seem to have the money. I'm not sure whether I should ask for my pay or not... 
                return true;
            case 8999:
                // $script:0831180509003979$ 
                // - As the old saying goes, "don't do something unless you're absolutely certain." It seems like you weren't one hundred percent certain. Why don't you try again?
                return true;
            case 9001:
                // $script:0831180509003980$ 
                // - Hmm... What do I do? ...Huh? Oh, nothing!
                switch (selection) {
                    // $script:0831180509003981$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509003982$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003983$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9002:
                // $script:0831180509003984$ 
                // - Should I do something to keep myself busy? Or should I just keep loafing around? Hmm... 
                switch (selection) {
                    // $script:0831180509003985$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509003986$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003987$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9003:
                // $script:0831180509003988$ 
                // - Should I keep doing this or not? I don't know... 
                switch (selection) {
                    // $script:0831180509003989$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509003990$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003991$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9010:
                // $script:0831180509003992$ 
                // - How should I word this delicately? Ahem, my contract has expired. I don't work for free! Whew, I said it... 
                return true;
            case 9011:
                // $script:0831180509003993$ functionID=1 
                // - Hmm, I need to tell $male:him,female:her$ that our contract expired but $male:he,female:she$ just won't stop talking. Is that a strategic ploy? Oh, ahem, you heard me? Well... our contract has expired.
                return true;
            case 9020:
                // $script:0831180509003994$ functionID=1 
                // - I got some much-needed rest over the last $MaidPassedDay$, and look how refreshed I look now! 
                return true;
            case 9021:
                // $script:0831180509003995$ functionID=1 
                // - Th-that doesn't mean I want to rest forever... 
                switch (selection) {
                    // $script:0831180509003996$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509003997$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003998$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9040:
                // $script:0831180509003999$ 
                // - I don't know what to do... 
                switch (selection) {
                    // $script:0831180509004000$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509004001$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004002$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9030:
                // $script:0831180509004003$ 
                // - I've been thinking, $OwnerName$. Maybe you should wait until you're rich to pay me. I don't want you to go hungry, you know?
                return true;
            case 9031:
                // $script:0831180509004004$ 
                // - Hmm, I can't stand such a messy house, but I'm not a charity, either. I don't think it's right to work without payment. $OwnerName$, just look at those dust bunnies. Are you really okay living in such filth?
                return true;
            case 9032:
                // $script:0831180509004005$ 
                // - $OwnerName$, if you don't pay your rent, you'll lose your house, and I'll lose my job. But if you do pay your rent... you won't have enough left to pay me. Hmmmm...
                return true;
            case 10:
                // $script:0831180509004006$ functionID=1 
                // - Who says guards can't cut gems, even if it's just a hobby?
                return true;
            case 11:
                // $script:0831180509004007$ functionID=1 
                // - Tell me whatever you like.
                return true;
            case 20:
                // $script:0831180509004008$ functionID=1 
                // - Since you asked, I can tell you, but don't complain if you find it boring.
                return true;
            case 21:
                // $script:0831180509004009$ functionID=1 
                // - How can I help you?
                switch (selection) {
                    // $script:0831180509004010$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004011$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004012$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 22:
                // $script:0831180509004013$ functionID=1 
                // - How can I help you?
                switch (selection) {
                    // $script:0831180509004014$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004015$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004016$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509004017$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 30:
                // $script:0831180509004018$ 
                // - This is... troublesome...
                switch (selection) {
                    // $script:0831180509004019$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509004020$
                    // - Tell me about the Royal Guard!
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,9011 | 
                        return false;
                    // $script:0831180509004021$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509004022$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 31:
                // $script:0831180509004023$ 
                // - Hmm, what should I do?
                switch (selection) {
                    // $script:0831180509004024$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509004025$
                    // - Tell me about the Royal Guard!
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,9011 | 
                        return false;
                    // $script:0831180509004026$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509004027$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 32:
                // $script:0831180509004028$ 
                // - I don't know what to do... 
                switch (selection) {
                    // $script:0831180509004029$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509004030$
                    // - Tell me about the Royal Guard!
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,9011 | 
                        return false;
                    // $script:0831180509004031$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509004032$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 40:
                // $script:0831180509004033$ 
                // - Why am I so indecisive?!
                switch (selection) {
                    // $script:0831180509004034$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004035$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004036$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 50:
                // $script:0831180509004037$ 
                // - A housekeeper guard is a rather unusual combo, isn't it?
                switch (selection) {
                    // $script:0831180509004038$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004039$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004040$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 60:
                // $script:0831180509004041$ 
                // - Was there something else you needed?
                switch (selection) {
                    // $script:0831180509004042$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509004043$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509004044$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 1000:
                // $script:0831180509004045$ 
                // - Come to think of it, I'm forgetting something! Or... maybe not? 
                // $script:0831180509004046$ 
                // - It's time I take control of my own life! I'm taking your advice, $OwnerName$!
                // $script:0831180509004047$ 
                // - I'm going to ask $npcName:11000160[gender:1]$ out to eat black noodles with me! I've been in love with her forever. I'm going to tell her how I feel! Right? Should I? I should, shouldn't I?
                switch (selection) {
                    // $script:0831180509004048$
                    // - Yes, you should!
                    case 0:
                        Id = 0; // TODO: 1011,1012 | 
                        return false;
                    // $script:0831180509004049$
                    // - Eh, the timing might not be quite right...
                    case 1:
                        Id = 0; // TODO: 1001,1002 | 
                        return false;
                }
                return true;
            case 1001:
                // $script:0831180509004050$ functionID=1 
                // - Yeah, I think so too. Girls like her don't go for guys like me, hah hah hah...
                return true;
            case 1002:
                // $script:0831180509004051$ functionID=1 
                // - I've waited three years, what's a few more? I can wait as long as needed!
                return true;
            case 1011:
                // $script:0831180509004052$ functionID=1 
                // - You think so? R-r-really? I mean, I do, too! Just let me catch my b-b-breath first!
                return true;
            case 1012:
                // $script:0831180509004053$ functionID=1 
                // - You've given me the courage I needed. Deep breaths. Deeeeeep breaths. Okay, I'm ready! I'm going to do this!
                return true;
            case 1100:
                // $script:0831180509004054$ 
                // - I've been doing some serious reflection.
                // $script:0831180509004055$ 
                // - The other guards think I'm too indecisive. Not a day go by where $npcName:11000119[gender:0]$ doesn't scold me. 
                // $script:0831180509004056$ 
                // - Maybe I'm not cut out to be a guard. $OwnerName$, what do you think?
                switch (selection) {
                    // $script:0831180509004057$
                    // - Yeah, maybe you should give up.
                    case 0:
                        Id = 0; // TODO: 1101,1102 | 
                        return false;
                    // $script:0831180509004058$
                    // - Are you really giving it your all, though?
                    case 1:
                        Id = 0; // TODO: 1111,1112 | 
                        return false;
                }
                return true;
            case 1101:
                // $script:0831180509004059$ functionID=1 
                // - Hah hah, you think so? I knew I shouldn't have joined the Royal Guard.
                return true;
            case 1102:
                // $script:0831180509004060$ functionID=1 
                // - Hmmm, let me just... think about it.
                return true;
            case 1111:
                // $script:0831180509004061$ functionID=1 
                // - I feel like you just punched me in the face. Thanks for the pep talk.
                return true;
            case 1112:
                // $script:0831180509004062$ functionID=1 
                // - You're right. I'm ashamed of myself. I've been whining without even trying my best. 
                return true;
            case 2000:
                // $script:0831180509004063$ 
                // - I've heard a strange noise outside for the past few hours. I hate ignoring it, but it's not like I can go out and check. 
                // $script:0831180509004064$ 
                // - I can't leave the house unattended, you know? What if we get robbed? I don't want that on my head.
                // $script:0831180509004065$ 
                // - If you want to go investigate the noise yourself, feel free.
                // $script:0831180509004066$ 
                // - But just to be clear, I never asked you to, okay? I don't want that responsibility.
                return true;
            case 2100:
                // $script:0831180509004067$ 
                // - I wasn't sure if I should tell you, but $npcName:11000119[gender:0]$ stopped by today...
                // $script:0831180509004068$ 
                // - He wanted to know about the recent increase in the number of adventurers fracturing bones in $map:2000118$.
                // $script:0831180509004069$ 
                // - Hey, I never asked anyone to do anything. If they volunteer to investigate the quakes and then trip and break some bones, how is that my fault?
                // $script:0831180509004070$ 
                // - He said he wanted to check out the place himself and then left for $map:2000118$. Ugh, what if $npcName:11000119[gender:0]$ gets hurt too?
                return true;
            case 2200:
                // $script:0831180509004071$ 
                // - I've been told, if I have time to sit around and fret about things, I should do something to change them. So today, I decided to do just that! ...I wonder if it was the right choice.
                // $script:0831180509004072$ 
                // - A salesman stopped by the house today. Usually, they get annoyed by my indecisiveness and leave, but I was determined to make a purchase today!
                // $script:0831180509004073$ 
                // - He said this bowl had a self-washing feature. Well... see this oil stain?
                // $script:0831180509004074$ 
                // - This is why I shouldn't try new things. Ugh.
                return true;
            case 3000:
                // $script:0831180509004075$ 
                // - I really admire Captain $npcName:11000119[gender:0]$. He's the reason the people of $map:2000001$ can sleep at night.
                // $script:0831180509004076$ 
                // - People often compare $npcName:11000076[gender:0]$ with $npcName:11000119[gender:0]$, but I think $npcName:11000119[gender:0]$ is better.
                // $script:0831180509004077$ 
                // - It's not because I've seen them fight or anything. It's the way the Empress treats them.
                // $script:0831180509004078$ 
                // - $npcName:11000075[gender:1]$ always looks composed when she talks to $npcName:11000076[gender:0]$. She looks at him with unshakable trust in her eyes.
                // $script:0831180509004079$ 
                // - But she's different in front of $npcName:11000119[gender:0]$. She looks disconcerted and worried. No one else makes her look like that.
                // $script:0831180509004080$ functionID=1 
                // - In other words, $npcName:11000119[gender:0]$ has the ability to disarm her. Get it, $OwnerName$?
                return true;
            case 3100:
                // $script:0831180509004081$ 
                // - Hmm, if i had a worthy rival, I'd be way stronger than I am now. Like, $npcName:11000119[gender:0]$!
                // $script:0831180509004082$ 
                // - Did you know there's a rivalry between $npcName:11000119[gender:0]$ and $npcName:11000076[gender:0]$? Everyone in $map:2000001$ knows.
                // $script:0831180509004083$ 
                // - Guard Captain $npcName:11000119[gender:0]$ and Knight Captain $npcName:11000076[gender:0]$ have been best friends since they were kids.
                // $script:0831180509004084$ 
                // - They're both really good at fighting, too. A lot of people have high expectations of them, and everyone thinks of them as rivals.
                // $script:0831180509004085$ 
                // - I don't know if they'd agree, though. One second they're screaming in each others' faces, the next they're fighting enemies, side by side.
                // $script:0831180509004086$ functionID=1 
                // - Some folks say $npcName:11000169[gender:0]$ at the armory should be my rival, but he has a long way to go. Hmph.
                return true;
            case 4000:
                // $script:0831180509004087$ 
                // - The Royal Guard is charged with the safely of the entire $map:2000001$ palace.
                // $script:0831180509004088$ 
                // - $map:2000001$ is home to the Empress and the nobility. Not a day goes by without an incident of some sort. We have long, grueling shifts.
                // $script:0831180509004089$ 
                // - Luckily, Captain $npcName:11000119[gender:0]$ has allowed us to pick up work on the side.
                // $script:0831180509004090$ 
                // - The truth is, quite a number of people have filed injury claims against me, and I'm not making enough as a guard to pay them all. Just my luck, you know?
                return true;
            case 4100:
                // $script:0831180509004091$ 
                // - If you're asking because you're thinking of joining the Royal Guard, I suggest you reconsider.
                // $script:0831180509004092$ 
                // - $npcName:11000119[gender:0]$ is strict. It takes a tremendous amount of determination and effort to train under him.
                // $script:0831180509004093$ 
                // - As for me... Well... 
                return true;
            case 5000:
                // $script:0831180509004094$ 
                // - When I lived in $map:2000001$, I never imagined I'd join the Royal Guard. But three years ago, my father applied for me, without telling me.
                // $script:0831180509004095$ 
                // - If he didn't, I'd still be living happily in $map:2000001$. Being a guard isn't so bad, I guess...
                // $script:0831180509004096$ 
                // - All I have to do is follow the captain's commands. I don't have to worry about making decisions.
                // $script:0831180509004097$ 
                // - Whenever I can't decide something, someone else comes along and decides for me. What more could I ask for?
                return true;
            case 5100:
                // $script:0831180509004098$ 
                // - $npcName:11000119[gender:0]$ said we could apply for different responsibilities if we wanted to. I'm getting tired of investigating the quakes in $map:2000118$, so I considered it.
                // $script:0831180509004099$ 
                // - I thought about applying for front gate duties in $map:2000001$, but then realized I didn't want to deal with tourists.
                // $script:0831180509004100$ 
                // - I also didn't want to fight on the front lines in $map:2000146$ because I don't want to get hurt.
                // $script:0831180509004101$ 
                // - I would love to try new things, but when I start thinking about them, I get so worried and can't make up my mind.
                // $script:0831180509004102$ 
                // - Hmmm, I think I'm going to have to mull this over for a week or two.
                return true;
            case 6000:
                // $script:0831180509004103$ 
                // - Have I told you about $npcName:11000160[gender:1]$? She works in front of $map:2000001$ $map:2000188$ to help travelers find their way.
                // $script:0831180509004104$ 
                // - One time, I was standing in front of $map:2000188$, unable to decide what I should eat for over an hour. Did I want black noodles or spicy noodles? Suddenly $npcName:11000160[gender:1]$ showed up and handed me a bowl of black noodles.
                // $script:0831180509004105$ 
                // - She solved my dilemma so easily! How could I not fall in love with her right then and there? I don't know if $npcName:11000160[gender:1]$ knows how I feel about her, though. 
                // $script:0831180509004106$ 
                // - I miss $npcName:11000160[gender:1]$... I've been trying to decide for hours. Should I go to $map:2000001$ to see her?
                return true;
            case 7000:
                // $script:0831180509004107$ 
                // - Should I tell her my true feelings? 
                // $script:0831180509004108$ 
                // - You see, I'm not the only one with a major crush on 
                //   $npcName:11000160[gender:1]$. I think $npcName:11000169[gender:0]$ from the armory also likes her. 
                // $script:0831180509004109$ 
                // - If $npcName:11000160[gender:1]$ rejects me, it'll make things so awkward. If she doesn't reject me, things would get weird between me and $npcName:11000169[gender:0]$...
                // $script:0831180509004110$ 
                // - So you understand why I can't decide what to do, right?
                return true;
            case 100:
                // $script:0831180509004111$ 
                // - Hmm, you look like a stranger. Oops, should I not have said that?
                switch (selection) {
                    // $script:0831180509004112$
                    // - What do you mean?
                    case 0:
                        Id = 0; // TODO: 101,102 | 
                        return false;
                    // $script:0831180509004113$
                    // - I thought the house was empty. My mistake.
                    case 1:
                        Id = 0; // TODO: 103,104 | 
                        return false;
                    // $script:0831180509004114$
                    // - Who are you?
                    case 2:
                        Id = 0; // TODO: 105,106 | 
                        return false;
                }
                return true;
            case 101:
                // $script:0831180509004115$ 
                // - Think about it. If you are a stranger, you might be mad I said that. If you're not a stranger, I just offended the boss's guest. 
                return true;
            case 102:
                // $script:0831180509004116$ 
                // - Ummm... Give me a moment to think how I should respond. I'm not quite sure what to say...
                return true;
            case 103:
                // $script:0831180509004117$ 
                // - Oh, did you? Hmm, what should I do? Let you go, or arrest you for attempted burglary? Hmm...
                return true;
            case 104:
                // $script:0831180509004118$ 
                // - Breaking and entering, huh? But what should I do? Contact the royal guard or arrest you myself? Not quite sure about the protocol here. Let me think about this... 
                return true;
            case 105:
                // $script:0831180509004119$ 
                // - Me? Hmm, should I tell you my name? Or shouldn't I...? 
                return true;
            case 106:
                // $script:0831180509004120$ 
                // - I'm the man in charge of keeping the house secure! Who are you?
                return true;
            default:
                return true;
        }
    }
}
