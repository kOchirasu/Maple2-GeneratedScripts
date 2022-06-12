using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003881: Gardener
/// </summary>
public class _11003881 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0417135107009878$
    // - Whenever a new herb is discovered, I plant it here.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0417135107009879$
                // - Whenever a new herb is discovered, I plant it here.
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
