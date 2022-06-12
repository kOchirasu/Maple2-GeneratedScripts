using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11002023: Lindse
/// </summary>
public class _11002023 : NpcScript {
    protected override int First() {
        return 60;
    }

    // Select 0:
    // $script:0831180306000436$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (60, 0):
                // $script:0831180306000439$
                // - You don't live here, do you? This shop is locals only. Please shop elsewhere.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (60, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
