using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004113: Junta
/// </summary>
public class _11004113 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0720125407010469$
    // - I am ready to leave at a moments notice.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0720125407010470$
                // - Guidance has been retasked toward the recovery of Lapenshards.
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
