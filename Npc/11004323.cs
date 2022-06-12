using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004323: Eve
/// </summary>
public class _11004323 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;40
    }

    // Select 0:
    // $script:1010140307011481$
    // - ...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1010140307011482$
                // - You...
                return 10;
            case (10, 1):
                // $script:1010140307011483$
                // - What are you doing here? Have you come to try and convince me to go home too?
                switch (selection) {
                    // $script:1010140307011484$
                    // - Nothing like that.
                    case 0:
                        return 20;
                }
                return -1;
            case (20, 0):
                // $script:1010140307011485$
                // - ...Really?
                switch (selection) {
                    // $script:1010140307011486$
                    // - You don't look well. Are you feeling all right?
                    case 0:
                        return 30;
                }
                return -1;
            case (30, 0):
                // $script:1010140307011487$
                // - You're not the first person to say that.
                return 30;
            case (30, 1):
                // $script:1010140307011488$
                // - Something $npcName:11000044[gender:0]$ said was bothering me. I came here hoping to find answers.
                return 30;
            case (30, 2):
                // $script:1010140307011489$
                // - Somehow $npcName:11004324[gender:0]$ figured out where I was going and came after me.
                return 30;
            case (30, 3):
                // $script:1010140307011490$
                // - All he's done since is nag, sigh.
                return 30;
            case (30, 4):
                // $script:1010140307011491$
                // - I'm not going to let anyone stop me from finding out what $npcName:11000044[gender:0]$ told me was true.
                switch (selection) {
                    // $script:0111232407012691$
                    // - Good for you!
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0111232407012692$
                // - Thanks! I appreciate your support.
                return -1;
            case (40, 0):
                // $script:0109125407012657$
                // - Sigh...
                return 40;
            case (40, 1):
                // $script:0109125407012658$
                // - $npcName:11004324[gender:0]$ is sweet, but sometimes I just need to be by myself.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (20, 0) => NpcTalkButton.SelectableDistractor,
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Next,
            (30, 2) => NpcTalkButton.Next,
            (30, 3) => NpcTalkButton.Next,
            (30, 4) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
