using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000807: Viata
/// </summary>
public class _11000807 : NpcScript {
    internal _11000807(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002975$ 
                // - Erm... Erm... 
                return true;
            case 20:
                // $script:0831180407002977$ 
                // - The Cruel Tower is like a living hell. I don't even want to think about it. I'm lucky to have gotten out of there alive.
                return true;
            default:
                return true;
        }
    }
}
