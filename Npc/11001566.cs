using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001566: Eupheria
/// </summary>
public class _11001566 : NpcScript {
    internal _11001566(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0504151707006054$ 
                // - Impossible... 
                return true;
            case 10:
                // $script:0515180307006109$ 
                // - Wake up, $npcName:11001233[gender:1]$. We still need to avenge Arazaad... 
                return true;
            default:
                return true;
        }
    }
}
