using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001336: Bodis
/// </summary>
public class _11001336 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1217012607005263$
    // - Someday we'll have a customer who returns their board...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1217012607005266$
                // - Back in my day, we'd explore the whole world on our skateboards. I even shredded over the hot desert sands... Ah, those were good times.
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
