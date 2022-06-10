using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001338: Derrick
/// </summary>
public class _11001338 : NpcScript {
    internal _11001338(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217012607005271$ 
                // - And what business do you have with a pro skater like me, hm?
                return true;
            case 30:
                // $script:1217012607005274$ 
                // - Hey, you want to take some pro skateboarding lessons? I teach... for a small fee.
                return true;
            default:
                return true;
        }
    }
}
