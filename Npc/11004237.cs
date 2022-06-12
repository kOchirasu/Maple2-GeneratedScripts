using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004237: Allon
/// </summary>
public class _11004237 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0809223207010929$
    // - Good work, $MyPCName$.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0809223207010930$
                // - Good work, $MyPCName$. I'd better head back to $map:02000001$ now.
                return 10;
            case (10, 1):
                // $script:0809223207010931$
                // - I haven't seen his face in some time.
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
