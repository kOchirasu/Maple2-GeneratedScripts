using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11002054: Tia
/// </summary>
public class _11002054 : NpcScript {
    protected override int First() {
        return 60;
    }

    // Select 0:
    // $script:1219175006000639$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (60, 0):
                // $script:1219175006000642$
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
