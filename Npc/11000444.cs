using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000444: Columbo
/// </summary>
public class _11000444 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;60
    }

    // Select 0:
    // $script:0831180407001867$
    // - Ah... I want to get better soon, so I can go on adventures again.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407001870$
                // - When can I sail again? Cough, cough! My leg had better heal quickly so I can get back to finding that pirate island.
                return -1;
            case (60, 0):
                // $script:0831180407001871$
                // - The sea may look calm from here, but it can destroy you in an instant.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            (60, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
