using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000388: Bodyguard
/// </summary>
public class _11000388 : NpcScript {
    internal _11000388(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001577$ 
                // - Can I help you? 
                return true;
            case 30:
                // $script:0831180407001580$ 
                // - The crowd's already whipped themselves into a frenzy. It's like this wherever we go. <i>Hey you!</i> Back up, buddy. 
                return true;
            default:
                return true;
        }
    }
}
