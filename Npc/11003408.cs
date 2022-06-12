using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003408: Evagor
/// </summary>
public class _11003408 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1115100307011843$
    // - You should stay put, stranger.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1115100307011844$
                // - You should stay put, stranger.
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
