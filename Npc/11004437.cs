using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004437: Nairin
/// </summary>
public class _11004437 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1213154907011978$
    // - Would you like to take on a mission for Green Hoods?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1213154907011979$
                // - Where should I start? Local ecology? Demographics? There's so much data to collate!
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
