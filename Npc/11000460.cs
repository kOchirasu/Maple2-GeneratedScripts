using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000460: Adam
/// </summary>
public class _11000460 : NpcScript {
    protected override int First() {
        return 50;
    }

    // Select 0:
    // $script:0831180407002044$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (50, 0):
                // $script:0831180407002047$
                // - Hey, I know what you're thinking, and that's not why I'm here at $map:02000107$. I'm all natural! No cosmetic surgery here! I just came to get some fresh air, and check out the latest beauty... trends. While I'm at it.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (50, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
