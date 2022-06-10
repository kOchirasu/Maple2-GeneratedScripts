using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004028: Holstatt
/// </summary>
public class _11004028 : NpcScript {
    internal _11004028(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614185307010043$ 
                // - ... 
                return true;
            case 20:
                // $script:0614185307010044$ 
                // - ... 
                return true;
            default:
                return true;
        }
    }
}
