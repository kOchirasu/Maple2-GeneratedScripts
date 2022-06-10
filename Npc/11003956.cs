using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003956: Priest
/// </summary>
public class _11003956 : NpcScript {
    internal _11003956(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614143707010003$ 
                // - Do you believe in the power of the light? 
                return true;
            case 20:
                // $script:0614143707010004$ 
                // - This Frontier Foundation is a beautiful place. I look forward to working with such capable individuals. 
                return true;
            default:
                return true;
        }
    }
}
