using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003429: Silver Wolf
/// </summary>
public class _11003429 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0719173007008675$
    // - I sense the war chief at the top of the hourglass. And yet... something is amiss.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0719173007008676$
                // - I sense the war chief at the top of the hourglass. And yet... something is amiss.
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
