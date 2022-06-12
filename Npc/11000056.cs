using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000056: Leonard
/// </summary>
public class _11000056 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407000241$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000244$
                // - Hmph, the oarsman at $map:63000002$ is so greedy. He charges a huge fee just to take you to $map:02000062$. Isn't that crazy?
                switch (selection) {
                    // $script:0831180407000245$
                    // - It really is.
                    case 0:
                        return 31;
                    // $script:0831180407000246$
                    // - I don't know.
                    case 1:
                        return 32;
                }
                return -1;
            case (31, 0):
                // $script:0831180407000247$
                // - Seriously! Some people stay in $map:63000002$ for ages just to make enough money to get on his boat!
                switch (selection) {
                    // $script:0831180407000248$
                    // - What do people do to make money?
                    case 0:
                        return 33;
                }
                return -1;
            case (32, 0):
                // $script:0831180407000251$
                // - Really? Well, I guess the fare would be nothing if I could win $npcName:11000441[gender:0]$'s prize money.
                switch (selection) {
                    // $script:0831180407000252$
                    // - Wait, what's this about $npc:11000441[gender:0]$'s prize money?
                    case 0:
                        return 34;
                }
                return -1;
            case (33, 0):
                // $script:0831180407000249$
                // - Oh, they hunt monsters or pick up junk that washes up on the shore. Some of it is pretty valuable.
                return 33;
            case (33, 1):
                // $script:0831180407000250$
                // - But I'll never go there. I don't want to be trampled by $npcName:22300149$ before I get to the mainland.
                return -1;
            case (34, 0):
                // $script:0831180407000253$
                // - I told you. Enter $map:61000005$ behind me and survive until the end, and $npc:11000441[gender:0]$ will shower you with money.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.SelectableDistractor,
            (33, 0) => NpcTalkButton.Next,
            (33, 1) => NpcTalkButton.Close,
            (34, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
