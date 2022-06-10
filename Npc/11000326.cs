using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000326: Lowen
/// </summary>
public class _11000326 : NpcScript {
    internal _11000326(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1121222006000827$ 
                // - You can buy Souvenirs in Furnish inside your house.
                return true;
            case 10:
                // $script:1121222006000828$ 
                // - Ahhh, what a wonderful world this is!
                return true;
            default:
                return true;
        }
    }
}
