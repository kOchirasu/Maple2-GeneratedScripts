using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004480: Throin
/// </summary>
public class _11004480 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1227192907012205$
    // - Yikes! You startled me. I... I didn't really expect another person to just walk up to me in a place like this.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1227192907012206$
                // - Yikes! You startled me. I... I didn't really expect another person to just walk up to me in a place like this.
                return 10;
            case (10, 1):
                // $script:1227192907012207$
                // - See this tree? I thought it was some kind of mechane at first. But all of my tests show that this is, in fact, a living plant.
                return 10;
            case (10, 2):
                // $script:1227192907012208$
                // - Those cogwheels are actually leaves. Eventually they'll fall off and the tree will grow new ones. I'm still trying to wrap my head around the ecosystem here...
                return 10;
            case (10, 3):
                // $script:1227192907012209$
                // - If my report is convincing enough, maybe Dr. $npcName:11004492[gender:0]$ will authorize a permanent research camp here.
                switch (selection) {
                    // $script:0114163707012710$
                    // - I'm sure it'll happen.
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:0114163707012711$
                // - I just want to lose myself in my research!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Next,
            (10, 2) => NpcTalkButton.Next,
            (10, 3) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
