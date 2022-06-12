using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001606: Eupheria
/// </summary>
public class _11001606 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0504151707006094$
    // - You're here.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0515180307006143$
                // - Has the time finally come time to avenge Arazaad? $npcName:11001231[gender:0]$... I'll make you pay!
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
