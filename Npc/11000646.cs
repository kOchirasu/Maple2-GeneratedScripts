using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000646: Prisoner 160919
/// </summary>
public class _11000646 : NpcScript {
    internal _11000646(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002642$ 
                // - Get me out of here... 
                return true;
            case 30:
                // $script:0831180407002645$ 
                // - It's been three days since the toilet overflowed...
                return true;
            default:
                return true;
        }
    }
}
