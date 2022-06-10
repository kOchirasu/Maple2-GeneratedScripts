using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000481: Quarry Worker
/// </summary>
public class _11000481 : NpcScript {
    internal _11000481(INpcScriptContext context) : base(context) {
        Id = 50;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002103$ 
                // - I'm busy. Why are you bothering me?
                return true;
            case 50:
                // $script:0831180407002108$ 
                // - I'm busy. If you're not going to help, then at least don't get in my way.
                return true;
            default:
                return true;
        }
    }
}
