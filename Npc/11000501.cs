using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000501: Balboa
/// </summary>
public class _11000501 : NpcScript {
    internal _11000501(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002179$ 
                // - How may I help you? 
                return true;
            case 20:
                // $script:0831180407002181$ 
                // - As long as you know who you are and what you believe, what others think of you doesn't matter. That's the way we Boroboros live. 
                return true;
            default:
                return true;
        }
    }
}
