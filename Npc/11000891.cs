using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000891: Chechy
/// </summary>
public class _11000891 : NpcScript {
    internal _11000891(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003257$ 
                // - This is bad, real bad!
                return true;
            case 20:
                // $script:0831180407003259$ 
                // - Welcome.
                return true;
            default:
                return true;
        }
    }
}
