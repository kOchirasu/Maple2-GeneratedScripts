using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004061: Junta
/// </summary>
public class _11004061 : NpcScript {
    internal _11004061(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614185307010095$ 
                // - I'm sorry about what happened...
                return true;
            case 10:
                // $script:0614185307010096$ 
                // - I'm sorry about what happened...
                return true;
            default:
                return true;
        }
    }
}
