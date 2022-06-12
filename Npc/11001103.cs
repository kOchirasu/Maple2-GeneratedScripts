using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001103: Rute
/// </summary>
public class _11001103 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:0831180306000404$
    // - You must be here to see me.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0809123006000906$
                // - The stuff's not ready yet. Come back later.
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
