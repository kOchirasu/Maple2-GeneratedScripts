using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000784: Carrie
/// </summary>
public class _11000784 : NpcScript {
    internal _11000784(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002956$ 
                // - Who are you? 
                return true;
            case 30:
                // $script:0831180407002959$ 
                // - Strange... I see cake everywhere, but I smell nothing. 
                return true;
            default:
                return true;
        }
    }
}
