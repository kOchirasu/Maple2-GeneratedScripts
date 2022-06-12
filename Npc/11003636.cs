using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003636: JCH-2YS
/// </summary>
public class _11003636 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1109121007009064$
    // - Identity confirmed... $MyPCName$...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1109121007009065$
                // - Initiating light banter protocol. I am just passing through town, stranger.
                switch (selection) {
                    // $script:1109121007009066$
                    // - Aren't you a polite robot?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1109121007009067$
                // - Rhetorical question detected. Response: Can I help you with something?
                switch (selection) {
                    // $script:1109121007009068$
                    // - No, no, I'm good.
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:1109121007009069$
                // - Detecting trace amounts of $npcName:11003535[gender:1]$ pheromones... Special encoders enabled. Message: "Code EK-LOVE."
                switch (selection) {
                    // $script:1109121007009070$
                    // - You're an agent...?
                    case 0:
                        return 13;
                }
                return -1;
            case (13, 0):
                // $script:1109121007009071$
                // - Resuming normal operations. Have a nice day.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.SelectableDistractor,
            (13, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
