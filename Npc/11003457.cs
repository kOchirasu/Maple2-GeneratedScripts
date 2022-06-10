using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003457: Rolling Thunder
/// </summary>
public class _11003457 : NpcScript {
    internal _11003457(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0706160807008669$ 
                // - Someday, I will live up to my father's legacy.
                return true;
            case 10:
                // $script:0706160807008670$ 
                // - The people of $map:02000051$ look up to me now. I hope I live up to their expectations.
                return true;
            default:
                return true;
        }
    }
}
