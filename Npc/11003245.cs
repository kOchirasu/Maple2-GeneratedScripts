using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003245: Oska
/// </summary>
public class _11003245 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0403155707008150$
    // - No... $npcName:11000001[gender:0]$...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0403155707008151$
                // - Ah... $npcName:11000001[gender:0]$...
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
