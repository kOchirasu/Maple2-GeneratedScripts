using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000764: Vanilla
/// </summary>
public class _11000764 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 1;2;3;4;5;6;9001;9002;9003;100
    }

    // Select 0:
    // $script:0831180509000905$
    // - Do you need something?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (1, 0):
                // $script:0831180509000906$
                // - Do you need something? Just a moment.
                switch (selection) {
                    // $script:0831180509000907$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000908$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000909$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (2, 0):
                // $script:0831180509000910$
                // - I'll listen, but make it quick.
                switch (selection) {
                    // $script:0831180509000911$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000912$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000913$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (3, 0):
                // $script:0831180509000914$
                // - Welcome. What do you need this time?
                switch (selection) {
                    // $script:0831180509000915$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000916$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000917$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (4, 0):
                // $script:0831180509000918$
                // - Do you need something? Just a moment.
                switch (selection) {
                    // $script:0831180509000919$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000920$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000921$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509000922$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (5, 0):
                // $script:0831180509000923$
                // - I'll listen, but make it quick.
                switch (selection) {
                    // $script:0831180509000924$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000925$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000926$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509000927$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (6, 0):
                // $script:0831180509000928$
                // - Welcome. What do you need this time?
                switch (selection) {
                    // $script:0831180509000929$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000930$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000931$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509000932$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (9, 0):
                // $script:0831180509000933$
                // - My paycheck? You want to pay me now?
                //   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
                switch (selection) {
                    // $script:0831180509000934$
                    // - Let me think about it some more.
                    case 0:
                        // TODO: goto 8040,8050,8060,9040
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000935$
                    // - (Pay $MaidSalary$.)
                    case 1:
                        // TODO: goto 8000,8001,8010,8011,8901
                        // TODO: gotoFail 8900,8910
                        return -1;
                }
                return -1;
            case (8000, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000936$
                // - Yes! I love you! You're the best! Thanks for paying me on time.
                //   <font color="#909090">(She winks at you.)</font>
                return -1;
            case (8001, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000937$
                // - Omigosh, you're paying me? Thanks!
                //   <font color="#909090">(She squeezes you in a big hug.)</font>
                return -1;
            case (8010, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000938$
                // - A little late, but at least you didn't forget. I like it when people keep their promises.
                return -1;
            case (8011, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509000939$
                // - I knew it. You just couldn't let me go, could you, $OwnerName$? You had me tricked for a second there!
                return -1;
            case (8020, 0):
                // functionID=1 
                // $script:0831180509000940$
                // - Hey, it's almost payday!
                return -1;
            case (8021, 0):
                // functionID=1 
                // $script:0831180509000941$
                // - Payday is my favorite day!
                switch (selection) {
                    // $script:0831180509000942$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000943$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000944$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509000945$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (8040, 0):
                // $script:0831180509000946$
                // - You're still talking? All right. I'm still listening.
                switch (selection) {
                    // $script:0831180509000947$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000948$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000949$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509000950$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (8050, 0):
                // $script:0831180509000951$
                // - Mm? What do you want to talk about now?
                switch (selection) {
                    // $script:0831180509000952$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000953$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000954$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509000955$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (8060, 0):
                // $script:0831180509000956$
                // - I've got nothing more to say.
                switch (selection) {
                    // $script:0831180509000957$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000958$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000959$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509000960$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (8900, 0):
                // $script:0831180509000961$
                // - Why did you hire me if you can't afford me? I'm disappointed in you. I deserve better than this.
                return -1;
            case (8901, 0):
                // $script:0831180509000962$
                // - I'm touched, but you've already paid me this month, and I don't offer extra services.
                //   <font color="#909090">(She winks.)</font>
                return -1;
            case (8910, 0):
                // $script:0831180509000963$
                // - I've never been treated so awfully in my life! I'm really, really upset! I can't believe you!
                return -1;
            case (8999, 0):
                // $script:0831180509000964$
                // - Huh? What's happening? Umm... I think you should try talking to me again later.
                return -1;
            case (9001, 0):
                // $script:0831180509000965$
                // - Hey, you're $MaidPassedDay$ behind on my pay!
                switch (selection) {
                    // $script:0831180509000966$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509000967$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000968$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9002, 0):
                // $script:0831180509000969$
                // - Hmph, I don't talk to people who don't pay me on time.
                switch (selection) {
                    // $script:0831180509000970$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509000971$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000972$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9003, 0):
                // $script:0831180509000973$
                // - I'm not in the mood to talk. You know why, don't you?
                switch (selection) {
                    // $script:0831180509000974$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509000975$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000976$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9010, 0):
                // $script:0831180509000977$
                // - No pay, no service. Simple as that, hon.
                return -1;
            case (9011, 0):
                // functionID=1 
                // $script:0831180509000978$
                // - You know very well I don't want to chit chat with you! You're $MaidPassedDay$ behind on my paycheck!
                return -1;
            case (9020, 0):
                // functionID=1 
                // $script:0831180509000979$
                // - Now is not the time to be checking out my profile...
                return -1;
            case (9021, 0):
                // functionID=1 
                // $script:0831180509000980$
                // - Do you even know owe me money?
                switch (selection) {
                    // $script:0831180509000981$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509000982$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000983$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9040, 0):
                // $script:0831180509000984$
                // - Screw it. Do whatever you want.
                switch (selection) {
                    // $script:0831180509000985$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509000986$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000987$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9030, 0):
                // $script:0831180509000988$
                // - Chat? Chaaaat? How about you pay me first?
                return -1;
            case (9031, 0):
                // $script:0831180509000989$
                // - Oh, welcome home, $OwnerName$! What do you need? I'll do anything!! Like the good, unpaid slave that I am.
                //   <font color="#909090">(She gives a loud snort.)</font>
                return -1;
            case (9032, 0):
                // $script:0831180509000990$
                // - Now that I know what you really think of me, I don't want to talk to you. Go away.
                return -1;
            case (10, 0):
                // functionID=1 
                // $script:0831180509000991$
                // - What? Oh, you want me to make you a necklace?
                return -1;
            case (11, 0):
                // functionID=1 
                // $script:0831180509000992$
                // - What do you think? I'm good, aren't I?
                return -1;
            case (20, 0):
                // functionID=1 
                // $script:0831180509000993$
                // - What? You're curious about me?
                return -1;
            case (21, 0):
                // functionID=1 
                // $script:0831180509000994$
                // - Don't think that you can probe the depths of my soul. Hmph.
                switch (selection) {
                    // $script:0831180509000995$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000996$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509000997$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (22, 0):
                // functionID=1 
                // $script:0831180509000998$
                // - Don't think that you can probe the depths of my soul. Hmph.
                switch (selection) {
                    // $script:0831180509000999$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001000$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001001$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509001002$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (30, 0):
                // $script:0831180509001003$
                // - You have questions for me? Just a moment.
                switch (selection) {
                    // $script:0831180509001004$
                    // - Did anything interesting happen?
                    case 0:
                        // TODO: goto 1000,1100,1200,1300,2000,2100,9011
                        return -1;
                    // $script:0831180509001005$
                    // - (Stare at her.)
                    case 1:
                        // TODO: goto 3000,3100,4000,4100,9011
                        return -1;
                    // $script:0831180509001006$
                    // - (Tell her a joke.)
                    case 2:
                        // TODO: goto 5000,5100,6000,7000,9011
                        return -1;
                    // $script:0831180509001007$
                    // - Back.
                    case 3:
                        // TODO: goto 8040,8050,8060,40,50,60,9040
                        return -1;
                }
                return -1;
            case (31, 0):
                // $script:0831180509001008$
                // - I'm kind of busy right now, but sure. Talk away.
                switch (selection) {
                    // $script:0831180509001009$
                    // - Did anything interesting happen?
                    case 0:
                        // TODO: goto 1000,1100,1200,1300,2000,2100,9011
                        return -1;
                    // $script:0831180509001010$
                    // - (Stare at her.)
                    case 1:
                        // TODO: goto 3000,3100,4000,4100,9011
                        return -1;
                    // $script:0831180509001011$
                    // - (Tell her a joke.)
                    case 2:
                        // TODO: goto 5000,5100,6000,7000,9011
                        return -1;
                    // $script:0831180509001012$
                    // - Back.
                    case 3:
                        // TODO: goto 8040,8050,8060,40,50,60,9040
                        return -1;
                }
                return -1;
            case (32, 0):
                // $script:0831180509001013$
                // - What is it? You can be a real pest sometimes, you know.
                switch (selection) {
                    // $script:0831180509001014$
                    // - Did anything interesting happen?
                    case 0:
                        // TODO: goto 1000,1100,1200,1300,2000,2100,9011
                        return -1;
                    // $script:0831180509001015$
                    // - (Stare at her.)
                    case 1:
                        // TODO: goto 3000,3100,4000,4100,9011
                        return -1;
                    // $script:0831180509001016$
                    // - (Tell her a joke.)
                    case 2:
                        // TODO: goto 5000,5100,6000,7000,9011
                        return -1;
                    // $script:0831180509001017$
                    // - Back.
                    case 3:
                        // TODO: goto 8040,8050,8060,40,50,60,9040
                        return -1;
                }
                return -1;
            case (40, 0):
                // $script:0831180509001018$
                // - You're still talking? All right. I'm still listening.
                switch (selection) {
                    // $script:0831180509001019$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001020$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001021$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (50, 0):
                // $script:0831180509001022$
                // - Mm? What do you want to talk about now?
                switch (selection) {
                    // $script:0831180509001023$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001024$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001025$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (60, 0):
                // $script:0831180509001026$
                // - I've got nothing more to say.
                switch (selection) {
                    // $script:0831180509001027$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001028$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return -1;
                    // $script:0831180509001029$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (1000, 0):
                // $script:0831180509001030$
                // - I craved sweets something fierce today. You know those macaroons that are crispy on the outside and moist inside? That's what I love. My favorite flavor is rose.
                return 1000;
            case (1000, 1):
                // $script:0831180509001031$
                // - A famous bakery opened a branch in $map:02000001$. It's not cheap, but there's always a long line outside.
                return 1000;
            case (1000, 2):
                // $script:0831180509001032$
                // - So, while you were out, I went and— Ooops, I mean, look at this spot on the ground. I should go find the mop!
                return 1000;
            case (1000, 3):
                // $script:0831180509001033$
                // - M-macaroons? What? Never heard of them. No idea what they are!
                switch (selection) {
                    // $script:0831180509001034$
                    // - Slacking on the job, huh?
                    case 0:
                        // TODO: goto 1001,1002
                        return -1;
                    // $script:0831180509001035$
                    // - I want to try a macaroon. Got any extra?
                    case 1:
                        // TODO: goto 1011,1012
                        return -1;
                }
                return -1;
            case (1001, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001036$
                // - Who said that? Do you have proof? Pfft, without proof, you still have to pay me!
                return -1;
            case (1002, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001037$
                // - What? I finished everything you asked and more. Give me a break!
                return -1;
            case (1011, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001038$
                // - Huh? I had no idea you liked macaroons, $OwnerName$! Here, have some! I'm so glad I bought extra! Tasty, huh?
                return -1;
            case (1012, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001039$
                // - Heeheehee, I guess I got caught. Here, try one. I waited hours for it!
                return -1;
            case (1100, 0):
                // $script:0831180509001040$
                // - Not a thing. Actually, one thing happened today: you kept interrupting me from my work!
                return 1100;
            case (1100, 1):
                // $script:0831180509001041$
                // - Something major and tragic happened today. I broke a nail! Do you know how much it costs to get my nails this cute?
                return 1100;
            case (1100, 2):
                // $script:0831180509001042$
                // - Aw, are you worried? Then you should know that I keep breathing in dust when I clean. Won't this stuff make me sick or something?
                return 1100;
            case (1100, 3):
                // $script:0831180509001043$
                // - I'm not complaining! I'm just not used to this type of thing.
                switch (selection) {
                    // $script:0831180509001044$
                    // - You do tend to complain a lot...
                    case 0:
                        // TODO: goto 1111,1112
                        return -1;
                    // $script:0831180509001045$
                    // - Don't worry. I'm used to your complaining by now.
                    case 1:
                        // TODO: goto 1101,1102
                        return -1;
                }
                return -1;
            case (1101, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001046$
                // - Um, are you deaf? I just said I'm not complaining! I'm just not used to working as a maid! Ugh, it upsets me that you think so little of me!
                return -1;
            case (1102, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001047$
                // - Um, hello, I don't complain that much! You know what, I don't care what you think. You're really ticking me off!
                return -1;
            case (1111, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001048$
                // - Awww, are you complaining about my complaining? That's kind of cute, $OwnerName$! You're like a grumpy old bear!
                return -1;
            case (1112, 0):
                // $script:0831180509001049$
                // - <font color="#909090">(She's quiet for a while.)</font>
                return 1112;
            case (1112, 1):
                // $script:0831180509001050$
                // - Hmph!
                return 1112;
            case (1112, 2):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001051$
                // - <font color="#909090">(She bursts out laughing.)</font>
                //   This is why we get along so well. You're so cute when you act goofy, $OwnerName$.
                return -1;
            case (1200, 0):
                // $script:0831180509001052$
                // - <font color="#909090">(She pretends she can't hear you.)</font>
                return 1200;
            case (1200, 1):
                // $script:0831180509001053$
                // - Oh no! This is bad... Where did my o-ring band go? I can't make any jewelry without it!
                return 1200;
            case (1200, 2):
                // $script:0831180509001054$
                // - Oh, hi $OwnerName$. I'm sorry, I'm a little busy right now. I lost something.
                return 1200;
            case (1200, 3):
                // $script:0831180509001055$
                // - Can we talk later? I'm too distracted to focus right now.
                switch (selection) {
                    // $script:0831180509001056$
                    // - Oooh, what'd you lose? Is it important?
                    case 0:
                        // TODO: goto 1201,1202
                        return -1;
                    // $script:0831180509001057$
                    // - I'll help you look for it.
                    case 1:
                        // TODO: goto 1211,1212
                        return -1;
                }
                return -1;
            case (1201, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001058$
                // - $OwnerName$! I just said that I'm distracted! Will you leave me alone until I find it?
                return -1;
            case (1202, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001059$
                // - It's something that I need to craft necklaces. You know what? That's not important right now! You're bothering me. Go away!
                return -1;
            case (1211, 0):
                // $script:0831180509001060$
                // - <font color="#909090">(You get down on your hands and knees, searching the ground carefully. You find a small ring and hold it up triumphantly.)</font>
                return 1211;
            case (1211, 1):
                // $script:0831180509001061$
                // - You found it! Thank you, thank you, $OwnerName$!
                return 1211;
            case (1211, 2):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001062$
                // - This ring is used to hope and close the small rings used in necklaces. I can't make necklaces without it!
                return -1;
            case (1212, 0):
                // $script:0831180509001063$
                // - <font color="#909090">(You carefully scan the floor, diligently searching, and then...)</font>
                return 1212;
            case (1212, 1):
                // $script:0831180509001064$
                // - Thud!
                return 1212;
            case (1212, 2):
                // $script:0831180509001065$
                // - <font color="#909090">(You bump heads with $MaidName$!)</font>
                return 1212;
            case (1212, 3):
                // $script:0831180509001066$
                // - Ouch!
                //   <font color="#909090">(She rubs her head with her palm, surprised.)</font>
                return 1212;
            case (1212, 4):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001067$
                // - <font color="#909090">(Suddenly, she bursts into laughter.)</font>
                //   Oh, $OwnerName$! You don't have to search for it that hard! Thank you for helping me. I know it'll turn up soon!
                return -1;
            case (1300, 0):
                // $script:0831180509001068$
                // - I was strolling through $map:02000064$ today and ran into $npc:11000711[gender:1]$. Do you know what she told me? She said I had bags under my eyes! That I looked "tired"!
                return 1300;
            case (1300, 1):
                // $script:0831180509001069$
                // - She looks even more ragged than I do. No matter what she does, she— ah, never mind.
                switch (selection) {
                    // $script:0831180509001070$
                    // - What were you going to say?
                    case 0:
                        // TODO: goto 1301,1302
                        return -1;
                    // $script:0831180509001071$
                    // - You're always so full of life and energy. Not tired at all.
                    case 1:
                        // TODO: goto 1311,1312
                        return -1;
                }
                return -1;
            case (1301, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001072$
                // - Forget it. It was unkind. I never thought you were into mean gossip, $OwnerName$. I don't think that's a good look on you.
                return -1;
            case (1302, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001073$
                // - Why do you care? Is it because it's about $npc:11000711[gender:1]$? Are you a fan of hers? Hmph!
                return -1;
            case (1311, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001074$
                // - Aw, thanks! I work hard to be that way, so thank you for noticing!
                return -1;
            case (1312, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001075$
                // - Awww, $OwnerName$. Are you trying to sweet talk me? That's totally unlike you!
                return -1;
            case (2000, 0):
                // $script:0831180509001076$
                // - I'm very busy at the moment. Please do not disturb me.
                return 2000;
            case (2000, 1):
                // $script:0831180509001077$
                // - ...
                return 2000;
            case (2000, 2):
                // $script:0831180509001078$
                // - ...Are you mad? I'm sorry, but I really don't have time for you right now.
                return -1;
            case (2100, 0):
                // $script:0831180509001079$
                // - I wish something amazing would happen. The days get so boring.
                return 2100;
            case (2100, 1):
                // $script:0831180509001080$
                // - Listening to $npc:11000406[gender:0]$ singing usually helps, but not today. I'm so bored.
                return -1;
            case (3000, 0):
                // $script:0831180509001081$
                // - Mm... Mm? Why are you staring at me? Please... stop...
                return 3000;
            case (3000, 1):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001082$
                // - <font color="#909090">($MaidName$'s cheeks are turning red.)</font>
                //   Oh, stop. You're making me blush!
                return -1;
            case (3100, 0):
                // $script:0831180509001083$
                // - Stop it, $OwnerName$! You're doing it again? Are you really that helpless to resist my good looks?
                return 3100;
            case (3100, 1):
                // functionID=1 openTalkReward=True 
                // $script:0831180509001084$
                // - Hey, $OwnerName$, did you know your eyes sparkle when you stare at me?
                return -1;
            case (4000, 0):
                // $script:0831180509001085$
                // - Stop staring. Your puppy eyes lost their charm long ago. Come now, no need to pout.
                return -1;
            case (4100, 0):
                // $script:0831180509001086$
                // - Fine. Let's see who can go the longest without blinking. Ready, set, go!
                return 4100;
            case (4100, 1):
                // $script:0831180509001087$
                // - Forget it. I'm not in the mood, so stop staring at me!
                return -1;
            case (5000, 0):
                // $script:0831180509001088$
                // - Ugh, why would you tell such an old joke? Nobody has laughed at that joke for years!
                return 5000;
            case (5000, 1):
                // $script:0831180509001089$
                // - This explains why you have so few friends, $OwnerName$. Tsk.
                return 5000;
            case (5000, 2):
                // $script:0831180509001090$
                // - I'll laugh to be nice. Haha. There.
                return -1;
            case (5100, 0):
                // $script:0831180509001091$
                // - Please stop with the lame jokes. I'll tell you some that are actually funny.
                return 5100;
            case (5100, 1):
                // $script:0831180509001092$
                // - First up: How do you get a tissue to dance?
                return 5100;
            case (5100, 2):
                // $script:0831180509001093$
                // - You put a little boogie in it! Hahaha, isn't that hilarious?
                return 5100;
            case (5100, 3):
                // $script:0831180509001094$
                // - Next up: What did the zero say to the eight?
                return 5100;
            case (5100, 4):
                // $script:0831180509001095$
                // - Stumped? Then I'll tell you: Nice belt! Hahaha, get it?
                return 5100;
            case (5100, 5):
                // $script:0831180509001096$
                // - Here's the last one, and it's a stumper. Don't be mad if you can't figure it out. Here goes: Why did the tomato blush?
                return 5100;
            case (5100, 6):
                // $script:0831180509001097$
                // - You don't know, do you? Hehehe, the answer is: Because he saw the salad dressing!
                return 5100;
            case (5100, 7):
                // $script:0831180509001098$
                // - Now those are some funny jokes. Don't tell me any more jokes unless they're funnier that those ones!
                return -1;
            case (6000, 0):
                // $script:0831180509001099$
                // - <font color="#909090">($MaidName$ looks at you mournfully.)</font>
                return 6000;
            case (6000, 1):
                // $script:0831180509001100$
                // - It's not you, $OwnerName$. I'm just really not in the mood for jokes right now.
                return 6000;
            case (6000, 2):
                // $script:0831180509001101$
                // - I was thinking of my sister. She's the one who taught me how to make jewelry.
                return 6000;
            case (6000, 3):
                // $script:0831180509001102$
                // - But I haven't heard from her in a long time. I don't even know where she is. Whenever I think of her, I get a pang in my heart so sharp I want to cry.
                return 6000;
            case (6000, 4):
                // $script:0831180509001103$
                // - I'm sorry. I don't know why I'm telling you this. Forget I said anything, okay?
                return 6000;
            case (6000, 5):
                // $script:0831180509001104$
                // - <font color="#909090">(You see $MaidName$'s eyes twinkle.)</font>
                return -1;
            case (7000, 0):
                // $script:0831180509001105$
                // - Hah! Hah! Hah! That's the funniest joke I've ever heard in my life! You're so hilarious, $OwnerName$!
                return 7000;
            case (7000, 1):
                // $script:0831180509001106$
                // - ...Not. Get a clue, $OwnerName$!
                return 7000;
            case (7000, 2):
                // $script:0831180509001107$
                // - How many times do I have to tell you? Stop telling lame jokes or you'll lose the few friends you have left!
                return 7000;
            case (7000, 3):
                // $script:0831180509001108$
                // - If you're reading lame joke books, why don't you go out and do something productive with your life? Like buying me treats or collecting necklace materials for me? Or helping the needy or something?
                return 7000;
            case (7000, 4):
                // $script:0831180509001109$
                // - Please just— Yikes. Um, I just realized I'm nagging at you like you're a friend. I'm sorry if I crossed a line, $OwnerName$. I just want what's best for you. You know that, right?
                return -1;
            case (100, 0):
                // $script:0831180509001110$
                // - Who are you? You can't just barge in here! Did you come to see me? Still, that doesn't make this okay!
                switch (selection) {
                    // $script:0831180509001111$
                    // - I'm here to see your master.
                    case 0:
                        // TODO: goto 101,102
                        return -1;
                    // $script:0831180509001112$
                    // - Oh, I don't need anything.
                    case 1:
                        // TODO: goto 103,104
                        return -1;
                    // $script:0831180509001113$
                    // - I came to see you.
                    case 2:
                        // TODO: goto 105,106
                        return -1;
                }
                return -1;
            case (101, 0):
                // $script:0831180509001114$
                // - Oh, you're a friend of $OwnerName$? Well, make yourself at home, and try not to bother me.
                return -1;
            case (102, 0):
                // $script:0831180509001115$
                // - Are you for real? And here I thought $OwnerName$ had no friends! This is amazing!!
                return -1;
            case (103, 0):
                // $script:0831180509001116$
                // - Well, if you have no business here, you'd better leave. I just mopped, and I don't need the floor getting all muddy again.
                return -1;
            case (104, 0):
                // $script:0831180509001117$
                // - Suuuuure. Just be honest and say you're here to talk to me. It happens all the time. I'm used to it, really.
                return -1;
            case (105, 0):
                // $script:0831180509001118$
                // - I don't think we've met. Are you a member of my fan club? I know you want to see me, but you shouldn't bother me at work, you know?
                return -1;
            case (106, 0):
                // $script:0831180509001119$
                // - I'm too popular for my own good. Not a day goes by without someone wanting my attention. So what do you want? My autograph?
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (1, 0) => NpcTalkButton.SelectableDistractor,
            (2, 0) => NpcTalkButton.SelectableDistractor,
            (3, 0) => NpcTalkButton.SelectableDistractor,
            (4, 0) => NpcTalkButton.SelectableDistractor,
            (5, 0) => NpcTalkButton.SelectableDistractor,
            (6, 0) => NpcTalkButton.SelectableDistractor,
            (9, 0) => NpcTalkButton.SelectableDistractor,
            (8000, 0) => NpcTalkButton.Close,
            (8001, 0) => NpcTalkButton.Close,
            (8010, 0) => NpcTalkButton.Close,
            (8011, 0) => NpcTalkButton.Close,
            (8020, 0) => NpcTalkButton.Close,
            (8021, 0) => NpcTalkButton.SelectableDistractor,
            (8040, 0) => NpcTalkButton.SelectableDistractor,
            (8050, 0) => NpcTalkButton.SelectableDistractor,
            (8060, 0) => NpcTalkButton.SelectableDistractor,
            (8900, 0) => NpcTalkButton.Close,
            (8901, 0) => NpcTalkButton.Close,
            (8910, 0) => NpcTalkButton.Close,
            (8999, 0) => NpcTalkButton.Close,
            (9001, 0) => NpcTalkButton.SelectableDistractor,
            (9002, 0) => NpcTalkButton.SelectableDistractor,
            (9003, 0) => NpcTalkButton.SelectableDistractor,
            (9010, 0) => NpcTalkButton.Close,
            (9011, 0) => NpcTalkButton.Close,
            (9020, 0) => NpcTalkButton.Close,
            (9021, 0) => NpcTalkButton.SelectableDistractor,
            (9040, 0) => NpcTalkButton.SelectableDistractor,
            (9030, 0) => NpcTalkButton.Close,
            (9031, 0) => NpcTalkButton.Close,
            (9032, 0) => NpcTalkButton.Close,
            (10, 0) => NpcTalkButton.Close,
            (11, 0) => NpcTalkButton.Close,
            (20, 0) => NpcTalkButton.Close,
            (21, 0) => NpcTalkButton.SelectableDistractor,
            (22, 0) => NpcTalkButton.SelectableDistractor,
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (50, 0) => NpcTalkButton.SelectableDistractor,
            (60, 0) => NpcTalkButton.SelectableDistractor,
            (1000, 0) => NpcTalkButton.Next,
            (1000, 1) => NpcTalkButton.Next,
            (1000, 2) => NpcTalkButton.Next,
            (1000, 3) => NpcTalkButton.SelectableDistractor,
            (1001, 0) => NpcTalkButton.Close,
            (1002, 0) => NpcTalkButton.Close,
            (1011, 0) => NpcTalkButton.Close,
            (1012, 0) => NpcTalkButton.Close,
            (1100, 0) => NpcTalkButton.Next,
            (1100, 1) => NpcTalkButton.Next,
            (1100, 2) => NpcTalkButton.Next,
            (1100, 3) => NpcTalkButton.SelectableDistractor,
            (1101, 0) => NpcTalkButton.Close,
            (1102, 0) => NpcTalkButton.Close,
            (1111, 0) => NpcTalkButton.Close,
            (1112, 0) => NpcTalkButton.Next,
            (1112, 1) => NpcTalkButton.Next,
            (1112, 2) => NpcTalkButton.Close,
            (1200, 0) => NpcTalkButton.Next,
            (1200, 1) => NpcTalkButton.Next,
            (1200, 2) => NpcTalkButton.Next,
            (1200, 3) => NpcTalkButton.SelectableDistractor,
            (1201, 0) => NpcTalkButton.Close,
            (1202, 0) => NpcTalkButton.Close,
            (1211, 0) => NpcTalkButton.Next,
            (1211, 1) => NpcTalkButton.Next,
            (1211, 2) => NpcTalkButton.Close,
            (1212, 0) => NpcTalkButton.Next,
            (1212, 1) => NpcTalkButton.Next,
            (1212, 2) => NpcTalkButton.Next,
            (1212, 3) => NpcTalkButton.Next,
            (1212, 4) => NpcTalkButton.Close,
            (1300, 0) => NpcTalkButton.Next,
            (1300, 1) => NpcTalkButton.SelectableDistractor,
            (1301, 0) => NpcTalkButton.Close,
            (1302, 0) => NpcTalkButton.Close,
            (1311, 0) => NpcTalkButton.Close,
            (1312, 0) => NpcTalkButton.Close,
            (2000, 0) => NpcTalkButton.Next,
            (2000, 1) => NpcTalkButton.Next,
            (2000, 2) => NpcTalkButton.Close,
            (2100, 0) => NpcTalkButton.Next,
            (2100, 1) => NpcTalkButton.Close,
            (3000, 0) => NpcTalkButton.Next,
            (3000, 1) => NpcTalkButton.Close,
            (3100, 0) => NpcTalkButton.Next,
            (3100, 1) => NpcTalkButton.Close,
            (4000, 0) => NpcTalkButton.Close,
            (4100, 0) => NpcTalkButton.Next,
            (4100, 1) => NpcTalkButton.Close,
            (5000, 0) => NpcTalkButton.Next,
            (5000, 1) => NpcTalkButton.Next,
            (5000, 2) => NpcTalkButton.Close,
            (5100, 0) => NpcTalkButton.Next,
            (5100, 1) => NpcTalkButton.Next,
            (5100, 2) => NpcTalkButton.Next,
            (5100, 3) => NpcTalkButton.Next,
            (5100, 4) => NpcTalkButton.Next,
            (5100, 5) => NpcTalkButton.Next,
            (5100, 6) => NpcTalkButton.Next,
            (5100, 7) => NpcTalkButton.Close,
            (6000, 0) => NpcTalkButton.Next,
            (6000, 1) => NpcTalkButton.Next,
            (6000, 2) => NpcTalkButton.Next,
            (6000, 3) => NpcTalkButton.Next,
            (6000, 4) => NpcTalkButton.Next,
            (6000, 5) => NpcTalkButton.Close,
            (7000, 0) => NpcTalkButton.Next,
            (7000, 1) => NpcTalkButton.Next,
            (7000, 2) => NpcTalkButton.Next,
            (7000, 3) => NpcTalkButton.Next,
            (7000, 4) => NpcTalkButton.Close,
            (100, 0) => NpcTalkButton.SelectableDistractor,
            (101, 0) => NpcTalkButton.Close,
            (102, 0) => NpcTalkButton.Close,
            (103, 0) => NpcTalkButton.Close,
            (104, 0) => NpcTalkButton.Close,
            (105, 0) => NpcTalkButton.Close,
            (106, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
