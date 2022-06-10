using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000473: Bunny Gal
/// </summary>
public class _11000473 : NpcScript {
    internal _11000473(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 40;50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002069$ 
                // - What is it? 
                return true;
            case 40:
                // $script:0831180407002073$ 
                // - I don't recognize you. Is this your first time here? 
                return true;
            case 50:
                // $script:0831180407002074$ 
                // - You've been staring at me. Interested? 
                return true;
            default:
                return true;
        }
    }
}
