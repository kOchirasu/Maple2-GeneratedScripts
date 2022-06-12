using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003348: Ralph's Lackey
/// </summary>
public class _11003348 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0517164307008496$
    // - This place has really transformed, thanks to you!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0517164307008498$
                // - We're all serious now. You just wait and see. The boss'll make you pay!
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
