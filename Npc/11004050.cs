using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004050: Rejan
/// </summary>
public class _11004050 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0614185307010073$
    // - Since none of Terrun Calibre elders are in a position to leave the island, I decided to come and help out.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0614185307010074$
                // - Since none of Terrun Calibre elders are in a position to leave the island, I decided to come and help out.
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
