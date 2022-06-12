using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003162: Pudge
/// </summary>
public class _11003162 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0306155707008070$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0306155707008073$
                // - Everyone likes flowers because they're pretty. I don't care about that, because I use them to make supplements, scented candles, and potions.
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
