using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003455: Rolling Thunder
/// </summary>
public class _11003455 : NpcScript {
    internal _11003455(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0706160807008665$ 
                // -  
                return true;
            case 10:
                // $script:0706160807008666$ 
                // -  
                return true;
            default:
                return true;
        }
    }
}
