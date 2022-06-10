using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000532: Bogler
/// </summary>
public class _11000532 : NpcScript {
    internal _11000532(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002296$ 
                // - Can I help you?
                return true;
            case 10:
                // $script:0831180407002297$ 
                // - Ah, we haven't had many guests lately. Do you know why?
                return true;
            default:
                return true;
        }
    }
}
