using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000837: Dennis
/// </summary>
public class _11000837 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003064$
    // - Shush, I'm on a mission right now. Please don't interrupt me.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003067$
                // - Even the slipperiest suspect can't escape from me once I set my sights on them.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
