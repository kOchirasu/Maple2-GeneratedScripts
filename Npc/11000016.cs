using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000016: Tru
/// </summary>
public class _11000016 : NpcScript {
    internal _11000016(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180610000001$ 
                // - What brings you here? 
                return true;
            case 40:
                // $script:1101173110001798$ 
                // - You want to go to $map:02000001$? Why are you asking me? You should go to the Chief. 
                switch (selection) {
                    // $script:1101173110001799$
                    // - I thought sea dogs were adventurous, and yet you won't even let a friendly stranger onto your boat?
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:1101173110001800$ 
                // - You sail to $map:02000001$ by first going to $map:02000062$, and right now the water's too choppy for this boat. Besides, when conditions are like that, only the Chief can authorize the departure of a large ship. 
                return true;
            default:
                return true;
        }
    }
}
