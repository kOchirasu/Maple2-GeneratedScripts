using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004027: Turka
/// </summary>
public class _11004027 : NpcScript {
    internal _11004027(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614185307010041$ 
                // - ...
                return true;
            case 20:
                // $script:0614185307010042$ 
                // - ...
                return true;
            default:
                return true;
        }
    }
}
