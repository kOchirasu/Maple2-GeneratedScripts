using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004460: Safehold Guardsman
/// </summary>
public class _11004460 : NpcScript {
    internal _11004460(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1227192907012067$ 
                // - All clear!
                return true;
            case 10:
                // $script:1227192907012068$ 
                // - All clear!
                // $script:1227192907012069$ 
                // - I'm a little nervous about this place, but this is a chance to set myself apart from the other guards!
                return true;
            default:
                return true;
        }
    }
}
