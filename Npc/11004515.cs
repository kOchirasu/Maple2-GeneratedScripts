using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004515: Mannstad Driver
/// </summary>
public class _11004515 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1228182607012475$
    // - We don't have enough fuel for our cars. We don't have enough ammo for our weapons. We just don't have enough...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1228182607012476$
                // - We don't have enough fuel for our cars. We don't have enough ammo for our weapons. We just don't have enough...
                return 10;
            case (10, 1):
                // $script:1228182607012477$
                // - Hey, you aren't carrying any aetherine on you, are you? Ugh, as if it'd just fall into our laps like that...
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
