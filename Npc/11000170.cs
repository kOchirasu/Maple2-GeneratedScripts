using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000170: Leta
/// </summary>
public class _11000170 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;30;40
    }

    // Select 0:
    // $script:0831180407000710$
    // - What seems to be the problem?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407000712$
                // - $npcName:11000174[gender:1]$ and I grew up together in the same neighborhood. I started to notice my heart racing and my mood brightening whenever I thought about $npcName:11000174[gender:1]$. I've honestly never felt like this about anyone else before.
                return -1;
            case (30, 0):
                // $script:0831180407000713$
                // - $npcName:11000174[gender:1]$ and I grew up together in the same neighborhood. I started to notice my heart racing and my mood brightening whenever I thought about $npcName:11000174[gender:1]$. I've honestly never felt like this about anyone else before.
                return -1;
            case (40, 0):
                // $script:0317164707008110$
                // - How may I help you?
                switch (selection) {
                    // $script:0317164707008111$
                    // - Have you seen anyone in a mask go through here?
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:0317164707008112$
                // - I sure did! Hard not to notice someone that odd. He ran off toward the Kerning Interchange.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
