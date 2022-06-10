using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004051: Oska
/// </summary>
public class _11004051 : NpcScript {
    internal _11004051(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614185307010075$ 
                // - The Green Hoods will do their part to purge the forces of darkness from Maple World. 
                return true;
            case 10:
                // $script:0614185307010076$ 
                // - The Green Hoods will do their part to purge the forces of darkness from Maple World. 
                return true;
            default:
                return true;
        }
    }
}
