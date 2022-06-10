using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001601: Jenna
/// </summary>
public class _11001601 : NpcScript {
    internal _11001601(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0504151707006089$ 
                // - Do you have business with me?
                return true;
            case 10:
                // $script:0515180307006138$ 
                // - The real fun is about to begin! I'm going to blow that $npcName:11001231[gender:0]$ guy to smithereens!
                return true;
            default:
                return true;
        }
    }
}
