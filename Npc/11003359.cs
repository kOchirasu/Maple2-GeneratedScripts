using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003359: Ralph's Lackey
/// </summary>
public class _11003359 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0517164307008512$
    // - You better prepare yourself.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0517164307008514$
                // - You better be ready this time. You'll see what I mean when you go inside. Heheheh...
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
