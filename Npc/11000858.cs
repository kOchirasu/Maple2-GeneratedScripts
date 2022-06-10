using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000858: Darphony
/// </summary>
public class _11000858 : NpcScript {
    internal _11000858(INpcScriptContext context) : base(context) {
        Id = 40;
        // TODO: RandomPick 40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003121$ 
                // - Ah... N-nice to meet you... 
                return true;
            case 40:
                // $script:0831180407003125$ 
                // - The w-wolves showed up again... They destroyed our fence, and some of our sheep were so scared that they ran into that thicket. 
                // $script:0831180407003126$ 
                // - But an $npcName:24000702$ carried off $npcName:11001013[gender:1]$'s $item:30000328$ in its jaws... 
                return true;
            default:
                return true;
        }
    }
}
