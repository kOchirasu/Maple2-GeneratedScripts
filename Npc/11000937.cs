using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000937: 
/// </summary>
public class _11000937 : NpcScript {
    internal _11000937(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1121222006000859$ 
                // - Can I help you? 
                return true;
            case 10:
                // $script:1121222006000860$ 
                // - Can I help you? 
                return true;
            default:
                return true;
        }
    }
}
