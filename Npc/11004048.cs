using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004048: Carriage Tender
/// </summary>
public class _11004048 : NpcScript {
    internal _11004048(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614185307010069$ 
                // - It's a long walk to the Frontier Foundation. Why not take a carriage? 
                return true;
            case 10:
                // $script:0614185307010070$ 
                // - It's a long walk to the Frontier Foundation. Why not take a carriage? 
                return true;
            default:
                return true;
        }
    }
}
