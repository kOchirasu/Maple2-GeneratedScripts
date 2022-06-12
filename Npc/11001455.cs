using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001455: Melatina
/// </summary>
public class _11001455 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1222171407005450$
    // - Hello.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1222171407005453$
                // - On $map:02010022$, hard work is considered a sin. Got nothing to do? Then soak in the majesty that surrounds us!
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
