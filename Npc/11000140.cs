using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000140: Dana
/// </summary>
public class _11000140 : NpcScript {
    internal _11000140(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1121222006000791$ 
                // - Can I help you?
                return true;
            case 10:
                // $script:1121222006000792$ 
                // - Can I help you?
                return true;
            default:
                return true;
        }
    }
}
