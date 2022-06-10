using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004544: Soldieretto Guide
/// </summary>
public class _11004544 : NpcScript {
    internal _11004544(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0108105807012638$ 
                // - This is the soldieretto lab. Are you a robot researcher?
                return true;
            case 10:
                // $script:0108105807012639$ 
                // - This is the soldieretto lab. Are you a robot researcher?
                // $script:0108105807012640$ 
                // - If you do not have any particular business with us, leave. Humans who come here tend to give us more work.
                return true;
            default:
                return true;
        }
    }
}
