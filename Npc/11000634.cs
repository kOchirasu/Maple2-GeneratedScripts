using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000634: Prisoner 140917
/// </summary>
public class _11000634 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 40;50
    }

    // Select 0:
    // $script:0831180407002575$
    // - Get me out of here... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407002579$
                // - Get me out of here, would ya? I've got a stash on the outside. A million mesos for my freedom. What'cha say?
                switch (selection) {
                    // $script:0831180407002580$
                    // - No way, you're in for fraud! That's the worst!
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:0831180407002581$
                // - Bah, how did you know I'm in here for fraud? Did the warden tell you? If you're not going to get me out of here, then scram!
                return -1;
            case (50, 0):
                // $script:1210061907004888$
                // - Get me out of here, would ya? I've got a stash on the outside. A million mesos for my freedom. What'cha say?
                switch (selection) {
                    // $script:1210061907004889$
                    // - Do you know someone named $npcName:11001231[gender:0]$?
                    case 0:
                        return 51;
                }
                return -1;
            case (51, 0):
                // $script:1210061907004890$
                // - Sure I do, sure! Just help me break out, and I'll tell you all about it.
                switch (selection) {
                    // $script:1210061907004891$
                    // - What does she look like?
                    case 0:
                        return 52;
                }
                return -1;
            case (52, 0):
                // $script:1210061907004892$
                // - She's got... hair. A real smart-looking gal. And really pretty, too.
                switch (selection) {
                    // $script:1210061907004893$
                    // - $npcName:11001231[gender:0]$ is a man.
                    case 0:
                        return 53;
                }
                return -1;
            case (53, 0):
                // $script:1210061907004894$
                // - You were testing me? Get outta here, you rat! If you ain't gonna help me, just leave me alone!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.SelectableDistractor,
            (51, 0) => NpcTalkButton.SelectableDistractor,
            (52, 0) => NpcTalkButton.SelectableDistractor,
            (53, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
