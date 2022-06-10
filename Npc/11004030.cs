using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004030: Tinchai
/// </summary>
public class _11004030 : NpcScript {
    internal _11004030(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614185307010047$ 
                // - Are lapenshards really the cause of all this? Just what are they?
                return true;
            case 20:
                // $script:0614185307010048$ 
                // - Are lapenshards really the cause of all this? Just what are they?
                return true;
            default:
                return true;
        }
    }
}
