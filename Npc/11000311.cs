using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000311: Isaac
/// </summary>
public class _11000311 : NpcScript {
    internal _11000311(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1121222006000825$ 
                // - How may I help you? 
                return true;
            case 10:
                // $script:1121222006000826$ 
                // - I'm going to be rich, no matter what it takes! 
                return true;
            default:
                return true;
        }
    }
}
