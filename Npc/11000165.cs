using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000165: Geo
/// </summary>
public class _11000165 : NpcScript {
    internal _11000165(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1121222006000793$ 
                // - Can I help you?
                return true;
            case 10:
                // $script:1121222006000794$ 
                // - Can I help you?
                return true;
            default:
                return true;
        }
    }
}
