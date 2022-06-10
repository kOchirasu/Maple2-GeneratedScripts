using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003359: Ralph's Lackey
/// </summary>
public class _11003359 : NpcScript {
    internal _11003359(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0517164307008512$ 
                // - You better prepare yourself. 
                return true;
            case 20:
                // $script:0517164307008514$ 
                // - You better be ready this time. You'll see what I mean when you go inside. Heheheh... 
                return true;
            default:
                return true;
        }
    }
}
