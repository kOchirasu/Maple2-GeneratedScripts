using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003964: Striker
/// </summary>
public class _11003964 : NpcScript {
    internal _11003964(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614143707010019$ 
                // - You seem like you're pretty tough too.
                return true;
            case 20:
                // $script:0614143707010020$ 
                // - You ever heard of the Gray Wolf? Well you're looking at him! The man, the myth, the legend! What do you mean you've never heard of me...
                return true;
            default:
                return true;
        }
    }
}
