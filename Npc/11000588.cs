using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000588: Vincent
/// </summary>
public class _11000588 : NpcScript {
    internal _11000588(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1121222006000845$ 
                // - Can I help you?
                return true;
            case 10:
                // $script:1121222006000846$ 
                // - People with long tails are so... unusual.
                return true;
            default:
                return true;
        }
    }
}
