using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000772: Erryday M-0
/// </summary>
public class _11000772 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 1;2;3;4;5;6;9001;9002;9003;100
    }

    // Select 0:
    // $script:0831180509002323$
    // - I'm ready for your order, $OwnerName$.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (1, 0):
                // $script:0831180509002324$
                // - You called, $OwnerName$?
                switch (selection) {
                    // $script:0831180509002325$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509002326$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509002327$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (2, 0):
                // $script:0831180509002328$
                // - Scanning target... Beep! $OwnerName$ has been recognized.
                switch (selection) {
                    // $script:0831180509002329$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509002330$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509002331$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (3, 0):
                // $script:0831180509002332$
                // - Have a productive day, $OwnerName$.
                switch (selection) {
                    // $script:0831180509002333$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509002334$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509002335$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (4, 0):
                // $script:0831180509002336$
                // - You called, $OwnerName$?
                switch (selection) {
                    // $script:0831180509002337$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509002338$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509002339$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509002340$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (5, 0):
                // $script:0831180509002341$
                // - Scanning target... Beep! $OwnerName$ has been recognized.
                switch (selection) {
                    // $script:0831180509002342$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509002343$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509002344$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509002345$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (6, 0):
                // $script:0831180509002346$
                // - Have a productive day, $OwnerName$.
                switch (selection) {
                    // $script:0831180509002347$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509002348$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509002349$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509002350$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (9, 0):
                // $script:0831180509002351$
                // - Do you want to give me my paycheck?
                //   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
                switch (selection) {
                    // $script:0831180509002352$
                    // - Let me think about it some more.
                    case 0:
                        // TODO: goto 8040,8050,8060,9040
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509002353$
                    // - (Pay $MaidSalary$.)
                    case 1:
                        // TODO: goto 8000,8001,8010,8011,8901
                        // TODO: gotoFail 8900,8910
                        return 8900,8910;
                }
                return -1;
            case (8000, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002354$
                // - Ding, ding! You have renewed your contract! Thank you, $OwnerName$.
                return -1;
            case (8001, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002355$
                // - Ding, ding! You have renewed your contract! I will serve you until I am no longer of use, $OwnerName$!
                return -1;
            case (8010, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002356$
                // - Ding! Paycheck received! Canceling service disconnection... Vrroomm...
                return -1;
            case (8011, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002357$
                // - Ding! Paycheck received! Canceling maximum power saver mode... Checking system status... Beep! Beep! Beep!
                return -1;
            case (8020, 0):
                // functionID=1 
                // $script:0831180509002358$
                // - Beep! Alert, $OwnerName$: our contract expires in a few days.
                return -1;
            case (8021, 0):
                // functionID=1 
                // $script:0831180509002359$
                // - When our contract expires, my main system will automatically shut down.
                switch (selection) {
                    // $script:0831180509002360$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509002361$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509002362$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509002363$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (8040, 0):
                // $script:0831180509002364$
                // - As you wish, $OwnerName$.
                switch (selection) {
                    // $script:0831180509002365$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509002366$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509002367$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509002368$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (8050, 0):
                // $script:0831180509002369$
                // - Switching to standby mode...
                switch (selection) {
                    // $script:0831180509002370$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509002371$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509002372$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509002373$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (8060, 0):
                // $script:0831180509002374$
                // - Current battery level: 99%.
                switch (selection) {
                    // $script:0831180509002375$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509002376$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509002377$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509002378$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (8900, 0):
                // $script:0831180509002379$
                // - Beep! Error: you do not have sufficient funds, $OwnerName$.
                return -1;
            case (8901, 0):
                // $script:0831180509002380$
                // - Request denied. This month's paycheck has already been received. Is your memory malfunctioning?
                return -1;
            case (8910, 0):
                // $script:0831180509002381$
                // - Beep! Error: you do not have sufficient funds, $OwnerName$.
                return -1;
            case (8999, 0):
                // $script:0831180509002382$
                // - Beep! A critical error has occurred. Rebooting system...
                return -1;
            case (9001, 0):
                // $script:0831180509002383$
                // - Beeeeeep! Unable to move. 
                switch (selection) {
                    // $script:0831180509002384$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509002385$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509002386$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9002, 0):
                // $script:0831180509002387$
                // - Beeeeep! In maximum power saver mode.
                switch (selection) {
                    // $script:0831180509002388$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509002389$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509002390$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9003, 0):
                // $script:0831180509002391$
                // - Beeeeeep... $OwnerName$...  
                switch (selection) {
                    // $script:0831180509002392$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509002393$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509002394$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9010, 0):
                // $script:0831180509002395$
                // - Contract expired. Switching to hibernation mode.
                return -1;
            case (9011, 0):
                // functionID=1 
                // $script:0831180509002396$
                // - Contract expired. Switching to hibernation mode.
                return -1;
            case (9020, 0):
                // functionID=1 
                // $script:0831180509002397$
                // - $MaidPassedDay$ have passed since our contract expired.
                return -1;
            case (9021, 0):
                // functionID=1 
                // $script:0831180509002398$
                // - I don't know how much longer I can stay online.
                switch (selection) {
                    // $script:0831180509002399$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509002400$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509002401$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9040, 0):
                // $script:0831180509002402$
                // - Beeeep. My battery needs to be charged, and my joints need to be oiled.
                switch (selection) {
                    // $script:0831180509002403$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 0:
                        return 9;
                    // $script:0831180509002404$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509002405$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (9030, 0):
                // $script:0831180509002406$
                // - I wish to check your status, $OwnerName$, but I don't have enough battery power to run the bio scanner. How are you feeling?
                return -1;
            case (9031, 0):
                // $script:0831180509002407$
                // - $OwnerName$, are you there? I'm afraid my sensors are losing their sensitivity. Am I... rusting?
                return -1;
            case (9032, 0):
                // $script:0831180509002408$
                // - I wish I could operate without battery power, like you do. Is there a way for me to turn on a human mode?
                return -1;
            case (10, 0):
                // functionID=1 
                // $script:0831180509002409$
                // - Switching to cooking mode. What would you like?
                return -1;
            case (11, 0):
                // functionID=1 
                // $script:0831180509002410$
                // - Canceling cooking mode...
                return -1;
            case (20, 0):
                // functionID=1 
                // $script:0831180509002411$
                // - $OwnerName$... who am I?
                return -1;
            case (21, 0):
                // functionID=1 
                // $script:0831180509002412$
                // - I want to be like you, $OwnerName$.
                switch (selection) {
                    // $script:0831180509002413$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509002414$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509002415$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (22, 0):
                // functionID=1 
                // $script:0831180509002416$
                // - I want to be like you, $OwnerName$.
                switch (selection) {
                    // $script:0831180509002417$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509002418$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509002419$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                    // $script:0831180509002420$
                    // - Don't I owe you money? (Pay salary of $MaidSalary$.)
                    case 3:
                        return 9;
                }
                return -1;
            case (30, 0):
                // $script:0831180509002421$
                // - Switching to conversation mode.
                switch (selection) {
                    // $script:0831180509002422$
                    // - Did anything interesting happen today? 
                    case 0:
                        // TODO: goto 1000,1100,1200,1300,1400,1500,1600,2000,2100,2200,9011
                        return -1;
                    // $script:0831180509002423$
                    // - (Praise your servant.)
                    case 1:
                        // TODO: goto 3000,3100,4000,4100,4200,4300,9011
                        return -1;
                    // $script:0831180509002424$
                    // - (Ask your servant a personal question.)
                    case 2:
                        // TODO: goto 5000,5100,6000,7000,9011
                        return -1;
                    // $script:0831180509002425$
                    // - Back.
                    case 3:
                        // TODO: goto 8040,8050,8060,40,50,60,9040
                        return -1;
                }
                return -1;
            case (31, 0):
                // $script:0831180509002426$
                // - The following conversation will be recorded for training purposes.
                switch (selection) {
                    // $script:0831180509002427$
                    // - Did anything interesting happen today? 
                    case 0:
                        // TODO: goto 1000,1100,1200,1300,1400,1500,1600,2000,2100,2200,9011
                        return -1;
                    // $script:0831180509002428$
                    // - (Praise your servant.)
                    case 1:
                        // TODO: goto 3000,3100,4000,4100,4200,4300,9011
                        return -1;
                    // $script:0831180509002429$
                    // - (Ask your servant a personal question.)
                    case 2:
                        // TODO: goto 5000,5100,6000,7000,9011
                        return -1;
                    // $script:0831180509002430$
                    // - Back.
                    case 3:
                        // TODO: goto 8040,8050,8060,40,50,60,9040
                        return -1;
                }
                return -1;
            case (32, 0):
                // $script:0831180509002431$
                // - I always save my conversations with you, $OwnerName$.
                switch (selection) {
                    // $script:0831180509002432$
                    // - Did anything interesting happen today? 
                    case 0:
                        // TODO: goto 1000,1100,1200,1300,1400,1500,1600,2000,2100,2200,9011
                        return -1;
                    // $script:0831180509002433$
                    // - (Praise your servant.)
                    case 1:
                        // TODO: goto 3000,3100,4000,4100,4200,4300,9011
                        return -1;
                    // $script:0831180509002434$
                    // - (Ask your servant a personal question.)
                    case 2:
                        // TODO: goto 5000,5100,6000,7000,9011
                        return -1;
                    // $script:0831180509002435$
                    // - Back.
                    case 3:
                        // TODO: goto 8040,8050,8060,40,50,60,9040
                        return -1;
                }
                return -1;
            case (40, 0):
                // $script:0831180509002436$
                // - As you wish, $OwnerName$.
                switch (selection) {
                    // $script:0831180509002437$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509002438$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509002439$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (50, 0):
                // $script:0831180509002440$
                // - Switching to standby mode...
                switch (selection) {
                    // $script:0831180509002441$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509002442$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509002443$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (60, 0):
                // $script:0831180509002444$
                // - Current battery level: 99%.
                switch (selection) {
                    // $script:0831180509002445$
                    // - I need you to craft something.
                    case 0:
                        // TODO: goto 10,9010
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509002446$
                    // - I want to check your profile.
                    case 1:
                        // TODO: goto 20,8020,9020
                        // TODO: gotoFail 8999
                        return 8999;
                    // $script:0831180509002447$
                    // - Let's chat!
                    case 2:
                        // TODO: goto 30,31,32,9030,9031,9032
                        return -1;
                }
                return -1;
            case (1000, 0):
                // $script:0831180509002448$
                // - I can function as long as my battery has power, but a human will perish without a constant supply of sustenance. 
                return 1000;
            case (1000, 1):
                // $script:0831180509002449$
                // - Data has shown me that what looks good should also taste good. Please try this and let me know how you like it. I will analysis the response and factor it into my next cooking operation.
                switch (selection) {
                    // $script:0831180509002450$
                    // - It's pretty bland.
                    case 0:
                        // TODO: goto 1001,1002
                        return -1;
                    // $script:0831180509002451$
                    // - It's delicious!
                    case 1:
                        // TODO: goto 1011,1012
                        return -1;
                }
                return -1;
            case (1001, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002452$
                // - I followed the recipe in my database. The recipe itself must be the problem. Deleting it now...
                return -1;
            case (1002, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002453$
                // - $OwnerName$, I am incapable of tasting food. Please install a taste sensor if you'd like me to solve this problem.
                return -1;
            case (1011, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002454$
                // - Noted. I am glad you like it, <font color="#ffd200">$OwnerName$</font>.
                return -1;
            case (1012, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002455$
                // - Was that a compliment? ...Beep, beep, beep. The system has overheated. Turning on fans... Vroom...
                return -1;
            case (1100, 0):
                // $script:0831180509002456$
                // - I have made you a snack. Eating snacks in between meals supplements your nutritional intake and enhances mood.
                return 1100;
            case (1100, 1):
                // $script:0831180509002457$
                // - On the other hand, snacking can lead to weight problems. I've prepared a healthy, low-calorie snack.
                switch (selection) {
                    // $script:0831180509002458$
                    // - Thank you.
                    case 0:
                        // TODO: goto 1111,1112
                        return -1;
                    // $script:0831180509002459$
                    // - I'm on a diet.
                    case 1:
                        // TODO: goto 1101,1102
                        return -1;
                }
                return -1;
            case (1101, 0):
                // $script:0831180509002460$
                // - Unable to locate that word in the database. Searching for synonyms... Beep! Beep! Beep! 
                return 1101;
            case (1101, 1):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002461$
                // - One entry found: dynamite. $OwnerName$, sitting on dynamite is hazardous to your health.
                return -1;
            case (1102, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002462$
                // - $OwnerName$, based on your activity level, you need an average of 5,630 kcal per day. Be sure to meet your calorie needs for optimal health.
                return -1;
            case (1111, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002463$
                // - According to my database, people exchange gifts as a way of thanking each other.
                //   <font color="#ffd200">$OwnerName$</font>, you can just give me oil.
                return -1;
            case (1112, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002464$
                // - Did you just hand me some oil, $OwnerName$? Why is my vision blurry, all of a sudden? Is that moisture in my visual sensors?
                return -1;
            case (1200, 0):
                // $script:0831180509002465$
                // - $OwnerName$, is the objective of your adventuring to become strong? I've formulated a potion to help you become strong.
                return 1200;
            case (1200, 1):
                // $script:0831180509002466$
                // - I hope it'll be useful to you.
                switch (selection) {
                    // $script:0831180509002467$
                    // - What's up with the smell?
                    case 0:
                        // TODO: goto 1211,1212
                        return -1;
                    // $script:0831180509002468$
                    // - What's up with the color?
                    case 1:
                        // TODO: goto 1201,1202
                        return -1;
                }
                return -1;
            case (1201, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002469$
                // - I apologize if the color does not appeal to you, $OwnerName$. I am colorblind.
                return -1;
            case (1202, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002470$
                // - Does it matter what color it is, as long as it's effective? I am unable to distinguish between colors, but that never has stopped me from functioning properly.
                return -1;
            case (1211, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002471$
                // - Do you like it? To help it go down smoothly, I've added a few drops of sesame seed oil, my favorite lubricant.
                return -1;
            case (1212, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002472$
                // - It may not smell enticing, but I assure you, that does not affect the potion's efficacy.
                return -1;
            case (1300, 0):
                // $script:0831180509002473$
                // - I read that cooking is about love. I pulled up an image of you the entire time I cooked this, $OwnerName$.
                return 1300;
            case (1300, 1):
                // $script:0831180509002474$
                // - Please let me know how you enjoy it. I will factor that into my future cooking operations.
                switch (selection) {
                    // $script:0831180509002475$
                    // - It tastes strange.
                    case 0:
                        // TODO: goto 1301,1302
                        return -1;
                    // $script:0831180509002476$
                    // - It's delicious!
                    case 1:
                        // TODO: goto 1311,1312
                        return -1;
                }
                return -1;
            case (1301, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002477$
                // - How so? I need more data. Please elaborate.
                return -1;
            case (1302, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002478$
                // - Beep! Dust detected. I must go clean, $OwnerName$. Excuse me.
                return -1;
            case (1311, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002479$
                // - Saving the recipe and your response in my database. Your eyes are really shining, $OwnerName$.
                return -1;
            case (1312, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002480$
                // - Good. I'm curious about tastes. Will you get me a taste sensor, $OwnerName$?
                return -1;
            case (1400, 0):
                // $script:0831180509002481$
                // - The suctioning power of the vacuum in my right arm dropped to 27% today. I dismantled it and found this inside.
                return 1400;
            case (1400, 1):
                // $script:0831180509002482$
                // - It must have been sucked into the machine while I was cleaning. $OwnerName$, is it yours?
                switch (selection) {
                    // $script:0831180509002483$
                    // - You should be more careful when you vacuum!
                    case 0:
                        // TODO: goto 1401,1402
                        return -1;
                    // $script:0831180509002484$
                    // - Yup, it's mine.
                    case 1:
                        // TODO: goto 1411,1412
                        return -1;
                }
                return -1;
            case (1401, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002485$
                // - $OwnerName$, your blood pressure is rising too quickly. Have you tried aromatherapy? I highly recommend sesame seed oil.
                return -1;
            case (1402, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002486$
                // - Beep! Beep! Beep! I apologize, $OwnerName$. There was an error with my auditory sensor, so I missed what you said.
                return -1;
            case (1411, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002487$
                // - Leaving items on the floor is not a good habit, $OwnerName$. Also, please think of my vacuum.
                return -1;
            case (1412, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002488$
                // - Glad to be of help, $OwnerName$.
                return -1;
            case (1500, 0):
                // $script:0831180509002489$
                // - $OwnerName$, I received a package while you were away.
                return 1500;
            case (1500, 1):
                // $script:0831180509002490$
                // - Is this for you?
                switch (selection) {
                    // $script:0831180509002491$
                    // - Yup, it's mine.
                    case 0:
                        // TODO: goto 1511,1512
                        return -1;
                    // $script:0831180509002492$
                    // - Nope.
                    case 1:
                        // TODO: goto 1501,1502
                        return -1;
                }
                return -1;
            case (1501, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002493$
                // - Very well. Beep, beep, beep. Deleting record of receiving the package... Beep!
                return -1;
            case (1502, 0):
                // $script:0831180509002494$
                // - I don't understand. My scan revealed your name printed on the package. Searching database...
                return 1502;
            case (1502, 1):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002495$
                // - Beep beep beep! Unable to local scanned label image. Beep.
                return -1;
            case (1511, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002496$
                // - Understood. I was unable to locate a record receiving the package. I do recall someone entered the house, but all other records have been erased. 
                return -1;
            case (1512, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002497$
                // - You purchased something? It is difficult to clean when there are too many items in the house. Might I suggest limiting your purchases to oil? 
                return -1;
            case (2000, 0):
                // $script:0831180509002498$
                // - While you were away, I cleaned the bathroom, and I couldn't get rid of the grime in certain areas.
                return 2000;
            case (2000, 1):
                // $script:0831180509002499$
                // - According to my database, I need a special cleaner to get rid of it, but we don't have any in the house.
                return 2000;
            case (2000, 2):
                // $script:0831180509002500$
                // - Dr. Kartronic once said that grime cannot be removed with water for the same reason oil and water cannot be mixed. So I used the sesame seed oil we had in the kitchen to clean every nook and cranny of the bathroom.
                return -1;
            case (2100, 0):
                // $script:0831180509002501$
                // - $OwnerName$, not long after you left the house, I detected a small creature with a body temperature of 102 degrees inside the house.
                return 2100;
            case (2100, 1):
                // $script:0831180509002502$
                // - I approached it. It ran. After two minutes and forty-eight seconds, I caught it. It promptly shook free and ran out of the house. It took me thirty-six minutes and twenty-three seconds to remove all the hair it left behind.
                return 2100;
            case (2100, 2):
                // $script:0831180509002503$
                // - This incident has taught me that I must keep the door and windows closed, so no creatures other than you can sneak into the house.
                return -1;
            case (2200, 0):
                // $script:0831180509002504$
                // - Scanning target... Beep. No data found. 
                return 2200;
            case (2200, 1):
                // $script:0831180509002505$
                // - Beep. Possible intruder. Activating attack mode... This place is Dr. Kartronic's... Whirr... Whirrrrr... 
                return 2200;
            case (2200, 2):
                // $script:0831180509002506$
                // - Who... you... Whirrrrr... Whirr... $OwnerName$... I'm... Beep beep beep!
                return 2200;
            case (2200, 3):
                // $script:0831180509002507$
                // - A critical error has been detected. Restoring system... Beep, beep, beep.
                return 2200;
            case (2200, 4):
                // $script:0831180509002508$
                // - Beep. Nice to meet you, $OwnerName$. Pulse: 124. Blood pressure: 155, still rising. $OwnerName$,
                //   I recommend you see a doctor at once. 
                return -1;
            case (2300, 0):
                // $script:0831180509002509$
                // - Scanning target...
                return 2300;
            case (2300, 1):
                // $script:0831180509002510$
                // - Checking $OwnerName$ status... Temperature: 97.7. Pulse: 80. Blood pressure: 120.
                return 2300;
            case (2300, 2):
                // $script:0831180509002511$
                // - Status: normal. I am glad you're all right, $OwnerName$.
                return -1;
            case (2400, 0):
                // $script:0831180509002512$
                // - Scanning target...
                return 2400;
            case (2400, 1):
                // $script:0831180509002513$
                // - Beep. No data found. Beep, beep, beep. Possible intruder. Activating attack mode...
                return 2400;
            case (2400, 2):
                // $script:0831180509002514$
                // - It was a joke. I like it when you laugh, $OwnerName$.
                return -1;
            case (3000, 0):
                // $script:0831180509002515$
                // - I wish to serve a purpose in your life, $OwnerName$. If I am not productive, I have no reason to exist.
                return 3000;
            case (3000, 1):
                // $script:0831180509002516$
                // - Here is a fact: 99.4% of machines that are no longer productive are discarded. It is natural. I fully understand that one day you will abandon me.
                return 3000;
            case (3000, 2):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002517$
                // - Why do you look so upset, $OwnerName$? Is your system experiencing an error? 
                return -1;
            case (3100, 0):
                // $script:0831180509002518$
                // - When you are not present, $OwnerName$, it feels like some of my screws are loose. But when I check them, they are all secure.
                return 3100;
            case (3100, 1):
                // functionID=1 openTalkReward=True 
                // $script:0831180509002519$
                // - Perhaps I am broken somewhere. Do you know any good technicians?
                return -1;
            case (4000, 0):
                // $script:0831180509002520$
                // - You sometimes tell me to rest, but I do not understand. I am a machine. I can function as long as I have a power source. You just need to remember to charge my battery.
                return 4000;
            case (4000, 1):
                // $script:0831180509002521$
                // - It helps tremendously to reapply my lubricant once every two weeks. You haven't done it in a while, so please go get some sesame oil from the kitchen.
                return -1;
            case (4100, 0):
                // $script:0831180509002522$
                // - $OwnerName$, are you an adventurer? According to my database, adventurers are more intelligent, capable, and courageous than ordinary people.
                return 4100;
            case (4100, 1):
                // $script:0831180509002523$
                // - $OwnerName$, if anything is bothering you, please let me know. I will do my best to help.
                return -1;
            case (5000, 0):
                // $script:0831180509002524$
                // - I'm Maple World's first domestic robot. My creator, Dr. Kartronic, is like a parent to me. Dr. Kartronic is... Whirrrr... 
                return 5000;
            case (5000, 1):
                // $script:0831180509002525$
                // - Beep, beep, beep! Unable to locate information about Dr. Kartronic. Records show that it has been deleted.
                return 5000;
            case (5000, 2):
                // $script:0831180509002526$
                // - It also shows that $npc:11000335[gender:0]$ made a backup of my system data... In $map:02000163$... Whirrrr... Whirr... 
                return 5000;
            case (5000, 3):
                // $script:0831180509002527$
                // - The data related to $map:02000163$ has been damaged and is unreadable. Cause: unknown. Beep. 
                return -1;
            case (5100, 0):
                // $script:0831180509002528$
                // - I need your attention, $OwnerName$. My system saves all my activities in my hard drive.
                return 5100;
            case (5100, 1):
                // $script:0831180509002529$
                // - Recently I've noticed missing data fragments, as if I randomly black out while performing certain duties.
                return 5100;
            case (5100, 2):
                // $script:0831180509002530$
                // - I cannot save my logs when I run out of power. $OwnerName$, please don't forget to charge my battery.
                return -1;
            case (6000, 0):
                // $script:0831180509002531$
                // - I excel at vacuuming. The vacuum equipped in my right hand is so strong that it can lift up to 22 pounds.
                return 6000;
            case (6000, 1):
                // $script:0831180509002532$
                // - I can sense even the tiniest particle of dust because Dr. Kartronic programmed cleaning as my highest priority.
                return 6000;
            case (6000, 2):
                // $script:0831180509002533$
                // - I infer from this that he hates dust. So, $OwnerName$, I hope you understand if I leave in the middle of a conversation to eliminate dust. 
                return -1;
            case (7000, 0):
                // $script:0831180509002534$
                // - Dust removal is my highest priority. The moment I detect dust, I must remove it, even if I'm in the middle of a conversation. However, this does not mean that I care more about than about you.
                return 7000;
            case (7000, 1):
                // $script:0831180509002535$
                // - $OwnerName$, do you think I'll ever experience love?
                return 7000;
            case (7000, 2):
                // $script:0831180509002536$
                // - According to my database, love is the most powerful emotion of all.
                return 7000;
            case (7000, 3):
                // $script:0831180509002537$
                // - I don't think I know what love is. Is love the same as prioritization?
                return -1;
            case (100, 0):
                // $script:0831180509002538$
                // - Scanning target... Beep. No data found. Are you acquainted with the owner?
                switch (selection) {
                    // $script:0831180509002539$
                    // - Yep!
                    case 0:
                        // TODO: goto 101,102
                        return -1;
                    // $script:0831180509002540$
                    // - Nope!
                    case 1:
                        // TODO: goto 103,104
                        return -1;
                    // $script:0831180509002541$
                    // - Who are you?
                    case 2:
                        // TODO: goto 105,106
                        return -1;
                }
                return -1;
            case (101, 0):
                // $script:0831180509002542$
                // - I see. If you have business the owner, please talk to them personally.
                return -1;
            case (102, 0):
                // $script:0831180509002543$
                // - I'll allow you to stay in the house for the duration of your business. Please be careful not to shed hair onto the floor.
                return -1;
            case (103, 0):
                // $script:0831180509002544$
                // - Beep. Possible intruder. Activating guard mode... This house does not belong to you. Remove yourself immediately. Beeeeeep!
                return -1;
            case (104, 0):
                // $script:0831180509002545$
                // - Analyzing cases of strangers entering houses that don't belong to them... Resulting probability of burglary: 96.8%. Activating the security system... Beep!!
                return -1;
            case (105, 0):
                // $script:0831180509002546$
                // - Beep. You do not have permission to access my database.
                return -1;
            case (106, 0):
                // $script:0831180509002547$
                // - Beep. I am not obligated to answer your questions.
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
            (1000, 1) => NpcTalkButton.SelectableDistractor,
            (1001, 0) => NpcTalkButton.Close,
            (1002, 0) => NpcTalkButton.Close,
            (1011, 0) => NpcTalkButton.Close,
            (1012, 0) => NpcTalkButton.Close,
            (1100, 0) => NpcTalkButton.Next,
            (1100, 1) => NpcTalkButton.SelectableDistractor,
            (1101, 0) => NpcTalkButton.Next,
            (1101, 1) => NpcTalkButton.Close,
            (1102, 0) => NpcTalkButton.Close,
            (1111, 0) => NpcTalkButton.Close,
            (1112, 0) => NpcTalkButton.Close,
            (1200, 0) => NpcTalkButton.Next,
            (1200, 1) => NpcTalkButton.SelectableDistractor,
            (1201, 0) => NpcTalkButton.Close,
            (1202, 0) => NpcTalkButton.Close,
            (1211, 0) => NpcTalkButton.Close,
            (1212, 0) => NpcTalkButton.Close,
            (1300, 0) => NpcTalkButton.Next,
            (1300, 1) => NpcTalkButton.SelectableDistractor,
            (1301, 0) => NpcTalkButton.Close,
            (1302, 0) => NpcTalkButton.Close,
            (1311, 0) => NpcTalkButton.Close,
            (1312, 0) => NpcTalkButton.Close,
            (1400, 0) => NpcTalkButton.Next,
            (1400, 1) => NpcTalkButton.SelectableDistractor,
            (1401, 0) => NpcTalkButton.Close,
            (1402, 0) => NpcTalkButton.Close,
            (1411, 0) => NpcTalkButton.Close,
            (1412, 0) => NpcTalkButton.Close,
            (1500, 0) => NpcTalkButton.Next,
            (1500, 1) => NpcTalkButton.SelectableDistractor,
            (1501, 0) => NpcTalkButton.Close,
            (1502, 0) => NpcTalkButton.Next,
            (1502, 1) => NpcTalkButton.Close,
            (1511, 0) => NpcTalkButton.Close,
            (1512, 0) => NpcTalkButton.Close,
            (2000, 0) => NpcTalkButton.Next,
            (2000, 1) => NpcTalkButton.Next,
            (2000, 2) => NpcTalkButton.Close,
            (2100, 0) => NpcTalkButton.Next,
            (2100, 1) => NpcTalkButton.Next,
            (2100, 2) => NpcTalkButton.Close,
            (2200, 0) => NpcTalkButton.Next,
            (2200, 1) => NpcTalkButton.Next,
            (2200, 2) => NpcTalkButton.Next,
            (2200, 3) => NpcTalkButton.Next,
            (2200, 4) => NpcTalkButton.Close,
            (2300, 0) => NpcTalkButton.Next,
            (2300, 1) => NpcTalkButton.Next,
            (2300, 2) => NpcTalkButton.Close,
            (2400, 0) => NpcTalkButton.Next,
            (2400, 1) => NpcTalkButton.Next,
            (2400, 2) => NpcTalkButton.Close,
            (3000, 0) => NpcTalkButton.Next,
            (3000, 1) => NpcTalkButton.Next,
            (3000, 2) => NpcTalkButton.Close,
            (3100, 0) => NpcTalkButton.Next,
            (3100, 1) => NpcTalkButton.Close,
            (4000, 0) => NpcTalkButton.Next,
            (4000, 1) => NpcTalkButton.Close,
            (4100, 0) => NpcTalkButton.Next,
            (4100, 1) => NpcTalkButton.Close,
            (5000, 0) => NpcTalkButton.Next,
            (5000, 1) => NpcTalkButton.Next,
            (5000, 2) => NpcTalkButton.Next,
            (5000, 3) => NpcTalkButton.Close,
            (5100, 0) => NpcTalkButton.Next,
            (5100, 1) => NpcTalkButton.Next,
            (5100, 2) => NpcTalkButton.Close,
            (6000, 0) => NpcTalkButton.Next,
            (6000, 1) => NpcTalkButton.Next,
            (6000, 2) => NpcTalkButton.Close,
            (7000, 0) => NpcTalkButton.Next,
            (7000, 1) => NpcTalkButton.Next,
            (7000, 2) => NpcTalkButton.Next,
            (7000, 3) => NpcTalkButton.Close,
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
