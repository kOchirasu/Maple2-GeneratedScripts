using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001405: Bomar
/// </summary>
public class _11001405 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:1217025507005337$
    // - Sigh...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:1217025507005341$
                // - P-please don't talk to me. I d-don't know anything!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
