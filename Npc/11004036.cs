using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004036: Eupheria
/// </summary>
public class _11004036 : NpcScript {
    internal _11004036(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614185307010057$ 
                // - Don't worry, I'll protect you. 
                return true;
            case 20:
                // $script:0614185307010058$ 
                // - Don't worry, I'll protect you. 
                return true;
            default:
                return true;
        }
    }
}
