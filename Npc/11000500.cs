using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000500: Flat Rock
/// </summary>
public class _11000500 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0831180407002177$
    // - Not just anyone can sit on me.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407002178$
                // - You kick me, and I'm not going to be the one in pain.
                return 10;
            case (10, 1):
                // $script:0626205807010385$
                // - You better leave while I'm still in a good mood. I'm no ordinary rock.
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
