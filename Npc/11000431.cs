using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000431: Ronin
/// </summary>
public class _11000431 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40;41
    }

    // Select 0:
    // $script:0831180407001797$
    // - I'd better rest while I can!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407001799$
                // - I've heard stories of treasure chests under the sea, but I've never seen one. How about you, $MyPCName$?
                return -1;
            case (40, 0):
                // $script:0831180407001800$
                // - Yes?
                switch (selection) {
                    // $script:0831180407001801$
                    // - $npcName:11000362[gender:0]$'s special...
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:0831180407001802$
                // - Go away.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
