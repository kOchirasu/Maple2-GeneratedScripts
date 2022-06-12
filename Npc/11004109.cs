using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004109: Blackeye
/// </summary>
public class _11004109 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0720125407010459$
    // - We'll always do our best.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0720125407010460$
                // - I'll do whatever I can to aid you.
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
