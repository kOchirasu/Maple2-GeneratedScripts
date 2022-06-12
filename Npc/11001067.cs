using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001067: Kumier
/// </summary>
public class _11001067 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:0831180407003634$
    // - Welcome.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407003638$
                // - Now, now. We should be laughing while we're here.
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
