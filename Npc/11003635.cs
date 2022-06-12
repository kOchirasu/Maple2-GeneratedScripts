using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003635: Chandler
/// </summary>
public class _11003635 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1109121007009054$
    // - Science is the answer!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1109121007009055$
                // - Ah, greetings, fellow scientist! Are you here to discuss the latest theories in electromathography?
                switch (selection) {
                    // $script:1109121007009056$
                    // - I'm looking for someone, actually.
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1109121007009057$
                // - In that case, you've found the right person, $MyPCName$.
                switch (selection) {
                    // $script:1109121007009058$
                    // - How do you know me?
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:1109121007009059$
                // - Everyone in Dark Wind knows you.
                switch (selection) {
                    // $script:1109121007009060$
                    // - Then you must have a message for $npcName:11003535[gender:1]$.
                    case 0:
                        return 13;
                }
                return -1;
            case (13, 0):
                // $script:1109121007009061$
                // - "Pancakes, with extra syrup!"
                switch (selection) {
                    // $script:1109121007009062$
                    // - If I give you pancakes, will you tell me the message?
                    case 0:
                        return 14;
                }
                return -1;
            case (14, 0):
                // $script:1109121007009063$
                // - That <i>is</i> the message. Now, about those theories...
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.SelectableDistractor,
            (13, 0) => NpcTalkButton.SelectableDistractor,
            (14, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
