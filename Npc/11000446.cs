using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000446: Ricky
/// </summary>
public class _11000446 : NpcScript {
    internal _11000446(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1121222006000841$ 
                // - Can I help you?
                return true;
            case 10:
                // $script:1121222006000842$ 
                // - Can I help you?
                return true;
            default:
                return true;
        }
    }
}
