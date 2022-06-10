using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003467: Screaming Fist
/// </summary>
public class _11003467 : NpcScript {
    internal _11003467(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0706160807008671$ 
                // - You need to settle down.
                return true;
            case 10:
                // $script:0706160807008672$ 
                // - Don't start any trouble.
                return true;
            default:
                return true;
        }
    }
}
