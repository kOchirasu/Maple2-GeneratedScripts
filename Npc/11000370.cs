using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000370: NRL-B
/// </summary>
public class _11000370 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0831180407001522$
    // - Beep!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407001523$
                // - Beep! Unauthorized access.
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
