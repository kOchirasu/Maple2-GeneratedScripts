using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003452: Brave Pig
/// </summary>
public class _11003452 : NpcScript {
    internal _11003452(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0706160807008659$ 
                // - It's a family name.
                return true;
            case 10:
                // $script:0706160807008660$ 
                // - You didn't think I'd actually be a pig, did you?
                return true;
            default:
                return true;
        }
    }
}
