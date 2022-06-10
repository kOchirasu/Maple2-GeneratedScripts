using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003157: Karen
/// </summary>
public class _11003157 : NpcScript {
    internal _11003157(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0306155707008050$ 
                // - How may I help you? 
                return true;
            case 30:
                // $script:0306155707008053$ 
                // - You want to know the secret to a beautiful garden? Take care of your plants with love, and they'll repay you by growing. 
                return true;
            default:
                return true;
        }
    }
}
