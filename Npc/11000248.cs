using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000248: Briel
/// </summary>
public class _11000248 : NpcScript {
    internal _11000248(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1121222006000807$ 
                // - Can I help you? 
                return true;
            case 10:
                // $script:1121222006000808$ 
                // - I'd like to get flowers too. 
                return true;
            default:
                return true;
        }
    }
}
