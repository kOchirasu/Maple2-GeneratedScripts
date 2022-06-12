using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001605: Rejan
/// </summary>
public class _11001605 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0504151707006093$
    // - Welcome.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0515180307006142$
                // - The sooner this is over with, the sooner I can go back to Calibre Island.
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
