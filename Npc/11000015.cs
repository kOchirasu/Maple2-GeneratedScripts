using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000015: Oska
/// </summary>
public class _11000015 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407000074$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000077$
                // - What brings you to this place?
                switch (selection) {
                    // $script:0831180407000078$
                    // - I came to see you.
                    case 0:
                        return 31;
                    // $script:0831180407000079$
                    // - I came to $map:02000076$ to see the elder.
                    case 1:
                        return 41;
                    // $script:0831180407000080$
                    // - I have business here.
                    case 2:
                        return 51;
                    // $script:0831180407000081$
                    // - That's none of your business.
                    case 3:
                        return 61;
                }
                return -1;
            case (31, 0):
                // $script:0831180407000082$
                // - Do you have a reason for coming to see me?
                switch (selection) {
                    // $script:0831180407000083$
                    // - I just thought I'd say hi.
                    case 0:
                        return 32;
                    // $script:0831180407000084$
                    // - Nope.
                    case 1:
                        return 33;
                }
                return -1;
            case (32, 0):
                // $script:0831180407000085$
                // - Oh. Well. Hi.
                return -1;
            case (33, 0):
                // $script:0831180407000086$
                // - Well, you're just being ridiculous. I've no time for that. Excuse me. 
                return -1;
            case (41, 0):
                // $script:0831180407000087$
                // - $npcName:11000001[gender:0]$'s house is on the hill behind the clock tower in the center of the village. He's always there, keeping an eye on everyone.
                return -1;
            case (51, 0):
                // $script:0831180407000088$
                // - I see. All I'll say then is that if you need help, the militia is always here.
                return -1;
            case (61, 0):
                // $script:0831180407000089$
                // - I hope I didn't upset you. You certainly don't have to explain yourself. But if you do, the rest of the militia and I may be able to help.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Close,
            (33, 0) => NpcTalkButton.Close,
            (41, 0) => NpcTalkButton.Close,
            (51, 0) => NpcTalkButton.Close,
            (61, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
