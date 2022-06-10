using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003454: Screaming Fist
/// </summary>
public class _11003454 : NpcScript {
    internal _11003454(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0706160807008663$ 
                // -  
                return true;
            case 10:
                // $script:0706160807008664$ 
                // -  
                return true;
            default:
                return true;
        }
    }
}
