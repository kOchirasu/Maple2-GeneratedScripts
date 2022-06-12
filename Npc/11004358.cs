using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004358: Evelyn
/// </summary>
public class _11004358 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1109213607011769$
    // - Oh look, $MyPCName$. Snow!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1109213607011770$
                // - I always love snow for the holidays.
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
