using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000610: Kama
/// </summary>
public class _11000610 : NpcScript {
    internal _11000610(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002506$ 
                // - What? 
                return true;
            case 10:
                // $script:0831180407002507$ 
                // - Stop bothering me and scram. 
                return true;
            default:
                return true;
        }
    }
}
