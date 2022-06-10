using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000418: Vogen
/// </summary>
public class _11000418 : NpcScript {
    internal _11000418(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1121222006000839$ 
                // - Can I help you?
                return true;
            case 10:
                // $script:1121222006000840$ 
                // - Let's see...
                return true;
            default:
                return true;
        }
    }
}
