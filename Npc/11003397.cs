using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003397: Kiro Karr
/// </summary>
public class _11003397 : NpcScript {
    internal _11003397(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0706160807008599$ 
                // -  
                return true;
            case 10:
                // $script:0706160807008600$ 
                // -  
                return true;
            default:
                return true;
        }
    }
}
