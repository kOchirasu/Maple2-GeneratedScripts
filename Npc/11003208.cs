using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003208: Zeta
/// </summary>
public class _11003208 : NpcScript {
    internal _11003208(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0404083307008237$ 
                // - Thank you for saving my brother! 
                return true;
            case 10:
                // $script:0404083307008238$ 
                // - I thought my bro was a goner... until you came along, that is. 
                return true;
            default:
                return true;
        }
    }
}
