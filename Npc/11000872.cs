using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000872: Skan
/// </summary>
public class _11000872 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003151$
    // - What? Do you have something to say to me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003154$
                // - Don't rely on Fairy Dew too much. This place is teeming with monsters that are stronger than you.
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
