using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003430: Temple Altar
/// </summary>
public class _11003430 : NpcScript {
    internal _11003430(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0706160807008647$ 
                // - <font color="#909090">(There appears to be an empty space under the altar.)</font>
                return true;
            case 10:
                // $script:0706160807008648$ 
                // - <font color="#909090">(There appears to be an empty space under the altar.)</font>
                return true;
            default:
                return true;
        }
    }
}
