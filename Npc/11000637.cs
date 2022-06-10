using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000637: Prisoner 140920
/// </summary>
public class _11000637 : NpcScript {
    internal _11000637(INpcScriptContext context) : base(context) {
        Id = 40;
        // TODO: RandomPick 40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002596$ 
                // - Get me out of here... 
                return true;
            case 40:
                // $script:0831180407002599$ 
                // - Excuse me... Please get me out of here! I promise I'll never misbehave again!
                return true;
            default:
                return true;
        }
    }
}
