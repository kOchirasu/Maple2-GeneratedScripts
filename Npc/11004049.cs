using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004049: Carriage Tender
/// </summary>
public class _11004049 : NpcScript {
    internal _11004049(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614185307010071$ 
                // - Would you like a carriage back to Tria? 
                return true;
            case 10:
                // $script:0614185307010072$ 
                // - Would you like a carriage back to Tria? 
                return true;
            default:
                return true;
        }
    }
}
