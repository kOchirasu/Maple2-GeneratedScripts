using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000779: Jayce
/// </summary>
public class _11000779 : NpcScript {
    internal _11000779(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 1;2;3;4;5;6;9001;9002;9003;100
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180509003461$ 
                // - Hm, yes? 
                return true;
            case 1:
                // $script:0831180509003462$ 
                // - $OwnerName$, let's go over your schedule for the day... 
                switch (selection) {
                    // $script:0831180509003463$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003464$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003465$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 2:
                // $script:0831180509003466$ 
                // - I know everything about you, $OwnerName$. 
                switch (selection) {
                    // $script:0831180509003467$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003468$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003469$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 3:
                // $script:0831180509003470$ 
                // - Don't strain yourself, now. 
                switch (selection) {
                    // $script:0831180509003471$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003472$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003473$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 4:
                // $script:0831180509003474$ 
                // - $OwnerName$, let's go over your schedule for the day... 
                switch (selection) {
                    // $script:0831180509003475$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003476$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003477$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509003478$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 5:
                // $script:0831180509003479$ 
                // - I know everything about you, $OwnerName$. 
                switch (selection) {
                    // $script:0831180509003480$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003481$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003482$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509003483$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 6:
                // $script:0831180509003484$ 
                // - Don't strain yourself, now. 
                switch (selection) {
                    // $script:0831180509003485$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003486$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003487$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509003488$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 9:
                // $script:0831180509003489$ 
                // - Would you like to pay me?
<b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b> 
                switch (selection) {
                    // $script:0831180509003490$
                    // - Let me think about it some more.
                    case 0:
                        Id = 0; // TODO: 8040,8050,8060,9040 | 8999
                        return false;
                    // $script:0831180509003491$
                    // - (Pay $MaidSalary$.)
                    case 1:
                        Id = 0; // TODO: 8000,8001,8010,8011,8901 | 8900,8910
                        return false;
                }
                return true;
            case 8000:
                // $script:0831180509003492$ functionID=1 
                // - Absolutely. I'll extend our employment contract. You'll want to read through all the fine print yourself on this one, $OwnerName$. 
                return true;
            case 8001:
                // $script:0831180509003493$ functionID=1 
                // - Agreed. This arrangement is mutually beneficial, so this extension was expected. Here's to a long and prosperous relationship. 
                return true;
            case 8010:
                // $script:0831180509003494$ functionID=1 
                // - Very well. I accept your terms. I hope you weren't expecting any thanks... I'm sure I've earned this. 
                return true;
            case 8011:
                // $script:0831180509003495$ functionID=1 
                // - Confirmed. I accept the position. We have a great working relationship, as long as you continue to maintain a professional distance. 
                return true;
            case 8020:
                // $script:0831180509003496$ functionID=1 
                // - $OwnerName$, our contract expires soon. No need to thank me. Managing your schedule is part of my job. 
                return true;
            case 8021:
                // $script:0831180509003497$ functionID=1 
                // - Just don't make me repeat myself. 
                switch (selection) {
                    // $script:0831180509003498$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003499$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003500$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509003501$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8040:
                // $script:0831180509003502$ 
                // - Don't strain yourself, now. 
                switch (selection) {
                    // $script:0831180509003503$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003504$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003505$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509003506$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8050:
                // $script:0831180509003507$ 
                // - $OwnerName$, let's go over your schedule for the day... 
                switch (selection) {
                    // $script:0831180509003508$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003509$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003510$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509003511$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8060:
                // $script:0831180509003512$ 
                // - Yes? 
                switch (selection) {
                    // $script:0831180509003513$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003514$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003515$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509003516$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 8900:
                // $script:0831180509003517$ 
                // - Ah, I expected this. Anyone can see that you're pretty wasteful. 
                return true;
            case 8901:
                // $script:0831180509003518$ 
                // - You're even more financially inept than I anticipated. What I mean is, you've already paid me this month. 
                return true;
            case 8910:
                // $script:0831180509003519$ 
                // - Yes, I already knew this would happen. I keep tabs on your bank account, you know. Please don't waste my time on this again. Now, I have some documents to sort through... 
                return true;
            case 8999:
                // $script:0831180509003520$ 
                // - This is hardly ideal. Please don't allow this to happen again. 
                return true;
            case 9001:
                // $script:0831180509003521$ 
                // - So. What is the plan? 
                switch (selection) {
                    // $script:0831180509003522$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509003523$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003524$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9002:
                // $script:0831180509003525$ 
                // - Time is money, and... aren't your broke? Make this quick. 
                switch (selection) {
                    // $script:0831180509003526$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509003527$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003528$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9003:
                // $script:0831180509003529$ 
                // - Our contract has expired. What else is there to discuss? 
                switch (selection) {
                    // $script:0831180509003530$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509003531$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003532$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9010:
                // $script:0831180509003533$ 
                // - My contract has expired, and I live and breath by contracts. I can't work until you sign a new one. 
                return true;
            case 9011:
                // $script:0831180509003534$ functionID=1 
                // - I'm stunned. Did you realize our contract expired, even after I reminded you? So let's talk about that. How could you let this happen? 
                return true;
            case 9020:
                // $script:0831180509003535$ functionID=1 
                // - It's been $MaidPassedDay$ since our contract expired. You don't need to give me any excuses. 
                return true;
            case 9021:
                // $script:0831180509003536$ functionID=1 
                // - Words won't change a thing. 
                switch (selection) {
                    // $script:0831180509003537$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509003538$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003539$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9040:
                // $script:0831180509003540$ 
                // - If you don't have anything important to say, I'd like to go. Do you mind? 
                switch (selection) {
                    // $script:0831180509003541$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        Id = 9;
                        return false;
                    // $script:0831180509003542$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003543$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 9030:
                // $script:0831180509003544$ 
                // - I don't have time to look after you unless you rehire me, but I'm not leaving either. My desk here is set up just the way I like it. So don't mind me. Just do whatever it is you need to do. 
                return true;
            case 9031:
                // $script:0831180509003545$ 
                // - You've been acting so strange lately, not at all like yourself. What are you up to? 
                return true;
            case 9032:
                // $script:0831180509003546$ 
                // - You want a drink? Really? Do you realize our contract remains unsigned? Now, excuse me. I have business to take care of. 
                return true;
            case 10:
                // $script:0831180509003547$ functionID=1 
                // - Would you like a drink? 
                return true;
            case 11:
                // $script:0831180509003548$ functionID=1 
                // - Come on, I insist. 
                return true;
            case 20:
                // $script:0831180509003549$ functionID=1 
                // - Please, let's not mix business with pleasure. 
                return true;
            case 21:
                // $script:0831180509003550$ functionID=1 
                // - I know everything about you, $OwnerName$. 
                switch (selection) {
                    // $script:0831180509003551$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003552$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003553$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 22:
                // $script:0831180509003554$ functionID=1 
                // - I know everything about you, $OwnerName$. 
                switch (selection) {
                    // $script:0831180509003555$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003556$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003557$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                    // $script:0831180509003558$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        Id = 9;
                        return false;
                }
                return true;
            case 30:
                // $script:0831180509003559$ 
                // - I'm rather busy, so make this quick. 
                switch (selection) {
                    // $script:0831180509003560$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509003561$
                    // - Tell me about $map:02000216$.
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,9011 | 
                        return false;
                    // $script:0831180509003562$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,6100,7000,9011 | 
                        return false;
                    // $script:0831180509003563$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 31:
                // $script:0831180509003564$ 
                // - $OwnerName$! You look absolutely wretched. 
                switch (selection) {
                    // $script:0831180509003565$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509003566$
                    // - Tell me about $map:02000216$.
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,9011 | 
                        return false;
                    // $script:0831180509003567$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,6100,7000,9011 | 
                        return false;
                    // $script:0831180509003568$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 32:
                // $script:0831180509003569$ 
                // - ...I have nothing to say. 
                switch (selection) {
                    // $script:0831180509003570$
                    // - Anything interesting happen today?
                    case 0:
                        Id = 0; // TODO: 1000,1100,2000,2100,2200,9011 | 
                        return false;
                    // $script:0831180509003571$
                    // - Tell me about $map:02000216$.
                    case 1:
                        Id = 0; // TODO: 3000,3100,4000,4100,9011 | 
                        return false;
                    // $script:0831180509003572$
                    // - (Ask your servant a personal question.)
                    case 2:
                        Id = 0; // TODO: 5000,5100,6000,6100,7000,9011 | 
                        return false;
                    // $script:0831180509003573$
                    // - Back.
                    case 3:
                        Id = 0; // TODO: 8040,8050,8060,40,50,60,9040 | 
                        return false;
                }
                return true;
            case 40:
                // $script:0831180509003574$ 
                // - Don't strain yourself, now. 
                switch (selection) {
                    // $script:0831180509003575$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003576$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003577$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 50:
                // $script:0831180509003578$ 
                // - $OwnerName$, let's go over your schedule for the day... 
                switch (selection) {
                    // $script:0831180509003579$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003580$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003581$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 60:
                // $script:0831180509003582$ 
                // - Yes? 
                switch (selection) {
                    // $script:0831180509003583$
                    // - I need you to craft something.
                    case 0:
                        Id = 0; // TODO: 10,9010 | 8999
                        return false;
                    // $script:0831180509003584$
                    // - I want to check your profile.
                    case 1:
                        Id = 0; // TODO: 20,8020,9020 | 8999
                        return false;
                    // $script:0831180509003585$
                    // - Let's chat!
                    case 2:
                        Id = 0; // TODO: 30,31,32,9030,9031,9032 | 
                        return false;
                }
                return true;
            case 1000:
                // $script:0831180509003586$ 
                // - Be straight with me for a minute. 
                // $script:0831180509003587$ 
                // - You know I'm not working for you because I like you... 
                // $script:0831180509003588$ 
                // - So... why don't you just let me go? 
                switch (selection) {
                    // $script:0831180509003589$
                    // - Hey, your skills are top notch.
                    case 0:
                        Id = 0; // TODO: 1011,1012 | 
                        return false;
                    // $script:0831180509003590$
                    // - I'm... I'm not really sure...
                    case 1:
                        Id = 0; // TODO: 1001,1002 | 
                        return false;
                }
                return true;
            case 1001:
                // $script:0831180509003591$ functionID=1 
                // - Talking to you makes me feel like I'm losing brain cells. 
                return true;
            case 1002:
                // $script:0831180509003592$ functionID=1 
                // - Am I really stuck with you? 
                return true;
            case 1011:
                // $script:0831180509003593$ functionID=1 
                // - Ah, perfect. That's just the way I like it. 
                return true;
            case 1012:
                // $script:0831180509003594$ functionID=1 
                // - I appreciate your honesty. I may have been wrong about you. 
                return true;
            case 1100:
                // $script:0831180509003595$ 
                // - Why are you staring at me? 
                // $script:0831180509003596$ 
                // - I'm used to people glaring at me at the Black Market, sure, but... 
                // $script:0831180509003597$ 
                // - I don't enjoy being gawked at by you. Please try to stop. 
                switch (selection) {
                    // $script:0831180509003598$
                    // - I can't help it...
                    case 0:
                        Id = 0; // TODO: 1101,1102 | 
                        return false;
                    // $script:0831180509003599$
                    // - I'm so, so sorry!
                    case 1:
                        Id = 0; // TODO: 1111,1112 | 
                        return false;
                }
                return true;
            case 1101:
                // $script:0831180509003600$ functionID=1 
                // - Perhaps there is such a thing as too much honesty, after all... 
                return true;
            case 1102:
                // $script:0831180509003601$ functionID=1 
                // - ... Does that mean you're not going to stop? 
                return true;
            case 1111:
                // $script:0831180509003602$ functionID=1 
                // - Oh. Well, you don't have to go that far. Now things are uncomfortable... 
                return true;
            case 1112:
                // $script:0831180509003603$ functionID=1 
                // - So you won't do it anymore? Good.  
                return true;
            case 2000:
                // $script:0831180509003604$ 
                // - Nothing I couldn't handle. 
                // $script:0831180509003605$ 
                // - Some men in masks barged into the house, demanding I hand over everything of value. 
                // $script:0831180509003606$ 
                // - Hmph. They won't be back. 
                // $script:0831180509003607$ 
                // - Even in my pencil skirt, I was able to bruise them up pretty good. I'm a certified instructor in several forms of martial arts. 
                // $script:0831180509003608$ 
                // - No need to look so shocked. In my line of work, self-defense is essential. Money makes people desperate, which can lead to crazy behavior, and I have to be able to make decisions without worrying about that. 
                return true;
            case 2100:
                // $script:0831180509003609$ 
                // - $OwnerName$, while you were out, $npcName:11000004[gender:0]$ called once and $npcName:11000096[gender:0]$ called twice. 
                // $script:0831180509003610$ 
                // - $npcName:11000004[gender:0]$ stated that he received new product, which he thought you might be interested in. 
                // $script:0831180509003611$ 
                // - $npcName:11000096[gender:0]$ called because he can't get a hold of $npcName:11000106[gender:1]$ and was wondering if you knew where she was. 
                // $script:0831180509003612$ 
                // - Later, he called back to ask my name. I guess that part isn't really relevant. 
                // $script:0831180509003613$ 
                // - Now, excuse me. I have some goods to oversee. 
                return true;
            case 2200:
                // $script:0831180509003614$ 
                // - $OwnerName$, you look exhausted.  
                // $script:0831180509003615$ 
                // - It's a good thing I just made this special juice. Drink it. It'll give you an energy boost. 
                // $script:0831180509003616$ 
                // - I whipped it up myself. Maybe we should name it. 
                // $script:0831180509003617$ 
                // - It has a whole $npcName:21000001$ in it. How about we call it... Power Mush? 
                return true;
            case 3000:
                // $script:0831180509003618$ 
                // - Most of the objects traded at the $map:02000216$ are rare and expensive. 
                // $script:0831180509003619$ 
                // - Why is the $map:02000216$ such a popular place to sell? It should be obvious. 
                // $script:0831180509003620$ 
                // - The $map:02000216$ is the only place you can trade valuable items quickly and safely. 
                // $script:0831180509003621$ functionID=1 
                // - More importantly, you can remain anonymous. We don't ask questions about where you obtained your item at the $map:02000216$. All we care about is how much it's worth. 
                return true;
            case 3100:
                // $script:0831180509003622$ 
                // - Today was exhausting. Funny how all it takes is a little ignorance to ruin your day, isn't it? We had a new customer show up at the $map:02000216$. 
                // $script:0831180509003623$ 
                // - He paid an exorbitant price for a cheap item without researching what he was buying. 
                // $script:0831180509003624$ 
                // - After he realized it, he raised a real ruckus, screaming that he'd been scammed, we'd hear from his lawyer, yadda yadda. 
                // $script:0831180509003625$ 
                // - It's not our fault he made a poor purchase. Even if we wanted to help, our policy at the $map:02000216$ is to never release the personal information of our sellers. 
                // $script:0831180509003626$ functionID=1 
                // - Even you aren't above that policy, $OwnerName$, so be careful what you purchase and sell at the $map:02000216$. 
                return true;
            case 4000:
                // $script:0831180509003627$ 
                // - Are you trying to ask about Blackstar? I had no idea you were even aware of that organization. 
                // $script:0831180509003628$ 
                // - Does this mean you've also heard of $npcName:11000251[gender:0]$? What exactly is it that you want to know? 
                // $script:0831180509003629$ 
                // - $npcName:11000251[gender:0]$ is one of the $map:02000216$'s many sponsors. He was instrumental in the establishment of the market. 
                // $script:0831180509003630$ 
                // - Do I hear suspicion in your tone? Are you trying to ruin our business relationship? 
                return true;
            case 4100:
                // $script:0831180509003631$ 
                // - I'm perfectly aware that not everyone has a positive opinion of our business... 
                // $script:0831180509003632$ 
                // - But no one can deny that the $map:02000216$ has helped revitalize the economy in the area. 
                // $script:0831180509003633$ 
                // - Most of the citizens of $map:02000100$, including Mayor $npcName:11000065[gender:0]$, support us. We've made ourselves vital, and now we're unstoppable.  
                return true;
            case 5000:
                // $script:0831180509003634$ 
                // - Ah, this is specifically covered in our contract. 
                // $script:0831180509003635$ 
                // - You'll see in Section IV, Article 17, that for the duration of my period in your employ, you are not to pry into my personal business. 
                // $script:0831180509003636$ 
                // - Now, if you're done trying to break the rules of our contract, I'd like to return to work. 
                return true;
            case 5100:
                // $script:0831180509003637$ 
                // - Such persistence, $OwnerName$! What exactly do you want to know so terribly much? 
                // $script:0831180509003638$ 
                // - My work history? My childhood? My relationship with my family? 
                // $script:0831180509003639$ 
                // - None of that makes a bit of difference. I know who I am: one of the top traders at the $map:02000216$ and your personal secretary. Does the rest matter? 
                return true;
            case 6000:
                // $script:0831180509003640$ 
                // - I do have a hypothetical quandary to discuss with you. I'm interested in your opinion. 
                // $script:0831180509003641$ 
                // - Say there was a girl who grew up in the slums of $map:02000100$. An orphan, with no memory of her parents, begging and stealing and trying to survive. 
                // $script:0831180509003642$ 
                // - Let's say one day she tried to steal a man's wallet and was caught. 
                // $script:0831180509003643$ 
                // - To her surprise, instead of throwing her in jail, the man made a joke, admired her cleverness, then took her to his home, where he gave her clean clothes, a delicious meal, and a safe place to sleep, away from the vultures at the $map:02000100$ 
                // $script:0831180509003644$ 
                // - She was so grateful for his kindness, she became determined to pay him back in any way she could. He had changed her life. 
                // $script:0831180509003645$ 
                // - For the next few decades, she worked tirelessly for that man. But then, one day, she learned that was he was doing was... morally abhorrent. 
                // $script:0831180509003646$ 
                // - Since then, she's been torn, unsure whether to follow her moral inclinations or remain loyal to the man who had saved her from a life on the streets. What would you do, if you were her? Remember, I'm asking for a friend. 
                return true;
            case 7000:
                // $script:0831180509003647$ 
                // - You seem awfully curious to find out why I took on secretarial duties. 
                // $script:0831180509003648$ 
                // - Let's just say... I'm doing it as a favor for someone who's been like a father to me since I was a child. 
                // $script:0831180509003649$ 
                // - I'm here to track your every move. That's all I can tell you. 
                // $script:0831180509003650$ 
                // - As for who this man is... Heh. I don't know, why don't you try to find out? It could be someone you know. 
                return true;
            case 100:
                // $script:0831180509003651$ 
                // - How may I help you? 
                switch (selection) {
                    // $script:0831180509003652$
                    // - I'm here to see the owner.
                    case 0:
                        Id = 0; // TODO: 101,102 | 
                        return false;
                    // $script:0831180509003653$
                    // - I'm here to see you.
                    case 1:
                        Id = 0; // TODO: 103,104 | 
                        return false;
                    // $script:0831180509003654$
                    // - Who are you?
                    case 2:
                        Id = 0; // TODO: 105,106 | 
                        return false;
                }
                return true;
            case 101:
                // $script:0831180509003655$ 
                // - Did you? Strange. I don't have you in the schedule... 
                return true;
            case 102:
                // $script:0831180509003656$ 
                // - If that's the case, please call me to schedule an appointment first. 
                return true;
            case 103:
                // $script:0831180509003657$ 
                // - Interesting. If you have business with me, please come see me at the $map:02000216$ instead. 
                return true;
            case 104:
                // $script:0831180509003658$ 
                // - Do I look like I have time for games? 
                return true;
            case 105:
                // $script:0831180509003659$ 
                // - I am $MaidName$, $OwnerName$'s personal secretary. And you are...? 
                return true;
            case 106:
                // $script:0831180509003660$ 
                // - I am the secretary of the owner of this house. Now, care to explain why you barged in uninvited? 
                return true;
            default:
                return true;
        }
    }
}
