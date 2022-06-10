using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003060: Surnuny
/// </summary>
public class _11003060 : NpcScript {
    internal _11003060(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0102155907007637$ 
                // - Welcome, welcome. 
                return true;
            case 30:
                // $script:0102155907007638$ 
                // - Hmm, I must say, I think I've seen you before. 
                switch (selection) {
                    // $script:0102155907007639$
                    // - Yeah, we met back in Tria.
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0102155907007640$ 
                // - Ah! Now I remember you, $MyPCName$! It's been awhile, hasn't it? Good to see you again, very good. 
                return true;
            case 40:
                // $script:0102155907007641$ 
                // - My kingdom... Ahhh, it was so very beautiful. You may hear stories about it, but I tell you the truth. 
                // $script:0102155907007642$ 
                // - Our king... I told him to be strong...
<font color="#909090">(He does his best to hide his despair, but it runs too deep.)</font> 
                return true;
            default:
                return true;
        }
    }
}
