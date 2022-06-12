using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004234: Lanemone
/// </summary>
public class _11004234 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0809223207010919$
    // - You're really amazing, you know that?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0809223207010920$
                // - You're really amazing, you know that?
                return 10;
            case (10, 1):
                // $script:0809223207010921$
                // - I hate tedious matters, but I suppose I can help if you're the one asking.
                return 10;
            case (10, 2):
                // $script:0809223207010922$
                // - But if you happen to find anything interesting, you'd better bring it to me instead of $npcName:11004103[gender:1]$! Promise.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Next,
            (10, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
