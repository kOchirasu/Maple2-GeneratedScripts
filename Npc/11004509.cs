using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004509: Mannstad Sentry
/// </summary>
public class _11004509 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1228182607012451$
    // - Look what we have here. It's about time they sent us some reinforcements.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1228182607012452$
                // - Look what we have here. It's about time they sent us some reinforcements.
                switch (selection) {
                    // $script:1228182607012453$
                    // - I'm not your reinforcements.
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1228182607012454$
                // - Tch... Figures. We don't have the numbers to hold this position for right now. Y'know, give a leshy a gun and I'd let it stand guard. That's how desperate we are!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
