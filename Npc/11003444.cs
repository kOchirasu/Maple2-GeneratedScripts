using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003444: Besherel
/// </summary>
public class _11003444 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0721140007008692$
    // - If you want something, you'll have to pay the price.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0721142007008710$
                // - If you want something, you'll have to pay the price.
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
