using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004541: Nuel
/// </summary>
public class _11004541 : NpcScript {
    internal _11004541(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0110183907012675$ 
                // - Ugh... I hate deadlines...
                return true;
            case 10:
                // $script:0110183907012676$ 
                // - Ugh... I hate deadlines...
                // $script:0110183907012677$ 
                // - Here to gawk at the soldierettos? Get a good look and then be on your way. I can't concentrate with all you... all you tourists hanging about!
                return true;
            default:
                return true;
        }
    }
}
