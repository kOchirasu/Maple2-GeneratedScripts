using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004507: Mannstad Sentry
/// </summary>
public class _11004507 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1228182607012441$
    // - I haven't seen you before. You that outlander everyone's talking about?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1228182607012442$
                // - I haven't seen you before. You that outlander everyone's talking about?
                return 10;
            case (10, 1):
                // $script:1228182607012443$
                // - Anyway, watch yourself out there. Our enemy won't hesitate to shoot you down.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
