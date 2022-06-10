using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003242: Armano
/// </summary>
public class _11003242 : NpcScript {
    internal _11003242(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0403155707008142$ 
                // - Why'd this gotta happen to <i>me</i>? 
                return true;
            case 30:
                // $script:0403155707008144$ 
                // - Ugh... Who are you...? 
                return true;
            default:
                return true;
        }
    }
}
