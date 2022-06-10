using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004060: Pemberton
/// </summary>
public class _11004060 : NpcScript {
    internal _11004060(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614185307010093$ 
                // - The lady is heartbroken. She needs to pull herself together quickly... 
                return true;
            case 10:
                // $script:0614185307010094$ 
                // - As the current crisis threatens all of Maple World, the Alemani family will spare no expense in addressing it. 
                return true;
            default:
                return true;
        }
    }
}
