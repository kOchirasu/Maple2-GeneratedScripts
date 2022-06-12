using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004051: Oska
/// </summary>
public class _11004051 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0614185307010075$
    // - The Green Hoods will do their part to purge the forces of darkness from Maple World.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0614185307010076$
                // - The Green Hoods will do their part to purge the forces of darkness from Maple World.
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
