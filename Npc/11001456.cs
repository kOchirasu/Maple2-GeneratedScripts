using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001456: Dolores
/// </summary>
public class _11001456 : NpcScript {
    internal _11001456(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1222171407005454$ 
                // - We just moved here.
                return true;
            case 30:
                // $script:1222171407005457$ 
                // - We haven't even finished unpacking, and my baby is already hurt. How dreadful!
                return true;
            default:
                return true;
        }
    }
}
