using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000810: Amy
/// </summary>
public class _11000810 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407002984$
    // - Sigh...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407002986$
                // - $MyPCName$, I don't know how to repay you and the Lumina Liberation Army for this. Thank you so much.
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
