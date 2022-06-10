using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003351: Ralph's Lackey
/// </summary>
public class _11003351 : NpcScript {
    internal _11003351(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0517164307008499$ 
                // - Taking down the boss... You're something else, you know that? 
                return true;
            case 30:
                // $script:0517164307008502$ 
                // - The big guy's been training hard for days now. You really lit a fire under his butt, I'll tell you that. 
                return true;
            default:
                return true;
        }
    }
}
