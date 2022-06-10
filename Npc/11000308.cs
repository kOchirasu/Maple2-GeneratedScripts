using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000308: Iun
/// </summary>
public class _11000308 : NpcScript {
    internal _11000308(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1121222006000821$ 
                // - Can I help you? 
                return true;
            case 10:
                // $script:1121222006000822$ 
                // - Can I help you? 
                return true;
            default:
                return true;
        }
    }
}
