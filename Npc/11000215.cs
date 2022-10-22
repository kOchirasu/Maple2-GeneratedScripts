using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000215: Evan
/// </summary>
public class _11000215 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;30;40;50;60;70;80;100
    }

    // Select 0:
    // $script:0831180407000911$
    // - What seems to be the problem?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407000913$
                // - Mm? What is it? Are you having a problem posting $item:30000038$?
                switch (selection) {
                    // $script:0831180407000914$
                    // - Actually, I kinda lost my $item:30000038$...
                    case 0:
                        // TODO: goto 21,22
                        // TODO: gotoFail 23
                        return 23;
                    // $script:0831180407000915$
                    // - Where am I supposed to post $item:30000038$ again?
                    case 1:
                        return 24;
                }
                return -1;
            case (21, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180407000916$
                // - Oh, I see. Here's another one. Try not to lose it this time.
                return -1;
            case (22, 0):
                // $script:0831180407000917$
                // - I remember giving you one, though. Why don't you check your bag one more time?
                return -1;
            case (23, 0):
                // $script:0831180407000918$
                // - Your bag looks really heavy. Why don't you lighten it first?
                return -1;
            case (24, 0):
                // $script:0831180407000919$
                // - There's a Dark Wind Bounty Bulletin Board in $map:02000138$. Take it there.
                return -1;
            case (30, 0):
                // $script:0831180407000920$
                // - Mm? What is it? Are you having a problem posting $item:30000038$?
                switch (selection) {
                    // $script:0831180407000921$
                    // - Actually, I kinda lost my $item:30000038$...
                    case 0:
                        // TODO: goto 31,32
                        // TODO: gotoFail 33
                        return 33;
                    // $script:0831180407000922$
                    // - Where am I supposed to post $item:30000038$ again?
                    case 1:
                        return 34;
                }
                return -1;
            case (31, 0):
                // functionID=2 openTalkReward=True 
                // $script:0831180407000923$
                // - Oh, I see. Here's another one. Try not to lose it this time.
                return -1;
            case (32, 0):
                // $script:0831180407000924$
                // - I remember giving you one, though. Why don't you check your bag one more time?
                return -1;
            case (33, 0):
                // $script:0831180407000925$
                // - Your bag looks really heavy. Why don't you lighten it first?
                return -1;
            case (34, 0):
                // $script:0831180407000926$
                // - There's a Dark Wind Bounty Bulletin Board in $map:02000137$. Take it there.
                return -1;
            case (40, 0):
                // $script:0831180407000927$
                // - Mm? What is it? Are you having a problem posting $item:30000038$?
                switch (selection) {
                    // $script:0831180407000928$
                    // - Actually, I kinda lost my $item:30000038$...
                    case 0:
                        // TODO: goto 41,42
                        // TODO: gotoFail 43
                        return 43;
                    // $script:0831180407000929$
                    // - Where am I supposed to post $item:30000038$ again?
                    case 1:
                        return 44;
                }
                return -1;
            case (41, 0):
                // functionID=3 openTalkReward=True 
                // $script:0831180407000930$
                // - Oh, I see. Here's another one. Try not to lose it this time.
                return -1;
            case (42, 0):
                // $script:0831180407000931$
                // - I remember giving you one, though. Why don't you check your bag one more time?
                return -1;
            case (43, 0):
                // $script:0831180407000932$
                // - Your bag looks really heavy. Why don't you lighten it first?
                return -1;
            case (44, 0):
                // $script:0831180407000933$
                // - There's a Dark Wind Bounty Bulletin Board in $map:02000135$. Take it there.
                return -1;
            case (50, 0):
                // $script:0831180407000934$
                // - Mm? What is it? Are you having a problem posting $item:30000038$?
                switch (selection) {
                    // $script:0831180407000935$
                    // - Actually, I kinda lost my $item:30000038$...
                    case 0:
                        // TODO: goto 51,52
                        // TODO: gotoFail 53
                        return 53;
                    // $script:0831180407000936$
                    // - Where am I supposed to post $item:30000038$ again?
                    case 1:
                        return 54;
                }
                return -1;
            case (51, 0):
                // functionID=4 openTalkReward=True 
                // $script:0831180407000937$
                // - Oh, I see. Here's another one. Try not to lose it this time.
                return -1;
            case (52, 0):
                // $script:0831180407000938$
                // - I remember giving you one, though. Why don't you check your bag one more time?
                return -1;
            case (53, 0):
                // $script:0831180407000939$
                // - Your bag looks really heavy. Why don't you lighten it first?
                return -1;
            case (54, 0):
                // $script:0831180407000940$
                // - There's a Dark Wind Bounty Bulletin Board in $map:02000146$. Take it there.
                return -1;
            case (60, 0):
                // $script:0831180407000941$
                // - There's been a rift within Dark Wind ever since $npcName:11000044[gender:0]$ became captain. The members are split between supporting the former captain, Winn Stilton, and supporting the new captain, $npcName:11000044[gender:0]$.
                return 60;
            case (60, 1):
                // $script:0831180407000942$
                // - I haven't decided which side I'm on, but honestly, supporting $npcName:11000044[gender:0]$ makes the most sense at this point.
                return -1;
            case (70, 0):
                // $script:0831180407000943$
                // - Captain $npcName:11000044[gender:0]$ was behind all of this! I can't believe I trusted him.
                return -1;
            case (80, 0):
                // $script:1122010507007443$
                // - Checking up on me again, are you?
                switch (selection) {
                    // $script:1122010507007444$
                    // - Don't worry. I'm not here to interrogate you.
                    case 0:
                        return 81;
                }
                return -1;
            case (81, 0):
                // $script:1122010507007445$
                // - Then why are you here, exactly?
                switch (selection) {
                    // $script:1122010507007446$
                    // - I'm just dropping by. I'll be back later.
                    case 0:
                        return 82;
                }
                return -1;
            case (82, 0):
                // $script:1122010507007447$
                // - And will you bring the $npcName:11001912[gender:0]$ with you next time?
                switch (selection) {
                    // $script:1122010507007448$
                    // - No, just me. I want another look at the secret room upstairs.
                    case 0:
                        return 83;
                }
                return -1;
            case (83, 0):
                // functionID=5 
                // $script:1122010507007449$
                // - The secret room? Again? That place must be something else...
                return -1;
            case (100, 0):
                // $script:1129150207009373$
                // - Dark Wind gradually grows more stable, but the world is in chaos, as always.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.SelectableDistractor,
            (21, 0) => NpcTalkButton.Close,
            (22, 0) => NpcTalkButton.Close,
            (23, 0) => NpcTalkButton.Close,
            (24, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (32, 0) => NpcTalkButton.Close,
            (33, 0) => NpcTalkButton.Close,
            (34, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Close,
            (42, 0) => NpcTalkButton.Close,
            (43, 0) => NpcTalkButton.Close,
            (44, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.SelectableDistractor,
            (51, 0) => NpcTalkButton.Close,
            (52, 0) => NpcTalkButton.Close,
            (53, 0) => NpcTalkButton.Close,
            (54, 0) => NpcTalkButton.Close,
            (60, 0) => NpcTalkButton.Next,
            (60, 1) => NpcTalkButton.Close,
            (70, 0) => NpcTalkButton.Close,
            (80, 0) => NpcTalkButton.SelectableDistractor,
            (81, 0) => NpcTalkButton.SelectableDistractor,
            (82, 0) => NpcTalkButton.SelectableDistractor,
            (83, 0) => NpcTalkButton.Close,
            (100, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
