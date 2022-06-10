using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003090: Orde
/// </summary>
public class _11003090 : NpcScript {
    internal _11003090(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0207122607007934$ 
                // - I guess field duty isn't that bad... 
                return true;
            case 10:
                // $script:0207122607007935$ 
                // - It's hard to keep the Shadow Gate staffed with enough soldiers. If any more rifts like this open up, Maple World could be in serious trouble. 
                return true;
            default:
                return true;
        }
    }
}
