using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000961: Tinnie
/// </summary>
public class _11000961 : NpcScript {
    internal _11000961(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003339$ 
                // - Why can't I shake this bad feeling...?
                return true;
            case 20:
                // $script:0831180407003341$ 
                // - One day, I want to follow in $npcName:11000015[gender:1]$'s footsteps and become the leader of the Green Hoods. I want to earn the same respect that she did.
                return true;
            default:
                return true;
        }
    }
}
