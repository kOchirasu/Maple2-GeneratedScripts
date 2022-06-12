using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004158: Miel
/// </summary>
public class _11004158 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010587$
    // - It's so close, but I can't reach it. It comes to me in the night and vanishes at dawn.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010588$
                // - Many things shine, not all of them valuable.
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
