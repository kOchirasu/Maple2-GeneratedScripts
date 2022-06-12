using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000076: Allon
/// </summary>
public class _11000076 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 40;50
    }

    // Select 0:
    // $script:0831180407000354$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407000358$
                // - I command the Royal Knights of Empress $npcName:11000075[gender:1]$. Our sacred duty is to keep her safe. 
                return 40;
            case (40, 1):
                // $script:0831180407000359$
                // - But after that shadow gate to the Land of Darkness appeared, the empress sent us here to guard the border between worlds.
                return 40;
            case (40, 2):
                // $script:0831180407000360$
                // - The minister is with the empress, but that doesn't reassure me much. I've been here for too long. I want this battle done and over with so I can go back to her.
                return -1;
            case (50, 0):
                // $script:0831180407000361$
                // - I lead the Lumiknights, the defenders of the empress, and yet I was completely oblivious of $npcName:11000044[gender:0]$'s true nature. It's disgraceful.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.Next,
            (40, 2) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
