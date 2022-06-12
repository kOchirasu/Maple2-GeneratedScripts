using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000252: Chairman Goldus
/// </summary>
public class _11000252 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407001053$
    // - What do <i>you</i> want?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407001055$
                // - Goldus never stops moving toward the future. There's nothing we can't make or sell.
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
