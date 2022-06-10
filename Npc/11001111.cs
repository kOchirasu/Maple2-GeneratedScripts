using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001111: Lennon
/// </summary>
public class _11001111 : NpcScript {
    internal _11001111(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0908154107003736$ 
                // - Hmm...  
                return true;
            case 30:
                // $script:0908154107003737$ 
                // - The soul inside this orb... If it's left alone for too long, it'll be swallowed by the enormous darkness that is the Shadow World. 
                return true;
            default:
                return true;
        }
    }
}
