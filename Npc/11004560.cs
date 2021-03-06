using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004560: Rovey
/// </summary>
public class _11004560 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;20
    }

    // Select 0:
    // $script:0220211107014495$
    // - Hm.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0220211107014496$
                // - And who might you be?
                return 10;
            case (10, 1):
                // $script:0220211107014497$
                // - I haven't seen you before, but you seem like a formidable opponent.
                switch (selection) {
                    // $script:0220211107014498$
                    // - And you are?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:0220211107014499$
                // - Ahem! I am Rovey, drillmaster for the Royal Knights.
                return 11;
            case (11, 1):
                // $script:0220211107014500$
                // - I've trained many knights around your age. In fact, you remind me of one particular fool whom I once taught...
                return 11;
            case (11, 2):
                // $script:0220211107014501$
                // - Well, I shan't waste any more words on you. I will see you in the rumble.
                return -1;
            case (20, 0):
                // $script:0220211107014502$
                // - !!
                return 20;
            case (20, 1):
                // $script:0220211107014503$
                // - You...
                switch (selection) {
                    // $script:0220211107014504$
                    // - $npcName:11004560[gender:0]$?!
                    case 0:
                        return 21;
                }
                return -1;
            case (21, 0):
                // $script:0220211107014505$
                // - I'm surprised that foolish sense of justice hasn't gotten you killed. Why did you come here?
                switch (selection) {
                    // $script:0220211107014506$
                    // - I'm here to fight.
                    case 0:
                        return 22;
                }
                return -1;
            case (22, 0):
                // $script:0220211107014507$
                // - It's been some time since we last sparred. I'm curious to see how you've grown.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Next,
            (11, 1) => NpcTalkButton.Next,
            (11, 2) => NpcTalkButton.Close,
            (20, 0) => NpcTalkButton.Next,
            (20, 1) => NpcTalkButton.SelectableDistractor,
            (21, 0) => NpcTalkButton.SelectableDistractor,
            (22, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
