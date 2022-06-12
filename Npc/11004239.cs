using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004239: Tinchai
/// </summary>
public class _11004239 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0809223207010935$
    // - Is this goodbye?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0809223207010936$
                // - Is this goodbye?
                return 10;
            case (10, 1):
                // $script:0809223207010937$
                // - You did a great job!
                return 10;
            case (10, 2):
                // $script:0809223207010938$
                // - I wish $npcName:11004238[gender:0]$ felt more like celebrating. I guess he's embarrassed about missing all the action.
                return 10;
            case (10, 3):
                // $script:0809223207010939$
                // - Next time, Guidance will be there to help! Just say the word.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Next,
            (10, 2) => NpcTalkButton.Next,
            (10, 3) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
