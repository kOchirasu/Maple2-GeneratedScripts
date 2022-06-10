using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003428: Silver Wolf
/// </summary>
public class _11003428 : NpcScript {
    internal _11003428(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0706160807008643$ 
                // -  
                return true;
            case 10:
                // $script:0706160807008644$ 
                // -  
                return true;
            default:
                return true;
        }
    }
}
