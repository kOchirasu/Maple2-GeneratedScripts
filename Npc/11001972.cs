using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001972: Blackeye
/// </summary>
public class _11001972 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0625222407010369$
    // - We must harden our resolve.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0625222407010370$
                // - We must harden our resolve.
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
