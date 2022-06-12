using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000183: Queen Bee
/// </summary>
public class _11000183 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407000768$
    // - What izzz it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000771$
                // - Honey izz very preciouz to uzz honeybeezz! We won't let anyone take it away!
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
