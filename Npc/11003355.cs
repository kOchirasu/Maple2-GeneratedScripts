using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003355: Ralph's Lackey
/// </summary>
public class _11003355 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0517164307008506$
    // - It won't be so easy next time.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0517164307008508$
                // - You better get ready. The big guy'll knock your teeth out!
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
