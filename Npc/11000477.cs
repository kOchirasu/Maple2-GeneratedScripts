using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000477: Praise Goldus
/// </summary>
public class _11000477 : NpcScript {
    internal _11000477(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002078$ 
                // - There's a name on it: $npcName:11000477$.
                return true;
            case 20:
                // $script:0831180407002079$ 
                // - The Goldus way! Put your back into it! Pinch a penny, make a penny!
                return true;
            default:
                return true;
        }
    }
}
