using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001564: Eupheria
/// </summary>
public class _11001564 : NpcScript {
    internal _11001564(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0504151707006052$ 
                // - There you are. 
                return true;
            case 10:
                // $script:0515180307006108$ 
                // - No matter $npcName:11001231[gender:0]$'s reasons or excuses, I will never forgive him for murdering Arazaad. 
                return true;
            default:
                return true;
        }
    }
}
