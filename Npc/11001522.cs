using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001522: Mage
/// </summary>
public class _11001522 : NpcScript {
    internal _11001522(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0515211707006111$ 
                // - Nice to meet you.
                return true;
            case 10:
                // $script:0515211707006112$ 
                // - If it weren't for the Archmage and $npcName:11000032[gender:0]$, I'd be back home working on my research. I'm still not convinced this mission is worthwhile. At least the name "Starlight Expedition" has a nice ring to it.
                return true;
            default:
                return true;
        }
    }
}
