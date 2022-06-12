using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004048: Carriage Tender
/// </summary>
public class _11004048 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0614185307010069$
    // - It's a long walk to the Frontier Foundation. Why not take a carriage?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0614185307010070$
                // - It's a long walk to the Frontier Foundation. Why not take a carriage?
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
