using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000154: Sophia
/// </summary>
public class _11000154 : NpcScript {
    internal _11000154(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000656$ 
                // - I can't get rid of these chubby cheeks, no matter how hard I try.
                return true;
            case 30:
                // $script:0831180407000659$ 
                // - Goodness, just LOOK at those clothes! Did you dig them out of some ancient ruins? Might be nice to wear something made in the last decade.
                return true;
            default:
                return true;
        }
    }
}
