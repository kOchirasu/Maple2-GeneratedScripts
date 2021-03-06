using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004524: Gentle Soldieretto
/// </summary>
public class _11004524 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0103163407012503$
    // - Beeep... Beeep...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0103163407012504$
                // - You appear malnourished.
                return 10;
            case (10, 1):
                // $script:0103163407012505$
                // - Feel free to refuel at our aetherine station.
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
