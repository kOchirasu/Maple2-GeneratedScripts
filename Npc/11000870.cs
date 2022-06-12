using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000870: Marlowe
/// </summary>
public class _11000870 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407003145$
    // - Huh?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407003147$
                // - Isn't this incredible? Frozen in time...
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
