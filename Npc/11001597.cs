using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001597: Eupheria
/// </summary>
public class _11001597 : NpcScript {
    internal _11001597(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0504151707006085$ 
                // - This is my fault...  
                return true;
            case 10:
                // $script:0515180307006134$ 
                // - This is all my doing. I should have stayed out of $npcName:11001229[gender:0]$'s way...  
                return true;
            default:
                return true;
        }
    }
}
