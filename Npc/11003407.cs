using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003407: Wolf Heart
/// </summary>
public class _11003407 : NpcScript {
    internal _11003407(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0706160807008603$ 
                // -  
                return true;
            case 10:
                // $script:0706160807008604$ 
                // -  
                return true;
            default:
                return true;
        }
    }
}
