using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003240: Armano
/// </summary>
public class _11003240 : NpcScript {
    internal _11003240(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0403155707008134$ 
                // - Why did you call me?
                return true;
            case 30:
                // $script:0403155707008137$ 
                // - Ugh... Who are you...?
                return true;
            default:
                return true;
        }
    }
}
