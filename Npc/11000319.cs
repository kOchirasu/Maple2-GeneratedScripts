using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000319: Shinby
/// </summary>
public class _11000319 : NpcScript {
    protected override int First() {
        return 50;
    }

    // Select 0:
    // $script:0831180407001238$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (50, 0):
                // $script:0831180407001243$
                // - Nice to meet you. I'm $npcName:11000319[gender:1]$. What's your name?
                switch (selection) {
                    // $script:0831180407001244$
                    // - I'm $MyPCName$.
                    case 0:
                        return 51;
                    // $script:0831180407001245$
                    // - It's a secret.
                    case 1:
                        return 52;
                }
                return -1;
            case (51, 0):
                // $script:0831180407001246$
                // - $MyPCName$? Ah, what a beautiful name!
                return -1;
            case (52, 0):
                // $script:0831180407001247$
                // - You don't have to tell me. It's $MyPCName$, right?
                switch (selection) {
                    // $script:0831180407001248$
                    // - How do you know that?
                    case 0:
                        return 53;
                }
                return -1;
            case (53, 0):
                // $script:0831180407001249$
                // - It's a secret. Ho, ho!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (50, 0) => NpcTalkButton.SelectableDistractor,
            (51, 0) => NpcTalkButton.Close,
            (52, 0) => NpcTalkButton.SelectableDistractor,
            (53, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
