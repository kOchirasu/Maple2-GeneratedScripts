using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003356: Ralph's Lackey
/// </summary>
public class _11003356 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0517164307008509$
    // - Get away from me. I <i>really</i> don't want to talk to you.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0517164307008511$
                // - There's no way the big guy will lose to such a weakling.
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
