using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004236: Oska
/// </summary>
public class _11004236 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0809223207010926$
    // - Amazing work, $MyPCName$.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0809223207010927$
                // - Amazing work, $MyPCName$.
                return 10;
            case (10, 1):
                // $script:0809223207010928$
                // - I wish everybody was more like you.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
