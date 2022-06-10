using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003210: Zeta
/// </summary>
public class _11003210 : NpcScript {
    internal _11003210(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0404083307008239$ 
                // - I came to repay you for saving my brother. Now we're even.
                return true;
            case 10:
                // $script:0404083307008240$ 
                // - Don't say I never did nothing for you.
                return true;
            default:
                return true;
        }
    }
}
