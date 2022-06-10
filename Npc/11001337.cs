using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001337: Lequan
/// </summary>
public class _11001337 : NpcScript {
    internal _11001337(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217012607005267$ 
                // - You have something to say to me?
                return true;
            case 30:
                // $script:1217012607005270$ 
                // - You here to talk, or you here to skate? Heh... Good luck.
                return true;
            default:
                return true;
        }
    }
}
