using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000167: Peter
/// </summary>
public class _11000167 : NpcScript {
    internal _11000167(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1121222006000797$ 
                // - Can I help you?
                return true;
            case 10:
                // $script:1121222006000798$ 
                // - Can I help you?
                return true;
            default:
                return true;
        }
    }
}
