using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000456: Geno
/// </summary>
public class _11000456 : NpcScript {
    internal _11000456(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002018$ 
                // - I love staying around the house. 
                return true;
            case 30:
                // $script:0831180407002021$ 
                // - My girlfriend keeps bugging me to go out, even though it's a great day to relax inside. You get that, right? Make her see reason. If she always insists on doing... things, I worry about our future. 
                return true;
            default:
                return true;
        }
    }
}
