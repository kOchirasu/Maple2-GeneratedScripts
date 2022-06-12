using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003061: Frozen Tree
/// </summary>
public class _11003061 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0102155907007643$
    // - <font color="#909090">(A chilling wind blows through the gap in the ice wall behind the frozen tree.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0102155907007644$
                // - <font color="#909090">(Something must be hidden behind this tree.)</font>
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
