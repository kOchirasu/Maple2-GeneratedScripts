using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004049: Carriage Tender
/// </summary>
public class _11004049 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0614185307010071$
    // - Would you like a carriage back to Tria?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0614185307010072$
                // - Would you like a carriage back to Tria?
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
