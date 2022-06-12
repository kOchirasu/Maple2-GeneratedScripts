using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004561: Startz
/// </summary>
public class _11004561 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0220211107014508$
    // - Hey.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0220211107014509$
                // - Hey.
                return 10;
            case (10, 1):
                // $script:0220211107014510$
                // - Didn't think I'd see you here.
                switch (selection) {
                    // $script:0220211107014511$
                    // - Same.
                    case 0:
                        return 20;
                }
                return -1;
            case (20, 0):
                // $script:0220211107014512$
                // - The Pink Beans dragged me out here to fight in their idiotic rumble.
                return 20;
            case (20, 1):
                // $script:0220211107014513$
                // - I don't know how they found out that I'm a decent fighter. What a hassle...
                return 20;
            case (20, 2):
                // $script:0220211107014514$
                // - If we end up facing off in the ring, I'll have to show you a thing or two.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (20, 0) => NpcTalkButton.Next,
            (20, 1) => NpcTalkButton.Next,
            (20, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
