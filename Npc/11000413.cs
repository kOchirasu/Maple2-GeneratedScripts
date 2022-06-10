using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000413: Jean Pierre
/// </summary>
public class _11000413 : NpcScript {
    internal _11000413(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1121222006000829$ 
                // - Can I help you?
                return true;
            case 20:
                // $script:1121222006000830$ 
                // - Please don't ask about my past.
                return true;
            default:
                return true;
        }
    }
}
