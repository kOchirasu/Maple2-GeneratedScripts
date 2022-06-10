using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000794: Yoyo
/// </summary>
public class _11000794 : NpcScript {
    internal _11000794(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 1;2;3;4;5;6;9001;9002;9003;100
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180509005838$ 
                // - What is it? 
                return true;
            case 1:
                // $script:0831180509005839$ 
                // - Did you call me? 
                switch (selection) {
                    // $script:0831180509005840$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005841$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005842$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 2:
                // $script:0831180509005843$ 
                // - What's wrong? 
                switch (selection) {
                    // $script:0831180509005844$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005845$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005846$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 3:
                // $script:0831180509005847$ 
                // - Beh, I wondered who it was, but it was just you, $OwnerName$. 
                switch (selection) {
                    // $script:0831180509005848$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005849$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005850$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 4:
                // $script:0831180509005851$ 
                // - Did you call me? 
                switch (selection) {
                    // $script:0831180509005852$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005853$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005854$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509005855$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 5:
                // $script:0831180509005856$ 
                // - What's wrong? 
                switch (selection) {
                    // $script:0831180509005857$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005858$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005859$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509005860$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 6:
                // $script:0831180509005861$ 
                // - Beh, I wondered who it was, but it was just you, $OwnerName$. 
                switch (selection) {
                    // $script:0831180509005862$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005863$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005864$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509005865$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 9:
                // $script:0831180509005866$ 
                // - Are you really going to pay me?
<b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b> 
                switch (selection) {
                    // $script:0831180509005867$
                    // - Let me think about it some more.
                    case 0:
                        Id = 0; // TODO: 8040,8050,8060,9040 | 8999
                        return false;
                    // $script:0831180509005868$
                    // - (Pay $MaidSalary$.)
                    case 1:
                        Id = 0; // TODO: 8000,8001,8010,8011,8901 | 8900,8910
                        return false;
                }
                return true;
            case 8000:
                // $script:0831180509005869$ functionID=1 
                // - Yippee! I'm going to go show my paycheck to $npcName:11000368[gender:0]$! And I'm going to treat him to some delicious food! $OwnerName$, you're the best. Thanks! 
                return true;
            case 8001:
                // $script:0831180509005870$ functionID=1 
                // - Hee hee! I'm so happy! I'm going to go shop today. I want to make some new shoes. $OwnerName$, I'll make you a pair too! 
                return true;
            case 8010:
                // $script:0831180509005871$ functionID=1 
                // - Really? Is this for me? Then... I can make things again, can't I? I'm happy, even if this is just a dream! I feel as if I can make any of my illusions real! 
                return true;
            case 8011:
                // $script:0831180509005872$ functionID=1 
                // - Mm? $OwnerName$... I-I'm sorry I misunderstood you... I thought you hated me. As a token of apology, I'll grant you a wish. Tell me when you want to use it! 
                return true;
            case 8020:
                // $script:0831180509005873$ functionID=1 
                // - I'm worried. I want to buy some crafting materials, but I don't have money.  I'll just wait until I get my next paycheck...  
                return true;
            case 8021:
                // $script:0831180509005874$ functionID=1 
                // - D-don't worry about it! I was just talking to myself! 
                switch (selection) {
                    // $script:0831180509005875$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005876$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005877$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509005878$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8040:
                // $script:0831180509005879$ 
                // - Did you call me? 
                switch (selection) {
                    // $script:0831180509005880$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005881$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005882$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509005883$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8050:
                // $script:0831180509005884$ 
                // - Are you bored? 
                switch (selection) {
                    // $script:0831180509005885$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005886$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005887$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509005888$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8060:
                // $script:0831180509005889$ 
                // - I'm listening. 
                switch (selection) {
                    // $script:0831180509005890$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005891$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005892$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509005893$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8900:
                // $script:0831180509005894$ 
                // - Mm? $OwnerName$, didn't you just try to pull something out of your pocket? What is it? What is it? I want to know! ...Whatever it is, I want it! 
                return true;
            case 8901:
                // $script:0831180509005895$ 
                // - $OwnerName$, please don't do this. You already paid me. I guess I could just take it, but I'm a good fairfolk and I don't like to be dishonest. Pay me a compliment instead! 
                return true;
            case 8910:
                // $script:0831180509005896$ 
                // - $OwnerName$!! You've got nothing but duuuust in your poooockets... Poor me. Poor you. What do we do now? 
                return true;
            case 8999:
                // $script:0831180509005897$ 
                // - What just happened? This doesn't make sense! Let me use my illusions to fix it! 
                return true;
            case 9001:
                // $script:0831180509005898$ 
                // - It's been $MaidPassedDay$... I feel weak...  
                switch (selection) {
                    // $script:0831180509005899$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509005900$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005901$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9002:
                // $script:0831180509005902$ 
                // - $OwnerName$, do you hate me?  
                switch (selection) {
                    // $script:0831180509005903$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509005904$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005905$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9003:
                // $script:0831180509005906$ 
                // - Why did you summon me? I don't even have the energy to talk...   
                switch (selection) {
                    // $script:0831180509005907$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509005908$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005909$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9010:
                // $script:0831180509005910$ 
                // - I can't! My contract's expired! I promised not to work without a contract!  
                return true;
            case 9011:
                // $script:0831180509005911$ functionID=1 
                // - That's not impooooortant. Our contract expired, and I have no moneeeeey to spend.  This is soooo depressing...  
                return true;
            case 9020:
                // $script:0831180509005912$ functionID=1 
                // - I don't know what to do. I can't do anything...  
                return true;
            case 9021:
                // $script:0831180509005913$ functionID=1 
                // - $OwnerName$, what do you do all day? Can I join you?  
                switch (selection) {
                    // $script:0831180509005914$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509005915$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005916$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9040:
                // $script:0831180509005917$ 
                // - Stop talking to me. I'm not happy with you.  
                switch (selection) {
                    // $script:0831180509005918$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509005919$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005920$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9030:
                // $script:0831180509005921$ 
                // - Since I've got nothing to do, I keep zoning out. But if I'm not paying attention, the illusions I cast on this house might disappear, and then I'll be doomed! I don't want you to find out about all the holes in the walls... 
                return true;
            case 9031:
                // $script:0831180509005922$ 
                // - I'm hungry... I'm still growing, so I need to eat well or I might be stunted for life. I want to grow tall!  
                return true;
            case 9032:
                // $script:0831180509005923$ 
                // - What if I forget how to make shoes because I haven't been practicing? I want to make shoes. $OwnerName$, don't you want me to make shoes? 
                return true;
            case 10:
                // $script:0831180509005924$ functionID=1 
                // - My shoe-making skills are famous amongst fairies. 
                return true;
            case 11:
                // $script:0831180509005925$ functionID=1 
                // - Ask me any time! 
                return true;
            case 20:
                // $script:0831180509005926$ functionID=1 
                // - What are you so curious about? 
                return true;
            case 21:
                // $script:0831180509005927$ functionID=1 
                // - Did you call me? 
                switch (selection) {
                    // $script:0831180509005928$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005929$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005930$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 22:
                // $script:0831180509005931$ functionID=1 
                // - Did you call me? 
                switch (selection) {
                    // $script:0831180509005932$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005933$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005934$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509005935$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 30:
                // $script:0831180509005936$ 
                // - Do you have something to say to me? 
                switch (selection) {
                    // $script:0831180509005937$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509005938$
                    // - (Talk about illusionism.)
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,9011 | 
                        return false;
                    // $script:0831180509005939$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509005940$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 31:
                // $script:0831180509005941$ 
                // - I have a feeling something's going to happen today. 
                switch (selection) {
                    // $script:0831180509005942$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509005943$
                    // - (Talk about illusionism.)
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,9011 | 
                        return false;
                    // $script:0831180509005944$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509005945$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 32:
                // $script:0831180509005946$ 
                // - I hope $npcName:11000368[gender:0]$ will come visit the house. 
                switch (selection) {
                    // $script:0831180509005947$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509005948$
                    // - (Talk about illusionism.)
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,9011 | 
                        return false;
                    // $script:0831180509005949$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,7000,9011 | 
                        return false;
                    // $script:0831180509005950$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 40:
                // $script:0831180509005951$ 
                // - Did you call me? 
                switch (selection) {
                    // $script:0831180509005952$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005953$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005954$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 50:
                // $script:0831180509005955$ 
                // - Are you bored? 
                switch (selection) {
                    // $script:0831180509005956$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005957$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005958$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 60:
                // $script:0831180509005959$ 
                // - I'm listening. 
                switch (selection) {
                    // $script:0831180509005960$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509005961$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509005962$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 1000:
                // $script:0831180509005963$ 
                // - $OwnerName$, I need your opinion on something. 
                // $script:0831180509005964$ 
                // - My dream is to go to $map:2000100$. I've heard it's filled with beautiful shiny things. I'd love to see it with my own eyes. 
                // $script:0831180509005965$ 
                // - But $npcName:11000368[gender:0]$ says I can't. It's too dangerous. $OwnerName$, what do you think? Can I go to $map:2000100$? 
                switch (selection) {
                    // $script:0831180509005966$
                    // - No.
                    case 0:
                        Id = 0; // TODO: 1001,1002 | 
                        return false;
                    // $script:0831180509005967$
                    // - Only if I go with you.
                    case 1:
                        Id = 0; // TODO: 1011,1012 | 
                        return false;
                }
                return true;
            case 1001:
                // $script:0831180509005968$ functionID=1 
                // - $OwnerName$, you're just like $npcName:11000368[gender:0]$! Both of you think I'm too weak to do anything, and it makes me so mad! 
                return true;
            case 1002:
                // $script:0831180509005969$ functionID=1 
                // - The more you say no, the more I want to do it. That's the way a fairy is! Ugh, I want to go there. I want to go there. I really want to go there! 
                return true;
            case 1011:
                // $script:0831180509005970$ functionID=1 
                // - Really?! You're going with me? Then let's go! I want to go right now! 
                return true;
            case 1012:
                // $script:0831180509005971$ functionID=1 
                // - Really? Yippee! I am sooooo so so so happy right now! 
                return true;
            case 1100:
                // $script:0831180509005972$ 
                // - This is bad... What do I do? 
                // $script:0831180509005973$ 
                // - I use illusions to help people, but I keep getting them in trouble. I'm a disgrace to the fairfolk. 
                // $script:0831180509005974$ 
                // - Maybe I should stop messing with illusions altogether.  
                switch (selection) {
                    // $script:0831180509005975$
                    // - You're overreacting.
                    case 0:
                        Id = 0; // TODO: 1111,1112 | 
                        return false;
                    // $script:0831180509005976$
                    // - Maybe... a little?
                    case 1:
                        Id = 0; // TODO: 1101,1102 | 
                        return false;
                }
                return true;
            case 1101:
                // $script:0831180509005977$ functionID=1 
                // - You don't have to say it. I already know it. Words can cut deep, you know. 
                return true;
            case 1102:
                // $script:0831180509005978$ functionID=1 
                // - You're so insensitive, $OwnerName$. Maybe that's why your face is so ugly. Hmph. 
                return true;
            case 1111:
                // $script:0831180509005979$ functionID=1 
                // - Do you mean that? Really? I wish everyone was more like you, $OwnerName$. 
                return true;
            case 1112:
                // $script:0831180509005980$ functionID=1 
                // - Thank you, $OwnerName$. I feel much better now. 
                return true;
            case 2000:
                // $script:0831180509005981$ 
                // - A friend of mine came to see me for the first time after a long time. His name is $npcName:11000368[gender:0]$ and he lives in $map:02000017$. 
                // $script:0831180509005982$ 
                // - He's round and furry. I love him very much. $OwnerName$, have you met him by any chance? 
                // $script:0831180509005983$ 
                // - I was so happy to see him that I danced. But then I noticed that $npcName:11000368[gender:0]$ looked very sad. 
                // $script:0831180509005984$ 
                // - $npcName:11000368[gender:0]$ said humans are destroying the forest and that a lot of the zelkovas and willows are gone now. 
                // $script:0831180509005985$ 
                // - I can't imagine losing my friends. I just said "see you later!" to them a few days ago... 
                return true;
            case 2100:
                // $script:0831180509005986$ 
                // - Not a thing... I may have cracked the wall over there...  
                // $script:0831180509005987$ 
                // - S-sorry! It's all my fault!! Wahhhh! 
                // $script:0831180509005988$ 
                // - I wanted to know if the $item:30000104$ $npcName:11000368[gender:0]$ gave me was real, so I threw it at the tree in the back of the house... All of it. 
                // $script:0831180509005989$ 
                // - The tree grew taller than the house in the blink of an eye! I thought I was going to be swallowed alive! 
                // $script:0831180509005990$ 
                // - $npcName:11000368[gender:0]$ said I should be careful... I should've listened to him. This is all because I didn't trust my friend. 
                return true;
            case 2200:
                // $script:0831180509005991$ 
                // - $OwnerName$! $OwnerName$! I've got something for you! 
                // $script:0831180509005992$ 
                // - Tah-dah! I made these shoes for you! I've even embroidered your name right here, $OwnerName$. Try them on! 
                // $script:0831180509005993$ 
                // - ...
...
...
They don't fit... $OwnerName$, your feet are too big. 
                // $script:0831180509005994$ 
                // - I thought you were the same size as me. I was wrong. I'm sad now. Waaahhh! 
                return true;
            case 3000:
                // $script:0831180509005995$ 
                // - My illusions don't last forever because they're thoughts from my head given shape and form. 
                // $script:0831180509005996$ 
                // - And thoughts never last long. To keep my illusions up, I have to think about them constantly, but my head gets filled with new thoughts all the time. 
                // $script:0831180509005997$ 
                // - Some of the other fairies have such great concentration they can retain illusions for a very long time, but not me. 
                // $script:0831180509005998$ functionID=1 
                // - I'm doomed! I made a hole in the wall, so I placed an illusion on it. Now the illusion's gone because I was distracted for a second. Waaaah. 
                return true;
            case 3100:
                // $script:0831180509005999$ 
                // - It's not easy to cast illusions. I have to be happy, or my thoughts won't materialize. 
                // $script:0831180509006000$ 
                // - The more exciting a thought, the easier it is to materialize it. That's why I can't resurrect the dead or hurt people with my illusions. Even if I could, I would never do it. 
                // $script:0831180509006001$ functionID=1 
                // - Humans often think fairies are mischievous because of our illusionism. But it's entertaining, isn't it? Heh heh! 
                return true;
            case 4000:
                // $script:0831180509006002$ 
                // - I can cast illusions. All fairies can. 
                // $script:0831180509006003$ 
                // - Illusionism is not magic. They're two different things. 
                // $script:0831180509006004$ 
                // - The fairies of Ellinia use magic. It's the great—and scary—power of nature. 
                // $script:0831180509006005$ 
                // - But we use illusionism, a mysterious and interesting power unique to us. 
                // $script:0831180509006006$ 
                // - Illusionism enables us to materialize the thoughts in our heads. The problem is that you can't always perfectly control your thoughts. You have to be careful when you cast illusions. 
                return true;
            case 4100:
                // $script:0831180509006007$ 
                // - Did you just ask me to cast an illusion? Did you really? 
                // $script:0831180509006008$ 
                // - All right! Count on me! Now, what kind of illusion do you want? 
                // $script:0831180509006009$ 
                // - You want to grow taller? That's easy, $OwnerName$! Real easy! 
                // $script:0831180509006010$ 
                // - Abracadingdong!
Yaliyali pingpong!
Grow tall! 
                // $script:0831180509006011$ 
                // - I-I'm sorry... Only your head grew bigger... Actually it was big before, and now it's even bigger...  
                return true;
            case 5000:
                // $script:0831180509006012$ 
                // - I thought I was the only fairfolk who loses shoes all the time, but I'm not. 
                // $script:0831180509006013$ 
                // - Sometimes I can hear one of the fairfolk crying about lost shoes somewhere near $map:02000023$. $OwnerName$, could you go help her? 
                // $script:0831180509006014$ 
                // - From her voice, I can tell she's a pretty fairfolk. Ahem, $OwnerName$, you look like you're too busy to help her. I'll go. 
                return true;
            case 5100:
                // $script:0831180509006015$ 
                // - I'm so scared of humans. I can't help it! You're scary and I'm shy! 
                // $script:0831180509006016$ 
                // - But, $OwnerName$, you're different. You're kind and affectionate. I hope all humans can be more like you.  
                // $script:0831180509006017$ 
                // - But I'm not ready to meet them. Once, a human swindled me out of all my money.  
                // $script:0831180509006018$ 
                // - $OwnerName$, I know you're good, but I can't trust the others of your kind.  
                return true;
            case 6000:
                // $script:0831180509006019$ 
                // - Some fairies hibernate. $npcName:11000368[gender:0]$ does. So does $npcName:11000677$. 
                // $script:0831180509006020$ 
                // - They say they can't stop themselves from falling asleep. I don't hibernate, so I wouldn't know. 
                // $script:0831180509006021$ 
                // - They get really irritated if their sleep is interrupted. Some fairies even attack anyone who wakes them up. 
                // $script:0831180509006022$ 
                // - So if you see some fairies hibernating, you'd better let them sleep. Got it? 
                return true;
            case 7000:
                // $script:0831180509006023$ 
                // - $npcName:11000368[gender:0]$ keeps telling everyone that I'm timid, and it's getting on my nerves! I'm not timid at all! 
                // $script:0831180509006024$ 
                // - Remember how I spent all of last Friday preparing dinner for you, $OwnerName$? And you said the soup was salty? See? I'm bold! I'm not too timid to use a lot of salt!  
                // $script:0831180509006025$ 
                // - You know what, I don't care what $npcName:11000368[gender:0]$ says. I'm not upset at him. 
                // $script:0831180509006026$ 
                // - I mean it! I know I'm not the timid fairfolk he thinks I am! I'm bold... and I'm magnanimous and forgiving! That's right, I'm pretty amazing! 
                return true;
            case 100:
                // $script:0831180509006027$ 
                // - A s-stranger...?! D-did you come for me?! 
                switch (selection) {
                    // $script:0831180509006028$
                    // - Yep!
                    case 0:
                        Id = 0; // TODO: 101,102 | 
                        return false;
                    // $script:0831180509006029$
                    // - Nope!
                    case 1:
                        Id = 0; // TODO: 103,104 | 
                        return false;
                    // $script:0831180509006030$
                    // - Who are you?
                    case 2:
                        Id = 0; // TODO: 105,106 | 
                        return false;
                }
                return true;
            case 101:
                // $script:0831180509006031$ 
                // - B-but wh-what for? I-I didn't do anything wrong! 
                return true;
            case 102:
                // $script:0831180509006032$ 
                // - Wh-what kind of business do you have with me? I'm one of the fairfolk! I c-can illusion you!! I can!! 
                return true;
            case 103:
                // $script:0831180509006033$ 
                // - Whew! ...Then why are you in this house? 
                return true;
            case 104:
                // $script:0831180509006034$ 
                // - Really? You scared me for a moment. 
                return true;
            case 105:
                // $script:0831180509006035$ 
                // - My name is $MaidName$. I'm one of the good fairies. 
                return true;
            case 106:
                // $script:0831180509006036$ 
                // - A fairfolk can stay in a human's house.  There's nothing wrong with that! 
                return true;
            default:
                return true;
        }
    }
}
