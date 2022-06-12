using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003094: Blackeye
/// </summary>
public class _11003094 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0207122607007940$
    // - Ahh it's you, $MyPCName$.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0207122607007941$
                // - Dark Wind is changing. It's not the same organization you once knew.
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
