using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004330: Kaitlyn
/// </summary>
public class _11004330 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;30
    }

    protected override int Select() {
        // Select 0:
        // $script:1102172107011631$
        // - Sigh...
        // Select 20:
        // $script:1010140307011542$
        // - Sigh...
        // TODO: 0,20
        return 0;
    }

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1102172107011632$
                // - Will he be okay without me? Maybe I should go back...
                return -1;
            case (30, 0):
                // $script:1010140307011543$
                // - Sigh...
                switch (selection) {
                    // $script:1010140307011544$
                    // - Why the long face?
                    case 0:
                        return 40;
                }
                return -1;
            case (40, 0):
                // $script:1010140307011545$
                // - $MyPCName$? It seems like I can't go anywhere without bumping into you.
                return 40;
            case (40, 1):
                // $script:1010140307011546$
                // - When I heard about the discovery of a new continent from somewhere else, I rushed over in order to study their unique magical practices. But I'm afraid I haven't learned much.
                return 40;
            case (40, 2):
                // $script:1010140307011547$
                // - It seems $npcName:11004329[gender:0]$ is, to the contrary, already deep into his research.
                return 40;
            case (40, 3):
                // $script:1010140307011548$
                // - I was hoping to find something that would improve Professor $npcName:11000032[gender:0]$'s condition.
                switch (selection) {
                    // $script:1010140307011549$
                    // - I believe in you.
                    case 0:
                        return 50;
                }
                return -1;
            case (50, 0):
                // $script:1010140307011550$
                // - Ahem! W-well I'm not going to make any progress sitting around talking to you! Excuse me.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.Next,
            (40, 2) => NpcTalkButton.Next,
            (40, 3) => NpcTalkButton.SelectableDistractor,
            (50, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
