using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003120: Wei Hong
/// </summary>
public class _11003120 : NpcScript {
    internal _11003120(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0321141707008118$ 
                // - I don't have time for small potatoes. 
                return true;
            case 30:
                // $script:0321141707008121$ 
                // - I don't know you, so I'll warn you once: Don't cross me. 
                return true;
            default:
                return true;
        }
    }
}
