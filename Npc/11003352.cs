using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003352: Ralph's Lackey
/// </summary>
public class _11003352 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0517164307008503$
    // - Get away!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0517164307008505$
                // - This time, the big guy'll mop the floor with you! No way he'll lose twice.
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
