using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000858: Darphony
/// </summary>
public class _11000858 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:0831180407003121$
    // - Ah... N-nice to meet you... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407003125$
                // - The w-wolves showed up again... They destroyed our fence, and some of our sheep were so scared that they ran into that thicket. 
                return 40;
            case (40, 1):
                // $script:0831180407003126$
                // - But an $npcName:24000702$ carried off $npcName:11001013[gender:1]$'s $item:30000328$ in its jaws... 
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
