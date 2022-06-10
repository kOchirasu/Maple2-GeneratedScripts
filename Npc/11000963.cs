using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000963: Kamil
/// </summary>
public class _11000963 : NpcScript {
    internal _11000963(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003345$ 
                // - There are wounded people here. They need help!
                return true;
            case 20:
                // $script:0831180407003347$ 
                // - Folks like me don't make money sitting around on our butts. We're always on the move, looking for new buyers.
                return true;
            default:
                return true;
        }
    }
}
