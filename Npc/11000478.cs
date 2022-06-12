using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000478: Kodor
/// </summary>
public class _11000478 : NpcScript {
    protected override int First() {
        return 50;
    }

    // Select 0:
    // $script:0831180407002080$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (50, 0):
                // $script:0831180407002085$
                // - I have a friend not far from here, but being away from him is agony. I wonder how he's doing...
                switch (selection) {
                    // $script:0831180407002086$
                    // - Who is he?
                    case 0:
                        return 51;
                    // $script:0831180407002087$
                    // - I'm sure he's fine.
                    case 1:
                        return 52;
                }
                return -1;
            case (51, 0):
                // $script:0831180407002088$
                // - That's... Um... Sheesh, $MyPCName$! You wouldn't know even if I told you! Don't you miss someone like that?
                return -1;
            case (52, 0):
                // $script:0831180407002089$
                // - Do you think so? I think so, too...
                return 52;
            case (52, 1):
                // $script:0831180407002090$
                // - I know he's doing well. He's strong enough to get through anything.
                return 52;
            case (52, 2):
                // $script:0831180407002091$
                // - But sometimes bad things happen, and that's why I'm worried about him. $MyPCName$, could you pray for his well-being?
                switch (selection) {
                    // $script:0831180407002092$
                    // - Of course.
                    case 0:
                        return 53;
                    // $script:0831180407002093$
                    // - It's not my business.
                    case 1:
                        return 54;
                }
                return -1;
            case (53, 0):
                // $script:0831180407002094$
                // - You're very kind! I consider you a good friend, $MyPCName$. I'll be praying for you, too.
                return -1;
            case (54, 0):
                // $script:0831180407002095$
                // - Oh, $MyPCName$... You must not have many friends...
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (50, 0) => NpcTalkButton.SelectableDistractor,
            (51, 0) => NpcTalkButton.Close,
            (52, 0) => NpcTalkButton.Next,
            (52, 1) => NpcTalkButton.Next,
            (52, 2) => NpcTalkButton.SelectableDistractor,
            (53, 0) => NpcTalkButton.Close,
            (54, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
