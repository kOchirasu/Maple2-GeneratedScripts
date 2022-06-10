using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000612: 
/// </summary>
public class _11000612 : NpcScript {
    internal _11000612(INpcScriptContext context) : base(context) {
        // TODO: Condition $script:0831180610000872$
        // Id = 20;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180610000870$ 
                // - How may I help you?
                return true;
            case 20:
                // $script:0831180610000872$ 
                // - I hope you enjoyed your stay.
                //   Would you like to leave the Guild Lounge now?
                return true;
            case 10:
                // $script:0831180610000871$ 
                // - Only members can use the Guild Lounge.
                return true;
            default:
                return true;
        }
    }
}
