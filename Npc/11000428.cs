using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000428: Hatto
/// </summary>
public class _11000428 : NpcScript {
    internal _11000428(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001782$ 
                // - Why are you bothering me? 
                return true;
            case 20:
                // $script:0831180407001784$ 
                // - A true adventurer dives head-first into trouble! He's not afraid of jumping off a cliff into a sea of lava or fighting giant, rampaging monsters! 
                return true;
            default:
                return true;
        }
    }
}
