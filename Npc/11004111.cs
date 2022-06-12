using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004111: Allon
/// </summary>
public class _11004111 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0720125407010463$
    // - Talk to me whenever you need assistance.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0720125407010464$
                // - Our knights always do their utmost.
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
