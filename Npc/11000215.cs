using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000215: Evan
/// </summary>
public class _11000215 : NpcScript {
    internal _11000215(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30;40;50;60;70;80;100
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000911$ 
                // - What seems to be the problem? 
                return true;
            case 20:
                // $script:0831180407000913$ 
                // - Mm? What is it? Are you having a problem posting $item:30000038$? 
                switch (selection) {
                    // $script:0831180407000914$
                    // - Actually, I kinda lost my $item:30000038$...
                    case 0:
                        Id = 0; // TODO: 21,22 | 23
                        return false;
                    // $script:0831180407000915$
                    // - Where am I supposed to post $item:30000038$ again?
                    case 1:
                        Id = 24;
                        return false;
                }
                return true;
            case 21:
                // $script:0831180407000916$ functionID=1 
                // - Oh, I see. Here's another one. Try not to lose it this time. 
                return true;
            case 22:
                // $script:0831180407000917$ 
                // - I remember giving you one, though. Why don't you check your bag one more time? 
                return true;
            case 23:
                // $script:0831180407000918$ 
                // - Your bag looks really heavy. Why don't you lighten it first? 
                return true;
            case 24:
                // $script:0831180407000919$ 
                // - There's a Dark Wind Bounty Bulletin Board in $map:02000138$. Take it there. 
                return true;
            case 30:
                // $script:0831180407000920$ 
                // - Mm? What is it? Are you having a problem posting $item:30000038$? 
                switch (selection) {
                    // $script:0831180407000921$
                    // - Actually, I kinda lost my $item:30000038$...
                    case 0:
                        Id = 0; // TODO: 31,32 | 33
                        return false;
                    // $script:0831180407000922$
                    // - Where am I supposed to post $item:30000038$ again?
                    case 1:
                        Id = 34;
                        return false;
                }
                return true;
            case 31:
                // $script:0831180407000923$ functionID=2 
                // - Oh, I see. Here's another one. Try not to lose it this time. 
                return true;
            case 32:
                // $script:0831180407000924$ 
                // - I remember giving you one, though. Why don't you check your bag one more time? 
                return true;
            case 33:
                // $script:0831180407000925$ 
                // - Your bag looks really heavy. Why don't you lighten it first? 
                return true;
            case 34:
                // $script:0831180407000926$ 
                // - There's a Dark Wind Bounty Bulletin Board in $map:02000137$. Take it there. 
                return true;
            case 40:
                // $script:0831180407000927$ 
                // - Mm? What is it? Are you having a problem posting $item:30000038$? 
                switch (selection) {
                    // $script:0831180407000928$
                    // - Actually, I kinda lost my $item:30000038$...
                    case 0:
                        Id = 0; // TODO: 41,42 | 43
                        return false;
                    // $script:0831180407000929$
                    // - Where am I supposed to post $item:30000038$ again?
                    case 1:
                        Id = 44;
                        return false;
                }
                return true;
            case 41:
                // $script:0831180407000930$ functionID=3 
                // - Oh, I see. Here's another one. Try not to lose it this time. 
                return true;
            case 42:
                // $script:0831180407000931$ 
                // - I remember giving you one, though. Why don't you check your bag one more time? 
                return true;
            case 43:
                // $script:0831180407000932$ 
                // - Your bag looks really heavy. Why don't you lighten it first? 
                return true;
            case 44:
                // $script:0831180407000933$ 
                // - There's a Dark Wind Bounty Bulletin Board in $map:02000135$. Take it there. 
                return true;
            case 50:
                // $script:0831180407000934$ 
                // - Mm? What is it? Are you having a problem posting $item:30000038$? 
                switch (selection) {
                    // $script:0831180407000935$
                    // - Actually, I kinda lost my $item:30000038$...
                    case 0:
                        Id = 0; // TODO: 51,52 | 53
                        return false;
                    // $script:0831180407000936$
                    // - Where am I supposed to post $item:30000038$ again?
                    case 1:
                        Id = 54;
                        return false;
                }
                return true;
            case 51:
                // $script:0831180407000937$ functionID=4 
                // - Oh, I see. Here's another one. Try not to lose it this time. 
                return true;
            case 52:
                // $script:0831180407000938$ 
                // - I remember giving you one, though. Why don't you check your bag one more time? 
                return true;
            case 53:
                // $script:0831180407000939$ 
                // - Your bag looks really heavy. Why don't you lighten it first? 
                return true;
            case 54:
                // $script:0831180407000940$ 
                // - There's a Dark Wind Bounty Bulletin Board in $map:02000146$. Take it there. 
                return true;
            case 60:
                // $script:0831180407000941$ 
                // - There's been a rift within Dark Wind ever since $npcName:11000044[gender:0]$ became captain. The members are split between supporting the former captain, Winn Stilton, and supporting the new captain, $npcName:11000044[gender:0]$. 
                // $script:0831180407000942$ 
                // - I haven't decided which side I'm on, but honestly, supporting $npcName:11000044[gender:0]$ makes the most sense at this point. 
                return true;
            case 70:
                // $script:0831180407000943$ 
                // - Captain $npcName:11000044[gender:0]$ was behind all of this! I can't believe I trusted him. 
                return true;
            case 80:
                // $script:1122010507007443$ 
                // - Checking up on me again, are you? 
                switch (selection) {
                    // $script:1122010507007444$
                    // - Don't worry. I'm not here to interrogate you.
                    case 0:
                        Id = 81;
                        return false;
                }
                return true;
            case 81:
                // $script:1122010507007445$ 
                // - Then why are you here, exactly? 
                switch (selection) {
                    // $script:1122010507007446$
                    // - I'm just dropping by. I'll be back later.
                    case 0:
                        Id = 82;
                        return false;
                }
                return true;
            case 82:
                // $script:1122010507007447$ 
                // - And will you bring the $npcName:11001912[gender:0]$ with you next time? 
                switch (selection) {
                    // $script:1122010507007448$
                    // - No, just me. I want another look at the secret room upstairs.
                    case 0:
                        Id = 83;
                        return false;
                }
                return true;
            case 83:
                // $script:1122010507007449$ functionID=5 
                // - The secret room? Again? That place must be something else... 
                return true;
            case 100:
                // $script:1129150207009373$ 
                // - Dark Wind gradually grows more stable, but the world is in chaos, as always. 
                return true;
            default:
                return true;
        }
    }
}
