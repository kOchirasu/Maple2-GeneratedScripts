using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000156: Sam
/// </summary>
public class _11000156 : NpcScript {
    internal _11000156(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000660$ 
                // - Can I help you?
                return true;
            case 20:
                // $script:0831180407000662$ 
                // - What do I do? I've got piles of packages, and the Royal Road to $map:02000001$ is all busted up.
                return true;
            default:
                return true;
        }
    }
}
