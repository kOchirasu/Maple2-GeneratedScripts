using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004551: Office Guard
/// </summary>
public class _11004551 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0109163907012668$
    // - You! Outlander! You better not be here to bother $npcName:11004401[gender:1]$.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0109163907012669$
                // - You! Outlander! You better not be here to bother $npcName:11004401[gender:1]$.
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
