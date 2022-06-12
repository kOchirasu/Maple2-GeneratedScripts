using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004564: Orde
/// </summary>
public class _11004564 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0220211107014526$
    // - Hm...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0220211107014527$
                // - Sigh...
                switch (selection) {
                    // $script:0220211107014528$
                    // - You doing okay?
                    case 0:
                        return 20;
                }
                return -1;
            case (20, 0):
                // $script:0220211107014529$
                // - Uh? Whuh?
                return 20;
            case (20, 1):
                // $script:0220211107014530$
                // - What are <i>you</i> doing here?! Oh, no. Don't tell me we're fighting, too...
                return 20;
            case (20, 2):
                // $script:0220211107014531$
                // - Listen up. The Pink Beans told me something. They said... they said if I win...
                return 20;
            case (20, 3):
                // $script:0220211107014532$
                // - ...then I'll get to interview $npcName:11004568[gender:1]$ herself! Could you imagine? That girl is practically a dragon, thanks to her adopted father!
                return 20;
            case (20, 4):
                // $script:0220211107014533$
                // - So if you get matched against me, throw the fight, okay?
                switch (selection) {
                    // $script:0220211107014534$
                    // - Well...
                    case 0:
                        return 30;
                }
                return -1;
            case (30, 0):
                // $script:0220211107014535$
                // - Fine, <i>don't</i> throw the fight. But I warn you, I'll give it everything I've got!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (20, 0) => NpcTalkButton.Next,
            (20, 1) => NpcTalkButton.Next,
            (20, 2) => NpcTalkButton.Next,
            (20, 3) => NpcTalkButton.Next,
            (20, 4) => NpcTalkButton.SelectableDistractor,
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
