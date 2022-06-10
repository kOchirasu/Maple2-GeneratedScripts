using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004037: Landevian
/// </summary>
public class _11004037 : NpcScript {
    internal _11004037(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614185307010059$ 
                // - Even though everything's going crazy right now, it's reassuring to have you around. 
                return true;
            case 20:
                // $script:0614185307010060$ 
                // - Even though everything's going crazy right now, it's reassuring to have you around. 
                return true;
            default:
                return true;
        }
    }
}
